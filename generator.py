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
TEST = 200
OFF = 0
random.seed()

#image = plt.imread("output/CobblestoneTexture.png")
image = plt.imread("output/grid.png")
tile0 = plt.imread("output/SingleTile0.png")
tile1 = plt.imread("output/SingleTile1.png")
tile2 = plt.imread("output/SingleTile2.png")
tile3 = plt.imread("output/SingleTile3.png")
tile4 = plt.imread("output/SingleTile4.png")

imgDict = {
    0: tile0,
    1: tile1,
    2: tile2,
    3: tile3,
    4: tile4
}

rooms = [] # Initialize array of all rooms
hallways = [] # Initialize array of all hallways

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
    
class Hallway(object):
    width = 1
    start = []
    end = []
    corner = []

    def __init__(self, start, end, corner, room1, room2, width) -> None:
        self.start = start
        self.end = end
        self.corner = corner
        self.room1 = room1
        self.room2 = room2
        self.width = width

def testOverlap(hallway, hallway2, loc1):
    hallwayPath = [[], []]
    hallway2Path = [[], []]
    intersect = False

    if hallway.start[0] != hallway.corner[0]:
        if hallway.start[0] > hallway.corner[0]:
            for i in range(hallway.start[0]-hallway.corner[0]):
                hallwayPath[0].append(i+hallway.corner[0])
            if hallway.corner[0] != hallway.end[0]:
                if hallway.corner[0] > hallway.end[0]:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.end[0])
                else:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.corner[0])
        else:
            for i in range(hallway.corner[0]-hallway.start[0]):
                hallwayPath[0].append(i+hallway.start[0])
            if hallway.corner[0] != hallway.end[0]:
                if hallway.corner[0] > hallway.end[0]:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.end[0])
                else:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.corner[0])             
    else:
        if hallway.start[1] > hallway.corner[1]:
            for i in range(hallway.start[1]-hallway.corner[1]):
                hallwayPath[0].append(i+hallway.corner[1])
            if hallway.corner[0] != hallway.end[0]:
                if hallway.corner[0] > hallway.end[0]:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.end[0])
                else:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.corner[0])
        else:
            for i in range(hallway.corner[1]-hallway.start[1]):
                hallwayPath[0].append(i+hallway.start[1])
            if hallway.corner[0] != hallway.end[0]:
                if hallway.corner[0] > hallway.end[0]:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.end[0])
                else:
                    for j in range(hallway.corner[0] - hallway.end[0]):
                        hallwayPath[1].append(j+hallway.corner[0])
    
    if hallway2.start[0] != hallway2.corner[0]:
        if hallway2.start[0] > hallway2.corner[0]:
            for i in range(hallway2.start[0]-hallway2.corner[0]):
                hallway2Path[0].append(i+hallway2.corner[0])
            if hallway2.corner[0] != hallway2.end[0]:
                if hallway2.corner[0] > hallway2.end[0]:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.end[0])
                else:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.corner[0])
        else:
            for i in range(hallway2.corner[0]-hallway2.start[0]):
                hallway2Path[0].append(i+hallway2.start[0])
            if hallway2.corner[0] != hallway2.end[0]:
                if hallway2.corner[0] > hallway2.end[0]:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.end[0])
                else:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.corner[0])             
    else:
        if hallway2.start[1] > hallway2.corner[1]:
            for i in range(hallway2.start[1]-hallway2.corner[1]):
                hallway2Path[0].append(i+hallway2.corner[1])
            if hallway2.corner[0] != hallway2.end[0]:
                if hallway2.corner[0] > hallway2.end[0]:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.end[0])
                else:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.corner[0])
        else:
            for i in range(hallway2.corner[1]-hallway2.start[1]):
                hallway2Path[0].append(i+hallway2.start[1])
            if hallway2.corner[0] != hallway2.end[0]:
                if hallway2.corner[0] > hallway2.end[0]:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.end[0])
                else:
                    for j in range(hallway2.corner[0] - hallway2.end[0]):
                        hallway2Path[1].append(j+hallway2.corner[0])

    for i in range(len(hallwayPath)):
        for j in range(len(hallway2Path)):
            if hallwayPath[i] == hallway2Path[j]:
                intersect = True
    if abs(hallway.start[0] - hallway2.start[0]) < math.floor(rooms[hallway.room1].roomWidth/2) and intersect == True:
        hallway.start[0] = hallway2.start[0]
    if abs(hallway.start[1] - hallway2.start[1]) < math.floor(rooms[hallway.room1].roomHeight/2)  and intersect == True:
        hallway.start[1] = hallway2.start[1]
    if abs(hallway.end[1] - hallway2.end[1]) < math.floor(rooms[hallway.room2].roomHeight/2)  and intersect == True:
        hallway.end[1] = hallway2.end[1]
    if abs(hallway.end[0] - hallway2.end[0]) < math.floor(rooms[hallway.room2].roomWidth/2)  and intersect == True:
        hallway.end[0] = hallway2.end[0]
    return hallway



# Generate rooms, hallways, and grid
def generate(grid): 

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
                roomWidth = random.randrange(roomWidthMin, roomWidthMax)
            if (roomHeightMax == roomHeightMin):
                roomHeight = roomHeightMin
            else:
                roomHeight = random.randrange(roomHeightMin, roomHeightMax)
            room = Room(roomWidth, roomHeight) # Generate room of random size
            randX = random.randrange(2, round((N-roomWidthMax-2))) # Generate random top-left corner coordinate for room
            randY = random.randrange(2, round((N-roomHeightMax-2))) # Generate random top-left corner coordinate for room
            randY += 1
            room.center = [randX + round(room.roomHeight / 2), randY + round(room.roomWidth / 2)] # Calculate the approximate center of each room
            
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

def main():
    # Parser arguments may be used 

    parser = argparse.ArgumentParser(description="DunGen Generator")

    #parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--room-num', dest='roomNum', required=False)
    parser.add_argument('--room-width-min', dest='roomWidthMin', required=False)
    parser.add_argument('--room-width-max', dest='roomWidthMax', required=False)
    parser.add_argument('--room-height-min', dest='roomHeightMin', required=False)
    parser.add_argument('--room-height-max', dest='roomHeightMax', required=False)
    parser.add_argument('--hallway-width', dest='hallwayWidth', required=False)
    args = parser.parse_args()

    global N
    N = 40
    if N < 10: # Minimum grid size, end if too small
        return
    
    global roomNumber
    roomNumber = 10
    if args.roomNum:
        if int(args.roomNum) > 1:
            roomNumber = int(args.roomNum)
    print("DEBUG roomNumber:", roomNumber)

    global roomWidthMin
    roomWidthMin = 2
    if args.roomWidthMin:
        if int(args.roomWidthMin) > 0:
            roomWidthMin = int(args.roomWidthMin)
    print("DEBUG roomWidthMin:", roomWidthMin)

    global roomWidthMax
    roomWidthMax = 4
    if args.roomWidthMax:
        if int(args.roomWidthMax) > roomWidthMin:
            roomWidthMax = int(args.roomWidthMax)
        else:
            roomWidthMax = roomWidthMin
    print("DEBUG roomWidthMax:", roomWidthMax)

    global roomHeightMin
    roomHeightMin = 2
    if args.roomHeightMin:
        if int(args.roomHeightMin) > 0:
            roomHeightMin = int(args.roomHeightMin)
    print("DEBUG roomHeightMin:", roomHeightMin)

    global roomHeightMax
    roomHeightMax = 4
    if args.roomHeightMax:
        if int(args.roomHeightMax) > roomHeightMin:
            roomHeightMax = int(args.roomHeightMax)
        else:
            roomHeightMax = roomHeightMin
    print("DEBUG roomHeightMax:", roomHeightMax)

    global hallwayWidth
    hallwayWidth = 1
    if args.hallwayWidth:
        if int(args.hallwayWidth) >= 0:
            hallwayWidth = int(args.hallwayWidth)
    print("DEBUG hallwayWidth:", hallwayWidth)

    """ if args.N and int(args.N) > 8:
        N = int(args.N)
    
    # set animation update interval
    updateInterval = 10
    if args.interval:
        updateInterval = int(args.interval) """
    updateInterval = 10

    #plt.rcParams['grid.color'] = (0.5, 0.5, 0.5, 0.1)

    grid = np.array([]) # Create grid
    grid = np.zeros(N*N).reshape(N, N)

    print("DEBUG: Start generation")
    generate(grid)

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
    
    res = [i for n, i in enumerate(walls) if i not in walls[:n]]

    with open("output/walls.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(res)

    roomData = []
    for i in rooms:
        room = [i.center[0], i.center[1], i.roomWidth, i.roomHeight]
        roomData.append(room)

    with open("output/rooms.csv", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(roomData)

    #for i in hallways:


    fig, ax = plt.subplots()
    alphas = ((grid/255) + 1) % 2
    
    #ax.set_alpha(1.0)
    img = ax.imshow(grid, interpolation='nearest', zorder=1, alpha=alphas)
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
								frames = 10,
								interval=updateInterval,
								save_count=10)
    
    plt.axis('off') # Remove grid axes

    for i in range(N):
        for j in range(N):
            if grid[i,j] == 255:
                imgNum = random.randint(0, 4)
                ax.imshow(imgDict[imgNum], extent=[j-.5, j+1-.5, i-.5, i+1-.5], zorder=1)
    
    ax.imshow(image, extent=[0, N-1, 0, N-1], zorder=0, alpha=0)

    plt.axis('off') # Remove grid axes
    plt.savefig("output/dungeon.png", bbox_inches='tight', dpi=600) # Output PNG of generated dungeon
    plt.show() # Display generated dungeon for Debug purposes
     
# call main
if __name__ == '__main__':
	main()