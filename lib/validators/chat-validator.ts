import type { Message, ChatRequest } from '@/lib/types/chat'

export class ChatValidator {
  static validateRequest(body: unknown): ChatRequest {
    if (!body || typeof body !== 'object') {
      throw new Error('Invalid request body')
    }

    const { messages } = body as any

    if (!messages || !Array.isArray(messages)) {
      throw new Error('Invalid messages format')
    }

    if (messages.length === 0) {
      throw new Error('Messages array cannot be empty')
    }

    const validatedMessages: Message[] = messages.map((msg, index) => {
      if (!msg || typeof msg !== 'object') {
        throw new Error(`Invalid message at index ${index}`)
      }

      const { role, content } = msg

      if (!role || !['user', 'assistant', 'system'].includes(role)) {
        throw new Error(`Invalid role at index ${index}`)
      }

      if (!content || typeof content !== 'string') {
        throw new Error(`Invalid content at index ${index}`)
      }

      return { role, content }
    })

    return { messages: validatedMessages }
  }
}