"""Base de conhecimento contábil brasileira OTIMIZADA"""

KNOWLEDGE_BASE = [
    # ----------------------------------------------------------------------
    # MEI - CONSOLIDADO E ATUALIZADO (Substitui mei_001, mei_002, mei_003, mei_004, mei_005, mei_006, mei_007)
    # ----------------------------------------------------------------------
    {
        "id": "mei_001_geral",
        "categoria": "MEI",
        "titulo": "Limites, Composição e Obrigações do DAS-MEI",
        "conteudo": "O limite anual do MEI é R$ 81.000. O DAS é obrigatório (vencimento dia 20) e composto por 5% do Salário Mínimo (INSS) + R$ 1 (ICMS) ou R$ 5 (ISS). A DASN-SIMEI (Declaração Anual) é obrigatória e tem prazo até 31 de maio. O não pagamento gera multas, juros e exclusão.",
        "tags": ["mei", "das", "limite", "inss", "dasn-simei", "prazo", "multa"]
    },
    {
        "id": "mei_002_desenquadramento",
        "categoria": "MEI",
        "titulo": "Regras de Desenquadramento por Faturamento e Outros",
        "conteudo": "Desenquadramento por excesso de faturamento (acima de R$ 97.200) é obrigatório e retroativo a janeiro. O MEI também é desenquadrado se exercer atividade não permitida, abrir filial, ou ter sócio. O MEI pode ter apenas 1 empregado, recebendo SM ou piso, e deve recolher 3% INSS patronal e 8% FGTS sobre esse salário.",
        "tags": ["desenquadramento", "excesso", "retroativo", "socio", "empregado", "inss patronal"]
    },
    # ----------------------------------------------------------------------
    # SIMPLES NACIONAL - CONSOLIDADO (Simples_001, Simples_002, Simples_004 e Fator R)
    # ----------------------------------------------------------------------
    {
        "id": "simples_001_calculo",
        "categoria": "Simples Nacional",
        "titulo": "Limites e Cálculo da Alíquota Efetiva",
        "conteudo": "Limite anual R$ 4.800.000 (Sublimite R$ 3.600.000). O cálculo do DAS utiliza a Alíquota Efetiva: (RBT12 x Alíquota Nominal - Parcela a Deduzir) / RBT12. O Fator R (Folha/Receita nos últimos 12 meses) deve ser >= 28% para tributação no Anexo III.",
        "tags": ["simples", "limite", "rbt12", "aliquota efetiva", "fator r", "anexo"]
    },
    {
        "id": "simples_002_acessorias", # Mantém Simples_003
        "categoria": "Simples Nacional",
        "titulo": "Obrigações Acessórias do Simples Nacional",
        "conteudo": "As principais obrigações são: PGDAS-D (mensal, para apuração do DAS), DEFIS (anual, informações econômicas e fiscais) e, se tiver funcionário, eSocial e DCTFWeb. Empresas do Simples não entregam ECF, ECD ou EFD ICMS/IPI (salvo exceções).",
        "tags": ["simples", "obrigacoes", "defis", "pgdas-d", "esocial", "acessorias"]
    },
    # ----------------------------------------------------------------------
    # LUCRO PRESUMIDO - ATUALIZADO (Presumido_001 e Presumido_002)
    # ----------------------------------------------------------------------
    {
        "id": "presumido_001_completo",
        "categoria": "Lucro Presumido",
        "titulo": "Cálculo, Adicional e Bases de Presunção",
        "conteudo": "IRPJ (15%) e CSLL (9%) incidem sobre a base presumida (Comércio 8%; Serviços 32%). Há adicional de 10% de IRPJ sobre o lucro presumido que exceder R$ 60.000/trimestre. O regime de PIS (0,65%) e COFINS (3%) é cumulativo. Pode optar pelo regime de Caixa ou Competência.",
        "tags": ["presumido", "irpj", "csll", "bases", "adicional", "caixa", "competencia"]
    },
    # ----------------------------------------------------------------------
    # LUCRO REAL (Tributos_002 e Tributos_001)
    # ----------------------------------------------------------------------
    {
        "id": "lucroreal_001",
        "categoria": "Lucro Real",
        "titulo": "IRPJ, CSLL e Compensação de Prejuízos",
        "conteudo": "IRPJ (15% + adicional de 10%) e CSLL (9%) são apurados sobre o Lucro Contábil ajustado (adições/exclusões). O regime permite a compensação de Prejuízos Fiscais, limitada a 30% do lucro real do período. PIS/COFINS são Não-Cumulativos (1,65% e 7,6%) com direito a crédito.",
        "tags": ["lucro real", "irpj", "csll", "prejuizo", "pis", "cofins", "nao cumulativo"]
    },
    # ----------------------------------------------------------------------
    # IMPOSTOS ESPECÍFICOS (ICMS, ISS)
    # ----------------------------------------------------------------------
    {
        "id": "icms_001_completo", # Atualiza icms_001
        "categoria": "ICMS/IPI",
        "titulo": "ICMS-ST, DIFAL e Não-Cumulatividade (CIAP)",
        "conteudo": "ICMS-ST é a antecipação por Substituto (cálculo por MVA). O DIFAL é o imposto ao destino em venda a não-contribuinte. A Não-Cumulatividade permite crédito sobre entradas, sendo o crédito de Imobilizado apropriado em 48 parcelas (CIAP).",
        "tags": ["icms", "difal", "st", "mva", "ciap", "credito"]
    },
    {
        "id": "iss_001_local", # Mantém iss_001
        "categoria": "ISS",
        "titulo": "ISS - Alíquotas e Regra de Localização",
        "conteudo": "Alíquota mínima 2%, máxima 5% (LC 116/2003). A regra geral é que o imposto é devido no município do estabelecimento prestador, salvo exceções legais onde incide no local da prestação (ex: construção, limpeza, guincho).",
        "tags": ["iss", "servicos", "retencao", "aliquota", "lc 116"]
    },
    # ----------------------------------------------------------------------
    # FOLHA DE PAGAMENTO E TRABALHISTA (folha_001, folha_002, folha_003, folha_004 + Adicionais)
    # ----------------------------------------------------------------------
    {
        "id": "folha_001_encargos",
        "categoria": "Folha Pagamento",
        "titulo": "Encargos Patronais e Desconto INSS Empregado",
        "conteudo": "Encargos Patronais: INSS Empresa (20% ou CPRB), RAT (1-3% x FAP) e Terceiros. FGTS: 8%. INSS Empregado é calculado por alíquotas progressivas (7,5% a 14%) sobre faixas salariais, retido na fonte. Teto de contribuição anualmente reajustado.",
        "tags": ["folha", "inss", "fgts", "rat", "patronal", "progressiva"]
    },
    {
        "id": "folha_002_rotinas",
        "categoria": "Folha Pagamento",
        "titulo": "Rotinas de Admissão, Férias e 13º Salário",
        "conteudo": "Admissão exige registro antes do início e envio do S-2200/S-2190 ao eSocial. Férias: 30 dias após 12 meses, pagamento (1/3 + salário) até 2 dias antes do início. 13º Salário: 1ª parcela até 30/Nov, 2ª até 20/Dez.",
        "tags": ["admissao", "ferias", "decimo terceiro", "esocial", "clt"]
    },
    {
        "id": "folha_003_rescisao",
        "categoria": "Folha Pagamento - Rescisão",
        "titulo": "Modalidades de Rescisão Contratual (CLT)",
        "conteudo": "As principais são: Sem Justa Causa (aviso prévio, multa 40% FGTS); Por Justa Causa (perde quase todos os direitos); Pedido de Demissão; e Rescisão por Acordo (Lei 13.467/17 - metade do aviso, multa 20% FGTS, 80% do FGTS liberado).",
        "tags": ["rescisao", "justa causa", "acordo", "fgts", "aviso previo", "clt"]
    },
    {
        "id": "folha_004_jornada",
        "categoria": "Folha Pagamento - Trabalhista",
        "titulo": "Jornada de Trabalho e Horas Extras",
        "conteudo": "Jornada padrão de 8h/dia, 44h/semana, com limite de 2h extras/dia. Horas extras são remuneradas com adicional mínimo de 50% (100% em domingos/feriados, salvo compensação).",
        "tags": ["jornada", "horas extras", "adicional", "clt"]
    },
    # ----------------------------------------------------------------------
    # OBRIGAÇÕES ACESSÓRIAS (Consolidações e Prazos)
    # ----------------------------------------------------------------------
    {
        "id": "obrigacao_001_prazos", # Mantém prazos_001
        "categoria": "Obrigações Acessórias - Prazos",
        "titulo": "Vencimentos de Tributos Comuns",
        "conteudo": "INSS/DCTFWeb: dia 20. PIS/COFINS: dia 25. FGTS: dia 7. IRPJ/CSLL Presumido: último dia útil do mês seguinte ao trimestre. ICMS/ISS: conforme legislação estadual/municipal. EFD-Reinf: dia 15.",
        "tags": ["prazos", "vencimento", "calendario", "tributario", "dctfweb", "reinf"]
    },
    {
        "id": "obrigacao_002_sped", # Mantém sped_001, sped_002, sped_003, reinf_001
        "categoria": "Obrigações Acessórias - SPED",
        "titulo": "ECD, ECF, EFD-Reinf e EFD ICMS/IPI",
        "conteudo": "SPED Contábil (ECD/Diário e Razão - Prazo Maio). SPED Fiscal (EFD ICMS/IPI - mensal, conforme UF). ECF (Substitui DIPJ - Prazo Julho). EFD-Reinf complementa eSocial com retenções e contribuições (Prazo dia 15).",
        "tags": ["sped", "ecd", "ecf", "reinf", "icms", "ipi", "obrigacao"]
    },
    {
        "id": "obrigacao_003_fiscal", # Mantém obrigacao_005, obrigacao_006
        "categoria": "Obrigações Acessórias - Fiscalização",
        "titulo": "CND, e-CAC e Caixa Postal",
        "conteudo": "A CND atesta a regularidade fiscal para licitações e créditos. O e-CAC (Receita Federal) é o portal de serviços e fiscalização. A Caixa Postal no e-CAC é o canal oficial de intimações e deve ser acompanhada diariamente.",
        "tags": ["cnd", "certidao", "e-cac", "rfb", "intimacao"]
    },
    # ----------------------------------------------------------------------
    # CONTABILIDADE GERAL (societario_001, 002, 003, 004, 005, 006, 008, 009 + CPC)
    # ----------------------------------------------------------------------
    {
        "id": "contabil_001_bp_dre", # Consolida societario_001, 002, 006
        "categoria": "Contabilidade Geral",
        "titulo": "Estrutura do BP, DRE e PL",
        "conteudo": "BP: Ativo = Passivo + PL. Ativo e Passivo são Circulante/Não Circulante. PL (Capital, Reservas, Prejuízos) é o valor residual. DRE: Receita Bruta - Deduções = Receita Líquida; - CMV/CPV = Lucro Bruto; - Despesas Operacionais = Lucro Antes IR/CSLL.",
        "tags": ["balanco", "dre", "pl", "ativo", "passivo", "estrutura"]
    },
    {
        "id": "contabil_002_principios", # Atualiza societario_003
        "categoria": "Contabilidade Geral",
        "titulo": "Princípio da Competência (CPC 00) e Caixa",
        "conteudo": "Competência (obrigatório para contabilidade fiscal): Reconhecimento de receita/despesa na ocorrência do fato gerador. Caixa: Reconhecimento apenas pelo fluxo financeiro (recebimento/pagamento). O CPC 00 reitera a competência como base fundamental.",
        "tags": ["competencia", "caixa", "regime", "cpc 00"]
    },
    {
        "id": "contabil_003_ativo", # Consolida societario_004, 005, cpc_001, cpc_002
        "categoria": "Contabilidade Geral - Ativo",
        "titulo": "CPC 27 (Imobilizado), CPC 04 (Intangível) e Impairment",
        "conteudo": "Imobilizado (CPC 27/Depreciação) e Intangível (CPC 04/Amortização) são ativos de longo prazo. Ambos devem ser submetidos ao Teste de Recuperabilidade (Impairment - CPC 01) para verificar se o valor contábil excede o valor recuperável.",
        "tags": ["depreciacao", "amortizacao", "imobilizado", "intangivel", "impairment", "cpc"]
    },
    {
        "id": "contabil_004_dfc_provisoes", # Consolida societario_008, 009
        "categoria": "Contabilidade Geral - Obrigações",
        "titulo": "DFC (CPC 03) e Provisões/Contingentes (CPC 25)",
        "conteudo": "DFC (Obrigatória): Detalha o fluxo de caixa em Operacionais, Investimento e Financiamento (métodos Direto/Indireto). Provisão (CPC 25): Obrigação presente com saída de recursos provável. Passivo Contingente: Possível obrigação não reconhecida (baixa probabilidade).",
        "tags": ["dfc", "fluxo de caixa", "provisao", "passivo", "contingente", "cpc"]
    },
    # ----------------------------------------------------------------------
    # CUSTOS E GERENCIAL (custos_001, 002, 003, 004 + gerencial_001, 002)
    # ----------------------------------------------------------------------
    {
        "id": "custos_001_completo",
        "categoria": "Contabilidade de Custos",
        "titulo": "Classificação, Custeio (Absorção/Variável) e Ponto de Equilíbrio",
        "conteudo": "Custos Fixos (não variam) vs. Variáveis (variam com produção). Absorção (fiscal, inclui fixos/variáveis) vs. Variável (gerencial, inclui só variáveis). PE (Ponto de Equilíbrio): Vendas para lucro zero (PE = Fixos / Margem de Contribuição Unitária).",
        "tags": ["custos", "fixos", "variaveis", "absorcao", "pe", "margem de contribuicao"]
    },
    {
        "id": "custos_002_gerencial",
        "categoria": "Contabilidade Gerencial",
        "titulo": "Orçamento Empresarial e Alavancagem Operacional",
        "conteudo": "O orçamento (Budget) projeta receitas e despesas para controle de desempenho. A Margem de Contribuição (Receita - Variáveis) mede o que sobra para cobrir fixos. Alavancagem operacional mede o impacto da variação de vendas no lucro.",
        "tags": ["orcamento", "budget", "margem", "alavancagem", "gerencial"]
    },
    # ----------------------------------------------------------------------
    # TÓPICOS GERAIS E NOVOS
    # ----------------------------------------------------------------------
    {
        "id": "geral_001_remuneracao", # Mantém societario_007
        "categoria": "Remuneração Sócios",
        "titulo": "Pró-Labore vs. Distribuição de Lucros",
        "conteudo": "Pró-Labore é a remuneração pelo trabalho, obrigatória e sujeita a INSS e IRRF. Distribuição de Lucros é a parte do resultado, isenta de INSS/IRRF, desde que a empresa mantenha escrituração contábil e apure o lucro conforme a legislação.",
        "tags": ["pro-labore", "distribuicao de lucros", "inss", "irrf", "socio"]
    },
    {
        "id": "geral_002_planejamento", # Mantém tributos_003
        "categoria": "Tributação",
        "titulo": "Planejamento Tributário (Legalidade e Elisão)",
        "conteudo": "Planejamento tributário visa reduzir legalmente a carga fiscal pela escolha do regime, aproveitamento de créditos e incentivos. Deve evitar a elisão abusiva, respeitando o princípio da legalidade.",
        "tags": ["planejamento", "tributario", "carga tributaria", "elisao", "regime"]
    },
    {
        "id": "geral_003_reforma", # Mantém reforma_001
        "categoria": "Reforma Tributária",
        "titulo": "Visão Geral da Reforma (EC 132/2023)",
        "conteudo": "A EC 132/2023 substitui 5 tributos (PIS, COFINS, IPI, ICMS, ISS) por 3 (IBS, CBS e Imposto Seletivo). O novo sistema (IVA Dual) terá um período de transição que se iniciará em 2026.",
        "tags": ["reforma", "iva", "ibs", "cbs", "imposto seletivo", "transicao"]
    },
    {
        "id": "geral_004_liquidez", # Consolida analise_001, analise_002
        "categoria": "Análise Financeira",
        "titulo": "Índices de Liquidez (Corrente e Seca)",
        "conteudo": "Liquidez Corrente (Ativo Circulante / Passivo Circulante) indica capacidade de pagamento de curto prazo. Liquidez Seca ((AC - Estoques) / PC) oferece visão mais conservadora ao excluir os estoques, menos líquidos.",
        "tags": ["liquidez", "indice", "analise", "curto prazo", "capital de giro"]
    }
]

# As funções auxiliares permanecem as mesmas, mas agora operam sobre a base atualizada:

def get_all_documents():
    """Retorna todos os documentos da base de conhecimento"""
    return [doc["conteudo"] for doc in KNOWLEDGE_BASE]

def get_document_by_id(doc_id: str):
    """Busca documento por ID"""
    return next((doc for doc in KNOWLEDGE_BASE if doc["id"] == doc_id), None)

def search_by_category(categoria: str):
    """Busca documentos por categoria"""
    return [doc for doc in KNOWLEDGE_BASE if doc["categoria"].lower() == categoria.lower()]