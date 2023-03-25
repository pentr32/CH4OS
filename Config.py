from pynput.keyboard import HotKey, Key

#region Glow settings
GlowEnabled = True

# RGB colors for the glow misc, when enemies are defusing the bomb.
Enemy_Defusing_Color_R = 0
Enemy_Defusing_Color_G = 150
Enemy_Defusing_Color_B = 204

# RGB colors for the glow misc, when enemies are flashed.
Enemy_Flashed_Color_R = 255
Enemy_Flashed_Color_G = 255
Enemy_Flashed_Color_B = 255
#endregion Glow settings

#region Aimbot settings
AimbotEnabled = False
#endregion Aimbot settings

#region Triggerbot settings
TriggerbotEnabled = False
#endregion Triggerbot settings

#region Bunnyhop settings
BunnyhopEnabled = False
#endregion Bunnyhop settings

#region Radar settings
RadarEnabled = False
#endregion Radar settings

#region Antiflash settings
AntiflashEnabled = False
#endregion Antiflash settings

#region RecoilControl settings
RecoilControlEnabled = False
#endregion RecoilControl settings


#region Toggle misc functions


def toggle_glow():
    global GlowEnabled
    GlowEnabled = not GlowEnabled


def toggle_aimbot():
    global AimbotEnabled
    AimbotEnabled = not AimbotEnabled


def toggle_triggerbot():
    global TriggerbotEnabled
    TriggerbotEnabled = not TriggerbotEnabled


def toggle_bunnyhop():
    global BunnyhopEnabled
    BunnyhopEnabled = not BunnyhopEnabled


def toggle_radar():
    global RadarEnabled
    RadarEnabled = not RadarEnabled


def toggle_antiflash():
    global AntiflashEnabled
    AntiflashEnabled = not AntiflashEnabled


def toggle_recoilcontrol():
    global RecoilControlEnabled
    RecoilControlEnabled = not RecoilControlEnabled
#endregion Toggle misc functions


Hotkey(HotKey.parse("numpad0"), toggle_glow())
# add_hotkey("numpad1", lambda: toggle_aimbot())
# add_hotkey("numpad2", lambda: toggle_triggerbot())
# add_hotkey("numpad3", lambda: toggle_bunnyhop())
# add_hotkey("numpad4", lambda: toggle_radar())
# add_hotkey("numpad5", lambda: toggle_antiflash())
# add_hotkey("numpad6", lambda: toggle_recoilcontrol())

# ToggleAutostrafe = ???
# ToggleChams = ???
# ToggleRankReveal = ???
# ToggleSoundESP = ???
# ToggleBoxESP = ???
# ToggleSnapLines = ???
# ToggleSkeleton
# ToggleFakeLag = ???
