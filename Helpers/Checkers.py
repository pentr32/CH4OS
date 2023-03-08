from Helpers.Offsets import *
from Helpers.Enums import MoveType_t
import time


def get_player_vars(pm, client, engine, engine_pointer):
    player = pm.read_uint(client + dwLocalPlayer)
    engine_pointer = pm.read_uint(engine + dwClientState)
    glow_manager = pm.read_uint(client + dwGlowObjectManager)
    crosshair_id = pm.read_uint(player + m_iCrosshairId)
    crosshair_target = pm.read_uint(client + dwEntityList + (crosshair_id - 1) * 0x10)
    immunity_gun_game = pm.read_uint(crosshair_target + m_bGunGameImmunity)
    local_team = pm.read_uint(player + m_iTeamNum)
    crosshair_team = pm.read_uint(crosshair_target + m_iTeamNum)
    local_player_move_type = pm.read_uint(player + m_MoveType)
    local_player_flag = pm.read_uint(player + m_fFlags)
    y_angle = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)

    return player, engine_pointer, glow_manager, crosshair_id, crosshair_target, immunity_gun_game, local_team, \
        crosshair_team, y_angle, local_player_move_type, local_player_flag


def get_entity_vars(pm, entity):
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
        except Exception:
            print("Could not load entity variables")
            time.sleep(0.2)
            continue

        return entity_glow, entity_team_id, entity_is_defusing, entity_is_flashed, entity_hp, entity_dormant
