from WinAPI.Keyboard import *


class Controls:
    ToggleAimbot = VK_NUMPAD1
    ToggleAntiflash = VK_NUMPAD5
    ToggleBunnyhop = VK_NUMPAD3
    ToggleGlow = VK_NUMPAD0
    ToggleRadar = VK_NUMPAD4
    ToggleTriggerbot = VK_NUMPAD2
    ToggleRecoilControl = VK_NUMPAD6

    # ToggleAutostrafe = ???
    # ToggleChams = ???
    # ToggleRankReveal = ???
    # ToggleSoundESP = ???
    # ToggleBoxESP = ???
    # ToggleSnapLines = ???
    # ToggleSkeleton
    # ToggleFakeLag = ???


class Settings:
    class Radar:
        Enabled = False

    class Bunnyhop:
        Enabled = False
        Key = 0x20  # VK_SPACE

    class Trigger:
        Enabled = True
        Delay = 0

    class Antiflash:
        Enabled = False

    class Glow:
        Enabled = True

        C4 = True
        C4_Color_R = 231
        C4_Color_G = 76
        C4_Color_B = 60
        C4_Color_A = 255

        Grenades = True
        Grenades_Color_R = 241
        Grenades_Color_G = 196
        Grenades_Color_B = 15
        Grenades_Color_A = 255

        Enemies = True
        Enemies_Color_R = 192
        Enemies_Color_G = 57
        Enemies_Color_B = 43
        Enemies_Color_A = 180

    # class Aimbot:
    #     Enabled = True
    #     Fov = 4.0
    #     Bone = 8
    #     Smooth = 2.0
    #     VisibleCheck = False
    #     RecoilControl = True
    #     YawRecoilReductionFactory = 2.0
    #     PitchRecoilReductionFactory = 2.0
    #     Curve = False
    #     CurveY = 0.5
    #     CurveX = 10.0
