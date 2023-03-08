import time
from keyboard import is_pressed
from Helpers.Offsets import *
from Helpers.Enums import MoveType_t


def can_bunnyhop(local_player_move_type, local_player_flags):
    player_can_bunnyhop = local_player_move_type not in [
        MoveType_t.MOVETYPE_LADDER,
        MoveType_t.MOVETYPE_FLY,
        MoveType_t.MOVETYPE_NOCLIP,
        MoveType_t.MOVETYPE_OBSERVER,
    ] and local_player_flags not in [262, 256]

    return player_can_bunnyhop


def bunnyhop(pm, client, player, local_player_move_type, local_player_flags):

    if can_bunnyhop(local_player_move_type, local_player_flags):
        force_jump = client + dwForceJump

        if is_pressed("space"):
            if player:
                pm.write_int(force_jump, 5)
                time.sleep(0.015)
                pm.write_int(force_jump, 4)

