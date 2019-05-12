import feature
import gameState 
import room 
import obj 
import sys 

playerIsAlive = True 
gameWon = False 

def printScreen(screen_file):
	with open(screen_file) as input_file:
		for line in input_file:
			sys.stdout.write(line)

def getGametype():
	game_type = input("(N)ew game or (L)oad game > ")
	game_type = game_type.upper()
	while game_type != "N" and game_type != "L":
		game_type = input("(N)ew game or (L)oad game > ")
		game_type = game_type.upper()
	return game_type 

def moveRoom(roomName):
	myGameState.currentRoom.loadRoom(gameName, roomName)
	print(myGameState.currentRoom.name)
	if myGameState.currentRoom.visited == False:
		print(myGameState.currentRoom.longForm)
	else:
		print(myGameState.currentRoom.shortForm)
	for i in range (len(myGameState.currentRoom.features)):
		if myGameState.currentRoom.features[i].name != "" and myGameState.currentRoom.features[i].name[-1] != 's':
			print("You see a " + myGameState.currentRoom.features[i].name + " here")
		else:
			print("You see some " + myGameState.currentRoom.features[i].name + " here")

	myGameState.currentRoom.markVisited(gameName)

def goToRoom(direction):
	if getattr(myGameState.currentRoom, direction) == "none":
		print("You can't go that way")
	else:
		moveRoom(getattr(myGameState.currentRoom, direction))

def look():
	print(myGameState.currentRoom.longForm)

title_screen = "dark_castle_title.txt"

printScreen(title_screen)

gameType = getGametype()

if gameType == "N":
	gameName = input("Enter a new game name: ")
	myGameState = gameState.gameState()
	while (myGameState.newGame(gameName) == -1):
		print("A game with that name already exists!")
		gameName = input("Enter a new game name: ")
else:
	gameName = input("Enter the saved game name to load: ")
	myGameState = gameState.gameState()
	while (myGameState.loadGame(gameName) == -1):
		print("No game with that name exists!")
		gameName = input("Enter the saved game name to load: ")

if myGameState.currentRoom.visited == False:
	print(myGameState.currentRoom.longForm)
else:
	print(myGameState.currentRoom.shortForm)
myGameState.currentRoom.markVisited(gameName)


while (playerIsAlive == True and gameWon == False): 

	command = input("> ")

	myCommand = command.lower()

	while(myCommand != 'north' and myCommand != 'south' and myCommand != 'east' and myCommand != 'west' and myCommand != 'look' and myCommand!='quit'):
		print("I don't understand that")
		myCommand = input("> ")
		myCommand = myCommand.lower()

	if(myCommand == 'north' or myCommand == 'south' or myCommand == 'east' or myCommand == 'west'):
		goToRoom(myCommand)

	elif myCommand == 'look':
		look()
	
	elif myCommand == 'quit':
		exit()

