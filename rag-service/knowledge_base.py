"""Base de conhecimento contábil brasileira"""

KNOWLEDGE_BASE = [
    {
        "id": "mei_001",
        "categoria": "MEI",
        "titulo": "Limites e DAS do MEI",
        "conteudo": "MEI tem limite anual de R$ 81.000. DAS mensal: Comércio R$ 67, Serviços R$ 71, Comércio+Serviços R$ 72. Vencimento todo dia 20.",
        "tags": ["mei", "das", "limite", "vencimento"]
    },
    {
        "id": "simples_001", 
        "categoria": "Simples Nacional",
        "titulo": "Limites Simples Nacional",
        "conteudo": "Limite anual R$ 4.800.000. Sublimite estadual R$ 3.600.000. Anexos I a V com alíquotas progressivas. Cálculo: (RBT12 x Alíquota - Parcela Deduzir) / RBT12",
        "tags": ["simples", "limite", "anexo", "aliquota"]
    },
    {
        "id": "presumido_001",
        "categoria": "Lucro Presumido", 
        "titulo": "Cálculo Lucro Presumido",
        "conteudo": "IRPJ: Base presunção x 15% + 10% se > R$ 20.000/mês. CSLL: Base x 9%. PIS: 0,65%. COFINS: 3%. Bases: Comércio 8%/12%, Serviços 32%/32%, Transporte 16%/16%",
        "tags": ["presumido", "irpj", "csll", "pis", "cofins"]
    },
    {
        "id": "icms_001",
        "categoria": "ICMS",
        "titulo": "Cálculo ICMS",
        "conteudo": "Por dentro: Valor / (1 - alíquota). Por fora: Valor x alíquota. DIFAL: (Alíq destino - Alíq origem) x Base. ST: (Base ST x Alíq - ICMS próprio)",
        "tags": ["icms", "difal", "substituicao", "tributaria"]
    },
    {
        "id": "iss_001",
        "categoria": "ISS",
        "titulo": "ISS Serviços",
        "conteudo": "Alíquota mínima 2%, máxima 5%. Base = preço do serviço. Retenção na fonte quando aplicável. Local da prestação define município competente.",
        "tags": ["iss", "servicos", "retencao", "aliquota"]
    },
    {
        "id": "folha_001",
        "categoria": "Folha Pagamento",
        "titulo": "Encargos Folha",
        "conteudo": "INSS Empresa: 20%. RAT: 1%, 2% ou 3% x FAP. FGTS: 8%. Terceiros conforme FPAS. INSS Empregado: tabela progressiva até R$ 7.507,49",
        "tags": ["folha", "inss", "fgts", "rat", "terceiros"]
    },
    {
        "id": "prazos_001",
        "categoria": "Prazos",
        "titulo": "Vencimentos Tributos",
        "conteudo": "PIS/COFINS: dia 25. INSS: dia 20. FGTS: dia 7. IRPJ/CSLL Presumido: último dia útil do mês seguinte ao trimestre. ICMS/ISS: conforme estado/município",
        "tags": ["prazos", "vencimento", "calendario", "tributario"]
    },
    {
    "id": "societario_001",
    "categoria": "Contabilidade Geral",
    "titulo": "Estrutura do Balanço Patrimonial (BP)",
    "conteudo": "BP: Ativo (Bens e Direitos, ordem decrescente de liquidez) = Passivo (Obrigações) + Patrimônio Líquido (PL). Ativo e Passivo divididos em Circulante (realizável/exigível até o próximo exercício) e Não Circulante.",
    "tags": ["balanco", "bp", "ativo", "passivo", "pl", "estrutura"]
},
{
    "id": "societario_002",
    "categoria": "Contabilidade Geral",
    "titulo": "Estrutura da Demonstração do Resultado (DRE)",
    "conteudo": "DRE apresenta a formação do resultado líquido. Sequência básica: Receita Bruta - Deduções = Receita Líquida. Receita Líquida - CMV/CPV/CSP = Lucro Bruto. Lucro Bruto - Despesas Operacionais = Lucro Antes IR/CSLL.",
    "tags": ["dre", "resultado", "lucro", "receita", "despesa"]
},
{
    "id": "societario_003",
    "categoria": "Contabilidade Geral",
    "titulo": "Princípio da Competência e Caixa",
    "conteudo": "Competência (CPC 00): Receitas e despesas são reconhecidas na ocorrência do fato gerador, independentemente de recebimento ou pagamento. Caixa: Reconhecimento apenas pelo fluxo financeiro (recebimento/pagamento).",
    "tags": ["competencia", "caixa", "regime", "cpc"]
},
{
    "id": "societario_004",
    "categoria": "Contabilidade Geral",
    "titulo": "Depreciação, Amortização e Exaustão",
    "conteudo": "Depreciação: Redução do valor de bens tangíveis (ex: máquinas) pelo uso ou obsolescência. Amortização: Redução do valor de bens intangíveis (ex: software). Exaustão: Redução do valor de recursos naturais (ex: jazidas).",
    "tags": ["depreciacao", "amortizacao", "exaustao", "ativo"]
},
{
    "id": "societario_005",
    "categoria": "Contabilidade Geral",
    "titulo": "Impairment (Teste de Recuperabilidade)",
    "conteudo": "NBC TG 01 (CPC 01) exige o teste de Impairment. Consiste em verificar se o valor contábil de um ativo excede seu valor recuperável (maior entre valor justo líquido de despesas de venda e valor em uso).",
    "tags": ["impairment", "cpc 01", "valor recuperavel", "ativo"]
},
{
    "id": "societario_006",
    "categoria": "Contabilidade Geral",
    "titulo": "Patrimônio Líquido (PL)",
    "conteudo": "O PL representa o valor residual dos ativos após deduzir todos os passivos. Composição: Capital Social, Reservas de Capital, Reservas de Lucros, Ajustes de Avaliação Patrimonial e Prejuízos Acumulados.",
    "tags": ["pl", "patrimonio", "capital social", "reservas"]
},
{
    "id": "analise_001",
    "categoria": "Análise Financeira",
    "titulo": "Índice de Liquidez Corrente",
    "conteudo": "Calculado por: Ativo Circulante / Passivo Circulante. Indica a capacidade da empresa de pagar suas dívidas de curto prazo (até o próximo exercício). Idealmente deve ser superior a 1.",
    "tags": ["liquidez", "indice", "analise", "curto prazo"]
},
{
    "id": "analise_002",
    "categoria": "Análise Financeira",
    "titulo": "Índice de Liquidez Seca",
    "conteudo": "Calculado por: (Ativo Circulante - Estoques) / Passivo Circulante. Exclui os estoques (menos líquidos) da análise. Oferece uma visão mais conservadora da capacidade de pagamento de curto prazo.",
    "tags": ["liquidez", "indice", "analise", "estoques"]
},
{
    "id": "custos_001",
    "categoria": "Contabilidade de Custos",
    "titulo": "Classificação de Custos",
    "conteudo": "Custos Fixos: Não variam com o volume de produção (ex: aluguel). Custos Variáveis: Variam proporcionalmente ao volume de produção (ex: matéria-prima). Custos Diretos: Facilmente rastreáveis ao produto (ex: mão de obra direta). Custos Indiretos: Necessitam rateio (ex: energia da fábrica).",
    "tags": ["custos", "fixos", "variaveis", "diretos", "indiretos"]
},
{
    "id": "custos_002",
    "categoria": "Contabilidade de Custos",
    "titulo": "Custeio por Absorção vs. Variável",
    "conteudo": "Custeio por Absorção: Imputa todos os custos (fixos e variáveis) aos produtos. Obrigatório para fins fiscais no Brasil. Custeio Variável: Considera apenas custos variáveis no produto; custos fixos vão direto para o resultado. Uso gerencial.",
    "tags": ["custeio", "absorcao", "variavel", "rateio", "gerencial"]
},
{
    "id": "custos_003",
    "categoria": "Contabilidade de Custos",
    "titulo": "Ponto de Equilíbrio (PE)",
    "conteudo": "PE é o volume de vendas onde a Receita Total se iguala ao Custo Total, resultando em lucro zero. PE = Custos e Despesas Fixas Totais / Margem de Contribuição Unitária. PE indica o mínimo que a empresa precisa vender para não ter prejuízo.",
    "tags": ["ponto de equilibrio", "pe", "margem de contribuicao", "lucro zero"]
},
{
    "id": "tributos_001",
    "categoria": "Tributação",
    "titulo": "Recuperação de Créditos de PIS/COFINS",
    "conteudo": "Regime Não Cumulativo (Lucro Real): Permite o crédito de PIS/COFINS (alíquotas 1,65% e 7,6%) sobre aquisições de bens e serviços essenciais à produção (insumos). É vedado o crédito no Lucro Presumido e Simples Nacional.",
    "tags": ["pis", "cofins", "credito", "nao cumulativo", "lucro real"]
},
{
    "id": "folha_002",
    "categoria": "Folha Pagamento",
    "titulo": "eSocial e DCTFWeb",
    "conteudo": "eSocial: Plataforma que unifica o envio das informações fiscais, previdenciárias e trabalhistas. DCTFWeb: Declaração que substituiu a GFIP para débitos previdenciários, sendo gerada a partir das informações do eSocial e da EFD-Reinf.",
    "tags": ["esocial", "dctfweb", "previdenciario", "obrigatorias"]
},
{
    "id": "societario_007",
    "categoria": "Remuneração Sócios",
    "titulo": "Pró-Labore vs. Distribuição de Lucros",
    "conteudo": "Pró-Labore é a remuneração dos sócios por seu trabalho na empresa, sendo obrigatório e sujeito à tributação de INSS (parte patronal e do sócio) e IRRF (se acima da isenção). Distribuição de Lucros é a parte do resultado líquido destinada aos sócios, sendo isenta de INSS e IRRF, desde que a empresa mantenha escrituração contábil e apure o lucro conforme a legislação.",
    "tags": ["pro-labore", "distribuicao de lucros", "inss", "irrf", "socio", "remuneracao"]
},
{
    "id": "sped_001",
    "categoria": "Obrigações Acessórias",
    "titulo": "SPED Fiscal (EFD ICMS/IPI)",
    "conteudo": "SPED Fiscal é uma obrigação acessória que reúne informações sobre ICMS e IPI. Deve ser transmitido mensalmente, geralmente até o dia 20 do mês subsequente. Inclui registros de entradas, saídas, inventário, apuração e ajustes.",
    "tags": ["sped", "efd", "icms", "ipi", "obrigacao"]
},
{
    "id": "sped_002",
    "categoria": "Obrigações Acessórias",
    "titulo": "ECD – Escrituração Contábil Digital",
    "conteudo": "A ECD substitui os livros Diário e Razão em formato digital. Obrigatória para empresas do Lucro Real e Lucro Presumido que distribuam lucros sem escrituração. Prazo: até o último dia útil de maio do ano seguinte ao exercício.",
    "tags": ["ecd", "sped", "contabilidade", "digital", "obrigacao"]
},
{
    "id": "sped_003",
    "categoria": "Obrigações Acessórias",
    "titulo": "ECF – Escrituração Contábil Fiscal",
    "conteudo": "Substitui a DIPJ e consolida informações contábeis e fiscais para cálculo do IRPJ e CSLL. Obrigatória para todas as pessoas jurídicas, inclusive imunes e isentas. Prazo: último dia útil de julho do ano seguinte.",
    "tags": ["ecf", "irpj", "csll", "sped", "obrigacao"]
},
{
    "id": "reinf_001",
    "categoria": "Obrigações Acessórias",
    "titulo": "EFD-Reinf",
    "conteudo": "Complementa o eSocial com informações sobre retenções e contribuições sem vínculo trabalhista. Inclui: serviços tomados/prestados, CPRB e comercialização da produção rural. Deve ser enviada até o dia 15 do mês seguinte.",
    "tags": ["efd-reinf", "retencao", "servicos", "previdencia", "obrigacao"]
},
{
    "id": "tributos_002",
    "categoria": "Tributação",
    "titulo": "IRPJ e CSLL no Lucro Real",
    "conteudo": "Lucro Real apura IRPJ (15% + adicional de 10%) e CSLL (9%) sobre o lucro contábil ajustado por adições e exclusões fiscais. Pode ser trimestral ou anual. É o regime mais complexo, mas permite compensar prejuízos e créditos fiscais.",
    "tags": ["irpj", "csll", "lucro real", "tributacao"]
},
{
    "id": "tributos_003",
    "categoria": "Tributação",
    "titulo": "Planejamento Tributário",
    "conteudo": "Planejamento tributário visa reduzir legalmente a carga fiscal por meio da escolha do regime mais adequado, aproveitamento de incentivos, créditos e reorganizações societárias. Deve respeitar o princípio da legalidade e evitar a elisão abusiva.",
    "tags": ["planejamento", "tributario", "carga tributaria", "elisao", "regime"]
},
{
    "id": "gerencial_001",
    "categoria": "Contabilidade Gerencial",
    "titulo": "Margem de Contribuição e Alavancagem Operacional",
    "conteudo": "Margem de contribuição = Receita - Custos e Despesas Variáveis. Indica quanto sobra para cobrir os custos fixos e gerar lucro. Alavancagem operacional mede o impacto da variação nas vendas sobre o lucro operacional.",
    "tags": ["gerencial", "margem", "alavancagem", "lucro", "analise"]
},
{
    "id": "gerencial_002",
    "categoria": "Contabilidade Gerencial",
    "titulo": "Orçamento Empresarial (Budget)",
    "conteudo": "O orçamento empresarial projeta receitas, custos e despesas para um período, servindo como base de controle e avaliação de desempenho. Tipos: Estático, Flexível e Contínuo (Rolling Forecast).",
    "tags": ["orcamento", "budget", "planejamento", "controle", "gerencial"]
},
{
    "id": "cpc_001",
    "categoria": "Normas Contábeis (CPC)",
    "titulo": "CPC 27 – Ativo Imobilizado",
    "conteudo": "Define o reconhecimento de imobilizados quando há probabilidade de benefícios econômicos futuros e mensuração confiável. O ativo deve ser depreciado sistematicamente ao longo de sua vida útil. Valor residual deve ser considerado.",
    "tags": ["cpc27", "imobilizado", "ativo", "depreciacao", "nbc tg 27"]
},
{
    "id": "cpc_002",
    "categoria": "Normas Contábeis (CPC)",
    "titulo": "CPC 04 – Ativo Intangível",
    "conteudo": "Estabelece critérios de reconhecimento para ativos intangíveis, como marcas, softwares e patentes. Devem ser identificáveis, controláveis e capazes de gerar benefícios futuros. Amortização ocorre durante a vida útil estimada.",
    "tags": ["cpc04", "intangivel", "ativo", "amortizacao", "nbc tg 04"]
},
{
    "id": "tributos_004",
    "categoria": "Tributação",
    "titulo": "ICMS – Regras de Não-Cumulatividade",
    "conteudo": "A não-cumulatividade do ICMS permite o crédito sobre entradas de mercadorias para comercialização ou insumos para industrialização. Créditos de Ativo Imobilizado (CIAP) são apropriados em 48 parcelas mensais. Vedado em casos de isenção ou não-incidência na saída subsequente.",
    "tags": ["icms", "nao cumulativo", "credito", "ciap", "fiscal"]
},
{
    "id": "tributos_005",
    "categoria": "Tributação",
    "titulo": "Substituição Tributária (ICMS-ST)",
    "conteudo": "ICMS-ST é o regime de arrecadação onde a responsabilidade pelo imposto devido nas operações subsequentes é atribuída a um único contribuinte (Substituto). O cálculo envolve MVA (Margem de Valor Agregado) ou pauta fiscal, garantindo o recolhimento antecipado.",
    "tags": ["icms-st", "substituicao tributaria", "mva", "antecipacao", "fiscal"]
},
{
    "id": "obrigacao_005",
    "categoria": "Obrigações Acessórias",
    "titulo": "Certidão Negativa de Débitos (CND)",
    "conteudo": "A CND atesta a regularidade fiscal de uma pessoa jurídica junto aos órgãos (RFB, PGFN, Estados e Municípios). É essencial para participação em licitações, obtenção de crédito e comprovação de idoneidade fiscal. Validade de 180 dias ou conforme órgão emissor.",
    "tags": ["cnd", "certidao", "regularidade fiscal", "debito", "rfb"]
},
{
    "id": "obrigacao_006",
    "categoria": "Obrigações Acessórias",
    "titulo": "Portal e-CAC e Caixa Postal",
    "conteudo": "O e-CAC (Centro Virtual de Atendimento) é o portal da Receita Federal para serviços virtuais (Consulta de Situação Fiscal, Extrato Simples Nacional). A Caixa Postal é o canal de comunicação oficial para intimações e avisos fiscais, exigindo acompanhamento diário.",
    "tags": ["e-cac", "rfb", "caixa postal", "intimacao", "servicos"]
},
{
    "id": "folha_003",
    "categoria": "Folha Pagamento",
    "titulo": "Obrigações do Contrato de Trabalho – Registro",
    "conteudo": "O empregador deve registrar o funcionário antes do início das atividades, formalizando o contrato de trabalho (CLT). Inclui: exame admissional, registro em livro/ficha/sistema, anotação na CTPS e envio dos eventos S-2200 e S-2190 (admissão) ao eSocial.",
    "tags": ["clt", "contrato", "trabalho", "admissao", "esocial"]
},
{
    "id": "folha_004",
    "categoria": "Folha Pagamento",
    "titulo": "Férias e 13º Salário",
    "conteudo": "Férias: Direito a 30 dias após 12 meses (período aquisitivo). Pagamento: 1/3 constitucional mais o salário normal, pago até 2 dias antes do início. 13º Salário: Pago em duas parcelas (1ª até 30/Nov, 2ª até 20/Dez).",
    "tags": ["ferias", "decimo terceiro", "encargos", "trabalhista"]
},
{
    "id": "societario_008",
    "categoria": "Contabilidade Geral",
    "titulo": "Demonstração dos Fluxos de Caixa (DFC)",
    "conteudo": "A DFC é obrigatória e detalha a movimentação do caixa em 3 atividades: Operacionais (receitas/despesas), Investimento (ativos não circulantes) e Financiamento (empréstimos/capital próprio). Métodos: Direto (recebimentos/pagamentos) ou Indireto (ajuste do Lucro Líquido).",
    "tags": ["dfc", "fluxo de caixa", "direto", "indireto", "cpc 03"]
},
{
    "id": "societario_009",
    "categoria": "Contabilidade Geral",
    "titulo": "Provisões e Passivos Contingentes",
    "conteudo": "Provisão (NBC TG 25/CPC 25): Reconhecida quando há obrigação presente resultante de evento passado, é provável a saída de recursos e o valor pode ser estimado confiavelmente. Passivo Contingente: Possível obrigação não reconhecida (geralmente ações judiciais de baixa probabilidade de perda).",
    "tags": ["provisao", "passivo", "contingente", "cpc 25", "risco"]
},
{
    "id": "simples_002",
    "categoria": "Simples Nacional",
    "titulo": "Fator R no Simples Nacional",
    "conteudo": "O Fator R determina a tributação de atividades dos Anexos III ou V. Se a Razão entre a Folha de Salários (12 meses) e a Receita Bruta (12 meses) for igual ou superior a 28%, a empresa é tributada pelo Anexo III (alíquotas menores); caso contrário, pelo Anexo V (alíquotas maiores).",
    "tags": ["simples", "fator r", "anexo v", "anexo iii", "folha"]
},
{
    "id": "presumido_002",
    "categoria": "Lucro Presumido",
    "titulo": "Regime de Caixa vs. Competência no Presumido",
    "conteudo": "O Lucro Presumido pode optar pelo regime de caixa (reconhecimento de receita no recebimento) ou competência (reconhecimento no fato gerador). A opção pelo regime de caixa deve ser formalizada e afeta a base de cálculo de PIS/COFINS, IRPJ e CSLL.",
    "tags": ["presumido", "caixa", "competencia", "regime", "irpj"]
},
{
    "id": "reforma_001",
    "categoria": "Reforma Tributária",
    "titulo": "Visão Geral da Reforma - Transição",
    "conteudo": "A Emenda Constitucional 132/2023 (Reforma Tributária) substitui 5 tributos (PIS, COFINS, IPI, ICMS e ISS) por 3: IBS (Estadual/Municipal), CBS (Federal) e Imposto Seletivo (IS). O período de transição dos impostos antigos para o novo sistema (IVA Dual) iniciará em 2026.",
    "tags": ["reforma", "iva", "ibs", "cbs", "imposto seletivo", "transicao"]
},
{
    "id": "custos_004",
    "categoria": "Contabilidade de Custos",
    "titulo": "Custos Conjuntos e Subprodutos",
    "conteudo": "Custos Conjuntos são os custos de produção de bens que surgem simultaneamente (coprodutos). A alocação é feita por métodos como Valor de Venda no Ponto de Separação. Subproduto é um produto secundário, de valor de venda baixo, cujas receitas geralmente abatem o custo de produção do produto principal.",
    "tags": ["custos", "conjuntos", "subproduto", "rateio", "industrial"]
},
{
    "id": "mei_002",
    "categoria": "MEI",
    "titulo": "Composição e Reajuste do DAS-MEI",
    "conteudo": "O valor mensal do DAS-MEI é fixo e composto por: 5% do Salário Mínimo (referente à Contribuição Previdenciária, INSS), mais R$ 1,00 (ICMS, para Comércio/Indústria) ou R$ 5,00 (ISS, para Serviços). O valor é reajustado anualmente junto ao Salário Mínimo.",
    "tags": ["mei", "das", "inss", "icms", "iss", "reajuste"]
},
{
    "id": "mei_003",
    "categoria": "MEI",
    "titulo": "Obrigatoriedade e Penalidades do DAS",
    "conteudo": "O pagamento do DAS é obrigatório, mesmo sem faturamento. O não pagamento gera juros e multa (0,33% ao dia, limitada a 20% do valor). O atraso por mais de 12 meses e a inadimplência levam à exclusão do Simples Nacional e à cobrança da dívida ativa pela PGFN.",
    "tags": ["das", "multa", "juros", "inadimplencia", "divida ativa", "cobranca"]
},
{
    "id": "mei_004",
    "categoria": "MEI",
    "titulo": "Declaração Anual do MEI (DASN-SIMEI)",
    "conteudo": "Todo MEI é obrigado a entregar a Declaração Anual do Simples Nacional (DASN-SIMEI) até o dia 31 de maio. Nela, o MEI informa a Receita Bruta Total e a Receita Bruta com Comércio/Indústria (sujeita a ICMS) ou Serviços (sujeita a ISS) do ano anterior, além da informação de empregado.",
    "tags": ["dasn-simei", "declaracao anual", "prazo", "receita bruta", "obrigatoria"]
},
{
    "id": "mei_005",
    "categoria": "MEI",
    "titulo": "Obrigações e Limites na Contratação de Funcionário",
    "conteudo": "O MEI pode contratar apenas 1 (um) empregado, que deve receber no máximo 1 (um) salário mínimo ou o piso salarial da categoria. O MEI fica obrigado a recolher FGTS (8%) e INSS patronal (3%) sobre o salário desse empregado, além de outras obrigações trabalhistas (eSocial).",
    "tags": ["empregado", "funcionario", "salario minimo", "inss patronal", "fgts", "trabalhista"]
},
{
    "id": "mei_006",
    "categoria": "Desenquadramento MEI por Faturamento",
    "titulo": "Regras de Desenquadramento por Excesso de Receita",
    "conteudo": "Se o MEI faturar entre R$ 81.000,01 e R$ 97.200 (limite de 20%), deverá recolher o DAS normal e a multa sobre o excesso de receita. Se ultrapassar R$ 97.200, o desenquadramento é obrigatório e retroativo a janeiro, devendo recolher os impostos como Simples Nacional desde o início do ano.",
    "tags": ["desenquadramento", "excesso", "limite", "multa", "simples nacional", "retroativo"]
},
{
    "id": "mei_007",
    "categoria": "Desenquadramento MEI",
    "titulo": "Desenquadramento por Atividade ou Sócio",
    "conteudo": "O MEI é desenquadrado se exercer atividade não permitida (ver lista do CGSN), se abrir filial, se participar como sócio ou administrador em outra empresa, ou se incluir sócio em sua estrutura. Nesses casos, o desenquadramento deve ser comunicado à Receita Federal e a empresa passa para o Simples Nacional ou Lucro Presumido.",
    "tags": ["desenquadramento", "atividade", "sociedade", "filial", "cgsn"]
},
{
    "id": "simples_003",
    "categoria": "Simples Nacional",
    "titulo": "Obrigações Acessórias do Simples Nacional",
    "conteudo": "As principais obrigações do Simples Nacional são: PGDAS-D (mensal, para apuração do DAS), DEFIS (anual, informações econômicas e fiscais) e, se tiver funcionário, eSocial e DCTFWeb. Empresas do Simples não entregam ECF, ECD ou EFD ICMS/IPI, salvo exceções estaduais.",
    "tags": ["simples", "obrigacoes", "defis", "pgdas-d", "esocial", "acessorias"]
},
{
    "id": "simples_004",
    "categoria": "Simples Nacional",
    "titulo": "Cálculo do Simples - Alíquota Efetiva",
    "conteudo": "O Simples Nacional utiliza a Alíquota Efetiva, que é o percentual real de imposto. Ela é calculada pela fórmula: (RBT12 * Alíquota Nominal - Parcela a Deduzir) / RBT12. O resultado deve ser aplicado sobre a Receita Bruta do Mês para encontrar o valor do DAS.",
    "tags": ["simples", "calculo", "aliquota efetiva", "rbt12", "das"]
}


]

def get_all_documents():
    """Retorna todos os documentos da base de conhecimento"""
    return [doc["conteudo"] for doc in KNOWLEDGE_BASE]

def get_document_by_id(doc_id: str):
    """Busca documento por ID"""
    return next((doc for doc in KNOWLEDGE_BASE if doc["id"] == doc_id), None)

def search_by_category(categoria: str):
    """Busca documentos por categoria"""
    return [doc for doc in KNOWLEDGE_BASE if doc["categoria"].lower() == categoria.lower()]