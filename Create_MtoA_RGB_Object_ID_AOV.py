import maya.cmds as cmds
import mtoa.aovs as aovs

# create RGB ID AOV
aovs.AOVInterface().addAOV("RGB_ID")

# create Write AOV Node
cmds.createNode( 'aiWriteRgba', name="aiWriteRgba_AOV" )
cmds.setAttr('aiWriteRgba_AOV.aovName', "RGB_ID", type='string')


# connecte Nodes
cmds.connectAttr('aiWriteRgba_AOV.outColor' , 'aiAOV_RGB_ID.defaultValue')


# create Color Nodes
cmds.createNode( 'aiFlat', name="aiFlat_Red" )
cmds.setAttr('aiFlat_Red.color' , 1, 0, 0)


cmds.createNode( 'aiFlat', name="aiFlat_Green" )
cmds.setAttr('aiFlat_Green.color' , 0, 1, 0)


cmds.createNode( 'aiFlat', name="aiFlat_Blue" )
cmds.setAttr('aiFlat_Blue.color' , 0, 0, 1)

# create aiSwitch
cmds.createNode( 'aiSwitch', name="aiSwitch_RGB" )

# create UserData ObjectID
cmds.createNode( 'aiUserDataInt', name="aiUserDataInt_RGB")
cmds.setAttr('aiUserDataInt_RGB.attribute', "objectID", type='string')

# connecting Nodes
cmds.connectAttr('aiUserDataInt_RGB.outValue' , 'aiSwitch_RGB.index')
cmds.connectAttr('aiSwitch_RGB.outColor' , 'aiWriteRgba_AOV.input')
cmds.connectAttr('aiFlat_Red.outColor' , 'aiSwitch_RGB.input1')
cmds.connectAttr('aiFlat_Green.outColor' , 'aiSwitch_RGB.input2')
cmds.connectAttr('aiFlat_Blue.outColor' , 'aiSwitch_RGB.input3')


# deselect all
cmds.select( clear=True )

# create a set and add an ObjectID Atrribute
newSet1 = cmds.sets( name= "setRed")
cmds.select( 'setRed', ne=True)
cmds.addAttr( longName='mtoa_constant_objectID', attributeType="byte", defaultValue=1 )
cmds.select( 'setRed', d=True, ne=True)

newSet1 = cmds.sets( name= "setGreen")
cmds.select( 'setGreen', ne=True)
cmds.addAttr( longName='mtoa_constant_objectID', attributeType="byte", defaultValue=2 )
cmds.select( 'setGreen', d=True, ne=True)

newSet1 = cmds.sets( name= "setBlue")
cmds.select( 'setBlue', ne=True)
cmds.addAttr( longName='mtoa_constant_objectID', attributeType="byte", defaultValue=3 )
cmds.select( 'setBlue', d=True, ne=True)









