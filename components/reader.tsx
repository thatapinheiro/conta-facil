"use client"

import { useEffect, useState } from "react"
import { Moon, Sun, Monitor } from "lucide-react"
import { Button } from "@/components/ui/button"

export function Reader({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark' | 'system'>('system')

  useEffect(() => {
    const root = window.document.documentElement
    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    
    root.classList.remove('light', 'dark')
    
    if (theme === 'system') {
      root.classList.add(systemTheme)
    } else {
      root.classList.add(theme)
    }
  }, [theme])

  const themes = [
    { value: 'light', icon: Sun, label: 'Claro' },
    { value: 'dark', icon: Moon, label: 'Escuro' },
    { value: 'system', icon: Monitor, label: 'Sistema' }
  ] as const

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 dark:from-slate-900 dark:to-slate-800 transition-colors duration-300">
      <div className="fixed top-4 right-4 z-50 flex gap-1 bg-white/80 dark:bg-slate-800/80 backdrop-blur-sm rounded-lg p-1 border shadow-sm">
        {themes.map(({ value, icon: Icon }) => (
          <Button
            key={value}
            variant={theme === value ? "default" : "ghost"}
            size="sm"
            onClick={() => setTheme(value)}
            className="h-8 w-8 p-0"
          >
            <Icon className="h-4 w-4" />
          </Button>
        ))}
      </div>
      {children}
    </div>
  )
}