from Frontend.GUI import (
    GraphicalUserInterface,
    SetAssistantStatus,
    ShowTextToScreen,
    TempDirectoryPath,
    SetMicrophoneStatus,
    AnswerModifier,
    QueryModifier,
    GetAssistantStatus,
    GetMicrophoneStatus
)
from Backend.Model import FirstLayerDMM
from Backend.Automation import Automation
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values
from asyncio import run
from time import sleep
import subprocess
import threading
import json
import os
import warnings
import asyncio
from Backend.Automation import Automation

try:
    from Backend.LanguageManager import get_language_status, get_current_language
except ImportError:
    def get_language_status():
        return "🌍 Current Language: Hindi"
    def get_current_language():
        return {"current_language": "Hindi"}

warnings.filterwarnings("ignore", category=UserWarning)
env_vars = dotenv_values(".env")
Username = env_vars.get("Username", "Anand Suthar")
Assistantname = env_vars.get("Assistantname", "SPINO")

def get_welcome_message():
    config = get_current_language()
    current_lang = config.get("current_language", "Hindi")
    
    if "hindi" in current_lang.lower():
        return f'''{Username}. नमस्ते {Assistantname}, आप कैसे हैं?
{Assistantname} : नमस्ते {Username}, मैं ठीक हूं। मैं आपकी कैसे मदद कर सकता हूं?'''
    else:
        return f'''{Username}. Hello {Assistantname}, How are you?
{Assistantname} : Welcome {Username}, I am doing well. How may I help you?'''

DefaultMessage = get_welcome_message()

subprocesses = []
Functions = ["open", "close", "play", "system", "content", "google search", 
             "youtube search", "switch language", "generate", "create image"]

def ShowDefaultChatIfNoChats():
    os.makedirs("Data", exist_ok=True)
    chatlog_file = r'Data\ChatLog.json'
    
    if not os.path.exists(chatlog_file):
        with open(chatlog_file, "w", encoding='utf-8') as f:
            json.dump([], f, indent=4)
    
    with open(chatlog_file, "r", encoding='utf-8') as file:
        content = file.read()
        if len(content) < 5 or content.strip() == "":
            with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
                file.write("")
            with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
                file.write(DefaultMessage)

def ReadChatLogJson():
    try:
        with open(r'Data\ChatLog.json', "r", encoding='utf-8') as file:
            chatlog_data = json.load(file)
        return chatlog_data
    except Exception as e:
        print(f"Error reading ChatLog.json: {e}")
        return []

def ChatLogIntegration():
    json_data = ReadChatLogJson()
    formatted_chatlog = ""
    
    for entry in json_data:
        if entry["role"] == "user":
            formatted_chatlog += f"User: {entry['content']}\n"
        elif entry["role"] == "assistant":
            formatted_chatlog += f"Assistant: {entry['content']}\n"
    
    formatted_chatlog = formatted_chatlog.replace("User", Username + " ")
    formatted_chatlog = formatted_chatlog.replace("Assistant", Assistantname + " ")

    with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
        file.write(AnswerModifier(formatted_chatlog))

def ShowChatsOnGUI():
    os.makedirs(os.path.dirname(TempDirectoryPath('Database.data')), exist_ok=True)
    
    if not os.path.exists(TempDirectoryPath('Database.data')):
        with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as f:
            f.write(DefaultMessage)
    
    with open(TempDirectoryPath('Database.data'), "r", encoding='utf-8') as file:
        Data = file.read()
    
    if len(str(Data)) > 0:
        lines = Data.split('\n')
        result = '\n'.join(lines)
        
        os.makedirs(os.path.dirname(TempDirectoryPath('Responses.data')), exist_ok=True)
        with open(TempDirectoryPath('Responses.data'), "w", encoding='utf-8') as file:
            file.write(result)

def InitialExecution():
    SetMicrophoneStatus("False")
    ShowTextToScreen("")
    ShowDefaultChatIfNoChats()
    ChatLogIntegration()
    ShowChatsOnGUI()
    lang_status = get_language_status()
    SetAssistantStatus(f"Ready - {lang_status}")

InitialExecution()

def MainExecution():
    TaskExecution = False
    ImageExecution = False
    ImageGenerationQuery = ""

    SetAssistantStatus("Listening...")
    Query = SpeechRecognition()
    
    if not Query or Query.strip() == "":
        SetAssistantStatus("I didn't hear anything. Please try again.")
        return False
    
    ShowTextToScreen(f"{Username} : {Query}")
    SetAssistantStatus("Thinking...")
    Decision = FirstLayerDMM(Query)

    print("")
    print(f"Decision : {Decision}")
    print("")

    if not Decision or len(Decision) == 0:
        SetAssistantStatus("I didn't understand that. Could you repeat?")
        return False

    G = any([i for i in Decision if i.startswith("general")])
    R = any([i for i in Decision if i.startswith("realtime")])

    Merged_query = " and ".join(
        [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
    )

    ImageExecution = False
    for queries in Decision:
        if "generate" in queries.lower() or "create image" in queries.lower():
            ImageGenerationQuery = str(queries)
            ImageExecution = True
            break

    for queries in Decision:
        if not TaskExecution:
            if any(queries.startswith(func) for func in Functions):
                try:
                    run(Automation(list(Decision)))
                    TaskExecution = True
                except Exception as e:
                    print(f"Automation error: {e}")
                    SetAssistantStatus(f"Error: {str(e)[:50]}")

    # if ImageExecution:
    #     os.makedirs(r"Frontend\Files", exist_ok=True)
    #     with open(r"Frontend\Files\ImageGeneration.data", "w") as file:
    #         file.write(f"{ImageGenerationQuery},True")

    #     try:
    #         p1 = subprocess.Popen(['python', r'Backend\ImageGeneration.py'],
    #                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                              stdin=subprocess.PIPE, shell=False)
    #         subprocesses.append(p1)
    #     except Exception as e:
    #         print(f"Error starting ImageGeneration.py: {e}")
    #         SetAssistantStatus("Image generation failed")

    for queries in Decision:
        if "switch language" in queries:
            lang_status = get_language_status()
            SetAssistantStatus(lang_status)
            ShowTextToScreen(f"{Assistantname} : {lang_status}")
            TextToSpeech(f"Language switched successfully.")
            return True

    if G and R or R:
        SetAssistantStatus("Searching...")
        try:
            from Backend.RealtimeSearchEngine import RealtimeSearchEngine
            Answer = RealtimeSearchEngine(QueryModifier(Merged_query))
        except ImportError:
            Answer = "Realtime search is not available right now. Please try general questions."
        
        ShowTextToScreen(f"{Assistantname} : {Answer}")
        SetAssistantStatus("Answering...")
        TextToSpeech(Answer)
        return True
    
    else:
        for Queries in Decision:
            if "general" in Queries:
                SetAssistantStatus("Thinking...")
                QueryFinal = Queries.replace("general ", "")
                Answer = ChatBot(QueryModifier(QueryFinal))
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                TextToSpeech(Answer)
                return True
            
            elif "realtime" in Queries:
                SetAssistantStatus("Searching...")
                QueryFinal = Queries.replace("realtime ", "")
                try:
                    from Backend.RealtimeSearchEngine import RealtimeSearchEngine
                    Answer = RealtimeSearchEngine(QueryModifier(QueryFinal))
                except ImportError:
                    Answer = "Realtime search is not available."
                
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                TextToSpeech(Answer)
                return True
            
            elif "exit" in Queries:
                config = get_current_language()
                current_lang = config.get("current_language", "Hindi")
                
                if "hindi" in current_lang.lower():
                    goodbye_msg = "अलविदा, फिर मिलेंगे!"
                else:
                    goodbye_msg = "Goodbye, see you soon!"
                
                ShowTextToScreen(f"{Assistantname} : {goodbye_msg}")
                SetAssistantStatus("Answering...")
                TextToSpeech(goodbye_msg)
                SetAssistantStatus("Shutting down...")
                sleep(2)
                os._exit(1)
    
    SetAssistantStatus("Ready - " + get_language_status())
    return True

def FirstThread():
    while True:
        CurrentStatus = GetMicrophoneStatus()

        if CurrentStatus == "True":
            try:
                MainExecution()
            except Exception as e:
                print(f"Error in MainExecution: {e}")
                SetAssistantStatus("Error occurred. Ready again.")
        else:
            AIStatus = GetAssistantStatus()
            
            if "Available..." in AIStatus:
                sleep(0.1)
            else:
                SetAssistantStatus("Available... - " + get_language_status())

def SecondThread():
    try:
        GraphicalUserInterface()
    except Exception as e:
        print(f"GUI Error: {e}")

if __name__ == "__main__":
    print(f"🤖 Starting {Assistantname} AI Assistant...")
    print(f"👤 User: {Username}")
    print(f"🌍 Initial Language: {get_language_status()}")
    
    thread2 = threading.Thread(target=FirstThread, daemon=True)
    thread2.start()

    # print("🧪 Testing Automation directly...")
    # asyncio.run(Automation(["generate image of modi"]))
    
    SecondThread()