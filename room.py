import re
import os
from feature import Feature
from obj import Obj

class Room:
    def __init__(self, name='', longForm='', shortForm='', north='', south='', east='', west='', visited='', features='', pickupObjects=''):
        self.name = name
        self.longForm = longForm
        self.shortForm = shortForm
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.visited = visited
        self.features = features
        self.pickupObjects = pickupObjects
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
    def loadRoom(self, gameName, roomName):
        roomPath = './saved_games/' + gameName + '/rooms/' + roomName + '.txt'
        if os.path.exists(roomPath) == False:
            return -1
        else:
            inputRoom = open(roomPath, 'r')
            for line in inputRoom:
                if 'features' in line:
                    words = re.split("[:,]+", line)
                    words = [x.strip() for x in words]
                    roomData = []
                    if len(words) > 1 and words[1] != '':
                        for x in words[1:]:
                            myFeature = Feature()
                            myFeature.loadFeature(gameName, x)
                            roomData.append(myFeature)
                elif 'pickupObjects' in line:
                    words = re.split("[:,]+", line)
                    words = [x.strip() for x in words]
                    roomData = []
                    if len(words) > 1 and words[1] != '':
                        for x in words[1:]:
                            myObject = Obj()
                            myObject.loadObject(gameName, x)
                            roomData.append(myObject)
                else:
                    words = re.split("[:]+", line)
                    words = [x.strip() for x in words]
                    if words[0] == 'visited':
                        if(words[1] == 'True'):
                            roomData = True
                        else:
                            roomData = False
                    else:
                        roomData = words[1]
                setattr(self, words[0], roomData)
    
    def markVisited(self, gameName, roomName):
        roomPath = './saved_games/' + gameName + '/rooms/' + roomName + '.txt'
        if os.path.exists(roomPath) == False:
            return -1
        else:
            inputRoom = open(roomPath, 'r')
            data = inputRoom.read()
            data = data.replace("False", "True")
            outputRoom = open(roomPath, 'w')
            outputRoom.write(data)
            self.visited = True
    
    def dropItemInRoom(self, gameName, roomName, objectName):
        roomPath = './saved_games/' + gameName + '/rooms/' + roomName + '.txt'
        if os.path.exists(roomPath) == False:
            return -1
        else:
            with open(roomPath, "a") as roomFile:
                addObject = ", " + objectName
                roomFile.write(addObject)
            self.pickupObjects.append(objectName)

    def pickupItemInRoom(self, gameName, roomName, objectName):
        roomPath = './saved_games/' + gameName + '/rooms/' + roomName + '.txt'
        if os.path.exists(roomPath) == False:
            return -1
        elif objectName in self.pickupObjects:
            with open(roomPath, 'r') as inputRoom:
                lines = inputRoom.readlines()
            with open(roomPath, "w") as inputRoom:
                for line in lines:
                    words = re.split("[:,]+", line)
                    words = [x.strip() for x in words]
                    print words
                    if words[0] == 'pickupObjects':
                        words.remove(objectName)
                        newline = words[0] + ':'
                        count = 1
                        for item in words[1:]:
                            if count == len(words) - 1:
                                newline += ' ' + item
                            else:
                                newline += ' ' + item + ','
                            count += 1
                        inputRoom.write(newline)
                    else:
                        inputRoom.write(line)
            self.pickupObjects.remove(objectName)
        else:
            return -1




myRoom = Room()

myRoom.loadRoom('alex', 'testroom')





