# high low game

print("pick a number from 1 to 1000")
print("i will make a guess")
print("if im right type '01'")
print("if the number is higher than my guess type '1'")
print("if it's lower type '-1'")

import random, time
time.sleep(2)

ans = True
tries = 0
guess = random.randint(1,1000)
low = 1
high = 1000

while ans !="1":
	write = guess
	ans = input(write)
	if ans == "1":
		print ("huh?")
		tries +=1
		write == guess + 1
	if ans == "-1":
		print ("huh?")
		tries +=1
		write == guess - 1
	if ans == "0":
		print("i got it in", tries, "attempts.")
		break
	