import pygame
import time

# Inicializar Pygame
pygame.mixer.init()

def speak(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main_menu():
    speak("audios/bienvenido.wav")
    speak("audios/modo_tutorial.wav")
    speak("audios/modo_normal.wav")
    
    user_input = input("Digite su opción (modo tutorial/modo normal): ").strip().lower()
    
    if user_input == "modo tutorial":
        tutorial_mode()
    elif user_input == "modo normal":
        normal_mode()  
    else:
        speak("audios/error.wav")
        main_menu()

def tutorial_mode():
    speak("audios/tutorial_main.wav")
    user_input = input("Digite su opción (Bandeja de entrada): ").strip().lower()
    
    if user_input == "bandeja de entrada":
        inbox_menu()
    else:
        speak("audios/error.wav")
        tutorial_mode()

def normal_mode():
    speak("audios/modo_normal_instrucciones.wav")
    
    user_input = input("Digite su opción (Bandeja de entrada): ").strip().lower()
    
    if user_input == "bandeja de entrada":
        inbox_menu()
    else:
        speak("audios/error.wav")
        normal_mode()

def inbox_menu():
    speak("audios/tutorial_correos.wav")

    subject = "materia prima"

    user_input = input("Digite el nombre del asunto del correo: ").strip().lower()
    
    if user_input == subject:
        email_options(subject)
    else:
        speak("audios/error.wav")
        inbox_menu()

def email_options(subject):
    speak("audios/tutorial_correo.wav")
    user_input = input("Digite su opción (reproducir/responder/imprimir/eliminar): ").strip().lower()
    
    if user_input == "reproducir":
        speak(f"audios/ejemplo.wav")
        speak(f"audios/continuar.wav")
        if input("si o no: ").strip().lower() == "si":
            speak("audios/yup.wav")
            email_options(subject)  
        else:
            speak("audios/nope.wav")
            tutorial_mode()
       
    elif user_input == "responder":
        response = input("Digite su respuesta: ")
        if response:
            speak("audios/tutorial_continuar.wav")
            if input("si o no: ").strip().lower() == "si":
                speak("audios/yup.wav")
                email_options(subject)  
            else:
                speak("audios/nope.wav")
                tutorial_mode()
        else:
            speak("audios/error.wav")
            email_options(subject)
    elif user_input == "imprimir":
        speak("audios/correo_impreso.wav")
        speak("audios/continuar.wav")
        if input("si o no: ").strip().lower() == "si":
            speak("audios/yup.wav")
            email_options(subject)  
        else:
            speak("audios/nope.wav")
            tutorial_mode()
    elif user_input == "eliminar":
        speak("audios/correo_eliminado.wav")
        speak("audios/continuar.wav")
        if input("si o no: ").strip().lower() == "si":
            speak("audios/yup.wav")
            email_options(subject)  
        else:
            speak("audios/nope.wav")
            tutorial_mode()
    else:
        speak("audios/error.wav")
        email_options(subject)

if __name__ == "__main__":
    main_menu()
