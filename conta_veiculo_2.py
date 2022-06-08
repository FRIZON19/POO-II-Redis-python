import redis
import json
import time

# Conectar com o REDIS
r = redis.Redis(host="127.0.0.1", port=6379, db=1, password="")
# criar dicionário vázio
veiculo = {}
# se o stream veiculo_consolidado estiver vazio
if r.xlen("veiculo_consolidado") == 0:
    # pega a primeira e a última entrada do stream 
    first_id = r.xinfo_stream("veiculo")['first-entry'][0]
    last_id = r.xinfo_stream("veiculo")['last-entry'][0]    
else:
    # senão estiver vazio pega a última entrada no stream veiculo_consolidado
    # atribui ao first_id o id da última entrada  do veículo consolidado e
    # a última entrada do stream veiculo
    veiculo = r.xinfo_stream("veiculo_consolidado")['last-entry'][1]
    first_id = veiculo[b"id"]
    last_id = r.xinfo_stream("veiculo")['last-entry'][0]    

# converte o first_id em um inteiro
first = int(first_id.decode("utf-8").split("-")[0])

count = 0
loops = 0
next_id = first


while(True):
    # armazena o stream veiculo na variável dados
    dados = r.xrange("veiculo", min=next_id, count=2)
    # verifica se o stream está vazio
    if len(dados) == 0:
        break
    # lê a quantidade de registros no stream
    count += len(dados)
    # atribui à variável next_id o primeiro id do stream 
    # veiculo armazenado na variável dados, retira caraceter 
    # especial '-'
    next_id = dados[-1][0].decode("utf-8")
    next_id = next_id.split("-")[0]
    next_id = next_id + "-1"

    # incrementa a variável loop
    loops += 1
    # executa o loop for na variável dados
    for item in dados:
        # armazena o valor do ano do veículo na variável ano, após tratamento
        ano = item[1][b'veiculo_ano'].decode("utf-8")
        # verifica se o ano está adicionado no dicionário, caso esteja, 
        # incrementa o valor em 1, se não estiver, adiciona o ano e o valor 1
        if ano in veiculo:
            veiculo[ano] += 1
        else:
            veiculo[ano] = 1

# atualiza o valor do id do dicionário veiculo com o último id do stream de dados
veiculo["id"] = next_id
# verifica se o dicionário veiculo possui registro, se existir, cria o stream 
# veiculo_consolidado com o dicionário veiculo
if any(veiculo):
    r.xadd("veiculo_consolidado", veiculo)
# imprime o dicionário veiculo
print("Total do %s:" %(veiculo))