import winsound
import time
              #to play the music


              #to stop the music 
#insound.PlaySound(None, winsound.SND_ALIAS)

              #to play music asynchronously
#winsound.PlaySound("filename",  winsound.SND_ALIAS | winsound.SND_ASYNC)


def intro():
    winsound.PlaySound('Title music.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    for i in range(100):
        print("")
    time.sleep(1)
    string = "  STAR WARS "
    print(string.center(70, '*'))
    print()
    string = "THERE HAVE BEEN REPORTS THAT PRINCESS LEIA"
    print(string.center(70))
    print()
    string = "HAS BEEN CAPTURED BY THE GALACTIC EMPIRE"
    print(string.center(70))
    print()
    string = "IT IS UP TO YOU TO SAVE HER"
    print(string.center(70))
    print()
    string = "PICK A CHARACTER, BUT BE WARNED, A DARK PATH LIES AHEAD."
    print(string.center(70))
    print()
    for i in range(36):
        time.sleep(0.5)
        print("")

intro()
