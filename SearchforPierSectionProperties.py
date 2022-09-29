import comtypes.client
#Create API helper object
helper = comtypes.client.CreateObject('ETABSv1.Helper')
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

#Create an instance of the ETABS object from the latest installed ETABS
myETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject")

#Start ETABS application
myETABSObject.ApplicationStart()

#Create SapModel object, the data structure of an ETABS Model
SapModel = myETABSObject.SapModel

#Initialize model
SapModel.InitializeNewModel()
dictReinf = {}
ret = SapModel.File.OpenFile("C:/Users/zli/Desktop/Ililani/Illilani-ULT-Slab0.1Ig-Walls-method-3-cracked_SD_ZL_Changes in roof walls_V6.edb")
ret = SapModel.DatabaseTables.GetAllFieldsInTable("Shear Wall Pier Design Summary - ACI 318-14")
ret = SapModel.DatabaseTables.GetTableForDisplayArray("Shear Wall Pier Design Summary - ACI 318-14", ["DesignType", "Story", "Pier", "ReinfPcent"], "null", 0)
if(ret[2][0] == None):
    ret = SapModel.DatabaseTables.GetTableForDisplayArray("Shear Wall Pier Design Summary - ACI 318-19", ["DesignType", "Story", "Pier", "ReinfPcent"], "null", 0)
    if(ret[2][0] == None):
        ret = SapModel.DatabaseTables.GetTableForDisplayArray("Shear Wall Pier Design Summary - ACI 318-11", ["DesignType", "Story", "Pier", "ReinfPcent"], "null", 0)
        if(ret[2][0] == None):
            ret = SapModel.DatabaseTables.GetTableForDisplayArray("Shear Wall Pier Design Summary - ACI 318-08", ["DesignType", "Story", "Pier", "ReinfPcent"], "null", 0)
            if([2][0] == None):
                ret = [[], [], [], [], [], []]
reinforcement = ret[:]
reinforcementBlocks = []
block = []
for i in reinforcement[4]:
    block.append(i)
    if(len(block) == 4):
        reinforcementBlocks.append(block)
        block = []
previousSignature = ("","")
numLegs = 0
for i in reinforcementBlocks:
    currentSignature = (i[1], i[0])
    numLegs += 1
    if(currentSignature != previousSignature):
        previousSignature = currentSignature
        if(numLegs != 2):
            dictReinf[currentSignature] = (i[2], i[3], False)
        else:
            dictReinf[currentSignature] = (i[2], i[3], True)
        numLegs = 0

print("Woohoo")
