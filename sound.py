try:
    import winsound as _winsound
    def play_music(file):
        _winsound.PlaySound(file, winsound.SND_ALIAS | winsound.SND_ASYNC)
except ImportError:
    def PlaySound(file):
        pass