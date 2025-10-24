/**
 * Serviço de memória conversacional para o Conta Fácil
 */

import type { Message } from '@/lib/types/chat'

interface ConversationMemory {
  messages: Message[]
  context: string[]
  lastActivity: Date
}

class MemoryService {
  private conversations = new Map<string, ConversationMemory>()
  private readonly MAX_MESSAGES = 20 // Últimas 20 mensagens
  private readonly MAX_CONTEXT = 5   // Últimos 5 contextos RAG
  private readonly CLEANUP_INTERVAL = 30 * 60 * 1000 // 30 minutos

  constructor() {
    // Limpeza automática de conversas antigas
    setInterval(() => this.cleanup(), this.CLEANUP_INTERVAL)
  }

  addMessage(sessionId: string, message: Message, ragContext?: string) {
    let memory = this.conversations.get(sessionId)
    
    if (!memory) {
      memory = {
        messages: [],
        context: [],
        lastActivity: new Date()
      }
    }

    // Adiciona mensagem
    memory.messages.push(message)
    
    // Mantém apenas as últimas mensagens
    if (memory.messages.length > this.MAX_MESSAGES) {
      memory.messages = memory.messages.slice(-this.MAX_MESSAGES)
    }

    // Adiciona contexto RAG se fornecido
    if (ragContext && ragContext.trim()) {
      memory.context.push(ragContext)
      if (memory.context.length > this.MAX_CONTEXT) {
        memory.context = memory.context.slice(-this.MAX_CONTEXT)
      }
    }

    memory.lastActivity = new Date()
    this.conversations.set(sessionId, memory)
  }

  getConversationHistory(sessionId: string): Message[] {
    const memory = this.conversations.get(sessionId)
    return memory?.messages || []
  }

  getRelevantContext(sessionId: string, currentQuery: string): string {
    const memory = this.conversations.get(sessionId)
    if (!memory) return ''

    // Combina contextos RAG anteriores
    const ragContext = memory.context.join('\n\n')
    
    // Últimas 3 interações para contexto conversacional
    const recentMessages = memory.messages.slice(-6) // 3 pares pergunta/resposta
    const conversationContext = recentMessages
      .map(m => `${m.role === 'user' ? 'Usuário' : 'Conta Fácil'}: ${m.content}`)
      .join('\n')

    return `HISTÓRICO DA CONVERSA:
${conversationContext}

CONTEXTOS RAG ANTERIORES:
${ragContext}

PERGUNTA ATUAL: ${currentQuery}`
  }

  private cleanup() {
    const now = new Date()
    const cutoff = new Date(now.getTime() - (2 * 60 * 60 * 1000)) // 2 horas

    for (const [sessionId, memory] of this.conversations.entries()) {
      if (memory.lastActivity < cutoff) {
        this.conversations.delete(sessionId)
      }
    }
  }

  clearSession(sessionId: string) {
    this.conversations.delete(sessionId)
  }

  getSessionCount(): number {
    return this.conversations.size
  }
}

export const memoryService = new MemoryService()