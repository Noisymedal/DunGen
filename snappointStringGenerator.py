output=""
boardSize=100
spaceSize=0.019
for i in range(0,boardSize):
    xval = -0.95+(i*spaceSize)
    for j in range(0,boardSize:
        yval = -0.95+(j*spaceSize)
        output+=("\n{\n\t\"Position\": {\n\t \"x\": "+str(xval)+",\n\t \"y\": 0.0,\n\t \"z\": "+str(yval)+"\n\t }\n}," )
file1 = open('snappoints.txt', 'w')
file1.write(output)
file1.close()
 