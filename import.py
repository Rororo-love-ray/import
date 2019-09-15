import random
print ('you can type the range')
small = input ('smallest: ')
big = input ('biggest: ')
small = int (small)
big = int (big)
r = random. randint(small, big)

x = 0
while x >= 0 :
	guess = input ('please guess number 1-100: ')
	guess = int (guess)
	x = x + 1
	if r == guess:
		print ('correct! you guess', x, 'times')
		break
	else:
		if guess > r:
			print ('answer smaller')
		if guess < r:
			print ('answer bigger')
