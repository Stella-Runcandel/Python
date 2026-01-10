import time
import datetime
import pygame 


def set_alarm(alarm_time):
    print(f'Alarm set for {alarm_time}')
    sound_file = 'C:\\Users\\mrram\\Music\\y2mate.com - Genshin AMV Time to Fall for Me Boy_1080p.mp3'
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up!!! 😎")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                alarm_state = input("Stop Alarm? : y/n")
                if alarm_state.lower() == "y":
                    print("Alarm turned off. Good morning.")
                    pygame.mixer.music.stop()
                    is_running = False
                #introduce loop to check check if user want's to quit, music should keep playing until user espons ->
                #then continue or stop
            is_running = False
        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter in alarm time in the following format: (HH:MM:SS) <military time>")
    set_alarm(alarm_time)