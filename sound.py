try:
    import winsound as sound
except ImportError:
    class winsound:
        def PlaySound(*args):
            pass
        SND_ALIAS = 0
        SND_ASYNC = 0
