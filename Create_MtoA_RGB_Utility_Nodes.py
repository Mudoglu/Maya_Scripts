import maya.cmds as cmds


shader = cmds.shadingNode( 'aiUtility', asShader=True, name="aiUtility_BLACK" )
cmds.setAttr('aiUtility_BLACK.shadeMode' , 2)
cmds.setAttr('aiUtility_BLACK.color' , 0, 0, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="aiUtility_BLACKSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'aiUtility', asShader=True, name="aiUtility_RED" )
cmds.setAttr('aiUtility_RED.shadeMode' , 2)
cmds.setAttr('aiUtility_RED.color' , 1, 0, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="aiUtility_REDSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'aiUtility', asShader=True, name="aiUtility_GREEN" )
cmds.setAttr('aiUtility_GREEN.shadeMode' , 2)
cmds.setAttr('aiUtility_GREEN.color' , 0, 1, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="aiUtility_GREENSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'aiUtility', asShader=True, name="aiUtility_BLUE" )
cmds.setAttr('aiUtility_BLUE.shadeMode' , 2)
cmds.setAttr('aiUtility_BLUE.color' , 0, 0, 1)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="aiUtility_BLUESG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

