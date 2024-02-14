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

roomNumber = 7
roomWidthMax = 30
roomWidthMin = 10
roomHeightMax = 30
roomHeightMin = 10
hallwayWidth = 5
N = 200

class Room(object):
    #roomSpace = [[]]
    roomWidth = 1
    roomHeight = 1
    connected = False
    center = [-10, -10]

    def __init__(self, roomWidth, roomHeight) -> None:
        self.roomWidth = roomWidth
        self.roomHeight = roomHeight

        self.roomSpace = [[255]*self.roomWidth]*self.roomHeight

    def getSpace(self) -> None:
        return self.roomSpace

def generate(grid):
    rooms = []

    for i in range(roomNumber):
        print("DEBUG: Generating room", i)
        successful = False
        while successful == False:
            room = Room(random.randrange(roomWidthMin, roomWidthMax), random.randrange(roomHeightMin, roomHeightMax))
            randX = random.randrange(3, N-roomWidthMax-3)
            randY = random.randrange(3, N-roomHeightMax-3)
            room.center = [randX + round(room.roomHeight / 2), randY + round(room.roomWidth / 2)]
            print("DEBUG: Room", i, "location found, initiate comparison")
            for j in range(len(rooms)):
                if pow(pow(rooms[j].center[0]-room.center[0], 2) + pow(rooms[j].center[1]-room.center[1], 2), .5) <= (roomWidthMax * 1.5):
                    print("DEBUG: Room placement failed")
                    successful = False
                    break
                else:
                    successful = True
            if i == 0:
                successful = True
        
        print("DEBUG: Room", i, "success")
        grid[randX:randX + room.roomHeight, randY:randY + room.roomWidth] = room.getSpace()
        grid[room.center[0], room.center[1]] = 200
        rooms.append(room)
    
    for i in range(len(rooms)):
        connectedRoom = (i + 1) % roomNumber
        """ while connectedRoom == i:
            connectedRoom = random.randrange(0, len(rooms)) """
        meX = rooms[i].center[0]
        meY = rooms[i].center[1]
        themX = rooms[connectedRoom].center[0]
        themY = rooms[connectedRoom].center[1]

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
        
        rooms[i].connected = True
        rooms[connectedRoom].connected = True

def update(frameNum, img, grid, N):

	""" # copy grid since we require 8 neighbors
	# for calculation and we go line by line
	newGrid = grid.copy()
	for i in range(N):
		for j in range(N):

			# compute 8-neighbor sum
			# using toroidal boundary conditions - x and y wrap around
			# so that the simulation takes place on a toroidal surface.
			total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

			# apply Conway's rules
			if grid[i, j] == ON:
				if (total < 2) or (total > 3):
					newGrid[i, j] = OFF
			else:
				if total == 3:
					newGrid[i, j] = ON

	# update data
	img.set_data(newGrid)
	grid[:] = newGrid[:] """
	return img,

def main():
    #parser = argparse.ArgumentParser(description="DunGen Generator")

    #parser.add_argument('--grid-size', dest='N', required=False)
    #parser.add_argument('--mov-file', dest='movfile', required=False)
    #parser.add_argument('--interval', dest='interval', required=False)
    #parser.add_argument('--word', dest='word', required=False)
    #args = parser.parse_args()

    if N < 10:
        return

    """ if args.N and int(args.N) > 8:
        N = int(args.N)
    
    # set animation update interval
    updateInterval = 10
    if args.interval:
        updateInterval = int(args.interval) """
    updateInterval = 10

    grid = np.array([])
    grid = np.zeros(N*N).reshape(N, N)

    print("DEBUG: Start generation")
    generate(grid)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
								frames = 10,
								interval=updateInterval,
								save_count=10)

    plt.axis('off')
    plt.savefig("output/dungeon.png", bbox_inches='tight')
    plt.show()
     
main()