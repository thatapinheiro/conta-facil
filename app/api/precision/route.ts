import { NextResponse } from 'next/server'
import { precisionControl } from '@/lib/services/precision-control'

export async function GET() {
  return NextResponse.json({
    config: precisionControl.getConfig(),
    message: 'Configuração atual de precisão'
  })
}

export async function POST(req: Request) {
  try {
    const body = await req.json()
    
    precisionControl.updateConfig(body)
    
    return NextResponse.json({
      config: precisionControl.getConfig(),
      message: 'Configuração de precisão atualizada'
    })
  } catch (error) {
    return NextResponse.json(
      { error: 'Erro ao atualizar configuração' },
      { status: 400 }
    )
  }
}