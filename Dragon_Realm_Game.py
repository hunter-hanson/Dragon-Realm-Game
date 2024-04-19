'''

'''
# imports (random and time)
import random
import time

# function that prints the first statments in the program
def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cabe, the dragon is friendly and will share his treasure with you.
	The other dragon is greedy and hungry, and will eat you on sight.''')
	print()

# function that asks which cave the person wants to choose and uses input validation thru a while loop
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('which cave will you go into? (1 or 2)')
		cave = input()
		
	return cave

# function that checks weather the dragon is friendly or not	
def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	time.sleep(2)
	
	friendlyCave = random.randint(1,2)
	
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')

# while loop that runs all the previously defined functions and asks weather the player wants to play again and loops the game	
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
	
	print('Do you wdant to play again? (yes of no)')
	playAgain = input()
	
	
