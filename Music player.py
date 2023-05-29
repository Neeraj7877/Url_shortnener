import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def main():
    while True:
        print("\nMusic Player Menu:")
        print("1. Play Music")
        print("2. Stop Music")
        print("3. Pause Music")
        print("4. Resume Music")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_path = input("Enter the path of the music file: ")
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                print("File not found!")
        elif choice == '2':
            stop_music()
        elif choice == '3':
            pause_music()
        elif choice == '4':
            resume_music()
        elif choice == '5':
            print("Exiting the music player...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
