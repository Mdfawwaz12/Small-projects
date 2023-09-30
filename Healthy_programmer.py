from pygame import mixer #mixer is a class that handled music
from time import time
def musiconloop(file,stopped):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a ==stopped:
            mixer.music.stop()
            break
def date():
    import datetime
    return datetime.datetime.now()

if __name__=='__main__':
    # musiconloop("master2.mp3","stop")
    water = time()
    eyes = time()
    exercise = time()
    water_second = 5
    eyes_second = 10
    exercise_second = 15
   
    while True:
        if time() - water > water_second:
            print("Water drinking time.Enter ''drank'' to stopped")
            musiconloop("master2.mp3", 'drank')
            water = time()
            s= [date()]
            f = open("water.txt","a")
            f.write("drank water at")
            f.write(str(s))
            f.write('\n')

        if time() - eyes > eyes_second:
            print("eyes relaxing time.Enter 'done' to stopped")
            musiconloop("master2.mp3", 'done')
            eyes = time()
            s= [date()]
            f = open("eyes_relax.txt","a")
            f.write("done at")
            f.write(str(s))
            f.write('\n')

        if time() - exercise > exercise_second:
            print("exercise time.Enter ''doneexe' to stopped")
            musiconloop("master2.mp3", 'doneexe')
            exercise = time()
            s= [date()]
            f = open("exercise.txt","a")
            f.write("exercise at")
            f.write(str(s))
            f.write('\n')
