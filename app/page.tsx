import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Bot, Calculator, FileText, Zap, ArrowRight } from "lucide-react"

export default function Home() {
  const features = [
    {
      icon: Bot,
      title: "IA Especializada",
      description: "Assistente contábil com conhecimento profundo em tributação brasileira"
    },
    {
      icon: Calculator,
      title: "Cálculos Automáticos",
      description: "Simples Nacional, Lucro Presumido, MEI e muito mais"
    },
    {
      icon: FileText,
      title: "Consultoria Fiscal",
      description: "Orientações sobre obrigações, prazos e legislação"
    },
    {
      icon: Zap,
      title: "Respostas Rápidas",
      description: "Streaming em tempo real com explicações detalhadas"
    }
  ]

  return (
    <div className="min-h-screen">
      <main className="container mx-auto px-4 py-16">
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 px-4 py-2 rounded-full text-sm font-medium mb-6">
            <Bot className="w-4 h-4" />
            Conta Fácil
          </div>
          
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-6 leading-tight">
            Conta Fácil
            <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent"> IA Contábil</span>
          </h1>
          
          <p className="text-xl text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto">
            Seu assistente especializado em contabilidade brasileira. Cálculos tributários, consultoria fiscal e orientações profissionais com IA.
          </p>
          
          <Link href="/chat">
            <Button size="lg" className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-3 text-lg">
              Começar Consulta
              <ArrowRight className="ml-2 w-5 h-5" />
            </Button>
          </Link>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {features.map((feature, index) => (
            <Card key={index} className="p-6 hover:shadow-lg transition-shadow border-0 bg-white/50 dark:bg-slate-800/50 backdrop-blur-sm">
              <feature.icon className="w-12 h-12 text-blue-600 mb-4" />
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                {feature.description}
              </p>
            </Card>
          ))}
        </div>

        <Card className="p-8 text-center bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 border-0">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            Pronto para começar?
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-6">
            Faça suas perguntas sobre contabilidade e receba respostas precisas e detalhadas.
          </p>
          <Link href="/chat">
            <Button variant="outline" size="lg" className="border-blue-200 hover:bg-blue-50 dark:border-blue-800 dark:hover:bg-blue-900/20">
              Iniciar Chat
            </Button>
          </Link>
        </Card>
      </main>
    </div>
  )
}
