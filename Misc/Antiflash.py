from Helpers.Offsets import *


def anti_flash(pm, player):

    is_flashed = pm.read_int(player + m_flFlashMaxAlpha)

    if is_flashed > 1:
        pm.write_int(player + m_flFlashMaxAlpha, 0)
