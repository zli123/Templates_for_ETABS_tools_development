import comtypes.client
import os
#Create API helper object
helper = comtypes.client.CreateObject('ETABSv1.Helper')
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

APIPath = 'C:\ETABS Template Files'
ModelPath = ""
ModelPath = APIPath + os.sep + 'test.edb'

#Create an instance of the ETABS object from the latest installed ETABS
myETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject")

#Start ETABS application
myETABSObject.ApplicationStart()

#Create SapModel object, the data structure of an ETABS Model
SapModel = myETABSObject.SapModel

#Initialize model
SapModel.InitializeNewModel()
dictPierData = {}
pierDataFromETABS = []
pierAssignmentFromETABS = []
ret = SapModel.File.OpenFile("C:/Users/zli/Desktop/Block F/Latest ETABS Model/Block-F-0.25S-1.0W-S-WT-11.08_correct_wall_thickness.edb")
ret = SapModel.DesignConcrete.GetCode()
codeVersion = ret[0]
ret = SapModel.DatabaseTables.GetTableForDisplayArray("Shear Wall Pier Design Summary - " + codeVersion, ["DesignType", "Story", "Pier", "ReinfPcent"], "null", 0)
#ret = SapModel.DesignShearWall.GetPierSummaryResults()

ret = SapModel.DatabaseTables.GetAllFieldsInTable("Pier Section Properties")
ret = SapModel.DatabaseTables.GetTableForDisplayArray("Pier Section Properties", ["Story", "Pier", "WidthBot", "ThickBot", "Material"], "null", 0)
wallGeometry = ret[:]
ret = SapModel.DatabaseTables.GetAllFieldsInTable("Pier Section Definitions - General Pier")
ret = SapModel.DatabaseTables.GetTableForDisplayArray("Pier Section Definitions - General Pier", ["Name", "Material"], "null", 0)

ret = SapModel.DatabaseTables.GetAllFieldsInTable("Area Assignments - Section Properties")

ret = SapModel.File.Save(ModelPath)
ret = myETABSObject.ApplicationExit(False)
SapModel = None
myETABSObject = None

print("Woohoo")
