import re
import os
from room import Room
from obj import Obj

class gameState:
    def __init__(self, name='', currentRoom='', inventory=''):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = inventory
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def loadGame(self, gameName):
        gamePath = './saved_games/' + gameName +'/game_state.txt'
        if os.path.exists(gamePath) == False:
            return -1
        inputGame = open(gamePath, 'r')
        for line in inputGame:
            if 'currentRoom' in line:
                words = re.split("[:]+", line)
                words = [x.strip() for x in words]
                gameStateData = Room()
                gameStateData.loadRoom(gameName, words[1])
            elif 'inventory' in line:
                words = re.split("[:,]+", line)
                words = [x.strip() for x in words]
                gameStateData = []
                if len(words) > 1 and words[1] != '':
                    for x in words[1:]:
                        myObject = Obj()
                        myObject.loadObject(gameName, x)
                        gameStateData.append(myObject)
            else:
                words = re.split("[:]+", line)
                words = [x.strip() for x in words]
                gameStateData = words[1]
            setattr(self, words[0], gameStateData)
""" 
    def saveGame(self, gameName):


    def newGame(self, gameName): """

myState = gameState()

myState.loadGame('alex')

print myState

print myState.currentRoom.name

    