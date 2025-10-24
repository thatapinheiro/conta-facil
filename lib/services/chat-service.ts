import { StreamingTextResponse } from 'ai'
import { streamCompletion } from '@/lib/ollama-client'
import { SYSTEM_PROMPT } from '@/lib/prompts/system-prompt'
import { ragClient } from '@/lib/services/rag-client'
import type { Message } from '@/lib/types/chat'

export class ChatService {
  static async processMessages(messages: Message[]): Promise<StreamingTextResponse> {
    // Pega a última mensagem do usuário para busca RAG
    const lastUserMessage = messages.filter(m => m.role === 'user').pop()
    let enhancedSystemPrompt = SYSTEM_PROMPT
    
    // Busca contexto RAG se houver mensagem do usuário
    if (lastUserMessage) {
      const ragContext = await ragClient.getContextForLLM(lastUserMessage.content)
      if (ragContext) {
        enhancedSystemPrompt = `${SYSTEM_PROMPT}\n\n${ragContext}`
      }
    }

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