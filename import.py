import random
from string import digits 
lists = [ 'adam' , 'john', 'ai ']
random_number = random.randint(0,2)
computer_pick3 = lists[random_number]
print("hello my name is " + computer_pick3 )

lists = [ 'nice to meet you' , "it's good to see you ", "what is in your mind"]
random_number = random.randint(0,2)
computer_pick4 = lists[random_number]
list2 = [ computer_pick3 , computer_pick4 ,]
random_number = random.randint(0,5)
computer_pick9 = list2[random_number]
print(computer_pick9)

print ("let's play a game choose a number ")
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
