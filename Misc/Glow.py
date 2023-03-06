

def SetEntityGlow(pm, entity_hp, enemy_team_id, entity_is_defusing, entity_is_flashed, entity_dormant, my_team_id, glow_manager, entity_glow):

    # Change color base on entity HP
    if entity_hp > 50 and not entity_hp == 100:
        r, g, b = 255, 165, 0
    elif entity_hp < 50:
        r, g, b = 255, 0, 0
    elif entity_hp == 100 and enemy_team_id == 2:
        r, g, b = 0, 255, 0
    else:
        r, g, b = 0, 255, 0

    # Change color base on entity is flashed
    if entity_is_flashed:
        r, g, b = 0, 150, 204

    # Change color base on entity is defusing
    if entity_is_defusing:
        r, g, b = 0, 150, 204

    # Enemy team = Terrorist / My team = Counter-Terrorist
    if enemy_team_id == 2 and my_team_id != 2 and not entity_dormant:

        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)   # Enable glow function

    # Enemy team = Counter-Terrorist / My team = Terrorist
    elif enemy_team_id == 3 and my_team_id != 3 and not entity_dormant:

        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)   # Enable glow function

