import { NextResponse } from 'next/server'
import { memoryService } from '@/lib/services/memory-service'

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url)
  const sessionId = searchParams.get('sessionId') || 'contabil-chat'
  
  const history = memoryService.getConversationHistory(sessionId)
  
  return NextResponse.json({
    sessionId,
    messageCount: history.length,
    messages: history,
    sessionCount: memoryService.getSessionCount()
  })
}

export async function DELETE(req: Request) {
  const { searchParams } = new URL(req.url)
  const sessionId = searchParams.get('sessionId') || 'contabil-chat'
  
  memoryService.clearSession(sessionId)
  
  return NextResponse.json({
    message: 'Memória da sessão limpa',
    sessionId
  })
}