from groq import Groq
from json import load, dump
import datetime
import os
from google import genai
import time
import requests
import random
from dotenv import dotenv_values

GEMINI_MODEL = "models/gemini-2.0-flash"

try:
    from Backend.LanguageManager import get_current_language, get_language_status
except ImportError:
    def get_current_language():
        return {"current_language": "Hindi"}
    def get_language_status():
        return "🌍 Current Language: Hindi"

from pathlib import Path

current_dir = Path(__file__).parent
root_dir = current_dir.parent  
env_path = root_dir / ".env"
env_vars = dotenv_values(str(env_path))

Username = env_vars.get("Username", "Anand Suthar")
Assistantname = env_vars.get("Assistantname", "SPINO")

cached_responses = {
    "hello": "Hello! I'm SPINO AI, ready to help you!",
    "hi": "Hi there! What can I do for you today?",
    "hey": "Hey! How can I assist you?",
    "how are you": "I'm running great! Thanks for asking!",
    "what is your name": "I'm SPINO, your AI assistant!",
    "who created you": "I was created by Anand Suthar!",
    "what can you do": "I can chat, answer questions, open apps, generate images, switch languages, and more!",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! See you later!",
}

groq_keys = [
    env_vars.get("GroqAPIKey1", ""),
    env_vars.get("GroqAPIKey2", ""),
    env_vars.get("GroqAPIKey3", ""),
    env_vars.get("GroqAPIKey4", ""),
]

groq_keys = [key for key in groq_keys if key and key.strip()]
groq_clients = []

for i, key in enumerate(groq_keys):
    try:
        client = Groq(api_key=key)
        groq_clients.append({"client": client, "index": i})
        print(f"✅ Groq client {i+1} initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Groq client {i+1}: {e}")

GeminiAPIKey = env_vars.get("GeminiAPIKey", "")
HuggingFaceAPIKey = env_vars.get("HuggingFaceAPIKey", "")
CohereAPIKey = env_vars.get("CohereAPIKey", "")

gemini_client = None
if GeminiAPIKey:
    try:
        gemini_client = genai.Client(api_key=GeminiAPIKey)
        print("✅ Gemini API initialized")
    except Exception as e:
        print(f"❌ Gemini init failed: {e}")

failed_groq_clients = set()
current_groq_index = 0

def get_next_groq_client():
    """Get next available Groq client with rotation"""
    global current_groq_index
    
    if not groq_clients:
        return None
    
    for _ in range(len(groq_clients)):
        client_info = groq_clients[current_groq_index]
        current_groq_index = (current_groq_index + 1) % len(groq_clients)
        
        if client_info["index"] not in failed_groq_clients:
            return client_info["client"]
    
    failed_groq_clients.clear()
    return groq_clients[0]["client"] if groq_clients else None

def mark_groq_client_failed(client_index):
    """Mark a Groq client as failed"""
    failed_groq_clients.add(client_index)
    print(f"⚠️ Marked Groq client {client_index} as failed")

messages = []

def get_system_prompt():
    """Get dynamic system prompt based on current language"""
    try:
        prompt_file = "Frontend/Files/LanguagePrompt.data"
        if os.path.exists(prompt_file):
            with open(prompt_file, "r", encoding="utf-8") as f:
                prompt = f.read().strip()
                if "You have access to real-time information" not in prompt:
                    prompt = prompt.replace(
                        "*** Do not tell time until I ask, do not talk too much, just answer the question. ***",
                        "*** You have access to real-time information and can answer questions about time, date, and current events. ***"
                    )
                return prompt
    except:
        pass
    
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

os.makedirs("Data", exist_ok=True)

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

def try_groq_api(Query):
    """Try Groq API with multiple key rotation"""
    try:
        with open(r"Data\ChatLog.json", "r", encoding="utf-8") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})
        SystemChatBot[0]["content"] = get_system_prompt()

        client = get_next_groq_client()
        if not client:
            raise Exception("No Groq clients available")

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages[-10:],
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
        messages.append({"role": "assistant", "content": Answer})

        if len(messages) > 20:
            messages = messages[-20:]
        
        with open(r"Data\ChatLog.json", "w", encoding="utf-8") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer)
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "rate limit" in error_msg.lower():
            for client_info in groq_clients:
                if client_info["client"] == client:
                    mark_groq_client_failed(client_info["index"])
                    break
        raise e

def try_gemini_api(Query):
    """Try Gemini API"""
    try:
        with open(r"Data\ChatLog.json", "r", encoding="utf-8") as f:
            messages = load(f)
        
        prompt = f"""{get_system_prompt()}

{RealtimeInformation()}

Recent conversation:
"""
        for msg in messages[-10:]:
            role = "User" if msg["role"] == "user" else "Assistant"
            prompt += f"{role}: {msg['content']}\n"
        
        prompt += f"\nUser: {Query}\nAssistant:"
        
        response = gemini_client.models.generate_content(
            model="models/gemini-2.0-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.7,
                top_p=0.9,
                max_output_tokens=1024,
            )
        )
        
        Answer = response.text.strip()
        
        messages.append({"role": "user", "content": Query})
        messages.append({"role": "assistant", "content": Answer})
        
        if len(messages) > 20:
            messages = messages[-20:]
        
        with open(r"Data\ChatLog.json", "w", encoding="utf-8") as f:
            dump(messages, f, indent=4)
        
        return AnswerModifier(Answer)
    except Exception as e:
        raise e

def try_huggingface_api(Query):
    """Try Hugging Face Inference API"""
    try:
        if not HuggingFaceAPIKey:
            return None
            
        API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.1"

        headers = {"Authorization": f"Bearer {HuggingFaceAPIKey}"}
        
        prompt = f"User: {Query}\nAssistant:"
        
        response = requests.post(
            API_URL, 
            headers=headers, 
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 200,
                    "temperature": 0.7,
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return str(result[0])[:500]
            return str(result)[:500]
        
        print(f"❌ HuggingFace API error: {response.status_code}")
        return None
        
    except Exception as e:
        print(f"❌ HuggingFace error: {e}")
        return None

def try_cohere_api(Query):
    """Try Cohere API as last resort"""
    try:
        if not CohereAPIKey:
            return None
            
        import cohere
        co_client = cohere.Client(api_key=CohereAPIKey)
        
        response = co_client.generate(
            prompt=Query,
            max_tokens=200,
            temperature=0.7,
        )
        
        return response.generations[0].text
        
    except Exception as e:
        print(f"❌ Cohere error: {e}")
        return None

def try_ollama_local(Query):
    """Use local Ollama"""
    try:
        import requests
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": Query,
                "stream": False
            },
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        return None
    except:
        return None

def ChatBot(Query):
    """This function sends the user's query to the chatbot and returns the AI's response."""
    
    query_lower = Query.lower().strip()
    
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

    if query_lower in cached_responses:
        print("📦 Using cached response (instant)")
        return cached_responses[query_lower]

    errors = []
    
    print("🖥️ Trying Local Ollama...")
    ollama_response = try_ollama_local(Query)
    if ollama_response:
        return ollama_response
    else:
        errors.append("Ollama: No response")
    
    if groq_clients:
        try:
            print("🔄 Trying Groq API (multiple keys)...")
            return try_groq_api(Query)
        except Exception as e:
            error_msg = str(e)
            errors.append(f"Groq: {error_msg[:100]}")
            print(f"❌ Groq failed: {error_msg}")
    
    if gemini_client:
        try:
            print("🔄 Trying Gemini API...")
            return try_gemini_api(Query)
        except Exception as e:
            errors.append(f"Gemini: {str(e)[:100]}")
            print(f"❌ Gemini failed: {e}")
    
    print("🔄 Trying HuggingFace API...")
    hf_response = try_huggingface_api(Query)
    if hf_response:
        return hf_response
    else:
        errors.append("HuggingFace: No response")
    
    print("🔄 Trying Cohere API...")
    cohere_response = try_cohere_api(Query)
    if cohere_response:
        return cohere_response
    else:
        errors.append("Cohere: No response")
    
    return f"All AI services are currently unavailable. Please try again later."

if __name__ == "__main__":
    print(f"🤖 {Assistantname} ChatBot - Testing Mode")
    print(f"Loaded {len(groq_clients)} Groq API keys")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        if user_input:
            response = ChatBot(user_input)
            print(f"{Assistantname}: {response}")