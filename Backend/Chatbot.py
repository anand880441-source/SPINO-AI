# from groq import Groq
# from json import load, dump
# import datetime
# from dotenv import dotenv_values

# env_vars = dotenv_values(".env")

# Username = env_vars.get("Username")
# Assistantname = env_vars.get("Assistantname")
# GroqAPIKey = env_vars.get("GroqAPIKey")

# client = Groq(api_key=GroqAPIKey)

# messages = []

# System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
# *** Do not tell time until I ask, do not talk too much, just answer the question.***
# *** Reply in only English, even if the question is in Hindi, reply in English.***
# *** Do not provide notes in the output, just answer the question and never mention your training data. ***
# """

# SystemChatBot = [
#     {"role": "system", "content": System}
# ]

# try:
#     with open(r"Data\ChatLog.json") as f:
#         messages = load(f)
# except FileNotFoundError:
#     with open(r"Data\ChatLog.json", "w") as f:
#         dump([], f)

# def RealtimeInformation():
#     current_date_time = datetime.datetime.now()
#     day = current_date_time.strftime("%A")
#     date = current_date_time.strftime("%d") 
#     month = current_date_time.strftime("%B")
#     year = current_date_time.strftime("%Y")
#     hour = current_date_time.strftime("%H")
#     minute = current_date_time.strftime("%M")
#     second = current_date_time.strftime("%S")

#     data = f"Please use this real-time information if needed:\n"
#     data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"  # Fixed: Date not Data
#     data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    
#     return data  

# def AnswerModifier(Answer):
#     lines = Answer.split('\n')
#     non_empty_lines = [line for line in lines if line.strip()]
#     modified_answer = '\n'.join(non_empty_lines)
#     return modified_answer

# def ChatBot(Query):
#     """This function sends the user's query to the chatbot and returns the AI's response. """

#     try:
#         with open(r"Data\ChatLog.json", "r") as f:
#             messages = load(f)

#             messages.append({"role": "user", "content": f"{Query}"})

#             completion = client.chat.completions.create(
#                 model="llama-3.3-70b-versatile",
#                 messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
#                 max_tokens=1024,
#                 temperature=0.7,
#                 top_p=1,
#                 stream=True,
#                 stop=None
#             )

#             Answer = ""

#             for chunk in completion:
#                 if chunk.choices[0].delta.content:
#                     Answer += chunk.choices[0].delta.content
            
#             Answer = Answer.replace("</s>", "")

#             messages.append({"role": "assistant", "content": Answer})

#             with open(r"Data\ChatLog.json", "w") as f:
#                 dump(messages, f, indent=4)

#             return AnswerModifier(Answer=Answer)

#     except Exception as e:

#         print(f"Error: {e}")
#         with open(r"Data\ChatLog.json", "w") as f:
#             dump([], f, indent=4)
#         return ChatBot(Query)


# if __name__ == "__main__":
#     while True:
#         user_input = input("Enter Your Questions: ")
#         print(ChatBot(user_input))





# from groq import Groq
# from json import load, dump
# import datetime
# from dotenv import dotenv_values

# env_vars = dotenv_values(".env")

# Username = env_vars.get("Username")
# Assistantname = env_vars.get("Assistantname")
# GroqAPIKey = env_vars.get("GroqAPIKey")

# client = Groq(api_key=GroqAPIKey)

# messages = []

# System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
# *** Do not tell time until I ask, do not talk too much, just answer the question.***
# *** Reply in only English, even if the question is in Hindi, reply in English.***
# *** Do not provide notes in the output, just answer the question and never mention your training data. ***
# """

# SystemChatBot = [
#     {"role": "system", "content": System}
# ]

# try:
#     with open(r"Data\ChatLog.json", "r") as f:
#         messages = load(f)
# except Exception:
#     # File doesn't exist or is invalid
#     messages = []
#     with open(r"Data\ChatLog.json", "w") as f:
#         dump([], f, indent=4)

# def RealtimeInformation():
#     current_date_time = datetime.datetime.now()
#     day = current_date_time.strftime("%A")
#     date = current_date_time.strftime("%d") 
#     month = current_date_time.strftime("%B")
#     year = current_date_time.strftime("%Y")
#     hour = current_date_time.strftime("%H")
#     minute = current_date_time.strftime("%M")
#     second = current_date_time.strftime("%S")

#     data = f"Please use this real-time information if needed:\n"
#     data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
#     data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    
#     return data  

# def AnswerModifier(Answer):
#     lines = Answer.split('\n')
#     non_empty_lines = [line for line in lines if line.strip()]
#     modified_answer = '\n'.join(non_empty_lines)
#     return modified_answer

# def ChatBot(Query):
#     """This function sends the user's query to the chatbot and returns the AI's response. """

#     try:
#         with open(r"Data\ChatLog.json", "r") as f:
#             messages = load(f)

#             messages.append({"role": "user", "content": f"{Query}"})

#             completion = client.chat.completions.create(
#                 model="llama-3.3-70b-versatile",
#                 messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
#                 max_tokens=1024,
#                 temperature=0.7,
#                 top_p=1,
#                 stream=True,
#                 stop=None
#             )

#             Answer = ""

#             for chunk in completion:
#                 if chunk.choices[0].delta.content:
#                     Answer += chunk.choices[0].delta.content
            
#             Answer = Answer.replace("</s>", "")

#             messages.append({"role": "assistant", "content": Answer})

#             with open(r"Data\ChatLog.json", "w") as f:
#                 dump(messages, f, indent=4)

#             return AnswerModifier(Answer=Answer)

#     except Exception as e:

#         print(f"Error: {e}")
#         with open(r"Data\ChatLog.json", "w") as f:
#             dump([], f, indent=4)
#         return ChatBot(Query)


# if __name__ == "__main__":
#     while True:
#         user_input = input("Enter Your Questions: ")
#         print(ChatBot(user_input))


#new:

from groq import Groq
from json import load, dump
import datetime
import os

# Import language manager
try:
    from Backend.LanguageManager import get_current_language, get_language_status
except ImportError:
    def get_current_language():
        return {"current_language": "Hindi"}
    def get_language_status():
        return "🌍 Current Language: Hindi"

# Load API key from environment
try:
    from dotenv import dotenv_values
    env_vars = dotenv_values(".env")
    Username = env_vars.get("Username", "Anand Suthar")
    Assistantname = env_vars.get("Assistantname", "SPINO")
    GroqAPIKey = env_vars.get("GroqAPIKey", "")
except:
    Username = "Anand Suthar"
    Assistantname = "SPINO"
    GroqAPIKey = ""

client = Groq(api_key=GroqAPIKey) if GroqAPIKey else None

messages = []

def get_system_prompt():
    """Get dynamic system prompt based on current language"""
    try:
        # Try to read from LanguagePrompt.data
        prompt_file = "Frontend/Files/LanguagePrompt.data"
        if os.path.exists(prompt_file):
            with open(prompt_file, "r", encoding="utf-8") as f:
                prompt = f.read().strip()
                # Add the time permission line
                if "You have access to real-time information" not in prompt:
                    prompt = prompt.replace(
                        "*** Do not tell time until I ask, do not talk too much, just answer the question. ***",
                        "*** You have access to real-time information and can answer questions about time, date, and current events. ***"
                    )
                return prompt
    except:
        pass
    
    # Fallback based on current language
    config = get_current_language()
    lang_name = config.get("current_language", "Hindi")
    
    if "hindi" in lang_name.lower():
        return f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname}.
*** I am currently speaking in Hindi. ***
*** Reply in Hindi language unless asked otherwise. ***
*** You have access to real-time information including current time, date, and news. ***
*** You can answer questions about time, date, and any other topics. ***
*** Provide professional, helpful answers with proper punctuation. ***
*** Do not mention your training data or that you're an AI. ***"""
    else:
        return f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname}.
*** I am currently speaking in English. ***
*** Reply in English language unless asked otherwise. ***
*** You have access to real-time information including current time, date, and news. ***
*** You can answer questions about time, date, and any other topics. ***
*** Provide professional, helpful answers with proper punctuation. ***
*** Do not mention your training data or that you're an AI. ***"""

SystemChatBot = [
    {"role": "system", "content": get_system_prompt()}
]

# Ensure Data directory exists
os.makedirs("Data", exist_ok=True)

# Load chat history
try:
    with open(r"Data\ChatLog.json", "r", encoding="utf-8") as f:
        messages = load(f)
except Exception:
    messages = []
    with open(r"Data\ChatLog.json", "w", encoding="utf-8") as f:
        dump([], f, indent=4)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d") 
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Current real-time information:\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour}:{minute}:{second}\n"
    
    return data  

def AnswerModifier(Answer):
    if not Answer:
        return ""
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    """This function sends the user's query to the chatbot and returns the AI's response."""
    
    if not client:
        return "Error: Groq API key not configured."
    
    # Check for language commands
    query_lower = Query.lower()
    
    if any(cmd in query_lower for cmd in ["switch to hindi", "हिंदी", "hindi me bolo", "hindi mein", "speak hindi"]):
        try:
            from Backend.LanguageManager import switch_to_hindi
            switch_to_hindi()
            return "✅ Language switched to Hindi. अब मैं हिंदी में बात करूंगा।"
        except:
            return "Language switched to Hindi"
    
    elif any(cmd in query_lower for cmd in ["switch to english", "अंग्रेजी", "english me bolo", "english mein", "speak english"]):
        try:
            from Backend.LanguageManager import switch_to_english
            switch_to_english()
            return "✅ Language switched to English. Now I will speak in English."
        except:
            return "Language switched to English"
    
    elif "current language" in query_lower or "कौन सी भाषा" in query_lower or "भाषा" in query_lower:
        return get_language_status()

    try:
        # Reload chat history for fresh conversation
        with open(r"Data\ChatLog.json", "r", encoding="utf-8") as f:
            messages = load(f)

        # Add user query
        messages.append({"role": "user", "content": f"{Query}"})

        # Get updated system prompt
        SystemChatBot[0]["content"] = get_system_prompt()

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages[-10:],  # Last 10 messages for context
            max_tokens=1024,
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

        # Add assistant response to history
        messages.append({"role": "assistant", "content": Answer})

        # Save updated history (keep last 20 messages to prevent file bloat)
        if len(messages) > 20:
            messages = messages[-20:]
        
        with open(r"Data\ChatLog.json", "w", encoding="utf-8") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer)

    except Exception as e:
        print(f"ChatBot Error: {e}")
        
        # Reset on major error
        try:
            with open(r"Data\ChatLog.json", "w", encoding="utf-8") as f:
                dump([], f, indent=4)
        except:
            pass
        
        return f"I encountered an error. Please try again."


if __name__ == "__main__":
    print(f"🤖 {Assistantname} ChatBot - Testing Mode")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        if user_input:
            response = ChatBot(user_input)
            print(f"{Assistantname}: {response}")