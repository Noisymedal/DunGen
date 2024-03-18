## Generated dungeon should be displayed, and a png of the
## displayed image can be found in the output folder

import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import cmath

# setting up the values for the grid
ON = 255
TEST = 200
OFF = 0
random.seed()

roomNumber = 30 # Number of rooms to be placed
roomWidthMax = 30 # Maximum width of any room
roomWidthMin = 10 # Minimum width of any room
roomHeightMax = 30 # Maximum height of any room
roomHeightMin = 10 # Minimum height of any room
hallwayWidth = 5 # Width of hallways
N = 200 # Size of grid

# Object for storing individual room information
class Room(object):
    roomWidth = 1 # Initialize roomWidth
    roomHeight = 1 # Initialize roomHeight
    connected = False # Is this room connected to another room in the grid?
    center = [-10, -10] # Find the approximate center of the room

    def __init__(self, roomWidth, roomHeight) -> None: # Initialize Room object
        self.roomWidth = roomWidth
        self.roomHeight = roomHeight

        self.roomSpace = [[255]*self.roomWidth]*self.roomHeight # Create array of room space

    def getSpace(self) -> None: # Returns room space
        return self.roomSpace

# Generate rooms, hallways, and grid
def generate(grid): 
    rooms = [] # Initialize array of all rooms

    for i in range(roomNumber): # Generate and place up to roomNumber rooms
        # print("DEBUG: Generating room", i)
        successful = False # Was the room successfully placed
        attempts = 0 # Total attempts to place room
        # Repeat up to a set number of times to place room in a safe location
        while successful == False: 
            room = Room(random.randrange(roomWidthMin, roomWidthMax), random.randrange(roomHeightMin, roomHeightMax)) # Generate room of random size
            randX = random.randrange(3, N-roomWidthMax-3) # Generate random top-left corner coordinate for room
            randY = random.randrange(3, N-roomHeightMax-3) # Generate random top-left corner coordinate for room
            room.center = [randX + round(room.roomHeight / 2), randY + round(room.roomWidth / 2)] # Calculate the approximate center of each room
            # print("DEBUG: Room", i, "location found, initiate comparison")

            # Begin placement test
            for j in range(len(rooms)):
                # Calculate distance from room center to room center
                if pow(pow(rooms[j].center[0]-room.center[0], 2) + pow(rooms[j].center[1]-room.center[1], 2), .5) <= ((roomWidthMax+roomHeightMax) / 2 * 1.5):
                    # print("DEBUG: Room placement failed")
                    successful = False
                    break
                else: # No rooms were too close, placement successful
                    successful = True
            if i == 0:
                successful = True
            attempts += 1
            if attempts > 5: # If too many attempts were made, abort room placement
                # print("DEBUG: Attempt limit reached")
                break
        
        # If placement successful, add it grid and list
        if successful == True:
            # print("DEBUG: Room", i, "success")
            grid[randX:randX + room.roomHeight, randY:randY + room.roomWidth] = room.getSpace() # Place room at location
            grid[room.center[0], room.center[1]] = 200 # Mark center of each room, debug feature
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

        # Determine relative location of each room and place a corresponding hallway
        if meX <= themX:
            grid[meX:themX+round(hallwayWidth/2), meY-round(hallwayWidth/2):meY+round(hallwayWidth/2)] = 255
            if meY <= themY:
                grid[themX-round(hallwayWidth/2):themX+round(hallwayWidth/2), meY:themY+round(hallwayWidth/2)] = 255
            else:
                grid[themX-round(hallwayWidth/2):themX+round(hallwayWidth/2), themY:meY+round(hallwayWidth/2)] = 255
        else:
            grid[themX:meX+round(hallwayWidth/2), themY-round(hallwayWidth/2):themY+round(hallwayWidth/2)] = 255
            if meY <= themY:
                grid[meX-round(hallwayWidth/2):meX+round(hallwayWidth/2), meY:themY+round(hallwayWidth/2)] = 255
            else:
                grid[meX-round(hallwayWidth/2):meX+round(hallwayWidth/2), themY:meY+round(hallwayWidth/2)] = 255
        
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

    #parser = argparse.ArgumentParser(description="DunGen Generator")

    #parser.add_argument('--grid-size', dest='N', required=False)
    #parser.add_argument('--mov-file', dest='movfile', required=False)
    #args = parser.parse_args()

    if N < 10: # Minimum grid size, end if too small
        return

    """ if args.N and int(args.N) > 8:
        N = int(args.N)
    
    # set animation update interval
    updateInterval = 10
    if args.interval:
        updateInterval = int(args.interval) """
    updateInterval = 10

    grid = np.array([]) # Create grid
    grid = np.zeros(N*N).reshape(N, N)

    # print("DEBUG: Start generation")
    generate(grid)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
								frames = 10,
								interval=updateInterval,
								save_count=10)

    plt.axis('off') # Remove grid axes
    plt.savefig("static/dungeon.png", bbox_inches='tight') # Output PNG of generated dungeon
    # plt.show() # Display generated dungeon for Debug purposes
     
main()