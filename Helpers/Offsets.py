import pymem
import re
import requests
from Helpers.Globals import *


def get_signature(pm, modulename, pattern, extra=0, offset=0, relative=True):
    if offset == 0:
        module = pymem.process.module_from_name(pm.process_handle, modulename)
        bytes = pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
        match = re.search(pattern, bytes).start()
        res = match + extra
        return res
    module = pymem.process.module_from_name(pm.process_handle, modulename)
    bytes = pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
    match = re.search(pattern, bytes).start()
    non_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra
    yes_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra - module.lpBaseOfDll
    return "0x{:X}".format(yes_relative) if relative else "0x{:X}".format(non_relative)


patterns = {}


def aob():

    response = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/config.json").json()
    for struct in response["signatures"]:
        old = str(struct["pattern"])
        new = old.replace("?", ".")
        new = new.split(" ")
        newone = ""
        for element in new:
            if element != ".":
                element = r'\x' + element
            newone = newone + element
        patterns[struct["name"]] = newone


aob()


game = pymem.Pymem(ProcessName)

m_ArmorValue = int("0x117CC", 0)
m_Collision = int("0x320", 0)
m_CollisionGroup = int("0x474", 0)
m_Local = int("0x2FCC", 0)
m_MoveType = int("0x25C", 0)
m_OriginalOwnerXuidHigh = int("0x31D4", 0)
m_OriginalOwnerXuidLow = int("0x31D0", 0)
m_aimPunchAngle = int("0x303C", 0)
m_aimPunchAngleVel = int("0x3048", 0)
m_bGunGameImmunity = int("0x9990", 0)
m_bHasDefuser = int("0x117DC", 0)
m_bHasHelmet = int("0x117C0", 0)
m_bInReload = int("0x32B5", 0)
m_bIsDefusing = int("0x997C", 0)
m_bIsScoped = int("0x9974", 0)
m_bSpotted = int("0x93D", 0)
m_bSpottedByMask = int("0x980", 0)
m_dwBoneMatrix = int("0x26A8", 0)
m_fAccuracyPenalty = int("0x3340", 0)
m_fFlags = int("0x104", 0)
m_flFallbackWear = int("0x31E0", 0)
m_flFlashDuration = int("0x10470", 0)
m_flFlashMaxAlpha = int("0x1046C", 0)
m_flNextPrimaryAttack = int("0x3248", 0)
m_hActiveWeapon = int("0x2F08", 0)
m_hMyWeapons = int("0x2E08", 0)
m_hObserverTarget = int("0x339C", 0)
m_hOwner = int("0x29DC", 0)
m_hOwnerEntity = int("0x14C", 0)
m_iAccountID = int("0x2FD8", 0)
m_iClip1 = int("0x3274", 0)
m_iCrosshairId = int("0x11838", 0)
m_iEntityQuality = int("0x2FBC", 0)
m_iFOVStart = int("0x31F8", 0)
m_iGlowIndex = int("0x10488", 0)
m_iHealth = int("0x100", 0)
m_iItemDefinitionIndex = int("0x2FBA", 0)
m_iItemIDHigh = int("0x2FD0", 0)
m_iObserverMode = int("0x3388", 0)
m_iShotsFired = int("0x103E0", 0)
m_iState = int("0x3268", 0)
m_iTeamNum = int("0xF4", 0)
m_lifeState = int("0x25F", 0)
m_nFallbackPaintKit = int("0x31D8", 0)
m_nFallbackSeed = int("0x31DC", 0)
m_nFallbackStatTrak = int("0x31E4", 0)
m_nForceBone = int("0x268C", 0)
m_nTickBase = int("0x3440", 0)
m_rgflCoordinateFrame = int("0x444", 0)
m_szCustomName = int("0x304C", 0)
m_szLastPlaceName = int("0x35C4", 0)
m_vecOrigin = int("0x138", 0)
m_vecVelocity = int("0x114", 0)
m_vecViewOffset = int("0x108", 0)
m_viewPunchAngle = int("0x3030", 0)

m_clrRender = int("0x70", 0)

dwClientState_State = int("0x108", 0)
dwClientState_MaxPlayer = int("0x388", 0)


dwGlowObjectManager = get_signature(game, ClientDll, bytes(patterns["dwGlowObjectManager"], encoding="raw_unicode_escape"), 4, 1)
dwGlowObjectManager = int(dwGlowObjectManager, 0)
print(f"dwGlowObjectManager -> {dwGlowObjectManager}")

dwEntityList = get_signature(game, ClientDll, bytes(patterns["dwEntityList"], encoding="raw_unicode_escape"), 0, 1)
dwEntityList = int( dwEntityList, 0)
print(f"dwEntityList -> {dwEntityList}")

dwClientState = get_signature(game, EngineDll, bytes(patterns["dwClientState"], encoding="raw_unicode_escape"), 0, 1)
dwClientState = int(dwClientState, 0)
print(f"dwClientState -> {dwClientState}")

dwForceJump = get_signature(game, ClientDll, bytes(patterns["dwForceJump"], encoding="raw_unicode_escape"), 0, 2)
dwForceJump = int(dwForceJump, 0)
print(f"dwForceJump -> {dwForceJump}")

dwLocalPlayer = get_signature(game, ClientDll, bytes(patterns["dwLocalPlayer"], encoding="raw_unicode_escape"), 4, 3)
dwLocalPlayer = int(dwLocalPlayer, 0)
print(f"dwLocalPlayer -> {dwLocalPlayer}")

dwClientState_ViewAngles = get_signature(game, "engine.dll", bytes(patterns["dwClientState_ViewAngles"], encoding="raw_unicode_escape"), 0, 4, False)
dwClientState_ViewAngles = int(dwClientState_ViewAngles, 0)
print(f"dwClientState_ViewAngles -> {dwClientState_ViewAngles}")

dwRadarBase = get_signature(game, ClientDll, bytes(patterns["dwRadarBase"], encoding="raw_unicode_escape"), 0, 1)
dwRadarBase = int(dwRadarBase, 0)
print(f"dwRadarBase -> {dwRadarBase}")

dwViewMatrix = get_signature(game, ClientDll, bytes(patterns["dwViewMatrix"], encoding="raw_unicode_escape"), 176, 3)
dwViewMatrix = int(dwViewMatrix, 0)
print(f"dwViewMatrix -> {dwViewMatrix}")

m_bDormant = get_signature(game, ClientDll, bytes(patterns["m_bDormant"], encoding="raw_unicode_escape"), 8, 2, False)
m_bDormant = int(m_bDormant, 0)
print(f"m_bDormant -> {m_bDormant}")

game.close_process()    # Close game handler once all the offsets have been found
