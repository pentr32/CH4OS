import pymem
import re
import requests
from Modules import *


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


def transform_patterns():  # unfinished

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


pm = pymem.Pymem(ProcessName)

m_ArmorValue = 0x117CC
m_Collision = 0x320
m_CollisionGroup = 0x474
m_Local = 0x2FCC
m_MoveType = 0x25C
m_OriginalOwnerXuidHigh = 0x31D4
m_OriginalOwnerXuidLow = 0x31D0
m_aimPunchAngle = 0x303C
m_aimPunchAngleVel = 0x3048
m_bGunGameImmunity = 0x9990
m_bHasDefuser = 0x117DC
m_bHasHelmet = 0x117C0
m_bInReload = 0x32B5
m_bIsDefusing = 0x997C
m_bIsScoped = 0x9974
m_bSpotted = 0x93D
m_bSpottedByMask = 0x980
m_dwBoneMatrix = 0x26A8
m_fAccuracyPenalty = 0x3340
m_fFlags = 0x104
m_flFallbackWear = 0x31E0
m_flFlashDuration = 0x10470
m_flFlashMaxAlpha = 0x1046C
m_flNextPrimaryAttack = 0x3248
m_hActiveWeapon = 0x2F08
m_hMyWeapons = 0x2E08
m_hObserverTarget = 0x339C
m_hOwner = 0x29DC
m_hOwnerEntity = 0x14C
m_iAccountID = 0x2FD8
m_iClip1 = 0x3274
m_iCrosshairId = 0x11838
m_iEntityQuality = 0x2FBC
m_iFOVStart = 0x31F8
m_iGlowIndex = 0x10488
m_iHealth = 0x100
m_iItemDefinitionIndex = 0x2FBA
m_iItemIDHigh = 0x2FD0
m_iObserverMode = 0x3388
m_iShotsFired = 0x103E0
m_iState = 0x3268
m_iTeamNum = 0xF4
m_lifeState = 0x25F
m_nFallbackPaintKit = 0x31D8
m_nFallbackSeed = 0x31DC
m_nFallbackStatTrak = 0x31E4
m_nForceBone = 0x268C
m_nTickBase = 0x3440
m_rgflCoordinateFrame = 0x444
m_szCustomName = 0x304C
m_szLastPlaceName = 0x35C4
m_vecOrigin = 0x138
m_vecVelocity = 0x114
m_vecViewOffset = 0x108
m_viewPunchAngle = 0x3030

m_clrRender = 0x70

# dwClientState_ViewAngles = 0x4D90
dwClientState_State = 0x108
dwClientState_MaxPlayer = 0x388

dwGlowObjectManager = get_signature(pm, Client, bytes(patterns["dwGlowObjectManager"], encoding="raw_unicode_escape"), 4, 1)
print(dwGlowObjectManager)

dwEntityList = get_signature(pm, Client, bytes(patterns["dwEntityList"], encoding="raw_unicode_escape"), 0, 1)
print(dwEntityList)

dwClientState = get_signature(pm, Engine, bytes(patterns["dwClientState"], encoding="raw_unicode_escape"), 0, 1)
print(dwClientState)

dwForceJump = get_signature(pm, Client, bytes(patterns["dwForceJump"], encoding="raw_unicode_escape"), 0, 2)
print(dwForceJump)

dwLocalPlayer = get_signature(pm, Client, bytes(patterns["dwLocalPlayer"], encoding="raw_unicode_escape"), 4, 3)
print(dwLocalPlayer)

dwClientState_ViewAngles = int(get_signature(pm, "engine.dll", bytes(patterns["dwClientState_ViewAngles"], encoding="raw_unicode_escape"), 0, 4, False), 0)
print(dwClientState_ViewAngles)

dwRadarBase = get_signature(pm, Client, bytes(patterns["dwRadarBase"], encoding="raw_unicode_escape"), 0, 1)
print(dwRadarBase)

m_bDormant = get_signature(pm, Client, bytes(patterns["m_bDormant"], encoding="raw_unicode_escape"), 8, 2, False)
print(m_bDormant)
