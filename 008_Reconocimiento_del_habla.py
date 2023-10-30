pip install SpeechRecognition
import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Configurar el micrófono
microphone = sr.Microphone()

try:
    print("Escuchando... (presiona Ctrl+C para detener)")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiente
        audio = recognizer.listen(source)

    # Realizar el reconocimiento del habla
    recognized_text = recognizer.recognize_google(audio)

    if recognized_text:
        print(f"Texto reconocido: {recognized_text}")
    else:
        print("No se pudo reconocer el habla.")

except KeyboardInterrupt:
    print("Proceso interrumpido por el usuario.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
