import redis

redis = redis.Redis()
redis.flushall()

FEM = "female_names_set"

with open("female-names.txt", "r") as f:
    for line in f:
        redis.zadd(FEM, {line.rstrip(): 0}) 

print("Finished loading the names")
print(redis.zrange(FEM, 4500, 4510))
print("Searching that start with susann")
for tup in redis.zscan_iter(FEM, "susann*"):
    print(tup[0], end=',')
print()

while True:
    name = input("Search for ('Enter' for quit): ")
    if name=="":
        break
    for tup in redis.zscan_iter(FEM, name+"*"):
        print(tup[0])

## b)
redis.flushall()
with open("nomes-registados-2018.csv", "r") as f:
    for line in f:
        name,gender,num = line.rstrip().split(",")
        redis.zadd(FEM, {name:num})

print("Finished loading the names")
print(redis.zrange(FEM, 3500, 3510))

while True:
    name = input("Search for ('Enter' for quit): ")
    if name=="":
        break
    for tup in redis.zscan_iter(FEM, name+"*"):
        print(tup)