
import maya.cmds as cmds
import mtoa.aovs as aovs

aovs.AOVInterface().addAOV("Material_ID")
ass = cmds.ls(type = 'aiStandardSurface')

for a in ass:
    cmds.setAttr(a+'.aovId1', "Material_ID", type="string" )
    