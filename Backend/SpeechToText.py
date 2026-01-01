# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from dotenv import dotenv_values
# import os
# import mtranslate as mt
# import time

# env_vars = dotenv_values(".env")

# InputLanguage = env_vars.get("InputLanguage")

# HtmlCode = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>Speech Recognition</title>
# </head>
# <body>
#     <button id="start" onclick="startRecognition()">Start Recognition</button>
#     <button id="end" onclick="stopRecognition()">Stop Recognition</button>
#     <p id="output"></p>
#     <script>
#         const output = document.getElementById('output');
#         let recognition;

#         function startRecognition() {
#             recognition = new webkitSpeechRecognition() || new SpeechRecognition();
#             recognition.lang = '';
#             recognition.continuous = true;

#             recognition.onresult = function(event) {
#                 const transcript = event.results[event.results.length - 1][0].transcript;
#                 output.textContent += transcript;
#             };

#             recognition.onend = function() {
#                 recognition.start();
#             };
#             recognition.start();
#         }

#         function stopRecognition() {
#             recognition.stop();
#             output.innerHTML = "";
#         }
#     </script>
# </body>
# </html>'''

# HtmlCode = str(HtmlCode).replace("recognition.lang = 'en-US';", f"recognition.lang = '{InputLanguage or 'en-US'}';")

# with open(r"Data\Voice.html", "w") as f:
#     f.write(HtmlCode)

# current_dir = os.getcwd()

# Link = f"{current_dir}/Data/Voice.html"

# chrome_options = Options()
# user_agent = "Mozilla/5.0 (Window NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
# chrome_options.add_argument(f'user-agent={user_agent}')
# chrome_options.add_argument(f'--use-fake-ui-for-media-stream')
# chrome_options.add_argument(f'--use-fake-device-for-media-stream')
# chrome_options.add_argument(f'--headless=new')

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# TempDirPath = rf"{current_dir}/Frontend/Files"

# def SetAssistantStatus(Status):
#     with open(rf'{TempDirPath}/Status.data', "w", encoding='utf-8') as file:
#         file.write(Status)
    
# def QueryModifier(Query):
#     new_query = Query.lower().strip()
#     query_words = new_query.split()
#     question_words = ["how", "what", "who", "where", "when", "why", "which", "whose", "can you", "what's", "where's", "how's", "can you"]

#     if any(word + " " in new_query for word in question_words):
#         if query_words[-1][-1] in ['.', '?', '!']:
#             new_query = new_query[:-1] + "?"
#         else:
#             new_query += "?"
#     else:
#         if query_words[-1][-1] in ['.', '?', '!']:
#             new_query = new_query[:-1] + "."
#         else:
#             new_query += "."
#     return new_query.capitalize()

# def UniversalTranslator(Text):
#     english_translation = mt.translate(Text, "en", "auto")
#     return english_translation.capitalize()

# def SpeechRecognition():
#     driver.get("file:///" + Link)
    
#     time.sleep(1)
    
#     driver.find_element(by=By.ID, value="start").click()
    
#     start_time = time.time()
#     timeout = 30
    
#     while True:
#         try:
#             Text = driver.find_element(by=By.ID, value="output").text

#             if Text:
#                 driver.find_element(by=By.ID, value="end").click()
                
#                 driver.execute_script("document.getElementById('output').innerHTML = '';")
                
#                 if InputLanguage.lower() == "en" or "en" in InputLanguage.lower():
#                     return QueryModifier(Text)
#                 else:
#                     SetAssistantStatus("Translating...")
#                     return QueryModifier(UniversalTranslator(Text))
            
#             if time.time() - start_time > timeout:
#                 driver.find_element(by=By.ID, value="end").click()
#                 return ""

#         except Exception as e:
#             pass

# if __name__ == "__main__":
#     while True:
#         Text = SpeechRecognition()
#         print(Text)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from dotenv import dotenv_values

# import os
# import mtranslate as mt

# env_vars = dotenv_values(".env")

# InputLanguage = env_vars.get("InputLanguage")

# HtmlCode = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>Speech Recognition</title>
# </head>
# <body>
#     <button id="start" onclick="startRecognition()">Start Recognition</button>
#     <button id="end" onclick="stopRecognition()">Stop Recognition</button>
#     <p id="output"></p>
#     <script>
#         const output = document.getElementById('output');
#         let recognition;

#         function startRecognition() {
#             recognition = new webkitSpeechRecognition() || new SpeechRecognition();
#             recognition.lang = '';
#             recognition.continuous = true;

#             recognition.onresult = function(event) {
#                 const transcript = event.results[event.results.length - 1][0].transcript;
#                 output.textContent += transcript;
#             };

#             recognition.onend = function() {
#                 recognition.start();
#             };
#             recognition.start();
#         }

#         function stopRecognition() {
#             recognition.stop();
#             output.innerHTML = "";
#         }
#     </script>
# </body>
# </html>'''

# HtmlCode = str(HtmlCode).replace("recognition.lang = ''; ", f"recognition.lang = '{InputLanguage}';")

# with open(r"Data\Voice.html", "w") as f:
#     f.write(HtmlCode)

# current_dir = os.getcwd()

# Link = f"{current_dir}/Data/Voice.html"

# chrome_options = Options()
# user_agent = "Mozilla/5.0 (Window NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
# chrome_options.add_argument(f'user-agent={user_agent}')
# chrome_options.add_argument(f'--use-fake-ui-for-media-stream')
# chrome_options.add_argument(f'--use-fake-device-for-media-stream')
# chrome_options.add_argument(f'--headless=new')

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# TempDirPath = rf"{current_dir}/Frontend/Files"

# def SetAssistantStatus(Status):
#     with open(rf'{TempDirPath}/Status.data', "w", encoding='utf-8') as file:
#         file.write(Status)
    
# def QueryModifier(Query):
#     new_query = Query.lower().strip()
#     query_words = new_query.split()
#     question_words = ["how", "what", "who", "where", "when", "why", "which", "whose", "can you", "what's", "where's", "how's", "can you"]

#     if any(word + " " in new_query for word in question_words):
#         if query_words[-1][-1] in ['.', '?', '!']:
#             new_query = new_query[:-1] + "?"
#         else:
#             new_query += "?"
#     else:
#         if query_words[-1][-1] in ['.', '?', '!']:
#             new_query = new_query[:-1] + "."
#         else:
#             new_query += "."
#     return new_query.capitalize()

# def UniversalTranslator(Text):
#     english_translation = mt.translate(Text, "en", "auto")
#     return english_translation.capitalize()

# def SpeechRecognition():
#     driver.get("file:///" + Link)

#     driver.find_element(by=By.ID, value="start").click()

#     while True:
#         try:
#             Text = driver.find_element(by=By.ID, value="output").text

#             if Text:
#                 driver.find_element(by=By.ID, value="end").click()

#                 if  InputLanguage.lower() == "en" or "en" in InputLanguage.lower():
#                     return QueryModifier(Text)
#                 else:
#                     SetAssistantStatus("Translating...")
#                     return QueryModifier(UniversalTranslator(Text))
#         except Exception as e:
#             pass

# if __name__ == "__main__":
#     while True:
#         Text = SpeechRecognition()
#         print(Text)




#new:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import os
import mtranslate as mt

# Import language manager
try:
    from Backend.LanguageManager import get_current_language, switch_to_hindi, switch_to_english
except ImportError:
    # Fallback if LanguageManager not available
    def get_current_language():
        return {"input_language": "hi-IN", "current_language": "Hindi"}
    def switch_to_hindi(): return True
    def switch_to_english(): return True

def create_html_file(language_code):
    """Create HTML file with specific language"""
    HtmlCode = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Speech Recognition</title>
</head>
<body>
    <button id="start" onclick="startRecognition()">Start Recognition</button>
    <button id="end" onclick="stopRecognition()">Stop Recognition</button>
    <p id="output"></p>
    <script>
        const output = document.getElementById('output');
        let recognition;

        function startRecognition() {
            recognition = new webkitSpeechRecognition() || new SpeechRecognition();
            recognition.lang = 'LANG_PLACEHOLDER';
            recognition.continuous = true;

            recognition.onresult = function(event) {
                const transcript = event.results[event.results.length - 1][0].transcript;
                output.textContent += transcript;
            };

            recognition.onend = function() {
                recognition.start();
            };
            recognition.start();
        }

        function stopRecognition() {
            recognition.stop();
            output.innerHTML = "";
        }
    </script>
</body>
</html>'''
    
    HtmlCode = HtmlCode.replace("'LANG_PLACEHOLDER'", f"'{language_code}'")
    
    os.makedirs("Data", exist_ok=True)
    with open(r"Data\Voice.html", "w", encoding="utf-8") as f:
        f.write(HtmlCode)

# Initialize with current language
config = get_current_language()
create_html_file(config["input_language"])

current_dir = os.getcwd()
Link = f"{current_dir}/Data/Voice.html"

# Chrome setup
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--use-fake-ui-for-media-stream')
chrome_options.add_argument('--use-fake-device-for-media-stream')
chrome_options.add_argument('--headless=new')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

TempDirPath = rf"{current_dir}/Frontend/Files"

def SetAssistantStatus(Status):
    os.makedirs(TempDirPath, exist_ok=True)
    with open(rf'{TempDirPath}/Status.data', "w", encoding='utf-8') as file:
        file.write(Status)
    
def QueryModifier(Query):
    if not Query or not Query.strip():
        return "."
    
    new_query = Query.lower().strip()
    query_words = new_query.split()
    
    if not query_words:
        return "."
    
    question_words = ["how", "what", "who", "where", "when", "why", "which", "whose", "can you", "what's", "where's", "how's"]
    
    if any(new_query.startswith(word) or f" {word} " in f" {new_query} " for word in question_words):
        if query_words[-1][-1] in ['.', '?', '!']:
            new_query = new_query[:-1] + "?"
        else:
            new_query += "?"
    else:
        if query_words[-1][-1] in ['.', '?', '!']:
            new_query = new_query[:-1] + "."
        else:
            new_query += "."
    
    return new_query.capitalize()

def UniversalTranslator(Text):
    try:
        english_translation = mt.translate(Text, "en", "auto")
        return english_translation.capitalize() if english_translation else Text
    except:
        return Text

def check_language_command(text):
    """Check if text contains language switch command"""
    text_lower = text.lower()
    
    # Hindi switch commands
    hindi_commands = [
        "हिंदी में बोलो", "हिंदी बोलो", "हिंदी", 
        "hindi me bolo", "hindi mein bolo", "hindi mein", "hindi me",
        "speak in hindi", "switch to hindi", "hindi language", "hindi bhasha"
    ]
    
    # English switch commands  
    english_commands = [
        "अंग्रेजी में बोलो", "अंग्रेजी बोलो", "अंग्रेजी",
        "english me bolo", "english mein bolo", "english mein", "english me",
        "speak in english", "switch to english", "english language", "english bhasha"
    ]
    
    for cmd in hindi_commands:
        if cmd in text_lower:
            switch_to_hindi()
            create_html_file("hi-IN")
            return "hindi_switch"
    
    for cmd in english_commands:
        if cmd in text_lower:
            switch_to_english()
            create_html_file("en-US")
            return "english_switch"
    
    return None

def SpeechRecognition():
    try:
        driver.get("file:///" + Link)
        driver.find_element(by=By.ID, value="start").click()

        while True:
            try:
                Text = driver.find_element(by=By.ID, value="output").text.strip()
                
                if Text:
                    driver.find_element(by=By.ID, value="end").click()
                    
                    # Check for language switch
                    lang_result = check_language_command(Text)
                    if lang_result == "hindi_switch":
                        SetAssistantStatus("Switched to Hindi")
                        return "✅ Language switched to Hindi. अब मैं हिंदी में बोलूंगा।"
                    elif lang_result == "english_switch":
                        SetAssistantStatus("Switched to English")
                        return "✅ Language switched to English. Now I will speak in English."
                    
                    # Get current language for processing
                    current_config = get_current_language()
                    current_input_lang = current_config.get("input_language", "hi-IN")
                    
                    # Process based on current language
                    if "en" in current_input_lang.lower():
                        SetAssistantStatus("Processing...")
                        return QueryModifier(Text)
                    else:
                        SetAssistantStatus("Translating...")
                        translated = UniversalTranslator(Text)
                        return QueryModifier(translated)
                        
            except Exception as e:
                # Continue listening
                continue
                
    except Exception as e:
        print(f"Speech recognition error: {e}")
        return "Error in speech recognition."

if __name__ == "__main__":
    print("🎤 Speech Recognition Started. Speak now...")
    while True:
        Text = SpeechRecognition()
        print(f"You said: {Text}")