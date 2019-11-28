import redis

r = redis.Redis()
r.flushall()
with open("female-names.txt", "r") as f:
	for word in f:
		letter = word[0]
		if r.exists(letter):
			r.incr(letter)
		else:
			r.set(letter, 1)
for key in r.keys():
	print(str(key)+ ">>" + str(r.get(key)))