/**
 * Controle de precisão para evitar respostas imprecisas
 */

import type { Message } from '@/lib/types/chat'

interface PrecisionConfig {
  temperature: number
  maxTokens: number
  strictMode: boolean
  requireRAG: boolean
}

class PrecisionControl {
  private config: PrecisionConfig = {
    temperature: 0.1,      // Baixa criatividade
    maxTokens: 800,        // Respostas concisas
    strictMode: true,      // Modo rigoroso
    requireRAG: true       // Exige contexto RAG
  }

  enhanceSystemPrompt(basePrompt: string, hasRAGContext: boolean): string {
    const precisionRules = `
REGRAS DE PRECISÃO OBRIGATÓRIAS:

1. APENAS RESPONDA se tiver CERTEZA da informação
2. Se não souber, diga: "Não tenho informação precisa sobre isso. Consulte um contador."
3. SEMPRE cite valores, percentuais e prazos EXATOS quando disponíveis
4. NÃO invente números, datas ou alíquotas
5. Use APENAS informações da base de conhecimento fornecida
6. Se a pergunta não for sobre contabilidade brasileira, responda: "Sou especializado apenas em contabilidade brasileira."

FORMATO OBRIGATÓRIO:
- Resposta direta e objetiva
- Máximo 3 parágrafos
- Cite a fonte legal quando possível
- Termine com: "Para casos específicos, consulte um contador habilitado."

${!hasRAGContext ? 'ATENÇÃO: Sem contexto específico disponível. Seja EXTRA cauteloso.' : ''}
`

    return `${basePrompt}\n\n${precisionRules}`
  }

  validateResponse(response: string): { isValid: boolean; issues: string[] } {
    const issues: string[] = []
    
    // Verifica se contém números suspeitos (muito específicos sem fonte)
    const suspiciousNumbers = /\d{1,2}\.\d{3}\.\d{3},\d{2}|\d+,\d{4,}/g
    if (suspiciousNumbers.test(response)) {
      issues.push('Números muito específicos sem fonte')
    }

    // Verifica se contém frases vagas
    const vaguePhases = [
      'geralmente', 'normalmente', 'costuma ser', 'pode ser que',
      'acredito que', 'imagino que', 'provavelmente'
    ]
    
    const hasVagueness = vaguePhases.some(phrase => 
      response.toLowerCase().includes(phrase)
    )
    
    if (hasVagueness) {
      issues.push('Contém linguagem vaga ou incerta')
    }

    // Verifica se é muito longa (pode indicar "viagem")
    if (response.length > 2000) {
      issues.push('Resposta muito extensa')
    }

    // Verifica se contém informações não contábeis
    const nonAccountingTerms = [
      'futebol', 'política', 'receita culinária', 'medicina',
      'engenharia', 'arquitetura', 'música', 'arte'
    ]
    
    const hasOffTopic = nonAccountingTerms.some(term =>
      response.toLowerCase().includes(term)
    )
    
    if (hasOffTopic) {
      issues.push('Contém tópicos não relacionados à contabilidade')
    }

    return {
      isValid: issues.length === 0,
      issues
    }
  }

  getOllamaParams(): Record<string, any> {
    return {
      temperature: this.config.temperature,
      max_tokens: this.config.maxTokens,
      top_p: 0.9,
      frequency_penalty: 0.1,
      presence_penalty: 0.1
    }
  }

  updateConfig(newConfig: Partial<PrecisionConfig>) {
    this.config = { ...this.config, ...newConfig }
  }

  getConfig(): PrecisionConfig {
    return { ...this.config }
  }
}

export const precisionControl = new PrecisionControl()