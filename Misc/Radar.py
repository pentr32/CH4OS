from Helpers.Offsets import *


def radar(pm, entity):
    pm.write_int(entity + m_bSpotted, 1)