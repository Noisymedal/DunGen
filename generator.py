## Generated dungeon should be displayed, and a png of the
## displayed image can be found in the output folder

import argparse
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math
import csv

# setting up the values for the grid
ON = 255
OFF = 0
random.seed()

image = plt.imread("textures/grid.png")

# Get tiles for Basic theme
tile0 = plt.imread("textures/Basic/SingleTile0.png")
tile1 = plt.imread("textures/Basic/SingleTile1.png")
tile2 = plt.imread("textures/Basic/SingleTile2.png")
tile3 = plt.imread("textures/Basic/SingleTile3.png")
tile4 = plt.imread("textures/Basic/SingleTile4.png")

BasicImgDict = {
    0: tile0,
    1: tile1,
    2: tile2,
    3: tile3,
    4: tile4
}

# Get tiles for Ice Palace theme
iceTile0 = plt.imread("textures/IcePalace/SingleTile0_IP.png")
iceTile1 = plt.imread("textures/IcePalace/SingleTile1_IP.png")
iceTile2 = plt.imread("textures/IcePalace/SingleTile2_IP.png")
iceTile3 = plt.imread("textures/IcePalace/SingleTile3_IP.png")
iceTile4 = plt.imread("textures/IcePalace/SingleTile4_IP.png")

IPImgDict = {
    0: iceTile0,
    1: iceTile1,
    2: iceTile2,
    3: iceTile3,
    4: iceTile4
}

# Get tiles for Mincraft theme
mcTile0 = plt.imread("textures/Minecraft_Dungeon/DungeonTile0_Mc.png")
mcTile1 = plt.imread("textures/Minecraft_Dungeon/DungeonTile1_mc.png")
mcTile2 = plt.imread("textures/Minecraft_Dungeon/DungeonTile2_mc.png")
mcTile3 = plt.imread("textures/Minecraft_Dungeon/DungeonTile3_mc.png")
mcTile4 = plt.imread("textures/Minecraft_Dungeon/DungeonTile4_mc.png")

MCImgDict = {
    0: mcTile0,
    1: mcTile1,
    2: mcTile2,
    3: mcTile3,
    4: mcTile4
}

# Object for storing individual room information
class Room(object):
    roomWidth = 1 # Initialize roomWidth
    roomHeight = 1 # Initialize roomHeight
    connected = False # Is this room connected to another room in the grid?
    center = [-10, -10] # Find the approximate center of the room

    def __init__(self, roomWidth, roomHeight) -> None: # Initialize Room object
        self.roomWidth = roomWidth
        self.roomHeight = roomHeight

        self.roomSpace = [[255]*(self.roomWidth)]*(self.roomHeight) # Create array of room space

    def getSpace(self) -> None: # Returns room space
        return self.roomSpace
    
# Object for storing individual hallway information
class Hallway(object):
    width = 1
    start = [] # Start coords
    end = [] # End coords
    corner = [] # Corner coords

    def __init__(self, start, end, corner, room1, room2, width) -> None:
        self.start = start
        self.end = end
        self.corner = corner
        self.room1 = room1
        self.room2 = room2
        self.width = width

# Adjust hallway positions for better alignment
def testOverlap(hallway, hallway2, loc1):
    hallwayPath = [[], []]
    hallway2Path = [[], []]
    intersect = False

    # Get hallway path
    if (hallway.start[1] == hallway.corner[1]):
        if (hallway.start[0] < hallway.corner[0]):
            for i in range(hallway.corner[0]- hallway.start[0]):
                hallwayPath.append([hallway.start[0] + i, hallway.start[1]])
            if (hallway.end[1] < hallway.corner[1]):
                for i in range(hallway.corner[1] - hallway.end[1]):
                    hallwayPath.append([hallway.corner[0], hallway.end[1] + i])
            else:
                for i in range(hallway.end[1] - hallway.corner[1]):
                    hallwayPath.append([hallway.corner[0], hallway.corner[1] + i])
        else:
            for i in range(hallway.start[0]- hallway.corner[0]):
                hallwayPath.append([hallway.corner[0] + i, hallway.start[1]])
            if (hallway.end[1] < hallway.corner[1]):
                for i in range(hallway.corner[1] - hallway.end[1]):
                    hallwayPath.append([hallway.corner[0], hallway.end[1] + i])
            else:
                for i in range(hallway.end[1] - hallway.corner[1]):
                    hallwayPath.append([hallway.corner[0], hallway.corner[1] + i])
    else:
        if (hallway.start[1] < hallway.corner[1]):
            for i in range(hallway.corner[1] - hallway.start[1]):
                hallwayPath.append([hallway.start[0], hallway.start[1] + i])
            if (hallway.end[0] < hallway.corner[0]):
                for i in range(hallway.corner[0] - hallway.end[0]):
                    hallwayPath.append([hallway.end[0] + i, hallway.end[1]])
            else:
                for i in range(hallway.end[0] - hallway.corner[1]):
                    hallwayPath.append([hallway.corner[0] + i, hallway.corner[1]])
        else:
            for i in range(hallway.start[1] - hallway.corner[1]):
                hallwayPath.append([hallway.start[0], hallway.corner[1] + i])
            if (hallway.end[0] < hallway.corner[0]):
                for i in range(hallway.corner[0] - hallway.end[0]):
                    hallwayPath.append([hallway.end[0] + i, hallway.end[1]])
            else:
                for i in range(hallway.end[0] - hallway.corner[1]):
                    hallwayPath.append([hallway.corner[0] + i, hallway.corner[1]])
    
    # Get second hallway path
    if (hallway2.start[1] == hallway2.corner[1]):
        if (hallway2.start[0] < hallway2.corner[0]):
            for i in range(hallway2.corner[0]- hallway2.start[0]):
                hallway2Path.append([hallway2.start[0] + i, hallway2.start[1]])
            if (hallway2.end[1] < hallway2.corner[1]):
                for i in range(hallway2.corner[1] - hallway2.end[1]):
                    hallway2Path.append([hallway2.corner[0], hallway2.end[1] + i])
            else:
                for i in range(hallway2.end[1] - hallway2.corner[1]):
                    hallway2Path.append([hallway2.corner[0], hallway2.corner[1] + i])
        else:
            for i in range(hallway2.start[0]- hallway2.corner[0]):
                hallway2Path.append([hallway2.corner[0] + i, hallway2.start[1]])
            if (hallway2.end[1] < hallway2.corner[1]):
                for i in range(hallway2.corner[1] - hallway2.end[1]):
                    hallway2Path.append([hallway2.corner[0], hallway2.end[1] + i])
            else:
                for i in range(hallway2.end[1] - hallway2.corner[1]):
                    hallway2Path.append([hallway2.corner[0], hallway2.corner[1] + i])
    else:
        if (hallway2.start[1] < hallway2.corner[1]):
            for i in range(hallway2.corner[1] - hallway2.start[1]):
                hallway2Path.append([hallway2.start[0], hallway2.start[1] + i])
            if (hallway2.end[0] < hallway2.corner[0]):
                for i in range(hallway2.corner[0] - hallway2.end[0]):
                    hallway2Path.append([hallway2.end[0] + i, hallway2.end[1]])
            else:
                for i in range(hallway2.end[0] - hallway2.corner[1]):
                    hallway2Path.append([hallway2.corner[0] + i, hallway2.corner[1]])
        else:
            for i in range(hallway2.start[1] - hallway2.corner[1]):
                hallway2Path.append([hallway2.start[0], hallway2.corner[1] + i])
            if (hallway2.end[0] < hallway2.corner[0]):
                for i in range(hallway2.corner[0] - hallway2.end[0]):
                    hallway2Path.append([hallway2.end[0] + i, hallway2.end[1]])
            else:
                for i in range(hallway2.end[0] - hallway2.corner[1]):
                    hallway2Path.append([hallway2.corner[0] + i, hallway2.corner[1]])

    # Determine if hallways intersect
    for i in range(len(hallwayPath)):
        for j in range(len(hallway2Path)):
            if hallwayPath[i] == hallway2Path[j]:
                intersect = True

    # Begin Adjustments
    if abs(hallway.start[0] - hallway2.start[0]) < math.floor(rooms[hallway.room1].roomWidth/2) and intersect == True:
        hallway.start[0] = hallway2.start[0]
    if abs(hallway.start[1] - hallway2.start[1]) < math.floor(rooms[hallway.room1].roomHeight/2)  and intersect == True:
        hallway.start[1] = hallway2.start[1]
    if abs(hallway.end[1] - hallway2.end[1]) < math.floor(rooms[hallway.room2].roomHeight/2)  and intersect == True:
        hallway.end[1] = hallway2.end[1]
    if abs(hallway.end[0] - hallway2.end[0]) < math.floor(rooms[hallway.room2].roomWidth/2)  and intersect == True:
        hallway.end[0] = hallway2.end[0]
    return hallway

intersections = []

# Find and list hallway intersections
def findIntersections(hallwayList):
    for a in range(len(hallwayList)):
        for b in range(len(hallwayList)):
            hallwayPath = []
            hallway2Path = []
            if a == b:
                break
            hallway = hallwayList[a]
            hallway2 = hallwayList[b]
            if (hallway.start[1] == hallway.corner[1]):
                if (hallway.start[0] < hallway.corner[0]):
                    for i in range(hallway.corner[0]- hallway.start[0]):
                        hallwayPath.append([hallway.start[0] + i, hallway.start[1], 1])
                    if (hallway.end[1] < hallway.corner[1]):
                        for i in range(hallway.corner[1] - hallway.end[1]):
                            hallwayPath.append([hallway.corner[0], hallway.end[1] + i, 0])
                    else:
                        for i in range(hallway.end[1] - hallway.corner[1]):
                            hallwayPath.append([hallway.corner[0], hallway.corner[1] + i, 0])
                else:
                    for i in range(hallway.start[0]- hallway.corner[0]):
                        hallwayPath.append([hallway.corner[0] + i, hallway.start[1], 1])
                    if (hallway.end[1] < hallway.corner[1]):
                        for i in range(hallway.corner[1] - hallway.end[1]):
                            hallwayPath.append([hallway.corner[0], hallway.end[1] + i, 0])
                    else:
                        for i in range(hallway.end[1] - hallway.corner[1]):
                            hallwayPath.append([hallway.corner[0], hallway.corner[1] + i, 0])
            else:
                if (hallway.start[1] < hallway.corner[1]):
                    for i in range(hallway.corner[1] - hallway.start[1]):
                        hallwayPath.append([hallway.start[0], hallway.start[1] + i, 0])
                    if (hallway.end[0] < hallway.corner[0]):
                        for i in range(hallway.corner[0] - hallway.end[0]):
                            hallwayPath.append([hallway.end[0] + i, hallway.end[1], 1])
                    else:
                        for i in range(hallway.end[0] - hallway.corner[1]):
                            hallwayPath.append([hallway.corner[0] + i, hallway.corner[1], 1])
                else:
                    for i in range(hallway.start[1] - hallway.corner[1]):
                        hallwayPath.append([hallway.start[0], hallway.corner[1] + i, 0])
                    if (hallway.end[0] < hallway.corner[0]):
                        for i in range(hallway.corner[0] - hallway.end[0]):
                            hallwayPath.append([hallway.end[0] + i, hallway.end[1], 1])
                    else:
                        for i in range(hallway.end[0] - hallway.corner[1]):
                            hallwayPath.append([hallway.corner[0] + i, hallway.corner[1], 1])
            if (hallway2.start[1] == hallway2.corner[1]):
                if (hallway2.start[0] < hallway2.corner[0]):
                    for i in range(hallway2.corner[0]- hallway2.start[0]):
                        hallway2Path.append([hallway2.start[0] + i, hallway2.start[1], 1])
                    if (hallway2.end[1] < hallway2.corner[1]):
                        for i in range(hallway2.corner[1] - hallway2.end[1]):
                            hallway2Path.append([hallway2.corner[0], hallway2.end[1] + i, 0])
                    else:
                        for i in range(hallway2.end[1] - hallway2.corner[1]):
                            hallway2Path.append([hallway2.corner[0], hallway2.corner[1] + i, 0])
                else:
                    for i in range(hallway2.start[0]- hallway2.corner[0]):
                        hallway2Path.append([hallway2.corner[0] + i, hallway2.start[1], 1])
                    if (hallway2.end[1] < hallway2.corner[1]):
                        for i in range(hallway2.corner[1] - hallway2.end[1]):
                            hallway2Path.append([hallway2.corner[0], hallway2.end[1] + i, 0])
                    else:
                        for i in range(hallway2.end[1] - hallway2.corner[1]):
                            hallway2Path.append([hallway2.corner[0], hallway2.corner[1] + i, 0])
            else:
                if (hallway2.start[1] < hallway2.corner[1]):
                    for i in range(hallway2.corner[1] - hallway2.start[1]):
                        hallway2Path.append([hallway2.start[0], hallway2.start[1] + i, 0])
                    if (hallway2.end[0] < hallway2.corner[0]):
                        for i in range(hallway2.corner[0] - hallway2.end[0]):
                            hallway2Path.append([hallway2.end[0] + i, hallway2.end[1], 1])
                    else:
                        for i in range(hallway2.end[0] - hallway2.corner[1]):
                            hallway2Path.append([hallway2.corner[0] + i, hallway2.corner[1], 1])
                else:
                    for i in range(hallway2.start[1] - hallway2.corner[1]):
                        hallway2Path.append([hallway2.start[0], hallway2.corner[1] + i, 0])
                    if (hallway2.end[0] < hallway2.corner[0]):
                        for i in range(hallway2.corner[0] - hallway2.end[0]):
                            hallway2Path.append([hallway2.end[0] + i, hallway2.end[1], 1])
                    else:
                        for i in range(hallway2.end[0] - hallway2.corner[1]):
                            hallway2Path.append([hallway2.corner[0] + i, hallway2.corner[1], 1])

            for i in range(len(hallwayPath)):
                for j in range(len(hallway2Path)):
                    # Mark intersection if hallways are moving perpendicularly
                    if (hallwayPath[i][0] == hallway2Path[j][0]) and (hallwayPath[i][1] == hallway2Path[j][1]) and (hallwayPath[i][2] != hallway2Path[j][2]):
                        intersections.append([hallwayPath[i][0], hallwayPath[i][1]])
            # Mark hallway corners as intersections
            if hallway.corner != hallway.start and hallway.corner != hallway.end:
                intersections.append([hallway.corner[0], hallway.corner[1]])
            if hallway2.corner != hallway2.start and hallway2.corner != hallway2.end:
                intersections.append([hallway2.corner[0], hallway2.corner[1]])

            if len(intersections) > 0:
                #print("length-1: ", len(intersections)-1)
                for c in range(len(intersections)-1, 0, -1):
                    
                    #print("intersections[",c,"]: ", intersections[c])
                    if c < 0:
                        break
                    if c >= len(intersections):
                        print("ERROR: Object intersections changed irrationally during runtime")
                        break
                    for d in hallways:
                        if d not in hallways:
                            print("ERROR: hallways changed irrationally during runtime")
                            break
                        #print("d.start: ", d.start, "d.end", d.end)
                        #print("check if ", intersections[c], " is ", d.start, " or ", d.end)
                        #print("d.end: ", d.end)
                        try:
                            if intersections[c] == (d.start or d.end):
                                print(c, len(intersections))
                                print("DEBUG: popping", intersections[c], " at index ", c)
                                if c != len(intersections) - 1:
                                    intersections.pop(c)
                                else:
                                    intersections.pop()
                        except IndexError:
                            print("--------------------------------")
                            print("indexError on index ", c)
                            print("---------------------------------")
                            c = len(intersections) - 1


    return intersections
            
# Determine locations occupied by segemnts of hallways
def fillHallways(hallwayList, intersections):
    # Find locations occupied by rooms
    roomLocations = []
    for a in range(len(rooms)):
        for i in range(rooms[a].roomWidth):
            for j in range(rooms[a].roomHeight):
                roomLocations.append([rooms[a].center[0]-math.floor(rooms[a].roomHeight/2) + j, rooms[a].center[1]-math.floor(rooms[a].roomWidth/2) + i])

    intersections = [o for n, o in enumerate(intersections) if o not in intersections[:n]]
    #print("DEBUG roomLocations:", roomLocations)
    #print("DEBUG intersections:", intersections)
    #for i in hallways:
        #print("DEBUG hallway start:", i.start)
        #print("DEBUG hallway corner:", i.corner)
        #print("DEBUG hallway end:", i.end)
    # Remove intersections that are in rooms
    for a in range(len(intersections)-1, -1, -1):
        #print("DEBUG: checking", intersections[a])
        if intersections[a] in roomLocations:
            #print("DEBUG: popping", intersections[a])
            intersections.pop(a)
    
    global hallwaySegments
    hallwaySegments = []
    for a in range(len(hallwayList)):
        hallwayPath = []
        hallway = hallwayList[a]
        if (hallway.start[1] == hallway.corner[1]):
            if (hallway.start[0] < hallway.corner[0]):
                for i in range(hallway.corner[0]- hallway.start[0]):
                    hallwayPath.append([hallway.start[0] + i, hallway.start[1]])
                if (hallway.end[1] < hallway.corner[1]):
                    for i in range(hallway.corner[1] - hallway.end[1], 0, -1):
                        hallwayPath.append([hallway.corner[0], hallway.end[1] + i])
                else:
                    for i in range(hallway.end[1] - hallway.corner[1]):
                        hallwayPath.append([hallway.corner[0], hallway.corner[1] + i])
            else:
                for i in range(hallway.start[0]- hallway.corner[0], 0, -1):
                    hallwayPath.append([hallway.corner[0] + i, hallway.start[1]])
                if (hallway.end[1] < hallway.corner[1]):
                    for i in range(hallway.corner[1] - hallway.end[1], 0, -1):
                        hallwayPath.append([hallway.corner[0], hallway.end[1] + i])
                else:
                    for i in range(hallway.end[1] - hallway.corner[1]):
                        hallwayPath.append([hallway.corner[0], hallway.corner[1] + i])
        else:
            if (hallway.start[1] < hallway.corner[1]):
                for i in range(hallway.corner[1] - hallway.start[1]):
                    hallwayPath.append([hallway.start[0], hallway.start[1] + i])
                if (hallway.end[0] < hallway.corner[0]):
                    for i in range(hallway.corner[0] - hallway.end[0], 0, -1):
                        hallwayPath.append([hallway.end[0] + i, hallway.end[1]])
                else:
                    for i in range(hallway.end[0] - hallway.corner[1]):
                        hallwayPath.append([hallway.corner[0] + i, hallway.corner[1]])
            else:
                for i in range(hallway.start[1] - hallway.corner[1], 0, -1):
                    hallwayPath.append([hallway.start[0], hallway.corner[1] + i])
                if (hallway.end[0] < hallway.corner[0]):
                    for i in range(hallway.corner[0] - hallway.end[0], 0, -1):
                        hallwayPath.append([hallway.end[0] + i, hallway.end[1]])
                else:
                    for i in range(hallway.end[0] - hallway.corner[1]):
                        hallwayPath.append([hallway.corner[0] + i, hallway.corner[1]])
        
        section = []
        exempt = []
        # Set up hallway sections
        for i in hallwayPath:
            # Ignore locations already registered
            for j in hallwaySegments:
                if i in j:
                    exempt.append(i)
            if (i in intersections or i in roomLocations or i in exempt) and section != []:
                hallwaySegments.append(section)
                section = []
            else:
                if i not in intersections and i not in roomLocations and i not in exempt:
                    section.append(i)
        hallwaySegments.append(section)
    
    # Remove empty segments
    for i in range(len(hallwaySegments)-1, 0, -1):
        if hallwaySegments[i] == []:
            hallwaySegments.remove([])
    
    # Remove duplicates
    hallwaySegments = [i for n, i in enumerate(hallwaySegments) if i not in hallwaySegments[:n]]

    interpretSegments(hallwaySegments)
    return intersections

# Convert hallway segments to interpritable data
def interpretSegments(hallwaySegments):
    global segmentsFinal
    segmentsFinal = []
    for i in hallwaySegments:
        centerX = 0
        centerY = 0
        minX = i[0][0]
        maxX = i[0][0]
        minY = i[0][1]
        maxY = i[0][1]
        for j in range(len(i)):
            if i[j][0] > maxX:
                maxX = i[j][0]
            if i[j][0] < minX:
                minX = i[j][0]
            if i[j][1] > maxY:
                maxY = i[j][1]
            if i[j][1] < minY:
                minY = i[j][1]
        width = maxX - minX + 1
        height = maxY - minY + 1
        if width == 0:
            width = 1
        if height == 0:
            height = 1
        centerX = minX + (width / 2)
        centerY = minY + (height / 2)
        segmentsFinal.append([centerX - 0.5, centerY - 0.5, height, width])

# Generate rooms, hallways, and grid
def generate(grid, N, roomNumber, roomWidthMin, roomWidthMax, roomHeightMin, roomHeightMax, hallwayWidth): 
    
    for i in range(roomNumber): # Generate and place up to roomNumber rooms
        successful = False # Was the room successfully placed
        attempts = 0 # Total attempts to place room
        # Repeat up to a set number of times to place room in a safe location
        while successful == False: 
            roomWidth = 0
            roomHeight = 0
            if (roomWidthMax == roomWidthMin):
                roomWidth = roomWidthMin
            else:
                roomWidth = random.randrange(roomWidthMin, roomWidthMax+1)
            if (roomHeightMax == roomHeightMin):
                roomHeight = roomHeightMin
            else:
                roomHeight = random.randrange(roomHeightMin, roomHeightMax+1)
            room = Room(roomWidth, roomHeight) # Generate room of random size
            randX = random.randrange(2, math.floor((N-roomWidthMax-2))) # Generate random top-left corner coordinate for room
            randY = random.randrange(2, math.floor((N-roomHeightMax-2))) # Generate random top-left corner coordinate for room
            randY += 1
            room.center = [randX + math.floor(room.roomHeight / 2), randY + math.floor(room.roomWidth / 2)] # Calculate the approximate center of each room
            
            # Begin placement test
            for j in range(len(rooms)):
                # Calculate distance from room center to room center
                if pow(pow(rooms[j].center[0]-room.center[0], 2) + pow(rooms[j].center[1]-room.center[1], 2), .5) <= ((roomWidthMax+roomHeightMax) / 2 * 1.5):
                    successful = False
                    break
                else: # No rooms were too close, placement successful
                    successful = True
            if i == 0:
                successful = True
            attempts += 1
            if attempts > 5: # If too many attempts were made, abort room placement
                break
        
        # If placement successful, add it grid and list
        if successful == True:
            grid[randX:randX + (room.roomHeight), randY:randY + (room.roomWidth)] = room.getSpace() # Place room at location
            rooms.append(room) # Add room to list of rooms
    
    # Add hallways between placed rooms
    for i in range(len(rooms)):
        connectedRoom = (i + 1) % len(rooms) # Connect to next room in list
        """ while connectedRoom == i: # Connect to a random room
            connectedRoom = random.randrange(0, len(rooms)) """
        meX = rooms[i].center[0] # Get i center X
        meY = rooms[i].center[1] # Get i center Y
        themX = rooms[connectedRoom].center[0] # Get connectedRoom center X
        themY = rooms[connectedRoom].center[1] # Get connectedRoom center Y

        hallway = Hallway(rooms[i].center, rooms[connectedRoom].center, [], i, connectedRoom, hallwayWidth)
        
        if hallway.start[0] <= hallway.end[0]:
            if hallway.start[1] <= hallway.end[1]:
                hallway.corner = [hallway.end[0],hallway.start[1]]
            else:
                hallway.corner = [hallway.end[0],hallway.start[1]]
        else:
            if hallway.start[1] <= hallway.end[1]:
                hallway.corner = [hallway.start[0],hallway.end[1]]
            else:
                hallway.corner = [hallway.start[0],hallway.end[1]]

        for j in range(len(hallways)):
            hallway = testOverlap(hallway, hallways[j], j)

        # Determine relative location of each room and place a corresponding hallway
        if hallway.start[0] <= hallway.end[0]:
            grid[hallway.start[0]:hallway.end[0]+math.floor(hallwayWidth), hallway.start[1]:hallway.start[1]+math.floor(hallwayWidth)] = 255
            if hallway.start[1] <= hallway.end[1]:
                grid[hallway.end[0]:hallway.end[0]+math.floor(hallwayWidth), hallway.start[1]:hallway.end[1]+math.floor(hallwayWidth)] = 255
                hallway.corner = [hallway.end[0],hallway.start[1]]
            else:
                grid[hallway.end[0]:hallway.end[0]+math.floor(hallwayWidth), hallway.end[1]:hallway.start[1]+math.floor(hallwayWidth)] = 255
                hallway.corner = [hallway.end[0],hallway.start[1]]
        else:
            grid[hallway.end[0]:hallway.start[0]+math.floor(hallwayWidth), hallway.end[1]:hallway.end[1]+math.floor(hallwayWidth)] = 255
            if hallway.start[1] <= hallway.end[1]:
                grid[hallway.start[0]:hallway.start[0]+math.floor(hallwayWidth), hallway.start[1]:hallway.end[1]+math.floor(hallwayWidth)] = 255
                hallway.corner = [hallway.start[0],hallway.end[1]]
            else:
                grid[hallway.start[0]:hallway.start[0]+math.floor(hallwayWidth), hallway.end[1]:hallway.start[1]+math.floor(hallwayWidth)] = 255
                hallway.corner = [hallway.start[0],hallway.end[1]]
        
        hallways.append(hallway)

        # Set rooms as connected
        rooms[i].connected = True
        rooms[connectedRoom].connected = True

# Update function, relic for animation, largely unused
def update(frameNum, img, grid, N):

	""" 
	newGrid = grid.copy()
	
	# update data
	img.set_data(newGrid)
	grid[:] = newGrid[:] """
	return img,

# Reset shared objects
def reset(grid, N, rooms, hallways, intersections, hallwaySegments):
    grid = np.zeros(N*N).reshape(N, N)
    rooms = []
    hallways = []
    intersections = []
    hallwaySegments = []
    
def getTheme():
    if theme == "Basic":
        return 0
    if theme == "MC":
        return 1
    if theme == "IP":
        return 2

global ran
ran = False
theme = "Basic"

def main(ran, N=40, roomNumber=5, roomWidthMin=2, roomWidthMax=5, roomHeightMin=2, roomHeightMax=5, hallwayWidth=1, theme="Basic"):
    random.seed()

    if theme != "Basic" and theme != "IP" and theme != "MC":
        print("ERROR: Unknown theme detected, cancelling generation")

    global grid
    global rooms
    rooms = [] # Initialize array of all rooms
    global hallways # Initialize array of all hallways
    hallways = []

    if ran == True:
        reset(grid, N, rooms, hallways, intersections, hallwaySegments)

    ran = True

    #print("DEBUG roomNumber:", roomNumber)
    #print("DEBUG roomWidthMin:", roomWidthMin)
    if roomWidthMax < roomWidthMin:
        roomWidthMax = roomWidthMin
    #print("DEBUG roomWidthMax:", roomWidthMax)
    #print("DEBUG roomHeightMin:", roomHeightMin)
    if roomHeightMax < roomHeightMin:
        roomHeightMax = roomHeightMin
    #print("DEBUG roomHeightMax:", roomHeightMax)
    #print("DEBUG hallwayWidth:", hallwayWidth)

    updateInterval = 10

    grid = np.array([]) # Create grid
    grid = np.zeros(N*N).reshape(N, N)

    #print("DEBUG: Start generation")
    generate(grid, N, roomNumber, roomWidthMin, roomWidthMax, roomHeightMin, roomHeightMax, hallwayWidth)

    # Find wall locations
    walls = []
    for i in range(N):
        for j in range(N):
            if grid[i,j] == 255:
                if grid[(i-1)%N, (j-1)%N] == 0:
                    walls.append([(j-1)%(N),(i-1)%(N)])
                if grid[(i-1)%N, (j)%N] == 0:
                    walls.append([(j)%(N),(i-1)%(N)])
                if grid[(i-1)%N, (j+1)%N] == 0:
                    walls.append([(j+1)%(N),(i-1)%(N)])
                if grid[(i)%N, (j-1)%N] == 0:
                    walls.append([(j-1)%(N),(i)%(N)])
                if grid[(i)%N, (j+1)%N] == 0:
                    walls.append([(j+1)%(N),(i)%(N)])
                if grid[(i+1)%N, (j-1)%N] == 0:
                    walls.append([(j-1)%(N),(i+1)%(N)])
                if grid[(i+1)%N, (j)%N] == 0:
                    walls.append([(j)%(N),(i+1)%(N)])
                if grid[(i+1)%N, (j+1)%N] == 0:
                    walls.append([(j+1)%(N),(i+1)%(N)])
    
    wallFinal = [i for n, i in enumerate(walls) if i not in walls[:n]]

    # Output wall locations
    with open("output/walls.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(wallFinal)

    grid2 = np.array([])
    grid2 = np.zeros(N*N).reshape(N, N)
    for i in range(N):
        grid2[i] = grid[i]
    for i in wallFinal:
        col, row = i
        grid2[row,col] = 1

    fillings = []
    for i in range(N):
        for j in range(N):
            if grid2[i,j] == 0:
                fillingHeight = 0
                fillingWidth = 0
                for i2 in range(i,N):
                    if grid2[i2,j] == 0:
                        fillingHeight += 1
                    else:
                        break
                for j2 in range(j,N):
                    lazyHeightCheck = 0
                    for i2 in range(i,i+fillingHeight):
                        if grid2[i2,j2] == 0:
                            lazyHeightCheck += 1
                        else:
                            break
                    if lazyHeightCheck == fillingHeight:
                        fillingWidth += 1
                    else:
                        break
                for i2 in range(i,i+fillingHeight):
                    for j2 in range(j,j+fillingWidth):
                        grid2[i2,j2] = 1
                fillings.append([j+(fillingWidth-1)/2,i+(fillingHeight-1)/2,fillingWidth,fillingHeight])

    with open("output/fillings.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(fillings)

    # Setup room information
    roomData = []
    adjustment=0.5
    roomNum = 0
    for i in rooms:
        if roomNum != 0:
            if (i.roomWidth % 2 == 1):
                if (i.roomHeight % 2 == 1):
                    room = [i.center[1], i.center[0], i.roomWidth, i.roomHeight]
                else:
                    room = [i.center[1], i.center[0]-adjustment, i.roomWidth, i.roomHeight]
            else:
                if (i.roomHeight % 2 == 1):
                    room = [i.center[1]-adjustment, i.center[0], i.roomWidth, i.roomHeight]
                else:
                    room = [i.center[1]-adjustment, i.center[0]-adjustment, i.roomWidth, i.roomHeight]
            roomData.append(room)
        roomNum += 1

    # Output room information
    with open("output/rooms.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(roomData)

    intersections = findIntersections(hallways)

    intersections = fillHallways(hallways, intersections)
    # Output hallway segments
    with open("output/hallwaySegments.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(segmentsFinal)

    #print("DEBUG intersections:", intersections)
    intersect = [i for n, i in enumerate(intersections) if i not in intersections[:n]]
    for i in range(len(intersect)):
        temp = intersect[i][0]
        intersect[i][0] = intersect[i][1]
        intersect[i][1] = temp
    # Output intersection information
    with open("output/intersect.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(intersect)

    #print("DEBUG intersections count:", len(intersections))
    #print("DEBUG hallwaySegments count:", len(hallwaySegments))

    fig, ax = plt.subplots()
    alphas = ((grid/255) + 1) % 2
    
    #ax.set_alpha(1.0)
    img = ax.imshow(grid, interpolation='nearest', zorder=1, alpha=alphas)
    
    plt.axis('off') # Remove grid axes

    # Place math.floor tiles depending on theme
    if theme == "Basic":
        for i in range(N):
            for j in range(N):
                if grid[i,j] == 255:
                    imgNum = random.randint(0, 4)
                    ax.imshow(BasicImgDict[imgNum], extent=[j-.5, j+1-.5, i-.5, i+1-.5], zorder=1)
    if theme == "IP":
        for i in range(N):
            for j in range(N):
                if grid[i,j] == 255:
                    imgNum = random.randint(0, 4)
                    ax.imshow(IPImgDict[imgNum], extent=[j-.5, j+1-.5, i-.5, i+1-.5], zorder=1)
    if theme == "MC":
        for i in range(N):
            for j in range(N):
                if grid[i,j] == 255:
                    imgNum = random.randint(0, 4)
                    ax.imshow(MCImgDict[imgNum], extent=[j-.5, j+1-.5, i-.5, i+1-.5], zorder=1)
    
    ax.imshow(image, extent=[0, N-1, 0, N-1], zorder=0, alpha=0)

    plt.axis('off') # Remove grid axes
    plt.savefig("static/dungeon.png", bbox_inches='tight', dpi=600) # Output PNG of generated dungeon
    #plt.show() # Display generated dungeon for Debug purposes
     
# call main
if __name__ == '__main__':
	main(ran)
