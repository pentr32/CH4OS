import keyboard
import pymem
import pymem.process

dwClientState = int("0x59F19C", 0)
dwEntityList = int("0x4DFFEF4", 0)
dwLocalPlayer = int("0xDEA964", 0)
m_hActiveWeapon = int("0x2F08", 0)
m_hMyWeapons = int("0x2E08", 0)
m_iItemDefinitionIndex = int("0x2FBA", 0)
m_iItemIDHigh = int("0x2FD0", 0)
m_nFallbackPaintKit = int("0x31D8", 0)
m_nFallbackSeed = int("0x31DC", 0)
m_nFallbackStatTrak = int("0x31E4", 0)
m_flFallbackWear = int("0x31E0", 0)
m_OriginalOwnerXuidLow = int("0x31D0", 0)
m_iEntityQuality = int("0x2FBC", 0)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
engine_state = pm.read_uint(engine + dwClientState)

def main():
    keyboard.add_hotkey('F6', lambda: change_skin())
    keyboard.add_hotkey('F7', lambda: force_full_update())
    keyboard.wait()

def force_full_update():
    pm.write_int(engine_state + 0x174, -1)

def change_skin():
    paint = 344 # https://github.com/adamb70/CSGO-skin-ID-dumper/blob/master/item_index.txt
    local_player = pm.read_uint(client + dwLocalPlayer)

    for i in range(0, 8):
        my_weapons = pm.read_uint(local_player + m_hMyWeapons + 0x4) & 0xFFF
        weapon_address = pm.read_uint(client + dwEntityList + (my_weapons - 1) * 0x10)

        if weapon_address:
            weapon_id = pm.read_short(weapon_address + m_iItemDefinitionIndex)
            pm.write_int(weapon_address + m_iEntityQuality, 3)
            # weapon_owner = pm.read_uint(weapon_address + m_OriginalOwnerXuidLow)
            pm.write_int(weapon_address + m_iItemIDHigh, -1)
            # pm.write_int(weapon_address + m_OriginalOwnerXuidLow, weapon_owner)
            # pm.write_int(weapon_address + m_nFallbackStatTrak, -1)
            # pm.write_int(weapon_address + m_iItemDefinitionIndex, weapon_id)
            pm.write_int(weapon_address + m_nFallbackPaintKit, paint)
            # pm.write_int(weapon_address + m_nFallbackSeed, 661)
            pm.write_float(weapon_address + m_flFallbackWear, float(0.001))
            force_full_update()

if __name__ == '__main__':
    main()