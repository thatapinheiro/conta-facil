import { NextResponse } from 'next/server'
import { ragClient } from '@/lib/services/rag-client'

export async function GET() {
  const testQueries = [
    "Qual o limite do MEI?",
    "Como calcular Simples Nacional?", 
    "Prazos de PIS e COFINS",
    "Pergunta irrelevante sobre futebol"
  ]

  const results = []

  for (const query of testQueries) {
    try {
      const ragResult = await ragClient.search(query, 3)
      const contextResult = await ragClient.getContextForLLM(query)
      
      results.push({
        query,
        found_sources: ragResult.sources.length,
        categories: ragResult.sources.map(s => s.categoria),
        similarity_scores: ragResult.similarity_scores,
        has_context: contextResult.length > 0,
        context_length: contextResult.length
      })
    } catch (error) {
      results.push({
        query,
        error: error instanceof Error ? error.message : 'Unknown error'
      })
    }
  }

  return NextResponse.json({
    rag_service_status: await ragClient.healthCheck(),
    test_results: results,
    timestamp: new Date().toISOString()
  })
}