import maya.cmds as cmds


shader = cmds.shadingNode( 'VRayLightMtl', asShader=True, name="VRayLightMtl_BLACK" )
cmds.setAttr('VRayLightMtl_BLACK.compensateCameraExposure' , 1)
cmds.setAttr('VRayLightMtl_BLACK.color' , 0, 0, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="VRayLightMtl_BLACKSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'VRayLightMtl', asShader=True, name="VRayLightMtl_RED" )
cmds.setAttr('VRayLightMtl_RED.compensateCameraExposure' , 1)
cmds.setAttr('VRayLightMtl_RED.color' , 1, 0, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="VRayLightMtl_REDSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'VRayLightMtl', asShader=True, name="VRayLightMtl_GREEN" )
cmds.setAttr('VRayLightMtl_GREEN.compensateCameraExposure' , 1)
cmds.setAttr('VRayLightMtl_GREEN.color' , 0, 1, 0)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="VRayLightMtl_GREENSG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)

shader = cmds.shadingNode( 'VRayLightMtl', asShader=True, name="VRayLightMtl_BLUE" )
cmds.setAttr('VRayLightMtl_BLUE.compensateCameraExposure' , 1)
cmds.setAttr('VRayLightMtl_BLUE.color' , 0, 0, 1)
shadingGroup = cmds.sets( shader, renderable=True, noSurfaceShader=True, empty=True, name="VRayLightMtl_BLUESG" )
cmds.connectAttr(shader+".outColor", shadingGroup+".surfaceShader", force=True)


