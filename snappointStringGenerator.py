
boardSize=39
spaceSize=0.019*2.5
zeroZero = [-0.95,-0.95]

def generateSnappoints():
    output=""
    for i in range(0,boardSize):
        xval = zeroZero[0]+(i*spaceSize)
        for j in range(0,boardSize):
            yval = zeroZero[1]+(j*spaceSize)
            output+=("\n{\n\t\"Position\": {\n\t \"x\": "+str(xval)+",\n\t \"y\": 0.0,\n\t \"z\": "+str(yval)+"\n\t }\n}," )
    file1 = open('snappoints.txt', 'w')
    file1.write(output)
    file1.close()

id=1
generateID():
    id=id+1
    return str(id)

def generateDungeonBricks(points):
    output=""

    for i in range(0,len(points)):
        output+="{\n\t\"GUID\": "+generateID()+","
        output+="\n\t\"Name\": \"DungeonBrick\","
        output+="\n\t\"Transform\": {"
        output+="\n\t\t\"posX\": "+points[i[0]]*spaceSize+","
        output+="\n\t\t\"posY\": 1.33155191,"
        output+="\n\t\t\"posZ\": "+points[i[1]]*spaceSize+","
        output+="\n\t\t\"rotX\": 0.0,
        output+="\n\t\t\"rotY\": 0.0,
        output+="\n\t\t\"rotZ\": 0.0,
        output+="\n\t\t\"scaleX\": 0.173,"
        output+="\n\t\t\"scaleY\": 0.173,"
        output+="\n\t\t\"scaleZ\": 0.173,"
        output+="\n\t},"
        output+="\n\t\"Nickname\": \"\","
        output+="\n\t\"Description\": \"\","
        output+="\n\t\"GMNotes\": \"\","
        output+="\n\t\"AltLookAngle\": {"
        output+="\n\t\t\"x\": 0.0\","
        output+="\n\t\t\"y\": 0.0\","
        output+="\n\t\t\"z\": 0.0\","
        output+="\n\t}," 
        output+="\n\t\"ColorDiffuse\": {"
        output+="\n\t\t\"r\": 1.0,"
        output+="\n\t\t\"g\": 1.0,"
        output+="\n\t\t\"b\": 1.0,"
        output+="\n\t},"
        output+="\n\t\"LayoutGroupSortIndex\": 0,"
        output+="\n\t\"Value\": 0,"
        output+="\n\t\"Locked: true,"
        output+="\n\t\"Grid\": true,"
        output+="\n\t\"Snap\": true,:
        output+="\n\t\"IngoreFoW\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"MeasureMovement\": false,"
        output+="\n\t\"DragSelectable\": true,"
        output+="\n\t\"Autoraise\": true,"
        output+="\n\t\"Sticky\": true,"
        output+="\n\t\"Tooltip\": true,"
        output+="\n\t\"GridProjection\": false,"
        output+="\n\t\"HideWhenFaceDown\": false,""
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
        output+="\n\t},""
        output+="\n\"LuaScript\": \"\","
        output+="\n\"LuaScriptState\": \"\","
        output+="\n\"XmlUI\": \"\""
        output+="\n\"}"
        if(i!=len(points)):
            output+=",\n"
    file2 = open('dungeonBricks.txt', 'w')
    file2.write(output)
    file2.close()
    
        



