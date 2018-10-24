try:
    import winsound as _winsound
    def play_music(file):
        _winsound.PlaySound(file, _winsound.SND_ALIAS | _winsound.SND_ASYNC)
    def stop_music(file):
        _winsound.PlaySound(None, _winsound.SND_ALIAS)
except ImportError:
    def play_music(file):
        pass
    def stop_music(file):
        pass