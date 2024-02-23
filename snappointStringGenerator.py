output=""
for i in range(0,100):
    xval = -0.95+(i*0.019)
    for j in range(0,100):
        yval = -0.95+(j*0.019)
        output+=("\n{\n\t\"Position\": {\n\t \"x\": "+str(xval)+",\n\t \"y\": 0.0,\n\t \"z\": "+str(yval)+"\n\t }\n}," )
file1 = open('snappoints.txt', 'w')
file1.write(output)
file1.close()
 