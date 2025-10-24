# 🤖 Consultor Contábil IA com RAG

Agente de IA especializado em consultoria contábil brasileira, utilizando RAG (Retrieval-Augmented Generation) e o AI SDK da Vercel.

## 🚀 Características

- **RAG (Retrieval-Augmented Generation)**: Busca informações em base de conhecimento contábil
- **Tools/Ferramentas**: Cálculos automáticos de impostos e consultas à legislação
- **API Gratuita**: Usa Vercel AI Gateway com modelos gratuitos (GPT-5-mini)
- **Interface Moderna**: Chat interativo com exemplos de perguntas
- **Conhecimento Especializado**: MEI, Simples Nacional, Lucro Presumido, Lucro Real, Pró-labore

## 🛠️ Tecnologias

- **Next.js 15** - Framework React
- **AI SDK v5** - Vercel AI SDK para LLMs
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **shadcn/ui** - Componentes UI

## 📚 Como Funciona o RAG

1. **Base de Conhecimento**: Informações contábeis estruturadas em `lib/rag-knowledge.ts`
2. **Busca Semântica**: Quando você faz uma pergunta, o sistema busca informações relevantes
3. **Contexto Enriquecido**: A IA usa as informações encontradas para dar respostas precisas
4. **Tools**: Ferramentas especializadas para cálculos e consultas específicas

## 🎯 Funcionalidades

### Tools Disponíveis

1. **buscarConhecimento**: Busca na base de conhecimento contábil
2. **calcularImposto**: Calcula impostos para MEI, Simples e Lucro Presumido
3. **buscarLegislacao**: Consulta legislação e normas contábeis

### Exemplos de Perguntas

- "Como calcular o IRPJ pelo lucro presumido?"
- "Quais são as obrigações fiscais de uma MEI?"
- "Explique a diferença entre Simples Nacional e Lucro Real"
- "Como fazer o cálculo de pró-labore?"
- "Calcule os impostos para um MEI com faturamento de R$ 5.000"

## 🔧 Expandindo a Base de Conhecimento

Para adicionar mais conhecimento ao RAG, edite o arquivo `lib/rag-knowledge.ts`:

\`\`\`typescript
export const baseConhecimentoExpandida: ConhecimentoContabil[] = [
  {
    id: 'novo-topico-001',
    categoria: 'Categoria',
    titulo: 'Título do Tópico',
    conteudo: 'Conteúdo detalhado...',
    tags: ['tag1', 'tag2'],
    referencias: ['Lei X', 'Norma Y'],
  },
  // ... mais itens
];
\`\`\`

## 🌐 API Gratuita

Este projeto usa o **Vercel AI Gateway** que fornece acesso gratuito a modelos como:
- OpenAI GPT-5-mini
- Anthropic Claude
- Google Gemini
- xAI Grok

Não é necessário configurar API keys! 🎉

## ⚠️ Aviso Legal

Este é um assistente educacional. Para decisões contábeis importantes, sempre consulte um contador profissional registrado no CRC.

## 📝 Próximos Passos

- [ ] Adicionar mais conteúdo à base de conhecimento
- [ ] Implementar embeddings para busca semântica avançada
- [ ] Adicionar integração com banco de dados vetorial (Pinecone, Supabase Vector)
- [ ] Criar ferramentas para mais cálculos (INSS, FGTS, etc)
- [ ] Adicionar upload de documentos para análise
- [ ] Implementar histórico de conversas
