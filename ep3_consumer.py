import redis

#r = redis.Redis(host='redis-17852.c15.us-east-1-2.ec2.cloud.redislabs.com', port=17852, db=0, password='senha_redis_lab')
#r = redis.Redis(host='url', port=0, db=0, password='pass')
r = redis.Redis(host="127.0.0.1", port=6379, db=1, password="")

while(True):
   print(r.xread({'veiculo': "$"}, count=1, block=50000))