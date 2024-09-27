import pygame
import time
import os

# Inicializar Pygame
pygame.mixer.init()

def speak(filename):
    audio_path = os.path.join(os.path.dirname(__file__), "audios", "Omniman", f"{filename}.wav")
    if not os.path.exists(audio_path):
        print(f"Error: El archivo de audio '{audio_path}' no existe.")
        return
    
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def get_user_input():
    input("Presione Enter para continuar...")

def play_audio_group(group):
    for audio in group.split(','):
        audio = audio.strip()
        if audio == "4_interrumpido":
            speak("4")
            pygame.mixer.music.stop()  # Interrumpir el audio 4
        else:
            speak(audio)

def run_script():
    # Secuencia de audios agrupados según el script
    audio_sequence = [
        "1,2", 
        "3,4", 
        "5,6,7,8,9,10", 
        "11",
        "12", 
        "no,interrumpido", 
        "13", 
        "14", 
        "15",
        "16", 
        "no,interrumpido", 
        "17", 
        "18", 
        "no"
    ]
    
    for group in audio_sequence:
        play_audio_group(group)
        get_user_input()

if __name__ == "__main__":
    run_script()