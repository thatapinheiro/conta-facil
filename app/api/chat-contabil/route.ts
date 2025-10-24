import { NextResponse } from 'next/server'
import { ChatService } from '@/lib/services/chat-service'
import { ChatValidator } from '@/lib/validators/chat-validator'
import { memoryService } from '@/lib/services/memory-service'

export const runtime = 'edge'

export async function POST(req: Request) {
  try {
    const body = await req.json()
    const { messages } = ChatValidator.validateRequest(body)
    
    // Gera ID da sessão baseado no chat ID ou cria um padrão
    const sessionId = body.sessionId || 'contabil-chat'
    
    const response = await ChatService.processMessages(messages, sessionId)
    
    // Salva resposta da IA na memória (será feito via streaming)
    const lastAssistantMessage = messages.filter(m => m.role === 'assistant').pop()
    if (lastAssistantMessage) {
      memoryService.addMessage(sessionId, lastAssistantMessage)
    }
    
    return response
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Unknown error'
    const status = message.includes('Invalid') ? 400 : 502
    
    return NextResponse.json({ error: message }, { status })
  }
}