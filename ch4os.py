from Helpers.Checkers import *
from Misc.Glow import SetEntityGlow
import time
import threading


def main():

    try:
        pm = pymem.Pymem(ProcessName)

    except Exception:
        print("Could not find the csgo.exe process !")
        quit(0)

    print("\n\nCH4OS started!")
    client = pymem.process.module_from_name(pm.process_handle, ClientDll).lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, EngineDll).lpBaseOfDll
    engine_pointer = pm.read_uint(engine + dwClientState)

    while True:
        time.sleep(0.0025)

        if client and engine and pm:
            try:
                player, engine_pointer, glow_manager, crosshairid, getcrosshairTarget, immunitygunganme, \
                    localTeam, crosshairTeam, y_angle = GetPlayerVars(pm, client, engine, engine_pointer)

            except Exception as e:
                time.sleep(2)
                continue

        for i in range(0, 64):  # Loop through all entities.
            entity = pm.read_uint(client + dwEntityList + i * 0x10)
            if entity:
                entity_glow, entity_team_id, entity_is_defusing, entity_is_flashed, entity_hp, entity_dormant = GetEntityVars(pm, entity)
                SetEntityGlow(pm, entity_hp, entity_team_id, entity_is_defusing, entity_is_flashed, entity_dormant, localTeam, glow_manager,
                              entity_glow)


if __name__ == "__main__":
    threading.Thread(target=main).start()