from Helpers.Offsets import *
from Helpers.Enums import Team
import time


def GetPlayerVars(pm, client, engine, engine_pointer):
    player = pm.read_uint(client + dwLocalPlayer)
    engine_pointer = pm.read_uint(engine + dwClientState)
    glow_manager = pm.read_uint(client + dwGlowObjectManager)
    crosshairid = pm.read_uint(player + m_iCrosshairId)
    getcrosshairtarget = pm.read_uint(client + dwEntityList + (crosshairid - 1) * 0x10)
    immunitygunganme = pm.read_uint(getcrosshairtarget + m_bGunGameImmunity)
    localteam = pm.read_uint(player + m_iTeamNum)
    crosshairteam = pm.read_uint(getcrosshairtarget + m_iTeamNum)
    y_angle = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)

    return player, engine_pointer, glow_manager, crosshairid, getcrosshairtarget, immunitygunganme, localteam, \
        crosshairteam, y_angle


def GetEntityVars(pm, entity):
    while True:
        try:
            entity_glow = pm.read_uint(entity + m_iGlowIndex)
            entity_team_id = pm.read_uint(entity + m_iTeamNum)
            entity_is_defusing = pm.read_bool(entity + m_bIsDefusing)
            entity_flash_duration = pm.read_float(entity + m_flFlashDuration)
            if entity_flash_duration > 0.1:
                entity_is_flashed = True
            else:
                entity_is_flashed = False
            entity_hp = pm.read_uint(entity + m_iHealth)
            entity_dormant = pm.read_uint(entity + m_bDormant)
        except Exception as e:
            print("Could not load entity variables")
            time.sleep(0.2)
            continue
        return entity_glow, entity_team_id, entity_is_defusing, entity_is_flashed, entity_hp, entity_dormant

