/**
 * Cliente para integração com serviço RAG Python
 */

interface RAGSearchRequest {
  query: string
  top_k?: number
}

interface RAGSearchResponse {
  context: string
  sources: Array<{
    id: string
    categoria: string
    titulo: string
  }>
  similarity_scores: number[]
}

interface RAGContextResponse {
  context: string
}

class RAGClient {
  private baseUrl: string

  constructor(baseUrl: string = 'http://localhost:8000') {
    this.baseUrl = baseUrl
  }

  async search(query: string, topK: number = 3): Promise<RAGSearchResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, top_k: topK })
      })

      if (!response.ok) {
        throw new Error(`RAG service error: ${response.status}`)
      }

      return await response.json()
    } catch (error) {
      console.error('RAG search failed:', error)
      return { context: '', sources: [], similarity_scores: [] }
    }
  }

  async getContextForLLM(query: string): Promise<string> {
    try {
      const response = await fetch(`${this.baseUrl}/context`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      })

      if (!response.ok) {
        throw new Error(`RAG service error: ${response.status}`)
      }

      const result: RAGContextResponse = await response.json()
      return result.context
    } catch (error) {
      console.error('RAG context failed:', error)
      return ''
    }
  }

  async healthCheck(): Promise<boolean> {
    try {
      const response = await fetch(`${this.baseUrl}/health`)
      return response.ok
    } catch {
      return false
    }
  }
}

export const ragClient = new RAGClient()