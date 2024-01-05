import shutil
import time
from datetime import datetime
import os
import pygame
import speech_recognition as sr
import vosk
import json
from bot_scrapper import *
import pyautogui
import pywhatkit
from PIL import Image

def speak(text):
    voice = "en-US-EricNeural"
    command = f'edge-tts --text "{text}" --voice {voice} --write-media output.mp3'
    os.system(command)
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def take_command():
    r = sr.Recognizer()
    model_path = "vosk-model-small-en-in-0.4"

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        model = vosk.Model(model_path)
        rec = vosk.KaldiRecognizer(model, 16000)
        rec.AcceptWaveform(audio.get_wav_data(convert_rate=16000))  # Directly pass audio data
        result = rec.Result()
        return json.loads(result)["text"].lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to the vosk service: {e}")
        return ""
    except Exception as e:
        print(f"Error during speech recognition: {e}")
        return ""

sleep_mode = False

click_on_chat_button()
while True:
    query = take_command().lower()
    print('\n You: ' + query)

    if 'open' in query:
        app_name = query.replace('open','')

        speak('opening' + app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.7)
        pyautogui.press('enter')

    elif 'switch tab' in query:
        pyautogui.hotkey('ctrl','tab')

    elif 'close tab' in query:
        pyautogui.hotkey('ctrl','w')

    elif 'close' in query:
        pyautogui.hotkey('alt','f4')
    elif 'play' in query:
        song_name = query.replace('play','')
        speak('Sure sir. Playing' + song_name + ' in youtube')
        pywhatkit.playonyt(song_name)

    elif 'stop' in query:
        pyautogui.press('k')  # Press 'k' to pause

    elif 'resume' in query or 'play' in query:
        pyautogui.press('k')  # Press 'k' to resume

    elif 'forward' in query:
        pyautogui.press('l')  # Press 'l' to skip forward

    elif 'backward' in query:
        pyautogui.press('j')  # Press 'j' to skip backward

    elif 'time' in query:
        current_time = datetime.now().strftime('%H:%M %p')
        speak('Current time is: ' + current_time)

    elif 'sleep' in query:
        speak("Ok sir. I am going to sleep but you can call me any time, just say wake up and i will be there for you.")
        sleep_mode = True

    elif 'generate' in query:
        import img_gen
        prompt = query.replace('generate','')
        speak("Ok sir, Generating " + prompt)
        img_gen.generate_image(prompt)
        time.sleep(5)
        image_path = os.path.join('output', '2.jpeg')
        img = Image.open(image_path)
        img.show()
        time.sleep(5)
        items = os.listdir('output')
        for item in items:
            item_path = os.path.join('output', item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    elif 'thank you' in query:
        speak("You're welcome! See you Soon.")
        break

    else:
        sendQuery(query)
        isBubbleLoaderVisible()
        response = retriveData()
        speak(response)

    while sleep_mode:
        query = take_command().lower()
        print(query)
        if 'wake up' in query:
            speak("I am awake now, How can i Help you sir?")
            sleep_mode = False




