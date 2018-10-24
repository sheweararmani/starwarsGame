from sound import winsound
import time
              #to play the music


              #to stop the music 
#winsound.PlaySound(None, winsound.SND_ALIAS)

              #to play music asynchronously
#winsound.PlaySound("filename", winsound.SND_ALIAS | winsound.SND_ASYNC)

              #to play music in a loop
#winsound.PlaySound("filename", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)


def intro():
    winsound.PlaySound('Title music.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    for _ in range(100):
        print("")
    time.sleep(1)
    string = "  STAR WARS "
    print(string.center(70, '*'))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "THERE HAVE BEEN REPORTS THAT PRINCESS LEIA"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "HAS BEEN CAPTURED BY THE GALACTIC EMPIRE"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "IT IS UP TO YOU TO SAVE HER"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "PICK A CHARACTER, BUT BE WARNED, A DARK PATH LIES AHEAD."
    print(string.center(70))
    time.sleep(0.5)
    print()
    for _ in range(36):
        time.sleep(0.5)
        print("")
