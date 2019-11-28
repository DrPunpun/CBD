import redis

#Create redis object
redis = redis.Redis()

#Key for list 
USER = "users"

#Function to store a name in redis
def storeList(username):
    return redis.rpush(USER, username)

#Function to get all usernames stored
def getAllUsersList():
    return redis.lrange(USER, 0, -1)

#Function to get keys stored in redis server
def getKeys():
    return redis.keys("*")

def main():
    test_list = ["Rafa", "Andre", "Pedro", "Joao", "Vasco", "Diogo", "Luis", "Mota"]
    for name in test_list:
        storeList(name)
    
    print(getAllUsersList())
    print(getKeys())

main()
#Delete all from redis server
redis.flushall()

##Do it all again, now with an HashMap
def storeHash(nmec, name):
    return redis.hset(USER, nmec, name)

def getAllUsersHash():
    return redis.hgetall(USER)

def main2():
    test_list = ["Rafa", "Andre", "Pedro", "Joao", "Vasco", "Diogo", "Luis", "Mota"]
    for nmec in range(len(test_list)):
        storeHash(nmec, test_list[nmec])
    
    print(getAllUsersHash())
    print(getKeys())

main2()
redis.flushall()