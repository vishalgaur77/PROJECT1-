
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import sys
import pyautogui
import tkinter as tk
from threading import Thread
from tkinter.scrolledtext import ScrolledText
import time
import winsound

# ---------- VOICE ---------- fire voice
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("voice", engine.getProperty("voices")[0].id)

ASSISTANT = "🔥 VISHAL AI 🔥"

# ---------- FIRE SOUND ----------
# def fire_sound():
#     try:
#         winsound.Beep(1400, 40)
#     except:
#         pass

# ---------- TYPING FIRE EFFECT ----------
def type_fire(text):
    for ch in text:
        chat_box.insert(tk.END, ch)
        chat_box.see(tk.END)
        chat_box.update()
        # fire_sound()
        time.sleep(0.02)

def speak(text):
    chat_box.insert(tk.END, f"{ASSISTANT}: ")
    type_fire(text)
    chat_box.insert(tk.END, "\n\n")
    engine.say(text)
    engine.runAndWait()

# ---------- LISTEN ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        chat_box.insert(tk.END, "🎤 Listening...\n")
        chat_box.see(tk.END)
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="en-in").lower()
        chat_box.insert(tk.END, f"You: {text}\n")
        chat_box.see(tk.END)
        return text
    except:
        return ""

# ---------- BRAIN ----------reeal
def run_command(text):

    if text in ["hello", "hi", "hey"]:
        return "Hello Vishal"

    if "how are you" in text:
        return "Main theek hoon, hamesha ready."

    if "who are you" in text:
        return "Main Vishal AI hoon, tumhara personal assistant."

    if "time" in text:
        return datetime.datetime.now().strftime("Time is %I:%M %p")

    if "date" in text:
        return datetime.datetime.now().strftime("Today is %d %B %Y")

    if text.startswith("open "):
        site = text.replace("open", "").strip()
        webbrowser.open(f"https://{site}.com")
        return f"{site} open kar raha hoon."

    if text.startswith("play "):
        song = text.replace("play", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        return f"{song} play kar raha hoon."

    if text.startswith("who is") or text.startswith("what is"):
        try:
            return wikipedia.summary(text, 3)
        except:
            return "Iske baare me info nahi mili."

    if "screenshot" in text:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot le liya gaya."

    if "notepad" in text:
        os.system("notepad")
        return "Notepad open ho gaya."

    if "calculator" in text:
        os.system("calc")
        return "Calculator open ho gaya."

    if "exit" in text or "stop" in text:
        speak("Bye Vishal")
        sys.exit()

    return "Ye command samajh nahi aayi."

# ---------- MAIN LOOP ----------
def main_loop():
    speak("Hello Vishal,  AI  personal assistant. Kaise madad kar sakta hoon?")
    while True:
        command = listen()
        if command:
            reply = run_command(command)
            speak(reply)

# ---------- UI ----------
root = tk.Tk()
root.title("VISHAL AI – FIRE MODE")
root.geometry("900x560")
root.configure(bg="#050b14")

title = tk.Label(
    root,
    text="🔥  V I S H A L . A I  🔥",
    font=("Orbitron", 26, "bold"),
    bg="#050b14",
    fg="#ff4500"
)
title.pack(pady=10)

# ---------- TITLE FIRE ANIMATION ----------
def fire_glow():
    colors = ["#ff4500", "#ff8c00", "#ffd700"]
    while True:
        for c in colors:
            title.config(fg=c)
            time.sleep(0.4)

Thread(target=fire_glow, daemon=True).start()

# ---------- CHAT BOX ----------
chat_box = ScrolledText(
    root,
    font=("Consolas", 12),
    bg="#01040a",
    fg="#84dfcc",
    insertbackground="#00ffff",
    wrap=tk.WORD
)
chat_box.pack(expand=True, fill="both", padx=12, pady=12)
chat_box.insert(tk.END, "🔥 Initializing Vishal AI...\n\n")

# ---------- 3D HUD RING ----------
hud = tk.Canvas(root, width=160, height=160, bg="#050b14", highlightthickness=0)
hud.place(x=10, y=60)

angle = 0
def hud_ring():
    global angle
    hud.delete("all")
    hud.create_oval(10, 10, 150, 150, outline="#00ffff", width=2)
    hud.create_arc(20, 20, 140, 140, start=angle, extent=80, outline="#ff4500", width=4)
    hud.create_oval(75, 75, 85, 85, fill="#00ffff", outline="")
    angle = (angle + 6) % 360
    root.after(40, hud_ring)

hud_ring()

# ---------- START ----------
Thread(target=main_loop, daemon=True).start()
root.mainloop()

# # end code   ai voice agent
# personal assistant. vishal ai
















