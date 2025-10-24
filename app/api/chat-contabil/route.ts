import { NextResponse } from 'next/server'
import { ChatService } from '@/lib/services/chat-service'
import { ChatValidator } from '@/lib/validators/chat-validator'

export const runtime = 'edge'

export async function POST(req: Request) {
  try {
    const body = await req.json()
    const { messages } = ChatValidator.validateRequest(body)
    
    return await ChatService.processMessages(messages)
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Unknown error'
    const status = message.includes('Invalid') ? 400 : 502
    
    return NextResponse.json({ error: message }, { status })
  }
}