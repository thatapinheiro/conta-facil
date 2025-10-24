"use client"

import { useChat } from "ai/react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Send, Bot, User, Loader2, Home, Sparkles, Square } from "lucide-react"
import Link from "next/link"

export default function ChatPage() {
  const { messages, input, handleInputChange, handleSubmit, isLoading, stop, append } = useChat({
    api: "/api/chat-contabil",
    id: "contabil-chat",
  })

  const examples = [
    "Como calcular impostos para MEI?",
    "Diferença entre Simples Nacional e Lucro Presumido",
    "Prazos de entrega do IRPJ",
    "Cálculo de pró-labore"
  ]

  const handleExampleClick = (example: string) => {
    append({ role: 'user', content: example })
  }

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      <header className="flex-none bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm px-4 py-3 border-b border-slate-200/50 dark:border-slate-700/50">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
              <Bot className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-gray-900 dark:text-white">Conta Fácil</h1>
              <p className="text-sm text-gray-600 dark:text-gray-400">IA Contábil especializada</p>
            </div>
          </div>
          <Link href="/">
            <Button variant="ghost" size="sm">
              <Home className="w-4 h-4 mr-2" />
              Início
            </Button>
          </Link>
        </div>
      </header>

      <main className="flex-1 p-4 overflow-hidden">
        <div className="h-full max-w-4xl mx-auto">
          <Card className="h-full border-0 bg-white/50 dark:bg-slate-800/50 backdrop-blur-sm shadow-xl">
            <div className="flex flex-col h-full">
              <ScrollArea className="flex-1 overflow-y-auto">
                <div className="p-6 overflow-y-auto">
                  {messages.length === 0 ? (
                    <div className="text-center py-12">
                      <div className="w-16 h-16 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
                        <Sparkles className="w-8 h-8 text-white" />
                      </div>
                      <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                        Como posso ajudar?
                      </h2>
                      <p className="text-gray-600 dark:text-gray-400 mb-8">
                        Faça perguntas sobre contabilidade, impostos e legislação brasileira
                      </p>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 max-w-2xl mx-auto">
                        {examples.map((example, index) => (
                          <Button
                            key={index}
                            variant="outline"
                            className="text-left h-auto p-4 border-slate-200 dark:border-slate-700 hover:bg-blue-50 dark:hover:bg-blue-900/20"
                            onClick={() => handleExampleClick(example)}
                            disabled={isLoading}
                          >
                            {example}
                          </Button>
                        ))}
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-6">
                      {messages.map((m) => (
                        <div
                          key={m.id}
                          className={`flex items-start gap-4 ${m.role === "user" ? "flex-row-reverse" : ""}`}
                        >
                          <div
                            className={`shrink-0 w-10 h-10 flex items-center justify-center rounded-full ${
                              m.role === "user" 
                                ? "bg-gradient-to-r from-blue-600 to-purple-600 text-white" 
                                : "bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300"
                            }`}
                          >
                            {m.role === "user" ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
                          </div>

                          <div
                            className={`flex-1 rounded-2xl px-4 py-3 max-w-[85%] ${
                              m.role === "user"
                                ? "bg-gradient-to-r from-blue-600 to-purple-600 text-white ml-4"
                                : "bg-slate-100 dark:bg-slate-700 text-slate-900 dark:text-slate-100 mr-4"
                            }`}
                          >
                            <div className="prose prose-sm dark:prose-invert max-w-none whitespace-pre-wrap">
                              {m.content}
                            </div>
                          </div>
                        </div>
                      ))}
                      {isLoading && (
                        <div className="flex items-start gap-4">
                          <div className="shrink-0 w-10 h-10 flex items-center justify-center rounded-full bg-slate-100 dark:bg-slate-700">
                            <Bot className="w-5 h-5 text-slate-600 dark:text-slate-300" />
                          </div>
                          <div className="flex-1 rounded-2xl px-4 py-3 bg-slate-100 dark:bg-slate-700 mr-4">
                            <div className="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                              <Loader2 className="w-4 h-4 animate-spin" />
                              Pensando...
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </ScrollArea>

              <div className="flex-none border-t border-slate-200/50 dark:border-slate-700/50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm p-4">
                <form onSubmit={handleSubmit} className="flex gap-3">
                  <Input
                    value={input}
                    onChange={handleInputChange}
                    placeholder="Digite sua pergunta sobre contabilidade..."
                    disabled={isLoading}
                    className="flex-1 border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                  {isLoading ? (
                    <Button 
                      type="button"
                      onClick={stop}
                      className="bg-red-600 hover:bg-red-700 text-white px-6"
                    >
                      <Square className="w-4 h-4" />
                    </Button>
                  ) : (
                    <Button 
                      type="submit" 
                      disabled={!input.trim()}
                      className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6"
                    >
                      <Send className="w-4 h-4" />
                    </Button>
                  )}
                </form>
              </div>
            </div>
          </Card>
        </div>
      </main>
    </div>
  )
}