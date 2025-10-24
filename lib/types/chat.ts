export interface Message {
  role: 'system' | 'user' | 'assistant'
  content: string
}

export interface ChatRequest {
  messages: Message[]
}

export interface ChatError {
  error: string
  status?: number
}