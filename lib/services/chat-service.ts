import { StreamingTextResponse } from 'ai'
import { streamCompletion } from '@/lib/ollama-client'
import { SYSTEM_PROMPT } from '@/lib/prompts/system-prompt'
import { ragClient } from '@/lib/services/rag-client'
import { memoryService } from '@/lib/services/memory-service'
import { precisionControl } from '@/lib/services/precision-control'
import type { Message } from '@/lib/types/chat'

export class ChatService {
  static async processMessages(messages: Message[], sessionId: string = 'default'): Promise<StreamingTextResponse> {
    // Pega a última mensagem do usuário
    const lastUserMessage = messages.filter(m => m.role === 'user').pop()
    let ragContext = ''
    let hasRAGContext = false
    
    // Busca contexto RAG e memória conversacional
    if (lastUserMessage) {
      ragContext = await ragClient.getContextForLLM(lastUserMessage.content)
      hasRAGContext = ragContext.length > 0
      
      const conversationContext = memoryService.getRelevantContext(sessionId, lastUserMessage.content)
      
      // Salva mensagem do usuário na memória
      memoryService.addMessage(sessionId, lastUserMessage, ragContext)
      
      // Combina contextos
      if (ragContext || conversationContext) {
        ragContext = `${ragContext}\n\n${conversationContext}`
      }
    }

    // Aplica controle de precisão ao prompt
    const enhancedSystemPrompt = precisionControl.enhanceSystemPrompt(
      `${SYSTEM_PROMPT}\n\n${ragContext}`,
      hasRAGContext
    )

    const fullMessages = [
      { role: 'system' as const, content: enhancedSystemPrompt },
      ...messages
    ]

    const response = await streamCompletion(fullMessages)
    
    if (!response.body) {
      throw new Error('Response body is null')
    }

    const transformStream = new TransformStream({
      transform(chunk, controller) {
        try {
          const text = new TextDecoder().decode(chunk)
          const lines = text.split('\n')
          
          for (const line of lines) {
            if (line.trim()) {
              const data = JSON.parse(line)
              if (data.message?.content) {
                controller.enqueue(data.message.content)
              }
            }
          }
        } catch (error) {
          console.error('Transform error:', error)
        }
      }
    })

    return new StreamingTextResponse(response.body.pipeThrough(transformStream))
  }
}