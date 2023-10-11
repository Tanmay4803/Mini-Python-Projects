nfrom playsound import playsound
import time

CLEAR = "/033[2J"
CLEAR_AND_RETURN = "/033[H"

def alarm(seconds):
    time_finished = 0

    print(CLEAR)
    while time_finished<seconds:
        time.sleep(1)
        time_finished += 1

        time_left = seconds - time_finished
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN} TIMER WILL GO OFF IN: {minutes_left:02d}:{seconds_left:02d}")

    playsound("sound.mp3")

minutes = 0
seconds = 5
total_seconds = minutes*60 + seconds
alarm(total_seconds)