# from groq import Groq
# from json import load, dump
# import datetime
# from dotenv import dotenv_values
# from ddgs import DDGS

# env_vars = dotenv_values(".env")

# Username = env_vars.get("Username")
# Assistantname = env_vars.get("Assistantname")
# GroqAPIKey = env_vars.get("GroqAPIKey")

# client = Groq(api_key=GroqAPIKey)

# System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
# *** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
# *** Just answer the question from the provided data in a professional way. ***"""

# try:
#     with open(r"Data\Chatbot.json", "r") as f:
#         messages = load(f)
# except:
#     with open(r"Data\Chatbot.json", "w") as f:
#         dump([], f)

# # def GoogleSearch(query):
# #     try:
# #         results = list(search(query, advanced=True, num_results=5, sleep_interval=2))
# #         Answer = ""
# #         Answer += f"The search results for '{query}' are:\n[start]\n"
        
# #         for i in results:
# #             Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"
        
# #         Answer += "[end]"
# #         return Answer
# #     except Exception as e:
# #         return f"Search error: {str(e)}"

# def GoogleSearch(query):
#     """Use DuckDuckGo instead of Google - much more reliable"""
#     try:
#         print(f"\n🔍 Searching DuckDuckGo for: '{query}'")
        
#         with DDGS() as ddgs:
#             results = list(ddgs.text(query, max_results=1))
            
#             print(f"✅ Found {len(results)} results")
            
#             if len(results) == 0:
#                 return f"No search results found for '{query}'. Try a different query."
            
#             Answer = f"The search results for '{query}' are:\n[start]\n"
            
#             for i, result in enumerate(results, 1):
#                 title = result.get('title', 'No title')
#                 description = result.get('body', 'No description')
#                 Answer += f"Result {i}:\nTitle: {title}\nDescription: {description}\n\n"
            
#             Answer += "[end]"
#             return Answer
            
#     except Exception as e:
#         error_msg = f"DuckDuckGo search failed: {str(e)}"
#         print(f"❌ {error_msg}")
#         return error_msg

# def AnswerModifier(Answer):
#     lines = Answer.split('\n')
#     non_empty_lines = [line for line in lines if line.strip()]
#     modified_answer = '\n'.join(non_empty_lines)
#     return modified_answer

# SystemChatBot = [
#     {"role": "system", "content": System},
#     {"role": "user", "content": "Hi"},
#     {"role": "assistant", "content": "Hello, how can I help you?"}
# ]

# def Information():
#     data = ""
#     current_date_time = datetime.datetime.now()
#     day = current_date_time.strftime("%A")
#     date = current_date_time.strftime("%d") 
#     month = current_date_time.strftime("%B")
#     year = current_date_time.strftime("%Y")
#     hour = current_date_time.strftime("%H")
#     minute = current_date_time.strftime("%M")
#     second = current_date_time.strftime("%S")

#     data = f"Use This Real-time Information If needed:\n"
#     data += f"Day: {day}\n"
#     data += f"Date: {date}\n"
#     data += f"Month: {month}\n"
#     data += f"Year: {year}\n"
#     data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"

#     return data  

# def RealtimeSearchEngine(prompt):
#     try:
#         with open(r"Data\Chatbot.json", "r") as f:
#             messages = load(f)
#     except:
#         messages = []

#     messages.append({"role": "user", "content": f"{prompt}"})

#     api_messages = [
#         {"role": "system", "content": System},
#         {"role": "system", "content": Information()},
#         {"role": "system", "content": GoogleSearch(prompt)}  
#     ]
#     api_messages.extend(messages[-2:]) 

#     completion = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=api_messages, 
#         temperature=0.7,
#         max_tokens=2048,
#         top_p=1,
#         stream=True,
#         stop=None
#     )

#     Answer = ""
#     for chunk in completion:
#         if chunk.choices[0].delta.content:
#             Answer += chunk.choices[0].delta.content

#     Answer = Answer.strip().replace("</s>", "")
#     messages.append({"role": "assistant", "content": Answer})

#     with open(r"Data\Chatbot.json", "w") as f:
#         dump(messages[-50:], f, indent=4)

#     return AnswerModifier(Answer=Answer)


# if __name__ == "__main__":
#     while True:
#         prompt = input("Enter your query: ")
#         print(RealtimeSearchEngine(prompt))




#new
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values
from ddgs import DDGS
import os

# Import language manager
try:
    from Backend.LanguageManager import get_current_language
except ImportError:
    def get_current_language():
        return {"current_language": "Hindi", "display_name": "Hindi"}

env_vars = dotenv_values(".env")

Username = env_vars.get("Username", "Anand Suthar")
Assistantname = env_vars.get("Assistantname", "SPINO")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey) if GroqAPIKey else None

def get_system_prompt():
    """Get dynamic system prompt based on current language"""
    config = get_current_language()
    current_lang = config.get("current_language", "Hindi")
    
    if "hindi" in current_lang.lower():
        return f"""नमस्ते, मैं {Username} हूं, आप {Assistantname} नामक एक बहुत ही सटीक और उन्नत AI चैटबॉट हैं जिसके पास इंटरनेट से वास्तविक समय की जानकारी है।
*** पेशेवर तरीके से उत्तर प्रदान करें, पूर्ण विराम, अल्पविराम, प्रश्न चिह्न जोड़ना सुनिश्चित करें और उचित व्याकरण का उपयोग करें।***
*** केवल प्रदान किए गए डेटा से प्रश्न का उत्तर दें। ***
*** हमेशा हिंदी में जवाब दें जब तक कि अंग्रेजी में जवाब देने के लिए न कहा जाए। ***"""
    else:
        return f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***
*** Always respond in English unless asked to answer in Hindi. ***"""

# Ensure Data directory exists
os.makedirs("Data", exist_ok=True)

# Load or create chat history
chatbot_file = r"Data\Chatbot.json"
try:
    with open(chatbot_file, "r", encoding="utf-8") as f:
        messages = load(f)
except:
    messages = []
    with open(chatbot_file, "w", encoding="utf-8") as f:
        dump([], f, indent=4)

def GoogleSearch(query):
    """Use DuckDuckGo for search - more reliable and free"""
    try:
        print(f"\n🔍 Searching for: '{query}'")
        
        with DDGS() as ddgs:
            # Get 3 results for better information
            results = list(ddgs.text(query, max_results=3))
            
            print(f"✅ Found {len(results)} results")
            
            if len(results) == 0:
                # Return a helpful message in current language
                config = get_current_language()
                current_lang = config.get("current_language", "Hindi")
                
                if "hindi" in current_lang.lower():
                    return f"'{query}' के लिए कोई खोज परिणाम नहीं मिले। कृपया एक अलग प्रश्न आज़माएं।"
                else:
                    return f"No search results found for '{query}'. Please try a different query."
            
            # Format results based on current language
            config = get_current_language()
            current_lang = config.get("current_language", "Hindi")
            
            if "hindi" in current_lang.lower():
                Answer = f"'{query}' के लिए खोज परिणाम:\n[शुरू]\n\n"
            else:
                Answer = f"The search results for '{query}' are:\n[start]\n\n"
            
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                description = result.get('body', 'No description')
                
                if "hindi" in current_lang.lower():
                    Answer += f"परिणाम {i}:\nशीर्षक: {title}\nविवरण: {description}\n\n"
                else:
                    Answer += f"Result {i}:\nTitle: {title}\nDescription: {description}\n\n"
            
            if "hindi" in current_lang.lower():
                Answer += "[समाप्त]"
            else:
                Answer += "[end]"
            
            return Answer
            
    except Exception as e:
        print(f"❌ Search error: {e}")
        
        # Error message in current language
        config = get_current_language()
        current_lang = config.get("current_language", "Hindi")
        
        if "hindi" in current_lang.lower():
            return f"खोज असफल रही। कृपया बाद में पुन: प्रयास करें। त्रुटि: {str(e)[:50]}"
        else:
            return f"Search failed. Please try again later. Error: {str(e)[:50]}"

def AnswerModifier(Answer):
    """Clean up the answer text"""
    if not Answer:
        return ""
    
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    
    # Ensure proper ending punctuation
    if modified_answer and modified_answer[-1] not in ['.', '!', '?']:
        modified_answer += '.'
    
    return modified_answer

def Information():
    """Get current date and time information"""
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d") 
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")
    
    # Format based on current language
    config = get_current_language()
    current_lang = config.get("current_language", "Hindi")
    
    if "hindi" in current_lang.lower():
        data = f"यदि आवश्यक हो तो इस वास्तविक समय की जानकारी का उपयोग करें:\n"
        data += f"दिन: {day}\n"
        data += f"तारीख: {date}\n"
        data += f"महीना: {month}\n"
        data += f"वर्ष: {year}\n"
        data += f"समय: {hour} बजे :{minute} मिनट :{second} सेकंड।\n"
    else:
        data = f"Use This Real-time Information If needed:\n"
        data += f"Day: {day}\n"
        data += f"Date: {date}\n"
        data += f"Month: {month}\n"
        data += f"Year: {year}\n"
        data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    
    return data

def RealtimeSearchEngine(prompt):
    """Main function for real-time searches with multilingual support"""
    
    if not client:
        config = get_current_language()
        current_lang = config.get("current_language", "Hindi")
        
        if "hindi" in current_lang.lower():
            return "क्षमा करें, AI सेवा उपलब्ध नहीं है। कृपया API कुंजी जांचें।"
        else:
            return "Sorry, AI service is not available. Please check API key."
    
    # Check for language switch commands first
    prompt_lower = prompt.lower()
    if any(cmd in prompt_lower for cmd in ["switch to hindi", "हिंदी", "hindi me", "speak hindi"]):
        try:
            from Backend.LanguageManager import switch_to_hindi
            switch_to_hindi()
            return "✅ Language switched to Hindi. अब मैं हिंदी में खोज करूंगा।"
        except:
            return "Language switched to Hindi."
    
    elif any(cmd in prompt_lower for cmd in ["switch to english", "अंग्रेजी", "english me", "speak english"]):
        try:
            from Backend.LanguageManager import switch_to_english
            switch_to_english()
            return "✅ Language switched to English. Now I will search in English."
        except:
            return "Language switched to English."
    
    try:
        # Load chat history
        with open(r"Data\Chatbot.json", "r", encoding="utf-8") as f:
            messages = load(f)
    except:
        messages = []

    # Add user query
    messages.append({"role": "user", "content": f"{prompt}"})

    # Prepare messages for API
    api_messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "system", "content": Information()},
        {"role": "system", "content": GoogleSearch(prompt)}
    ]
    
    # Add recent conversation context (last 2 messages)
    api_messages.extend(messages[-2:]) 

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=api_messages, 
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.strip().replace("</s>", "")
        
        # Add assistant response to history
        messages.append({"role": "assistant", "content": Answer})

        # Save history (keep last 50 messages)
        with open(r"Data\Chatbot.json", "w", encoding="utf-8") as f:
            dump(messages[-50:], f, indent=4, ensure_ascii=False)

        return AnswerModifier(Answer=Answer)

    except Exception as e:
        error_msg = str(e)
        print(f"❌ API Error: {error_msg}")
        
        # Return error in current language
        config = get_current_language()
        current_lang = config.get("current_language", "Hindi")
        
        if "hindi" in current_lang.lower():
            return f"क्षमा करें, मैं अभी खोज नहीं कर पा रहा हूं। कृपया बाद में पुन: प्रयास करें। त्रुटि: {error_msg[:50]}"
        else:
            return f"Sorry, I couldn't perform the search right now. Please try again later. Error: {error_msg[:50]}"


if __name__ == "__main__":
    print("🔍 Realtime Search Engine - Testing Mode")
    print("Type 'exit' to quit\n")
    
    # Show current language
    try:
        from Backend.LanguageManager import get_language_status
        print(get_language_status())
    except:
        pass
    
    while True:
        prompt = input("\nEnter your query: ").strip()
        
        if prompt.lower() == 'exit':
            break
        
        if prompt:
            result = RealtimeSearchEngine(prompt)
            print(f"\n📝 Result:\n{result}")