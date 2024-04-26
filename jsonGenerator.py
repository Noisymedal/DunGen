import snappointStringGenerator as gen0
import csv
with open('output/walls.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

with open('output/fillings.csv', newline='') as f2:
    reader = csv.reader(f2)
    data2 = list(reader)

with open('output/rooms.csv', newline='') as f3:
    reader = csv.reader(f3)
    data3 = list(reader)

with open('output/intersect.csv', newline='')  as f4:
    reader = csv.reader(f4)
    data4 = list(reader)

with open('output/hallwaySegments.csv', newline='')  as f5:
    reader = csv.reader(f5)
    data5 = list(reader)


#THEME, 0 is basic, 1 is minecraft, 2 is Ice Palace
theme=0

def generateJson():
    output=""
    output+="{"
    output+="\n\"SaveName\": \"Dun-Gen Tool Testing\","
    output+="\n\"EpochTime\": 1708982873,"
    output+="\n\"Date\": \"2/26/2024 3:27:53 PM\","
    output+="\n\"VersionNumber\": \"v13.2.2\","
    output+="\n\"GameMode\": \"Dun-Gen Tool Testing\","
    output+="\n\"GameType\": \"\","
    output+="\n\"GameComplexity\": \"\","
    output+="\n\"Tags\": [],"
    output+="\n\"Gravity\": 0.5,"
    output+="\n\"PlayArea\": 0.5,"
    output+="\n\"Table\": \"Table_RPG\","
    output+="\n\"Sky\": \"Sky_Museum\","
    output+="\n\"Note\": \"\","
    output+="\n\"TabStates\": {"
    output+=gen0.generateTabstates()
    output+="\n},"
    output+="\n\t\"Grid\": {"
    output+="\n\t\"Type\": 0,"
    output+="\n\t\"Lines\": false,"
    output+="\n\t\"Color\": {"
    output+="\n\t\t\"r\": 0.0,"
    output+="\n\t\t\"g\": 0.0,"
    output+="\n\t\t\"b\": 0.0"
    output+="\n\t},"
    output+="\n\t\"Opacity\": 0.75,"
    output+="\n\t\"ThickLines\": false,"
    output+="\n\t\"Snapping\": false,"
    output+="\n\t\"Offset\": false,"
    output+="\n\t\"BothSnapping\": false,"
    output+="\n\t\"xSize\": 2.0,"
    output+="\n\t\"ySize\": 2.0,"
    output+="\n\t\"PosOffset\": {"
    output+="\n\t\t\"x\": 0.0,"
    output+="\n\t\t\"y\": 1.0,"
    output+="\n\t\"z\": 0.0"
    output+="\n\t}"
    output+="\n},"
    output+="\n\"Lighting\": {"
    output+="\n\t\"LightIntensity\": 0.54,"
    output+="\n\t\"LightColor\": {"
    output+="\n\t\t\"r\": 1.0,"
    output+="\n\t\t\"g\": 0.9804,"
    output+="\n\t\t\"b\": 0.8902"
    output+="\n\t},"
    output+="\n\"AmbientIntensity\": 1.3,"
    output+="\n\t\"AmbientType\": 0,"
    output+="\n\t\"AmbientSkyColor\": {"
    output+="\n\t\t\"r\": 0.5,"
    output+="\n\t\t\"g\": 0.5,"
    output+="\n\t\t\"b\": 0.5"
    output+="\n\t},"
    output+="\n\t\"AmbientEquatorColor\": {"
    output+="\n\t\t\"r\": 0.5,"
    output+="\n\n\t\t\"g\": 0.5,"
    output+="\n\t\t\"b\": 0.5"
    output+="\n\t},"
    output+="\n\t\"AmbientGroundColor\": {"
    output+="\n\t\t\"r\": 0.5,"
    output+="\n\t\t\"g\": 0.5,"
    output+="\n\t\t\"b\": 0.5"
    output+="\n\t},"
    output+="\n\t\"ReflectionIntensity\": 1.0,"
    output+="\n\t\"LutIndex\": 0,"
    output+="\n\t\"LutContribution\": 1.0"
    output+="\n},"
    output+="\n\"Hands\": {"
    output+="\n\t\"Enable\": true,"
    output+="\n\t\"DisableUnused\": false,"
    output+="\n\t\"Hiding\": 0"
    output+="\n},"
    output+="\n\"ComponentTags\": {"
    output+="\n\t\"labels\": []"
    output+="\n},"
    output+="\n\"Turns\": {"
    output+="\n\t\"Enable\": false,"
    output+="\n\t\"Type\": 0,"
    output+="\n\t\"TurnOrder\": [],"
    output+="\n\n\t\"Reverse\": false,"
    output+="\n\t\"SkipEmpty\": false,"
    output+="\n\t\"DisableInteractions\": false,"
    output+="\n\t\"PassTurns\": true,"
    output+="\n\t\"TurnColor\": \"\""
    output+="\n},"
    output+="\n\"DecalPallet\": [],"
    output+="\n\"LuaScript\": \"--[[ Lua code. See documentation: https://api.tabletopsimulator.com/ --]]\\n\\n--[[ The onLoad event is called after the game save finishes loading. --]]\\nfunction onLoad()\\n    --[[ print('onLoad!') --]]\\nend\\n\\n--[[ The onUpdate event is called once per frame. --]]\\nfunction onUpdate()\\n    --[[ print('onUpdate loop!') --]]\\nend\","
    output+="\n\"LuaScriptState\": \"\","
    output+="\n\"XmlUI\": \"<!-- Xml UI. See documentation: https://api.tabletopsimulator.com/ui/introUI/ -->\","
    output+="\n\"ObjectStates\": ["
    output+=gen0.generateHandtrigger()
    output+=gen0.generateBoard()
    output+=gen0.generateDungeonBricks(data,theme) #WALLS
    # output+=gen0.generateDungeonHats(data)+","
    output+=gen0.generateDungeonFillings(data2,0) #THIS ONES IS FOR FILLINGS
    # output+=gen0.generateDungeonFillingHats(data2)+","
    output+=gen0.generateDungeonFillings(data3,0) #THIS ONE IS FOR THE ROOMS
    # output+=gen0.generateDungeonFillingHats(data3)
    output+=gen0.generateDungeonIntersects(data4)#Intersects
    output+=gen0.generateDungeonFillings(data5,1)#HallwaySegments
    output+="\n]\n}"
    file1 = open('TS_Save_7.json', 'w')
    file1.write(output)
    file1.close()
    print("A")
    return output

generateJson()
