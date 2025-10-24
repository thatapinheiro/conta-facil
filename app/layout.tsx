import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { Reader } from '@/components/reader'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Conta Fácil - IA Contábil',
  description: 'Conta Fácil - Assistente contábil inteligente com IA',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR" suppressHydrationWarning>
      <body className={inter.className}>
        <Reader>{children}</Reader>
      </body>
    </html>
  )
}
