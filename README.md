# 📊 Automatizador de Relatórios de Vendas (YoY - Year over Year)

Script em Python desenvolvido para automatizar o ciclo completo de geração de relatórios gerenciais de vendas, desde a busca inteligente dos arquivos por loja e ano, cruzamento e cálculo de indicadores, até a estilização avançada em planilha Excel e envio automatizado por e-mail.

---

## 🚀 Arquitetura e Fluxo do Projeto

O projeto é dividido em **3 etapas principais**:

### 1. Ingestão e Localização Dinâmica de Arquivos
* **Busca Automatizada:** O script utiliza variáveis de mês e ano para localizar dinamicamente as planilhas correspondentes na pasta de dados.
* **Comparação YoY:** Subtração automática do ano (ex: Ano Atual `2026` vs. Ano Anterior `2025`) para parear os arquivos da mesma loja e do mesmo mês.
* **Loop por Lojas:** Execução estruturada repetida para o escopo completo das **6 lojas** da rede.

### 2. Processamento e Motor de Cálculos
* **Pandas DataFrame:** Agrupamento e manipulação robusta dos dados transacionais.
* **Indicadores Calculados:** 
  * Vendas correntes vs. *Last Week* (LW).
  * Atingimento de Metas e Projeções (`% META 3D`, `PROJ R$`, `PROJ X META R$`).
  * Indicadores de Performance de Venda: **PMV** (Preço Médio de Venda), **M.UP** (Markup), **TKM** (Ticket Médio), **P.A.** (Peças por Atendimento) e Projeção de Peças (`PROJ PÇS`).
  * Indicadores de Estoque (`STK PÇS`, `STK VLR`, `STK CST`, `STK PMV`).

### 3. Exportação, Estilização e Envio
* **Formatação Visual (Openpyxl):** Aplicação de padrões corporativos idênticos aos relatórios gerenciais oficiais (cabeçalhos destacados, fontes em negrito, cores condicionais para valores positivos/negativos e bordas duplas em totais).
* **Armazenamento:** Salvamento automático da planilha pronta em um diretório de saída versionado.
* **Disparo por E-mail:** Envio automatizado do relatório gerado diretamente para a lista de e-mails da gerência/diretoria.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas** (Manipulação e cálculo de dados)
* **Openpyxl** (Manipulação e formatação avançada de arquivos Excel)
* **Smtplib / Email** (Automação de envio de e-mails)

---

## 📁 Estrutura do Projeto

```text
📁 Store-Sales-Project/
│
├── 📁 data/                # Planilhas de entrada (organizadas por pastas/lojas)
├── 📁 output/              # Relatórios finais gerados e formatados (.xlsx)
├── 📁 src/                 # Códigos-fonte da automação
│   ├── 📄 main.py          # Script principal orquestrador
│   ├── 📄 processor.py     # Lógica de cálculo e Pandas
│   └── 📄 exporter.py      # Estilização com Openpyxl e envio de e-mail
│
├── 📄 requirements.txt     # Dependências do projeto
└── 📄 README.md            # Documentação do projeto
