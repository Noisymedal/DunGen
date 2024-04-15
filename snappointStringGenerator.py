#number of spaces across on the board, note that we start counting from 0
boardSize=38
#the size of each space on the board
spaceSize=0.019*2.5#DEPRECATED BUT DO NOT TOUCH
#this is the top left space coordinates for the snappoints
zeroZero = [-0.925,-0.933]


#This is the variable I'm using for snap-points distancing.
snapSize=0.049
snapZeroZero=[-0.905,-0.905]
#This is the top-left space coordinates for the object generation
wallOffsets=[-17,-16]
#This is the scalar for object positioning, it includes spaceSize for tweaking mutiple things at once, in the future once everything is nice and synced up
wallSpaceSize=spaceSize*1.81

#this generates the snap points tht will be used for the main board
def generateSnappoints():
    #output variable that we will be writing to the file
    output=""
    #for every space x
    for i in range(boardSize):
        xval = snapZeroZero[0]+(i*snapSize)
        #create a column of spaces y
        for j in range(boardSize):
            yval = snapZeroZero[1]+(j*snapSize)
            #and append them to the string
            output+=("\n{\n\t\"Position\": {\n\t \"x\": "+str(xval)+",\n\t \"y\": 0.0,\n\t \"z\": "+str(yval)+"\n\t }\n}" )
            if(not(i==boardSize-1 and j==boardSize-1)):
                output+=",\n"

    #once all the strings are made write them to an output file
    output+="]},\n"
    #file1 = open('snappoints.txt', 'w')
    #file1.write(output)
    #file1.close()
    return output


#every object we make will need a unique ID
#the board is ID 0 so our object IDs will start at 1 and iterate up from there
id=1
def generateID():
    global id
    #write the output to string
    output=str(id)
    #make the ID one bigger
    id=id+1
    #return the string
    return str(id)

#generate the dungeon bricks that will tile our walls
def generateDungeonBricks(points):
    #create the output string
    output=""

    #Append EVERY SINGLE LINE for making an object to the string, for every object we need
    for i in range(0,len(points)):
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posY\": 1.33155191,"
        output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        output+="\n\t\t\"scaleX\": 0.4301,"
        output+="\n\t\t\"scaleY\": 0.173,"
        output+="\n\t\t\"scaleZ\": 0.4301"
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121579/A2A1360574D2A3F86B15759A7AC7C972C344C87A/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\","
        output+="\n\"ChildObjects\": ["
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        # output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posX\": 0.0,"
        output+="\n\t\t\"posY\": 1.6265,"
        # output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"posZ\": 0.0,"
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        # output+="\n\t\t\"scaleX\": 0.4301,"
        output+="\n\t\t\"scaleX\": 1.0,"
        output+="\n\t\t\"scaleY\": 0.02,"
        # output+="\n\t\t\"scaleZ\": 0.4301"
        output+="\n\t\t\"scaleZ\": 1.0"
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166216512/747BFC5FEEA8E6EC0635B2E74280C1244FF97FA4/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\""
        output+="\n}"
        output+="\n]"
        output+="\n}"
        #if the object is NOT the last one, add a comma, for formatting purposes
        if(i!=len(points)):
            output+=",\n"
    #write the output to a file
    #file2 = open('dungeonBricks.txt', 'w')
    #file2.write(output)
    #file2.close()
    return output

#identical to dungeonBricks but for the grey Dungeon tiles above our bricks to obscure the unexplored dungeon
def generateDungeonHats(points):
    output=""


    #Append EVERY SINGLE LINE for making an object to the string, for every object we need
    for i in range(0,len(points)):
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posY\": 1.6265,"
        output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        output+="\n\t\t\"scaleX\": 0.4301,"
        output+="\n\t\t\"scaleY\": 0.02,"
        output+="\n\t\t\"scaleZ\": 0.4301"
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166216512/747BFC5FEEA8E6EC0635B2E74280C1244FF97FA4/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\""
        output+="\n}"
        if(i!=len(points)-1):
            output+=",\n"
    #file3 = open('dungeonHats.txt', 'w')
    #file3.write(output)
    #file3.close()
    return output

#These should be the large blocks that fill out the unexplorable space in the dungeon, the areas that aren't hallways or rooms
def generateDungeonFillings(points):
    #create the output string
    output=""

    #Append EVERY SINGLE LINE for making an object to the string, for every object we need
    for i in range(0,len(points)):
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posY\": 1.33155191,"
        output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        output+="\n\t\t\"scaleX\": "+str(0.4301*float(points[i][2]))+","
        output+="\n\t\t\"scaleY\": 0.173,"
        output+="\n\t\t\"scaleZ\": "+str(0.4301*float(points[i][3]))
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/2508015499658746495/79F41D75E30BE548C96F9D7FE8123BF32E8DDAA9/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\","
        output+="\n\"ChildObjects\": ["
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        # output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posX\": 0.0,"
        output+="\n\t\t\"posY\": 1.6265,"
        # output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"posZ\": 0.0,"
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        # output+="\n\t\t\"scaleX\": "+str(0.4301*float(points[i][2]))+","
        output+="\n\t\t\"scaleX\": 1.0,"
        output+="\n\t\t\"scaleY\": 0.02,"
        # output+="\n\t\t\"scaleZ\": "+str(0.4301*float(points[i][3])) 
        output+="\n\t\t\"scaleZ\": 1.0"
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166216512/747BFC5FEEA8E6EC0635B2E74280C1244FF97FA4/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\""
        output+="\n}"
        output+="\n]"
        output+="\n}"
        #if the object is NOT the last one, add a comma, for formatting purposes
        if(i!=len(points)):
            output+=",\n"
    #write the output to a file
    #file2 = open('dungeonBricks.txt', 'w')
    #file2.write(output)
    #file2.close()
    return output

#identical to dungeonBricks but for the grey Dungeon tiles above our bricks to obscure the unexplored dungeon
def generateDungeonFillingHats(points):
    output=""


    #Append EVERY SINGLE LINE for making an object to the string, for every object we need
    for i in range(0,len(points)):
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"Custom_Model\","
        output+="\n\t\"Transform\": {"
        output+="\n\t\t\"posX\": "+str(float(points[i][0])*wallSpaceSize*10+zeroZero[0]+wallOffsets[0])+","
        output+="\n\t\t\"posY\": 1.6265,"
        output+="\n\t\t\"posZ\": "+str(float(points[i][1])*wallSpaceSize*10+zeroZero[1]+wallOffsets[1])+","
        output+="\n\t\t\"rotX\": 0.0,"
        output+="\n\t\t\"rotY\": 0.0,"
        output+="\n\t\t\"rotZ\": 0.0,"
        output+="\n\t\t\"scaleX\": "+str(0.4301*float(points[i][2]))+","
        output+="\n\t\t\"scaleY\": 0.02,"
        output+="\n\t\t\"scaleZ\": "+str(0.4301*float(points[i][3])) 
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0,"
        output+="\n\t\t\"y\": 0.0,"
        output+="\n\t\t\"z\": 0.0"
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked\": true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,"
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,"
        output+="\n\t\"Hands\": false,"
        output+="\n\t\"CustomMesh\": {"
        output+="\n\t\"MeshURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166121478/309C68514D70709FCBF5A377C2535C0E460381CD/\","
        output+="\n\t\"DiffuseURL\": \"http://cloud-3.steamusercontent.com/ugc/5967903001166216512/747BFC5FEEA8E6EC0635B2E74280C1244FF97FA4/\","
        output+="\n\t\"NormalURL\": \"\","
        output+="\n\t\"ColliderURL\": \"\","
        output+="\n\t\"Convex\": true,"
        output+="\n\t\"MaterialIndex\": 0,"
        output+="\n\t\"TypeIndex\": 0,"
        output+="\n\t\"CastShadows\": true"
        output+="\n\t},"
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\""
        output+="\n}"
        if(i!=len(points)-1):
            output+=",\n"
    #file3 = open('dungeonHats.txt', 'w')
    #file3.write(output)
    #file3.close()
    return output





#I don't exactly know what tabstates are, but the .json files in TTS have them, and the generation works so I don't want to delete them
def generateTabstates():
    output=""
    colorNameArray=["\"Grey\"","\"White\"","\"Brown\"","\"Red\"","\"Orange\"","\"Yellow\"","\"Green\"","\"Blue\"","\"Teal\"","\"Purple\"","\"Pink\"","\"Black\""]
    colorDataArray=[[0.5,0.5,0.5],[1.0,1.0,1.0],[0.443,0.231,0.09],[0.856,0.1,0.094],[0.956,0.392,0.113],[0.905,0.898,0.172],[0.192,0.701,0.168],[0.118,0.53,1.0],[0.129,0.694,0.607],[0.627,0.125,0.941],[0.96,0.439,0.807],[0.25,0.25,0.25]]
    for i in range(len(colorNameArray)):
        output+="\n\t\t\""+generateID()+"\": {"
        if(i==0):
            output+="\n\t\t\t\"title\": \"Rules\","
        else:
            output+="\n\t\t\t\"title\": "+str(colorNameArray[i])+","
        output+="\n\t\t\t\"body\": \"\","
        output+="\n\t\t\t\"color\": "+str(colorNameArray[i])+","
        output+="\n\t\t\t\"visibleColor\": {"
        output+="\n\t\t\"r\": "+str(colorDataArray[i][0])+","
        output+="\n\t\t\"g\": "+str(colorDataArray[i][1])+","
        output+="\n\t\t\"b\": "+str(colorDataArray[i][2])
        output+="\n\t\t},"
        output+="\n\t\t\"id\": "+str(i)
        output+="\n}"
        if(i!=len(colorNameArray)-1):
            output+=",\n"
    return output

#I'm pretty sure these are the player hand zones
def generateHandtrigger():
    output=""
    handTriggerArray=[["\"Red\"",    -15.11,4.81,-20.11,  0.0,0.0,0.0,   11.77,9.17,4.87,  0.86,0.10,0.09,0.0],
                      ["\"Yellow\"", -30.22,4.81,10.17,   0.0,0.90,0.0,  11.66,9.17,4.82,  0.91,0.9,0.17,0.0],
                      ["\"Purple\"", 30.25,4.81,9.59,     0.0,270.0,0.0, 11.66,9.17,4.91,  0.63,0.13,0.94,0.0],
                      ["\"Blue\"",   15.47,4.81,19.83,    0.0,180.0,0.0, 11.77,9.17,4.87,  0.18,0.53,1.0,0.0],
                      ["\"White\"",  15.2,4.81,-20.14,    0.0,0.0,0.0,   11.77,9.17,4.87,  1.0,1.0,1.0,0.0],
                      ["\"Green\"",  -15.19,4.81,19.79,   0.0,180.0,0.0, 11.77,9.17,4.87,  0.19,0.70,0.17,0.0],
                      ["\"Pink\"",   30.1,4.81,-8.45,     0.0,270.0,0.0, 11.66,9.17,4.92,  0.96,0.44,0.81,0.0],
                      ["\"Orange\"", -30.24,4.81,-8.82,   0.0,90.0,0.0,  11.66,9.17,4.92,  0.96,0.39,0.11,0.0],
                      ["\"Teal\"",   0.0,4.81,19.8,       0.0,180.0,0.0, 11.77,9.17,4.87, 0.13,0.69,0.61,0.0],
                      ["\"Brown\"",  0.0,4.81,-20.0,      0.0,180.0,0.0, 11.77,9.17,4.87,  0.44,0.23,0.09,0.0]]
    for i in range(len(handTriggerArray)):
        output+="\n\t{"
        output+="\n\t\t\"GUID\": \"b58fbf\","
        output+="\n\t\t\"Name\": \"HandTrigger\","
        output+="\n\t\t\"Transform\": {"
        output+="\n\t\t\t\"posX\": "+str(handTriggerArray[i][1])+","
        output+="\n\t\t\t\"posY\": "+str(handTriggerArray[i][2])+","
        output+="\n\t\t\t\"posZ\": "+str(handTriggerArray[i][3])+","
        output+="\n\t\t\t\"rotX\": "+str(handTriggerArray[i][4])+","
        output+="\n\t\t\t\"rotY\": "+str(handTriggerArray[i][5])+","
        output+="\n\t\t\t\"rotZ\": "+str(handTriggerArray[i][6])+","
        output+="\n\t\t\t\"scaleX\": "+str(handTriggerArray[i][7])+","
        output+="\n\t\t\t\"scaleY\": "+str(handTriggerArray[i][8])+","
        output+="\n\t\t\t\"scaleZ\": "+str(handTriggerArray[i][9])+""
        output+="\n\t\t},"
        output+="\n\t\t\"Nickname\": \"\","
        output+="\n\t\t\"Description\": \"\","
        output+="\n\t\t\"GMNotes\": \"\","
        output+="\n\t\t\"AltLookAngle\": {"
        output+="\n\t\t\t\"x\": 0.0,"
        output+="\n\t\t\t\"y\": 0.0,"
        output+="\n\t\t\t\"z\": 0.0"
        output+="\n\t\t},"
        output+="\n\t\t\"ColorDiffuse\": {"
        output+="\n\t\t\t\"r\": "+str(handTriggerArray[i][10])+","
        output+="\n\t\t\t\"g\": "+str(handTriggerArray[i][11])+","
        output+="\n\t\t\t\"b\": "+str(handTriggerArray[i][12])+","
        output+="\n\t\t\t\"a\": "+str(handTriggerArray[i][13])+""
        output+="\n\t\t},"
        output+="\n\t\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\t\"Value\": 0,"
        output+="\n\t\t\"Locked\": true,"
        output+="\n\t\t\"Grid\": false,"
        output+="\n\t\t\"Snap\": true,"
        output+="\n\t\t\"IgnoreFoW\": false,"
        output+="\n\t\t\"MeasureMovement\": false,"
        output+="\n\t\t\"DragSelectable\": true,"
        output+="\n\t\t\"Autoraise\": true,"
        output+="\n\t\t\"Sticky\": true,"
        output+="\n\t\t\"Tooltip\": true,"
        output+="\n\t\t\"GridProjection\": false,"
        output+="\n\t\t\"HideWhenFaceDown\": false,"
        output+="\n\t\t\"Hands\": false,"
        output+="\n\t\t\"FogColor\": "+str(handTriggerArray[i][0])+","
        output+="\n\t\t\"LuaScript\": \"\","
        output+="\n\t\t\"LuaScriptState\": \"\","
        output+="\n\t\t\"XmlUI\": \"\""
        output+="\n\t}"
        if(i!=len(handTriggerArray)):
            output+=",\n"
    return output

def generateBoard():
    output=""
    output+="\n\t{"
    output+="\n\t\t\"GUID\": \"0\","
    output+="\n\t\t\"Name\": \"Custom_Tile\","
    output+="\n\t\t\"Transform\": {"
    output+="\n\t\t\t\"posX\": -1.2,"
    output+="\n\t\t\t\"posY\": 0.9591922,"
    output+="\n\t\t\t\"posZ\": -0.2,"#Up/Down
    output+="\n\t\t\t\"rotX\": 0.0,"
    output+="\n\t\t\t\"rotY\": 180,"
    output+="\n\t\t\t\"rotZ\": 0.0,"
    output+="\n\t\t\t\"scaleX\": 17.6989784,"
    output+="\n\t\t\t\"scaleY\": 1.0,"
    output+="\n\t\t\t\"scaleZ\": 17.6989784"
    output+="\n\t\t},"
    output+="\n\t\t\"Nickname\": \"\","
    output+="\n\t\t\"Description\": \"\","
    output+="\n\t\t\"GMNotes\": \"\","
    output+="\n\t\t\"AltLookAngle\": {"
    output+="\n\t\t\t\"x\": 0.0,"
    output+="\n\t\t\t\"y\": 0.0,"
    output+="\n\t\t\t\"z\": 0.0"
    output+="\n\t\t},"
    output+="\n\t\t\"ColorDiffuse\": {"
    output+="\n\t\t\t\"r\": 1.0,"
    output+="\n\t\t\t\"g\": 1.0,"
    output+="\n\t\t\t\"b\": 1.0"
    output+="\n\t\t},"
    output+="\n\t\t\"LayoutGroupSortIndex\": 0,"
    output+="\n\t\t\"Value\": 0,"
    output+="\n\t\t\"Locked\": true,"
    output+="\n\t\t\"Grid\": true,"
    output+="\n\t\t\"Snap\": true,"
    output+="\n\t\t\"IgnoreFoW\": false,"
    output+="\n\t\t\"MeasureMovement\": false,"
    output+="\n\t\t\"DragSelectable\": true,"
    output+="\n\t\t\"Autoraise\": true,"
    output+="\n\t\t\"Sticky\": true,"
    output+="\n\t\t\"Tooltip\": true,"
    output+="\n\t\t\"GridProjection\": false,"
    output+="\n\t\t\"HideWhenFaceDown\": false,"
    output+="\n\t\t\"Hands\": false,"
    output+="\n\t\t\"CustomImage\": {"
    output+="\n\t\t\t\"ImageURL\": \"file:///C:\\\\Users\\\\BrownIan\\\\OneDrive - University of Wisconsin-Stout\\\\Documents\\\\GitHub\\\\DunGen\\\\output\\\\dungeon.png\","
    output+="\n\t\t\t\"ImageSecondaryURL\": \"file:///C:\\\\Users\\\\BrownIan\\\\OneDrive - University of Wisconsin-Stout\\\\Documents\\\\GitHub\\\\DunGen\\\\output\\\\dungeon.png\","
    output+="\n\t\t\t\"ImageScalar\": 1.0,"
    output+="\n\t\t\t\"WidthScale\": 0.0,"
    output+="\n\t\t\t\"CustomTile\": {"
    output+="\n\t\t\t\t\"Type\": 0,"
    output+="\n\t\t\t\t\"Thickness\": 0.2,"
    output+="\n\t\t\t\t\"Stackable\": false,"
    output+="\n\t\t\t\t\"Stretch\": true"
    output+="\n\t\t\t}"
    output+="\n\t\t},"
    output+="\n\t\t\"LuaScript\": \"\","
    output+="\n\t\t\"LuaScriptState\": \"\","
    output+="\n\t\t\"XmlUI\": \"\","
    output+="\n\t\t\"AttachedSnapPoints\": ["
    output+=generateSnappoints()
    return output