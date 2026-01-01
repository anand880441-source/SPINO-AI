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

# try:
#     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
#     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
#     webbrowser._tryorder = ['chrome'] + webbrowser._tryorder
# except:
#     pass

# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.366'

# env_vars = dotenv_values(".env")
# GroqAPIKey = env_vars.get("GroqAPIKey")
# client = Groq(api_key=GroqAPIKey)

# professional_responses = [
#     "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
#     "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
# ]

# messages = []
# SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'Assistant')}. You're a content writer who writes letters, articles, blogs, and other documents professionally."}]

# def GoogleSearch(Topic):
#     search(Topic)
#     return True
# # GoogleSearch("onepower esports")

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

# # Content("Application for a job")

# def YouTubeSearch(Topic):
#     Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
#     webbrowser.open(Url4Search)
#     return True

# # YouTubeSearch("onepower esports")

# def PlayYoutube(query):
#     playonyt(query)
#     return True

# def OpenApp(app, sess=requests.session()):
#     """Open apps - tries local apps first, then opens as website"""
    
#     print(f"🌐 Opening: {app}")
    
#     # List of apps that SHOULD have desktop versions
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
#         # Add other desktop-only apps here
#     }
    
#     app_lower = app.lower()
    
#     # Check if it's a known desktop app that should be tried first
#     if app_lower in desktop_apps:
#         desktop_app_name = desktop_apps[app_lower]
#         print(f"💻 Trying desktop app: {desktop_app_name}")
        
#         try:
#             appopen(desktop_app_name, match_closest=False, output=False, throw_error=True)
#             print(f"✅ Opened desktop app: {desktop_app_name}")
#             return True
#         except Exception as e:
#             print(f"📱 Desktop app not found: {e}")
#             # Fall through to website opening
    
#     # For websites/web apps (like Canva, Google, etc.), open directly as website
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
# # OpenApp("whatsapp")
# # OpenApp("canva")

# def CloseApp(app):
#     if "chrome" in app.lower():
#         pass
#     else:
#         try:
#             close(app, match_closest=True, output=False, throw_error=True)
#             return True
#         except:
#             return False

# # CloseApp("whatsApp")

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
#         if command.startswith("open "):
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
#             print(f"Feature not implemented yet: {command}")
#         else:
#             print(f"No function found for: {command}")
    
#     if funcs:
#         results = await asyncio.gather(*funcs, return_exceptions=True)
#         for result in results:
#             if isinstance(result, Exception):
#                 print(f"Error executing command: {result}")
#             elif isinstance(result, str):
#                 yield result
#             else:
#                 yield result
#     else:
#         yield "No valid commands to execute."

# async def Automation(commands: list[str]):
#     async for result in TranslateAndExecute(commands):
#         pass
#     return True


# # if __name__ == "__main__":
# #     asyncio.run(Automation(["open facebook", "open instagram","play tu hai kaha","content song for me"]))



#new:
from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from rich import print
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os
import threading
import time

# Import language manager
try:
    from Backend.LanguageManager import switch_to_hindi, switch_to_english, get_language_status
except ImportError:
    def switch_to_hindi(): return True
    def switch_to_english(): return True
    def get_language_status(): return "🌍 Current Language: Hindi"

try:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser._tryorder = ['chrome'] + webbrowser._tryorder
except:
    pass

# Load Groq API key if needed for content generation
try:
    from dotenv import dotenv_values
    from groq import Groq
    env_vars = dotenv_values(".env")
    GroqAPIKey = env_vars.get("GroqAPIKey")
    if GroqAPIKey:
        client = Groq(api_key=GroqAPIKey)
    else:
        client = None
except:
    client = None

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

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
    if not client:
        return "Error: Groq API not configured for content writing."
    
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

def VoiceControl(command):
    """Handle voice control commands for speech"""
    from Backend.TextToSpeech import pause_speech, resume_speech, stop_speech, get_speech_status
    
    command = command.lower().strip()
    
    if command in ["pause", "wait", "hold on", "रुको", "प्रतीक्षा करो"]:
        success = pause_speech()
        return f"⏸️ Speech {'paused' if success else 'already paused'}"
    
    elif command in ["resume", "continue", "go on", "जारी रखो", "आगे बढ़ो"]:
        success = resume_speech()
        return f"▶️ Speech {'resumed' if success else 'not paused'}"
    
    elif command in ["stop", "halt", "बंद करो", "रोको"]:
        success = stop_speech()
        return f"⏹️ Speech {'stopped' if success else 'already stopped'}"
    
    elif command in ["status", "स्थिति"]:
        status = get_speech_status()
        return f"📊 Speech status: {status['state']}"
    
    return "Unknown voice control command"

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, sess=requests.session()):
    print(f"🌐 Opening: {app}")
    
    # Desktop apps
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
    
    # Websites
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
        if command.startswith("open "):
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
        elif command.startswith("switch language "):
            language = command.removeprefix("switch language ").strip().lower()
            if language in ["hindi", "hi", "हिंदी"]:
                func = asyncio.to_thread(switch_to_hindi)
            elif language in ["english", "en", "अंग्रेजी"]:
                func = asyncio.to_thread(switch_to_english)
            else:
                print(f"Unknown language: {language}")
                continue
            funcs.append(func)
        elif command.startswith(("general ", "realtime ")):
            print(f"Chatbot response: {command}")
        else:
            print(f"No function found for: {command}")
    
    if funcs:
        results = await asyncio.gather(*funcs, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Error executing command: {result}")
            elif isinstance(result, str):
                yield result
            else:
                yield result
    else:
        yield "No valid commands to execute."

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True

if __name__ == "__main__":
    print("🤖 Automation System - Testing")
    print("Commands: open [app], close [app], play [song], switch language [hindi/english]")
    
    test_commands = ["open notepad", "switch language hindi", "play classical music"]
    asyncio.run(Automation(test_commands))