# DOCUMENTACAO BD REDIS 
## Passo 1 — Instalando e Configurando o Redis

>>sudo apt update

>>sudo apt install redis-server

Isso irá baixar e instalar o Redis e suas dependências. Em seguida, há uma alteração importante na configuração a ser feita no arquivo de configuração do Redis, que foi gerada automaticamente durante a instalação.

>>sudo nano /etc/redis/redis.conf

>>sudo systemctl restart redis.service

Com isso, você instalou e configurou o Redis e ele está funcionando na sua máquina. No entanto, antes de você começar a usá-lo, é prudente verificar primeiro se o Redis está funcionando corretamente.

## Passo 2 — Testando o Redis
>>sudo systemctl status redis

### Para testar se o Redis está funcionando corretamente, conecte-se ao servidor usando o cliente da linha de comando:

>>redis-cli

No prompt que segue, teste a conectividade com o comando ping:

>>ping

Este resultado confirma que a conexão com o servidor ainda está viva. A seguir, verifique se você é capaz de definir chaves executando:

>>set test "It's working!"

## Imagen Docker:
>>docker run -p 6379:6379 --name redis-mod redislabs/redismod

>>docker exec -it redis-mod redis-cli 

    Teste de conexao

-----------------------------------------------
### Documentacao.
https://redis.io/docs/

https://redis.io/

https://try.redis.io/