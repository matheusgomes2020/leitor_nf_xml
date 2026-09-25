import os
import pandas as pd
import xmltodict

def ler_xml_danfe(nota):

    with open(nota, "rb") as arquivo:
        documento = xmltodict.parse(arquivo)

    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']

    produtos = dic_notafiscal['det']
    lista_produtos = []
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))

    resposta = {
        'valor_total' : [valor_total],
        'cnpj_vendeu' : [cnpj_vendeu],
        'nome_vendeu' : [nome_vendeu],
        'cpf_comprou' : [cpf_comprou],
        'nome_comprou' : [nome_comprou],
        'lista_produtos' : [lista_produtos],
    }
    return resposta

caminho_pasta = 'notas_fiscais_danfe' # Pasta onde guardou os ficheiros
tabela_final = pd.DataFrame() # Tabela vazia que vai receber todos os dados

# Percorre todos os ficheiros dentro da pasta
for arquivo in os.listdir(caminho_pasta):
    
    # Confirma que é mesmo um ficheiro XML antes de tentar abrir
    if arquivo.endswith('.xml'):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        
        try:
            # 1. Lê os dados da nota usando a sua função
            dados_nota = ler_xml_danfe(caminho_completo)
            
            # 2. Transforma o dicionário numa tabela temporária
            tabela_temporaria = pd.DataFrame.from_dict(dados_nota)
            
            # 3. Empilha (cola) a tabela temporária na tabela mestre
            tabela_final = pd.concat([tabela_final, tabela_temporaria], ignore_index=True)
            
        except Exception as e:
            # Se uma nota tiver um formato estranho, o código avisa em vez de bloquear
            print(f"Erro ao ler a nota {arquivo}: {e}")

# No final do ciclo, exporta tudo de uma só vez
tabela_final.to_excel('Consolidado_DANFEs.xlsx', index=False)
print("Processamento concluído com sucesso!")