# 🧾 Extrator de Dados de Notas Fiscais (XML para Excel)

## 📝 Descrição
Este projeto é uma automação em Python desenvolvida para resolver um problema clássico de rotinas administrativas e contábeis: a extração manual de dados de notas fiscais. 

O script lê arquivos XML de notas fiscais (tanto DANFE quanto Notas de Serviço NFS-e), extrai as informações cruciais (como fornecedor, cliente, valores e produtos) e consolida tudo automaticamente em uma planilha estruturada do Excel. É uma ferramenta ideal para acelerar processos de compras, fechamentos contábeis e alimentação de sistemas ERP ou planilhas de PCP (Planejamento e Controle da Produção).

## 🚀 Funcionalidades
- **Suporte a Múltiplos Formatos:** Leitura e estruturação de dados de DANFE (produtos) e NFS-e (serviços).
- **Extração Precisa:** Captura automática do Valor Total, CNPJ/CPF (Emissor e Destinatário), Razão Social e Lista de Produtos/Serviços.
- **Processamento em Lote:** Capacidade de ler múltiplos arquivos XML dentro de um diretório e unificá-los (facilmente adaptável via biblioteca `os`).
- **Exportação Direta:** Geração automática de arquivos `.xlsx` formatados e prontos para análise usando o `pandas`.

## 🛠️ Pré-requisitos
Para rodar este projeto na sua máquina, você precisará do Python 3.x instalado e das seguintes bibliotecas:

- `pandas` (Para manipulação e estruturação dos dados)
- `xmltodict` (Para converter a estrutura XML em um dicionário Python navegável)
- `openpyxl` (Motor necessário para o pandas exportar os dados para Excel)

Você pode instalar todas as dependências de uma vez executando o comando abaixo no seu terminal:

```bash
pip install pandas xmltodict openpyxl
```

## ⚙️ Como Usar
1. **Clone o repositório** para a sua máquina local.
2. Coloque os seus arquivos XML de notas fiscais (ex: `DANFE.xml` ou `NotaServico.xml`) na mesma pasta do script (ou configure o caminho da pasta no código).
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. O script irá processar os arquivos e gerar automaticamente as planilhas de saída (ex: `NFsSP.xlsx` e `NFsRJ.xlsx`) no mesmo diretório, contendo todos os dados estruturados e prontos para uso.

## 💡 Próximos Passos (Roadmap)
- [ ] Implementar leitura em lote (loop) para processar dezenas de notas fiscais de uma pasta automaticamente.
- [ ] Adicionar blocos `try-except` para lidar com notas fiscais que tenham formatações XML fora do padrão.
- [ ] Integrar tratamento para remover caracteres especiais dos CNPJs antes da exportação.
