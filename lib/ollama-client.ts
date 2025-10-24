import type { Message } from '@/lib/types/chat'

const OLLAMA_HOST = process.env.OLLAMA_HOST || 'http://localhost:11434'
const MODEL = process.env.OLLAMA_MODEL || 'mistral'

export async function streamCompletion(messages: Message[]): Promise<Response> {
  const response = await fetch(`${OLLAMA_HOST}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: MODEL,
      messages,
      stream: true,
    }),
  })

  if (!response.ok) {
    throw new Error(`Ollama API error: ${response.status}`)
  }

  if (!response.body) {
    throw new Error('Response body is null')
  }

  return response
}

export async function listModels() {
  try {
    const response = await fetch(`${OLLAMA_HOST}/api/tags`)
    if (!response.ok) {
      throw new Error(`Failed to list models: ${response.statusText}`)
    }
    return response.json()
  } catch (error) {
    console.error('[List Models Error]:', error)
    throw error
  }
}