# Register Vietnamese language display name for Settings
init python:
    try:
        renpy.languages["vietnamese"] = "Tiếng Việt"
    except Exception:
        pass
