import redis

redis = redis.Redis()
redis.flushall()

MemMessages = "memory_of_all_users_message"

def add_acount():
    while True:
        name = input("Your name? ")
        if not redis.exists(name):
            redis.sadd(name, name)
            redis.hset(MemMessages, name, "")
            break
        print("That name is already taken.", end=" ")

message2 = '''
    Menu:
    1) Follow Account
    2) Read Messages
    3) Write Message
    0) Leave 
    '''

def follow(user, name):
    if redis.exists(name):
        redis.sadd(user, name)
    else:
        print("User doesn't exist")

def write(user):
    li_messages = redis.hget(MemMessages, user).decode("utf-8") 
    li_messages += "\n->" + input("Escreva a sua mensage: ")
    redis.hset(MemMessages, user, li_messages)

def read(user):
    for name in redis.smembers(user):
        print(name, redis.hget(MemMessages, name).decode("utf-8"))

def menu_user(user):
    while True:
        op = input(message2)
        if op=='0':
            break
        if op=='1':
            follow(user, input("Who do you want to follow? "))
        if op=='2':
            read(user)
        if op=='3':
            write(user)

def login(name):
    if redis.exists(name):
        menu_user(name)
    else:
        print("Login failed: No such user.")

message = '''
    Menu:
    1) Add Account
    2) Login
    0) Leave 
    '''

def menu_init():
    while True:
        op = input(message)
        if op=='0':
            break
        if op=='1':
            add_acount()
        if op=='2':
            login(input("Name? "))

menu_init()