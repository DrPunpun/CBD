f = open("female-names.txt", "r")
count = {}
for line in f:
	letter = line[0]
	if letter in count:
		count[letter] += 1
	else:
		count[letter] = 1
f.close()
w = open("initials4redis.txt", "w")
for letter in range(ord('a'), ord('z')+1):
	char = chr(letter)
	w.write(" set " + chr(letter - 32) + " " + str(count[char]) + "\n")
w.close()