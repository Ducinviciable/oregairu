## Force default language to Vietnamese on startup so you can play immediately.
init -2000 python:
    try:
        # Set Ren'Py's default language to 'vietnamese' so the game starts with it.
        import renpy
        renpy.config.default_language = "vietnamese"
    except Exception:
        pass
