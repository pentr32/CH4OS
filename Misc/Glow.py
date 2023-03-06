

def SetEntityGlow(pm, entity_hp, enemy_team_id, entity_is_defusing, entity_is_flashed, entity_dormant, my_team_id, glow_manager, entity_glow):

    if entity_hp > 50 and not entity_hp == 100:
        r, g, b = 255, 165, 0
    elif entity_hp < 50:
        r, g, b = 255, 0, 0
    elif entity_hp == 100 and enemy_team_id == 2:
        r, g, b = 0, 255, 0
    else:
        r, g, b = 0, 255, 0

    if enemy_team_id == 2 and my_team_id != 2 and not entity_dormant:

        if entity_is_flashed:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(150))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(104))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(250))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
        else:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

        if entity_is_defusing:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(150))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(104))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(250))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
        else:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

    elif enemy_team_id == 3 and my_team_id != 3 and not entity_dormant:

        if entity_is_flashed:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(150))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(104))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(250))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
        else:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

        if entity_is_defusing:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(150))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(104))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(250))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
        else:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A

            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

