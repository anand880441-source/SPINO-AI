# import pygame
# import random
# import asyncio
# import edge_tts
# import os
# from dotenv import dotenv_values

# env_vars = dotenv_values(".env")
# AssistantVoice = env_vars.get("AssistantVoice")

# async def TextToAudioFile(text) -> None:
#     file_path = r"Data\speech.mp3"

#     if os.path.exists(file_path):
#         os.remove(file_path)

#     communicate = edge_tts.Communicate(text, AssistantVoice, pitch='+5Hz', rate='+13%')
#     await communicate.save(r'Data\speech.mp3')

# def TTS(Text, func=lambda r=None: True):
#     while True:
#         try:
#             asyncio.run(TextToAudioFile(Text))

#             pygame.mixer.init()

#             pygame.mixer.music.load(r"Data\speech.mp3")
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 if func() == False:
#                     break
#                 pygame.time.Clock().tick(10)  # FIXED: Added parentheses ()
#             return True
        
#         except Exception as e:
#             print(f"Error in TTS: {e}")

#         finally:
#             try:
#                 func(False)
#                 pygame.mixer.music.stop()
#                 pygame.mixer.quit()

#             except Exception as e:
#                 print(f"Error in finally block: {e}")

# def TextToSpeech(Text, func=lambda r=None: True):
#     Data = str(Text).split(".")

#     responses = [
#         "The rest of the result has been printed to the chat screen, kindly check it out sir.",
#         "The rest of the text is now on the chat screen, sir, please check it.",
#         "You can see the rest of the text on the chat screen, sir.",
#         "The remaining part of the text is now on the chat screen, sir.",
#         "Sir, you'll find more text on the chat screen for you to see.",
#         "The rest of the answer is now on the chat screen, sir.",
#         "Sir, please look at the chat screen, the rest of the answer is there.",
#         "You'll find the complete answer on the chat screen, sir.",
#         "The next part of the text is on the chat screen, sir.",
#         "Sir, please check the chat screen for more information.",
#         "There's more text on the chat screen for you, sir.",
#         "Sir, take a look at the chat screen for additional text.",
#         "You'll find more to read on the chat screen, sir.",
#         "Sir, check the chat screen for the rest of the text.",
#         "The chat screen has the rest of the text, sir.",
#         "There's more to see on the chat screen, sir, please look.",
#         "Sir, the chat screen holds the continuation of the text.",
#         "You'll find the complete answer on the chat screen, kindly check it out sir.",
#         "Please review the chat screen for the rest of the text, sir.",
#         "Sir, look at the chat screen for the complete answer."
#     ]

#     if len(Data) > 4 and len(Text) >= 250:
#         TTS(" ".join(Text.split(".")[0:2]) + ". " + random.choice(responses), func)

#     else:
#         TTS(Text, func)


# if __name__ == "__main__":
#     while True:
#         TextToSpeech(input("Enter the text: "))
#         # TTS(input("Enter the text: "))



#new:
import pygame
import random
import asyncio
import edge_tts
import os

# Import language manager
try:
    from Backend.LanguageManager import get_current_language
except ImportError:
    # Fallback
    def get_current_language():
        return {"assistant_voice": "hi-IN-MadhurNeural"}

def get_assistant_voice():
    """Get current assistant voice from config"""
    config = get_current_language()
    return config.get("assistant_voice", "hi-IN-MadhurNeural")

async def TextToAudioFile(text) -> None:
    file_path = r"Data\speech.mp3"
    
    # Ensure Data directory exists
    os.makedirs("Data", exist_ok=True)
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except:
            pass

    current_voice = get_assistant_voice()
    
    # Adjust voice parameters based on language
    if "hi-" in current_voice.lower():
        # Hindi voice settings
        communicate = edge_tts.Communicate(text, current_voice, pitch='+0Hz', rate='+10%')
    else:
        # English voice settings
        communicate = edge_tts.Communicate(text, current_voice, pitch='+5Hz', rate='+13%')
    
    await communicate.save(file_path)

def TTS(Text, func=lambda r=None: True):
    """Convert text to speech and play it"""
    if not Text or not Text.strip():
        return False
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # Convert text to audio file
            asyncio.run(TextToAudioFile(Text))
            
            # Initialize pygame mixer
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            
            # Load and play the audio
            pygame.mixer.music.load(r"Data\speech.mp3")
            pygame.mixer.music.play()
            
            # Wait while audio is playing
            while pygame.mixer.music.get_busy():
                if func() == False:  # Check if should stop
                    break
                pygame.time.Clock().tick(10)  # 10 FPS check
            
            return True
            
        except Exception as e:
            print(f"TTS Error (Attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                pygame.time.wait(1000)  # Wait 1 second before retry
            else:
                print("TTS failed after all retries")
                return False
        
        finally:
            try:
                func(False)  # Signal playback ended
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except:
                pass
    
    return False

def TextToSpeech(Text, func=lambda r=None: True):
    """Smart text-to-speech with length checking"""
    if not Text or not Text.strip():
        return False
    
    # Split into sentences
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
    
    # Check if text is too long
    if len(sentences) > 4 and len(Text) >= 250:
        # Speak first 2 sentences + random message
        short_text = " ".join(sentences[:2]) + " " + random.choice(responses)
        return TTS(short_text, func)
    else:
        # Speak full text
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