# código usando 2 while, um para prod e um para venda

opcao = input('Qual tipo de estrutura irá ser usada para a listagem?\nA. Lista com sub-listas'
      '\nB. Dicionário com sub-listas\nC. Dicionário com dicionários\n').lower()
qtdProd = int(input('Quantos produtos serão exibidos? '))
qtdVend = int(input ('Quantas vendas serão exibidas? '))
arqEntProd = open("produtos.txt", 'r')
produtos = []
produtosD = {}
p = arqEntProd.readline().rstrip()
aux = 0
while p != '' and aux < qtdProd:
      p = p.split(';')
      p[0] = int(p[0])
      p[4] = int(p[4].replace(".",""))
      p[5] = float(p[5])
      p[6] = float(p[6])
      del(p[7])
      codProd = p[0]
      dicionarioP = {
            'Nome do Produto': p[1],
            'Unidade de Venda': p[2],
            'Forma de Venda': p[3],
            'Qtde em Estoque': p[4],
            'Preço de Custo': p[5],
            'Margem Bruta Típica': p[6]
      }
      if opcao == 'a':
            produtos.append(p)
      elif opcao == 'b':
            del(p[0])
            produtosD[codProd] = p
      elif opcao == 'c':
            produtosD[codProd] = dicionarioP
      aux += 1
      p = arqEntProd.readline().rstrip()
arqEntProd.close()
#vendas
aux = 0
arqEntVend = open("vendas.txt", 'r')
vendas = []
vendasD = {}
v = arqEntVend.readline().rstrip()
while v != '' and aux < qtdVend:
      v = v.split(';')
      v[0] = int(v[0])
      v[1] = int(v[1])
      v[2] = int(v[2])
      v[3] = int(v[3])
      v[4] = int(v[4].replace(".", ""))
      v[5] = float(v[5])
      del(v[6])

      dicionarioV = {
            'Ano': v[0],
            'Mês': v[1],
            'Dia': v[2],
            'Código do Produto': v[3],
            'Qtde Vendida': v[4],
            'Preço Venda': v[5]
      }
      aux += 1
      if opcao == 'a':
            vendas.append(v)
      elif opcao == 'b':
            vendasD[aux] = v
      elif opcao == 'c':
            vendasD[aux] = dicionarioV
      v = arqEntVend.readline().rstrip()
arqEntVend.close()

print('PRODUTOS:')
if opcao == 'a':
      for produto in produtos:
            print(produto)
elif opcao == 'b' or 'c':
      for chave, valor in produtosD.items():
            print(chave, ' : ', valor)
print('VENDAS:')
if opcao == 'a':
      for venda in vendas:
            print(venda)
elif opcao == 'b' or 'c':
      for chave, valor in vendasD.items():
            print(chave, ' : ', valor)