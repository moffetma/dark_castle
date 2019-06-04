import feature
import gameState 
import room 
import obj 
import sys 
from parser import Parse
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
	if myGameState.currentRoom.visited == False:
		print(myGameState.currentRoom.longForm)
	else:
		print(myGameState.currentRoom.shortForm)
	for i in range (len(myGameState.currentRoom.pickupObjects)):
		if myGameState.currentRoom.pickupObjects[i].name != "" and myGameState.currentRoom.pickupObjects[i].name[-1] != 's':
			print("You see a " + myGameState.currentRoom.pickupObjects[i].name + " here")
		else:
			print("You see some " + myGameState.currentRoom.pickupObjects[i].name + " here")

	myGameState.currentRoom.markVisited(gameName)

def goToRoom(direction, room):
	if direction is not None:
		if getattr(myGameState.currentRoom, direction.lower()) == "none":
			print("You can't go that way")
			return
		else:
			moveRoom(getattr(myGameState.currentRoom, direction))
			return
	if hasattr(myGameState.currentRoom, room.lower()):
		moveRoom(getattr(myGameState.currentRoom, room.lower()))
	else:
		print("You can't go to that room")	
	

def look():
	print(myGameState.currentRoom.longForm)
	for i in range (len(myGameState.currentRoom.pickupObjects)):
		if myGameState.currentRoom.pickupObjects[i].name != "" and myGameState.currentRoom.pickupObjects[i].name[-1] != 's':
			print("You see a " + myGameState.currentRoom.pickupObjects[i].name + " here")
		else:
			print("You see some " + myGameState.currentRoom.pickupObjects[i].name + " here")

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

moveRoom(myGameState.currentRoom.name)

while (playerIsAlive == True and gameWon == False): 

	command = input("> ")
	parser = Parse()
	action, room, direction, item, objects = parser.parse_user_input(command)

	if (action is not None):
		action = action.lower()
	if (action == 'go') :
		if (room is not None or direction is not None):
			goToRoom(direction, room)

	elif (action == 'look'):
		look()
	
	elif action == 'quit':
		exit()

	elif (action is None and room is None and direction is None and item is None and objects is None):
		print("I don't understand that")

	elif (room is None and direction is None and item is None and objects is None):
		print("I don't understand that")


