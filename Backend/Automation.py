# from AppOpener import close, open as appopen
# from webbrowser import open as webopen
# from pywhatkit import search, playonyt
# from dotenv import dotenv_values
# from rich import print
# from groq import Groq
# import webbrowser
# import subprocess
# import requests
# import keyboard
# import asyncio
# import os
# from bs4 import BeautifulSoup
# import sys
# import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# if parent_dir not in sys.path:
#     sys.path.append(parent_dir)

# try:
#     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
#     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
#     webbrowser._tryorder = ['chrome'] + webbrowser._tryorder
# except:
#     pass

# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.366'

# env_vars = dotenv_values(".env")

# GroqAPIKey1 = env_vars.get("GroqAPIKey1")
# GroqAPIKey2 = env_vars.get("GroqAPIKey2")
# GroqAPIKey3 = env_vars.get("GroqAPIKey3")
# GroqAPIKey4 = env_vars.get("GroqAPIKey4")

# GroqAPIKey = GroqAPIKey1 or GroqAPIKey2 or GroqAPIKey3 or GroqAPIKey4

# if GroqAPIKey:
#     client = Groq(api_key=GroqAPIKey)
#     print(f"✅ Groq API initialized with key: {GroqAPIKey[:20]}...")
# else:
#     client = None
#     print("❌ No Groq API keys found in .env file")
#     print("Make sure your .env has: GroqAPIKey1=your_key_here")

# professional_responses = [
#     "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
#     "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
# ]

# messages = []
# SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'Assistant')}. You're a content writer who writes letters, articles, blogs, and other documents professionally."}]

# def GoogleSearch(Topic):
#     search(Topic)
#     return True

# def Content(Topic):
#     def OpenNotepad(File):
#         default_text_editor = 'notepad.exe'
#         subprocess.Popen([default_text_editor, File])

#     def ContentWriterAI(prompt):
#         messages.append({"role": "user", "content": f"{prompt}"})
#         completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=SystemChatBot + messages,
#             max_tokens=2048,
#             temperature=0.7,
#             top_p=1,
#             stream=True,
#             stop=None
#         )
#         Answer = ""
#         for chunk in completion:
#             if chunk.choices[0].delta.content:
#                 Answer += chunk.choices[0].delta.content
#         Answer = Answer.replace("</s>", "")
#         messages.append({"role": "assistant", "content": Answer})
#         return Answer
    
#     Topic = Topic.replace("Content ", "")
#     ContentByAPI = ContentWriterAI(Topic)
#     filename = rf"Data\{Topic.lower().replace(' ','')}.txt"
#     os.makedirs("Data", exist_ok=True)
    
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(ContentByAPI)
    
#     OpenNotepad(filename)
#     return True


# def YouTubeSearch(Topic):
#     Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
#     webbrowser.open(Url4Search)
#     return True


# def PlayYoutube(query):
#     playonyt(query)
#     return True

# def OpenApp(app, sess=requests.session()):
#     """Open apps - tries local apps first, then opens as website"""
    
#     print(f"🌐 Opening: {app}")
    
#     desktop_apps = {
#         'whatsapp': 'whatsapp',
#         'telegram': 'telegram',
#         'discord': 'discord',
#         'spotify': 'spotify',
#         'notepad': 'notepad',
#         'calculator': 'calculator',
#         'paint': 'mspaint',
#         'word': 'winword',
#         'excel': 'excel',
#         'powerpoint': 'powerpnt',
#         'outlook': 'outlook',
#         'vscode': 'code',
#         'visual studio code': 'code',
#         'chrome': 'chrome',
#         'firefox': 'firefox',
#         'edge': 'msedge',
#     }
    
#     app_lower = app.lower()
    
#     if app_lower in desktop_apps:
#         desktop_app_name = desktop_apps[app_lower]
#         print(f"💻 Trying desktop app: {desktop_app_name}")
        
#         try:
#             appopen(desktop_app_name, match_closest=False, output=False, throw_error=True)
#             print(f"✅ Opened desktop app: {desktop_app_name}")
#             return True
#         except Exception as e:
#             print(f"📱 Desktop app not found: {e}")
    
#     website_apps = {
#         'canva': 'https://www.canva.com',
#         'facebook': 'https://www.facebook.com',
#         'instagram': 'https://www.instagram.com',
#         'youtube': 'https://www.youtube.com',
#         'twitter': 'https://twitter.com',
#         'whatsapp': 'https://web.whatsapp.com',
#         'telegram': 'https://web.telegram.org',
#         'gmail': 'https://mail.google.com',
#         'google': 'https://www.google.com',
#         'github': 'https://github.com',
#         'linkedin': 'https://linkedin.com',
#         'netflix': 'https://netflix.com',
#         'amazon': 'https://amazon.com',
#         'flipkart': 'https://flipkart.com',
#         'spotify': 'https://open.spotify.com',
#         'discord': 'https://discord.com',
#         'reddit': 'https://reddit.com',
#         'chatgpt': 'https://chat.openai.com',
#         'notion': 'https://notion.so',
#         'figma': 'https://figma.com',
#         'gemini': 'https://gemini.google.com',
#         'deepseek': 'https://chat.deepseek.com',
#         'w3school': 'https://www.w3schools.com',
#         'w3schools': 'https://www.w3schools.com',
#         'stackoverflow': 'https://stackoverflow.com',
#     }
    
#     if app_lower in website_apps:
#         url = website_apps[app_lower]
#         print(f"🔗 Opening website: {url}")
        
#         try:
#             subprocess.run(f'start chrome "{url}"', shell=True)
#             print("✅ Opening in Chrome")
#             return True
#         except Exception as e:
#             print(f"⚠️ Chrome method failed: {e}")
            
#             try:
#                 webbrowser.open(url)
#                 print("✅ Opening in default browser")
#                 return True
#             except Exception as e:
#                 print(f"❌ Failed to open: {e}")
#                 return False
    
#     print(f"🔍 Unknown app, trying local first...")
    
#     try:
#         appopen(app, match_closest=False, output=False, throw_error=True)
#         print(f"✅ Opened local app: {app}")
#         return True
#     except Exception as e:
#         print(f"📱 Local app not found, opening as website...")
    
#     url = f"https://www.{app_lower.replace(' ', '')}.com"
#     print(f"🔗 Trying as website: {url}")
    
#     try:
#         subprocess.run(f'start chrome "{url}"', shell=True)
#         print("✅ Opening in Chrome")
#         return True
#     except:
#         try:
#             webbrowser.open(url)
#             print("✅ Opening in browser")
#             return True
#         except Exception as e:
#             print(f"❌ Failed to open: {e}")
#             return False

# def CloseApp(app):
#     if "chrome" in app.lower():
#         pass
#     else:
#         try:
#             close(app, match_closest=True, output=False, throw_error=True)
#             return True
#         except:
#             return False

# def VoiceControl(command):
#     """Handle voice control commands for speech"""
#     try:
#         from Backend.TextToSpeech import pause_speech, resume_speech, stop_speech, get_speech_status
        
#         command = command.lower().strip()
        
#         if command in ["pause", "wait", "hold on", "stop speaking", "रुको", "बंद करो"]:
#             success = pause_speech()
#             return f"⏸️ Speech {'paused' if success else 'already paused'}"
        
#         elif command in ["resume", "continue", "go on", "speak", "बोलो", "जारी रखो"]:
#             success = resume_speech()
#             return f"▶️ Speech {'resumed' if success else 'not paused'}"
        
#         elif command in ["stop", "halt", "stop completely", "शांत", "पूर्णतः बंद करो"]:
#             success = stop_speech()
#             return f"⏹️ Speech {'stopped' if success else 'already stopped'}"
        
#         elif command in ["status", "what's happening", "स्थिति"]:
#             status = get_speech_status()
#             return f"📊 Speech status: {status['state']}"
        
#         return "Unknown voice control command"
#     except ImportError:
#         return "❌ Voice control module not available"
#     except Exception as e:
#         return f"❌ Error in voice control: {str(e)}"

# def GenerateImage(prompt):
#     """Generate image using HuggingFace"""
#     try:
#         print(f"🎨 Generating image: {prompt}")
        
#         try:
#             # CORRECT IMPORT: Use ImageGeneration (not ImageGenerator)
#             from Backend.ImageGeneration import GenerateImages
            
#             # Generate the images
#             result = GenerateImages(prompt)
            
#             if result > 0:
#                 return f"✅ Successfully generated {result} images of '{prompt}'"
#             else:
#                 return f"❌ Failed to generate images of '{prompt}'"
                
#         except ImportError as e:
#             print(f"⚠️ Import error: {e}")
#             print("Trying alternative import...")
            
#             # Alternative import
#             try:
#                 from ImageGeneration import GenerateImages
#                 result = GenerateImages(prompt)
#                 return f"✅ Generated {result} images (alternative import)"
#             except ImportError:
#                 # Fallback to Google search
#                 search_url = f"https://www.google.com/search?tbm=isch&q={prompt.replace(' ', '+')}"
#                 webbrowser.open(search_url)
#                 return f"🔍 Opened image search for: {prompt}"
                
#     except Exception as e:
#         print(f"❌ Error in GenerateImage: {e}")
#         return f"❌ Error generating image: {str(e)}"

# def System(command):
#     if command == "mute":
#         keyboard.press_and_release("volume mute")
#     elif command == "unmute":
#         keyboard.press_and_release("volume mute")
#     elif command == "volume up":
#         keyboard.press_and_release("volume up")
#     elif command == "volume down":
#         keyboard.press_and_release("volume down")
#     else:
#         print(f"Unknown system command: {command}")
#         return False
#     return True

# async def TranslateAndExecute(commands: list[str]):
#     funcs = []
#     for command in commands:
#         command = command.strip()
        
#         # Image Generation (NEW)
#         if (command.startswith("generate image ") or 
#             command.startswith("create image ") or 
#             "image of" in command.lower()):
            
#             prompt = command.lower()
#             prompt = prompt.replace("generate image of", "")
#             prompt = prompt.replace("generate image", "")
#             prompt = prompt.replace("create image of", "")
#             prompt = prompt.replace("create image", "")
#             prompt = prompt.replace("image of", "")
#             prompt = prompt.strip()
            
#             if prompt:
#                 print(f"🖼️ Detected image generation: {prompt}")
#                 func = asyncio.to_thread(GenerateImage, prompt)
#                 funcs.append(func)
#                 continue  

#         # Voice Control (NEW)
#         elif command.startswith("voice "):
#             voice_command = command.removeprefix("voice ").strip()
#             if voice_command:
#                 func = asyncio.to_thread(VoiceControl, voice_command)
#                 funcs.append(func)
                
#         # YouTube Search (NEW)
#         elif command.startswith("youtube search "):
#             query = command.removeprefix("youtube search ").strip()
#             if query:
#                 func = asyncio.to_thread(YouTubeSearch, query)
#                 funcs.append(func)
                
#         # Write command (NEW - alias for content)
#         elif command.startswith("write "):
#             topic = command.removeprefix("write ").strip()
#             if topic:
#                 print(f"✍️ Detected write command: {topic}")
#                 func = asyncio.to_thread(Content, topic)
#                 funcs.append(func)
                
#         # Language Switching (NEW)
#         elif command.startswith("switch language "):
#             language = command.removeprefix("switch language ").strip().lower()
#             try:
#                 from Backend.LanguageManager import switch_to_hindi, switch_to_english
                
#                 if language in ["hindi", "hi", "हिंदी"]:
#                     func = asyncio.to_thread(switch_to_hindi)
#                     funcs.append(func)
#                 elif language in ["english", "en", "अंग्रेजी"]:
#                     func = asyncio.to_thread(switch_to_english)
#                     funcs.append(func)
#                 else:
#                     print(f"❌ Unknown language: {language}")
#             except ImportError:
#                 print("❌ LanguageManager not available")
                
#         # Existing commands
#         elif command.startswith("open "):
#             app_name = command.removeprefix("open ").strip()
#             if app_name:
#                 func = asyncio.to_thread(OpenApp, app_name)
#                 funcs.append(func)
                
#         elif command.startswith("close "):
#             app_name = command.removeprefix("close ").strip()
#             if app_name:
#                 func = asyncio.to_thread(CloseApp, app_name)
#                 funcs.append(func)
                
#         elif command.startswith("play "):
#             query = command.removeprefix("play ").strip()
#             if query:
#                 func = asyncio.to_thread(PlayYoutube, query)
#                 funcs.append(func)
                
#         elif command.startswith("content "):
#             topic = command.removeprefix("content ").strip()
#             if topic:
#                 func = asyncio.to_thread(Content, topic)
#                 funcs.append(func)
                
#         elif command.startswith("google search "):
#             query = command.removeprefix("google search ").strip()
#             if query:
#                 func = asyncio.to_thread(GoogleSearch, query)
#                 funcs.append(func)
                
#         elif command.startswith("system "):
#             sys_command = command.removeprefix("system ").strip()
#             if sys_command:
#                 func = asyncio.to_thread(System, sys_command)
#                 funcs.append(func)
                
#         elif command.startswith(("general ", "realtime ")):
#             print(f"Chatbot response needed for: {command}")
#             # You can add chatbot response here
#             yield f"Processing: {command}"
            
#         # Auto-detect content/write commands (NEW)
#         elif any(keyword in command.lower() for keyword in 
#                 ["application", "letter", "essay", "article", "blog", "document"]):
#             print(f"📝 Detected content-related command: {command}")
#             func = asyncio.to_thread(Content, command)
#             funcs.append(func)
            
#         else:
#             print(f"❌ No function found for: {command}")
    
#     if funcs:
#         results = await asyncio.gather(*funcs, return_exceptions=True)
#         for result in results:
#             if isinstance(result, Exception):
#                 print(f"❌ Error executing command: {result}")
#                 yield f"Error: {result}"
#             elif isinstance(result, str):
#                 yield result
#             elif result is True:
#                 yield "✅ Command executed successfully"
#             else:
#                 yield f"Result: {result}"
#     else:
#         yield "No valid commands to execute."

# async def Automation(commands: list[str]):
#     async for result in TranslateAndExecute(commands):
#         pass
#     return True


# # if __name__ == "__main__":
# #     asyncio.run(Automation(["open facebook", "open instagram","play tu hai kaha","content song for me"]))

# # if __name__ == "__main__":
# #     # Test voice commands
# #     asyncio.run(Automation([
# #         "voice pause",
# #         "voice resume", 
# #         "voice stop",
# #         "voice status"
# #     ]))

# # if __name__ == "__main__":
#     # Test image generation
#     # asyncio.run(Automation(["generate image of narendra modi", "create image sunset"]))





from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os
from bs4 import BeautifulSoup
import sys
from pathlib import Path
import keyboard

def setup_voice_hotkeys():
    keyboard.add_hotkey('ctrl+shift+p', lambda: VoiceControl("pause"))
    keyboard.add_hotkey('ctrl+shift+r', lambda: VoiceControl("resume")) 
    keyboard.add_hotkey('ctrl+shift+s', lambda: VoiceControl("stop"))
    print("✅ Voice hotkeys set: Ctrl+Shift+P (pause), R (resume), S (stop)")

current_dir = Path(__file__).parent
root_dir = current_dir.parent  
env_path = root_dir / ".env"

current_dir_py = os.path.dirname(os.path.abspath(__file__))
parent_dir_py = os.path.dirname(current_dir_py)
if parent_dir_py not in sys.path:
    sys.path.append(parent_dir_py)

try:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser._tryorder = ['chrome'] + webbrowser._tryorder
except:
    pass

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.366'

env_vars = dotenv_values(str(env_path))

groq_keys = [
    env_vars.get("GroqAPIKey1", ""),
    env_vars.get("GroqAPIKey2", ""),
    env_vars.get("GroqAPIKey3", ""),
    env_vars.get("GroqAPIKey4", ""),
]

groq_keys = [key for key in groq_keys if key and key.strip()]

if groq_keys:
    client = Groq(api_key=groq_keys[0])
    print(f"✅ Groq API initialized with key: ...{groq_keys[0][-8:]}")
else:
    client = None
    print("❌ No Groq API keys found")

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

messages = []
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'Assistant')}. You're a content writer who writes letters, articles, blogs, and other documents professionally."}]

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer
    
    Topic = Topic.replace("Content ", "")
    ContentByAPI = ContentWriterAI(Topic)
    filename = rf"Data\{Topic.lower().replace(' ','')}.txt"
    os.makedirs("Data", exist_ok=True)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(ContentByAPI)
    
    OpenNotepad(filename)
    return True


def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True


def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, sess=requests.session()):
    """Open apps - tries local apps first, then opens as website"""
    
    print(f"🌐 Opening: {app}")
    
    desktop_apps = {
        'whatsapp': 'whatsapp',
        'telegram': 'telegram',
        'discord': 'discord',
        'spotify': 'spotify',
        'notepad': 'notepad',
        'calculator': 'calculator',
        'paint': 'mspaint',
        'word': 'winword',
        'excel': 'excel',
        'powerpoint': 'powerpnt',
        'outlook': 'outlook',
        'vscode': 'code',
        'visual studio code': 'code',
        'chrome': 'chrome',
        'firefox': 'firefox',
        'edge': 'msedge',
    }
    
    app_lower = app.lower()
    
    if app_lower in desktop_apps:
        desktop_app_name = desktop_apps[app_lower]
        print(f"💻 Trying desktop app: {desktop_app_name}")
        
        try:
            appopen(desktop_app_name, match_closest=False, output=False, throw_error=True)
            print(f"✅ Opened desktop app: {desktop_app_name}")
            return True
        except Exception as e:
            print(f"📱 Desktop app not found: {e}")
    
    website_apps = {
        'canva': 'https://www.canva.com',
        'facebook': 'https://www.facebook.com',
        'instagram': 'https://www.instagram.com',
        'youtube': 'https://www.youtube.com',
        'twitter': 'https://twitter.com',
        'whatsapp': 'https://web.whatsapp.com',
        'telegram': 'https://web.telegram.org',
        'gmail': 'https://mail.google.com',
        'google': 'https://www.google.com',
        'github': 'https://github.com',
        'linkedin': 'https://linkedin.com',
        'netflix': 'https://netflix.com',
        'amazon': 'https://amazon.com',
        'flipkart': 'https://flipkart.com',
        'spotify': 'https://open.spotify.com',
        'discord': 'https://discord.com',
        'reddit': 'https://reddit.com',
        'chatgpt': 'https://chat.openai.com',
        'notion': 'https://notion.so',
        'figma': 'https://figma.com',
        'gemini': 'https://gemini.google.com',
        'deepseek': 'https://chat.deepseek.com',
        'w3school': 'https://www.w3schools.com',
        'w3schools': 'https://www.w3schools.com',
        'stackoverflow': 'https://stackoverflow.com',
    }
    
    if app_lower in website_apps:
        url = website_apps[app_lower]
        print(f"🔗 Opening website: {url}")
        
        try:
            subprocess.run(f'start chrome "{url}"', shell=True)
            print("✅ Opening in Chrome")
            return True
        except Exception as e:
            print(f"⚠️ Chrome method failed: {e}")
            
            try:
                webbrowser.open(url)
                print("✅ Opening in default browser")
                return True
            except Exception as e:
                print(f"❌ Failed to open: {e}")
                return False
    
    print(f"🔍 Unknown app, trying local first...")
    
    try:
        appopen(app, match_closest=False, output=False, throw_error=True)
        print(f"✅ Opened local app: {app}")
        return True
    except Exception as e:
        print(f"📱 Local app not found, opening as website...")
    
    url = f"https://www.{app_lower.replace(' ', '')}.com"
    print(f"🔗 Trying as website: {url}")
    
    try:
        subprocess.run(f'start chrome "{url}"', shell=True)
        print("✅ Opening in Chrome")
        return True
    except:
        try:
            webbrowser.open(url)
            print("✅ Opening in browser")
            return True
        except Exception as e:
            print(f"❌ Failed to open: {e}")
            return False

def CloseApp(app):
    if "chrome" in app.lower():
        pass
    else:
        try:
            close(app, match_closest=True, output=False, throw_error=True)
            return True
        except:
            return False

def VoiceControl(command):
    """Handle voice control commands for speech"""
    try:
        from Backend.TextToSpeech import pause_speech, resume_speech, stop_speech, get_speech_status
        
        command = command.lower().strip()
        
        if command in ["pause", "wait", "hold on", "stop speaking", "रुको", "बंद करो"]:
            success = pause_speech()
            return f"⏸️ Speech {'paused' if success else 'already paused'}"
        
        elif command in ["resume", "continue", "go on", "speak", "बोलो", "जारी रखो"]:
            success = resume_speech()
            return f"▶️ Speech {'resumed' if success else 'not paused'}"
        
        elif command in ["stop", "halt", "stop completely", "शांत", "पूर्णतः बंद करो"]:
            success = stop_speech()
            return f"⏹️ Speech {'stopped' if success else 'already stopped'}"
        
        elif command in ["status", "what's happening", "स्थिति"]:
            status = get_speech_status()
            return f"📊 Speech status: {status['state']}"
        
        return "Unknown voice control command"
    except ImportError:
        return "❌ Voice control module not available"
    except Exception as e:
        return f"❌ Error in voice control: {str(e)}"

def GenerateImage(prompt):
    """Generate image using HuggingFace"""
    try:
        print(f"🎨 Generating image: {prompt}")
        
        try:
            from Backend.ImageGeneration import GenerateImages
            
            result = GenerateImages(prompt)
            
            if result > 0:
                return f"✅ Successfully generated {result} images of '{prompt}'"
            else:
                return f"❌ Failed to generate images of '{prompt}'"
                
        except ImportError as e:
            print(f"⚠️ Import error: {e}")
            print("Trying alternative import...")
            
            try:
                from ImageGeneration import GenerateImages
                result = GenerateImages(prompt)
                return f"✅ Generated {result} images (alternative import)"
            except ImportError:
                search_url = f"https://www.google.com/search?tbm=isch&q={prompt.replace(' ', '+')}"
                webbrowser.open(search_url)
                return f"🔍 Opened image search for: {prompt}"
                
    except Exception as e:
        print(f"❌ Error in GenerateImage: {e}")
        return f"❌ Error generating image: {str(e)}"

def System(command):
    if command == "mute":
        keyboard.press_and_release("volume mute")
    elif command == "unmute":
        keyboard.press_and_release("volume mute")
    elif command == "volume up":
        keyboard.press_and_release("volume up")
    elif command == "volume down":
        keyboard.press_and_release("volume down")
    else:
        print(f"Unknown system command: {command}")
        return False
    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        command = command.strip()
        
        if (command.startswith("generate image ") or 
            command.startswith("create image ") or 
            "image of" in command.lower()):
            
            prompt = command.lower()
            prompt = prompt.replace("generate image of", "")
            prompt = prompt.replace("generate image", "")
            prompt = prompt.replace("create image of", "")
            prompt = prompt.replace("create image", "")
            prompt = prompt.replace("image of", "")
            prompt = prompt.strip()
            
            if prompt:
                print(f"🖼️ Detected image generation: {prompt}")
                func = asyncio.to_thread(GenerateImage, prompt)
                funcs.append(func)
                continue  

        elif command == "pause" or command == "resume" or command == "stop":
            func = asyncio.to_thread(VoiceControl, command)
            funcs.append(func)
                
        elif command.startswith("youtube search "):
            query = command.removeprefix("youtube search ").strip()
            if query:
                func = asyncio.to_thread(YouTubeSearch, query)
                funcs.append(func)
                
        elif command.startswith("write "):
            topic = command.removeprefix("write ").strip()
            if topic:
                print(f"✍️ Detected write command: {topic}")
                func = asyncio.to_thread(Content, topic)
                funcs.append(func)
                
        elif command.startswith("switch language "):
            language = command.removeprefix("switch language ").strip().lower()
            try:
                from Backend.LanguageManager import switch_to_hindi, switch_to_english
                
                if language in ["hindi", "hi", "हिंदी"]:
                    func = asyncio.to_thread(switch_to_hindi)
                    funcs.append(func)
                elif language in ["english", "en", "अंग्रेजी"]:
                    func = asyncio.to_thread(switch_to_english)
                    funcs.append(func)
                else:
                    print(f"❌ Unknown language: {language}")
            except ImportError:
                print("❌ LanguageManager not available")
                
        elif command.startswith("open "):
            app_name = command.removeprefix("open ").strip()
            if app_name:
                func = asyncio.to_thread(OpenApp, app_name)
                funcs.append(func)
                
        elif command.startswith("close "):
            app_name = command.removeprefix("close ").strip()
            if app_name:
                func = asyncio.to_thread(CloseApp, app_name)
                funcs.append(func)
                
        elif command.startswith("play "):
            query = command.removeprefix("play ").strip()
            if query:
                func = asyncio.to_thread(PlayYoutube, query)
                funcs.append(func)
                
        elif command.startswith("content "):
            topic = command.removeprefix("content ").strip()
            if topic:
                func = asyncio.to_thread(Content, topic)
                funcs.append(func)
                
        elif command.startswith("google search "):
            query = command.removeprefix("google search ").strip()
            if query:
                func = asyncio.to_thread(GoogleSearch, query)
                funcs.append(func)
                
        elif command.startswith("system "):
            sys_command = command.removeprefix("system ").strip()
            if sys_command:
                func = asyncio.to_thread(System, sys_command)
                funcs.append(func)
                
        elif command.startswith(("general ", "realtime ")):
            print(f"Chatbot response needed for: {command}")
            yield f"Processing: {command}"
            
        elif any(keyword in command.lower() for keyword in 
                ["application", "letter", "essay", "article", "blog", "document"]):
            print(f"📝 Detected content-related command: {command}")
            func = asyncio.to_thread(Content, command)
            funcs.append(func)
            
        else:
            print(f"❌ No function found for: {command}")
    
    if funcs:
        results = await asyncio.gather(*funcs, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"❌ Error executing command: {result}")
                yield f"Error: {result}"
            elif isinstance(result, str):
                yield result
            elif result is True:
                yield "✅ Command executed successfully"
            else:
                yield f"Result: {result}"
    else:
        yield "No valid commands to execute."

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True

try:
    setup_voice_hotkeys()
    print("✅ Voice hotkeys initialized")
except Exception as e:
    print(f"⚠️ Failed to setup hotkeys: {e}")

if __name__ == "__main__":
    setup_voice_hotkeys()