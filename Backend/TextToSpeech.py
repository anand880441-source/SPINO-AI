import pygame
import random
import asyncio
import edge_tts
import os

speech_paused = False
speech_stopped = False

try:
    from Backend.LanguageManager import get_current_language
except ImportError:
    def get_current_language():
        return {"assistant_voice": "hi-IN-MadhurNeural"}

def get_assistant_voice():
    """Get current assistant voice from config"""
    config = get_current_language()
    return config.get("assistant_voice", "hi-IN-MadhurNeural")

async def TextToAudioFile(text) -> None:
    file_path = r"Data\speech.mp3"
    
    os.makedirs("Data", exist_ok=True)
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except:
            pass

    current_voice = get_assistant_voice()
    
    if "hi-" in current_voice.lower():
        communicate = edge_tts.Communicate(text, current_voice, pitch='+0Hz', rate='+10%')
    else:
        communicate = edge_tts.Communicate(text, current_voice, pitch='+5Hz', rate='+13%')
    
    await communicate.save(file_path)

def pause_speech():
    global speech_paused
    try:
        if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            speech_paused = True
            return True
    except:
        pass
    return False

def resume_speech():
    global speech_paused
    try:
        if speech_paused and pygame.mixer.get_init():
            pygame.mixer.music.unpause()
            speech_paused = False
            return True
    except:
        pass
    return False

def stop_speech():
    global speech_stopped, speech_paused
    try:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            speech_stopped = True
            speech_paused = False
            return True
    except:
        pass
    return False

def get_speech_status():
    try:
        if not pygame.mixer.get_init():
            return {"state": "stopped", "paused": False, "stopped": True}
        
        if speech_paused:
            return {"state": "paused", "paused": True, "stopped": False}
        elif speech_stopped:
            return {"state": "stopped", "paused": False, "stopped": True}
        elif pygame.mixer.music.get_busy():
            return {"state": "playing", "paused": False, "stopped": False}
        else:
            return {"state": "stopped", "paused": False, "stopped": True}
    except:
        return {"state": "unknown", "paused": False, "stopped": True}

def TTS(Text, func=lambda r=None: True):
    """Convert text to speech and play it"""
    global speech_paused, speech_stopped
    
    if not Text or not Text.strip():
        return False
    
    # Reset flags
    speech_paused = False
    speech_stopped = False
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            asyncio.run(TextToAudioFile(Text))
            
            # Initialize mixer if not already initialized
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            
            pygame.mixer.music.load(r"Data\speech.mp3")
            pygame.mixer.music.play()
            
            # Playback loop
            while pygame.mixer.music.get_busy():
                if speech_stopped:
                    pygame.mixer.music.stop()
                    break
                    
                if speech_paused:
                    pygame.time.Clock().tick(10)
                    continue
                    
                if func() == False:
                    break
                    
                pygame.time.Clock().tick(10)
            
            return True
            
        except Exception as e:
            print(f"TTS Error (Attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                pygame.time.wait(1000)
            else:
                print("TTS failed after all retries")
                return False
    
    return False

def TextToSpeech(Text, func=lambda r=None: True):
    """Smart text-to-speech with length checking"""
    if not Text or not Text.strip():
        return False
    
    sentences = [s.strip() + '.' for s in str(Text).split('.') if s.strip()]
    
    responses = [
        "The rest of the result has been printed to the chat screen, kindly check it out sir.",
        "The rest of the text is now on the chat screen, sir, please check it.",
        "You can see the rest of the text on the chat screen, sir.",
        "The remaining part of the text is now on the chat screen, sir.",
        "Sir, you'll find more text on the chat screen for you to see.",
        "The rest of the answer is now on the chat screen, sir.",
        "Sir, please look at the chat screen, the rest of the answer is there.",
        "You'll find the complete answer on the chat screen, sir.",
        "The next part of the text is on the chat screen, sir.",
        "Sir, please check the chat screen for more information.",
        "There's more text on the chat screen for you, sir.",
        "Sir, take a look at the chat screen for additional text.",
        "You'll find more to read on the chat screen, sir.",
        "Sir, check the chat screen for the rest of the text.",
        "The chat screen has the rest of the text, sir.",
        "There's more to see on the chat screen, sir, please look.",
        "Sir, the chat screen holds the continuation of the text.",
        "You'll find the complete answer on the chat screen, kindly check it out sir.",
        "Please review the chat screen for the rest of the text, sir.",
        "Sir, look at the chat screen for the complete answer."
    ]
    
    if len(sentences) > 4 and len(Text) >= 250:
        short_text = " ".join(sentences[:2]) + " " + random.choice(responses)
        return TTS(short_text, func)
    else:
        return TTS(Text, func)

if __name__ == "__main__":
    print("🔊 Text-to-Speech Testing Mode")
    print("Type 'exit' to quit")
    
    while True:
        user_text = input("\nEnter text to speak: ").strip()
        
        if user_text.lower() == 'exit':
            break
        
        if user_text:
            success = TextToSpeech(user_text)
            if success:
                print("✅ Speech played successfully")
            else:
                print("❌ Failed to play speech")