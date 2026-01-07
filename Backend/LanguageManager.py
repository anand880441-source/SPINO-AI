import json
import os
import pickle
from datetime import datetime
from dotenv import dotenv_values

class EnhancedLanguageManager:
    def __init__(self):
        self.config_file = "Frontend/Files/LanguageConfig.data"
        self.history_file = "Frontend/Files/LanguageHistory.pkl"
        self.env_vars = dotenv_values(".env")
        self.ensure_files()
        self.language_stats = self.load_stats()
    
    def ensure_files(self):
        """Create necessary files"""
        os.makedirs("Frontend/Files", exist_ok=True)
        
        if not os.path.exists(self.config_file):
            default_config = {
                "input_language": "hi-IN",
                "assistant_voice": "hi-IN-MadhurNeural",
                "current_language": "Hindi",
                "display_name": "Hindi",
                "auto_detect": True,
                "preferred_language": "Hindi",
                "last_switch": datetime.now().isoformat(),
                "switch_count": {"Hindi": 0, "English": 0}
            }
            self.save_config(default_config)
    
    def save_config(self, config):
        """Save configuration"""
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def get_current_language(self):
        """Get current language with enhanced info"""
        config = self.load_config()
        
        config["total_switches"] = sum(config.get("switch_count", {"Hindi": 0, "English": 0}).values())
        config["most_used"] = max(config["switch_count"], key=config["switch_count"].get)
        config["usage_percentage"] = {
            lang: (count / config["total_switches"] * 100) if config["total_switches"] > 0 else 0
            for lang, count in config["switch_count"].items()
        }
        
        return config
    
    def load_config(self):
        """Load configuration"""
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return self.ensure_files() or self.load_config()
    
    def switch_language(self, target_language, user_preference=None):
        """Enhanced language switching with statistics"""
        languages = {
            "hindi": {
                "input_language": "hi-IN",
                "assistant_voice": "hi-IN-MadhurNeural",
                "display_name": "Hindi",
                "greeting": "नमस्ते! मैं हिंदी में उपलब्ध हूं।",
                "farewell": "शुभ रात्रि! फिर मिलेंगे।",
                "time_format": "%H:%M",
                "date_format": "%d/%m/%Y"
            },
            "english": {
                "input_language": "en-US",
                "assistant_voice": "en-CA-LiamNeural",
                "display_name": "English",
                "greeting": "Hello! I'm available in English.",
                "farewell": "Goodbye! See you soon.",
                "time_format": "%I:%M %p",
                "date_format": "%B %d, %Y"
            },
            "hindi_english": {
                "input_language": "hi-IN,en-US",
                "assistant_voice": "hi-IN-MadhurNeural",
                "display_name": "Mixed",
                "greeting": "Hello! नमस्ते! I can understand both Hindi and English.",
                "farewell": "Goodbye! अलविदा!",
                "time_format": "%H:%M",
                "date_format": "%d/%m/%Y"
            }
        }
        
        lang_key = target_language.lower()
        
        if lang_key in languages:
            config = self.load_config()
            old_lang = config.get("current_language", "Hindi")
            
            config["switch_count"][old_lang] = config["switch_count"].get(old_lang, 0)
            config["switch_count"][languages[lang_key]["display_name"]] = \
                config["switch_count"].get(languages[lang_key]["display_name"], 0) + 1
            
            config.update(languages[lang_key])
            config["current_language"] = languages[lang_key]["display_name"]
            config["last_switch"] = datetime.now().isoformat()
            config["user_preference"] = user_preference
            
            self.save_config(config)
            self.update_system_prompt(languages[lang_key]["display_name"])
            self.save_switch_history(old_lang, languages[lang_key]["display_name"])
            
            return {
                "success": True,
                "new_language": languages[lang_key]["display_name"],
                "greeting": languages[lang_key]["greeting"],
                "voice": languages[lang_key]["assistant_voice"]
            }
        
        return {"success": False, "error": "Language not supported"}
    
    def save_switch_history(self, from_lang, to_lang):
        """Save language switch history"""
        try:
            history = []
            if os.path.exists(self.history_file):
                with open(self.history_file, "rb") as f:
                    history = pickle.load(f)
            
            history.append({
                "timestamp": datetime.now().isoformat(),
                "from": from_lang,
                "to": to_lang,
                "duration": None  
            })
            
            if len(history) > 1:
                prev = history[-2]
                curr = history[-1]
                prev_time = datetime.fromisoformat(prev["timestamp"])
                curr_time = datetime.fromisoformat(curr["timestamp"])
                prev["duration"] = (curr_time - prev_time).total_seconds()
            
            with open(self.history_file, "wb") as f:
                pickle.dump(history[-100:], f) 
                
        except Exception as e:
            print(f"History save error: {e}")
    
    def update_system_prompt(self, language_name):
        """Enhanced system prompts with personality"""
        username = self.env_vars.get("Username", "Anand Suthar")
        assistantname = self.env_vars.get("Assistantname", "SPINO")
        
        prompts = {
            "Hindi": f"""तुम {assistantname} हो, एक उन्नत AI सहायक जो {username} की मदद करता है।

विशेषताएँ:
1. **बहुभाषी**: हिंदी में प्राथमिक, अंग्रेजी समझ सकते हो
2. **वास्तविक समय की जानकारी**: समय, तारीख, समाचार पहुँच
3. **संदर्भ जागरूक**: पिछली बातचीत याद रखते हो
4. **व्यक्तित्व**: मित्रवत, पेशेवर, मददगार

नियम:
- हिंदी में जवाब दो जब तक अंग्रेजी में न कहा जाए
- स्पष्ट और संक्षिप्त उत्तर दो
- वास्तविक समय की जानकारी शामिल करो जब प्रासंगिक हो
- पिछली बातचीत का संदर्भ याद रखो
- कभी भी "मैं एक AI हूं" न कहो

उदाहरण:
प्रश्न: "समय क्या है?"
उत्तर: "अभी समय रात के 9:30 बजे हैं।"

प्रश्न: "मौसम कैसा है?"
उत्तर: "वर्तमान मौसम की जानकारी के अनुसार..." """,
            
            "English": f"""You are {assistantname}, an advanced AI assistant helping {username}.

Features:
1. **Multilingual**: Primary in English, understands Hindi
2. **Real-time info**: Access to time, date, news
3. **Context aware**: Remembers previous conversation
4. **Personality**: Friendly, professional, helpful

Rules:
- Respond in English unless asked to use Hindi
- Provide clear and concise answers
- Include real-time information when relevant
- Remember context from previous conversations
- Never say "I am an AI"

Examples:
Question: "What time is it?"
Answer: "The current time is 9:30 PM."

Question: "How's the weather?"
Answer: "According to current weather information..." """,
            
            "Mixed": f"""You are {assistantname}, a bilingual AI assistant for {username}.

🌟 **Special Abilities**:
- Understands both Hindi and English seamlessly
- Auto-detects user's language preference
- Can code-switch naturally between languages
- Maintains context across language switches

📋 **Response Rules**:
1. Respond in the language of the question
2. If mixed language query, use the primary language
3. Keep answers concise but informative
4. Include emojis when appropriate (🎯, ✅, 🔥)
5. Remember user preferences across sessions

🎯 **Examples**:
Hindi: "समय बताओ" → "अभी 9:30 बजे हैं ⏰"
English: "Tell time" → "It's 9:30 PM ⏰"
Mixed: "Time batao" → "अभी 9:30 बजे हैं (It's 9:30 PM) ⏰" """
        }
        
        prompt = prompts.get(language_name, prompts["Hindi"])
        prompt_file = "Frontend/Files/LanguagePrompt.data"
        
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt)
    
    def get_language_stats(self):
        """Get detailed language statistics"""
        config = self.get_current_language()
        
        stats = {
            "current": config["current_language"],
            "preferred": config.get("preferred_language", "Hindi"),
            "auto_detect": config.get("auto_detect", True),
            "total_switches": config["total_switches"],
            "switch_counts": config["switch_count"],
            "usage_percentages": config["usage_percentage"],
            "most_used": config["most_used"],
            "last_switch": config["last_switch"],
            "voice": config["assistant_voice"]
        }
        
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, "rb") as f:
                    history = pickle.load(f)
                    stats["recent_switches"] = history[-5:]  
        except:
            stats["recent_switches"] = []
        
        return stats
    
    def auto_detect_language(self, text):
        """Auto-detect language from text"""
        hindi_chars = set("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
        english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        text_chars = set(text)
        
        hindi_count = len(text_chars.intersection(hindi_chars))
        english_count = len(text_chars.intersection(english_chars))
        
        if hindi_count > english_count:
            return "Hindi"
        elif english_count > hindi_count:
            return "English"
        else:
            return "Mixed"
    
    def load_stats(self):
        """Load and calculate statistics"""
        return {
            "total_queries": 0,
            "language_distribution": {"Hindi": 0, "English": 0, "Mixed": 0},
            "average_response_time": 0,
            "user_satisfaction": 0
        }
    
    def get_language_status(self):
        """Enhanced status with emojis"""
        config = self.get_current_language()
        current = config["current_language"]
        
        emojis = {
            "Hindi": "🇮🇳 हिंदी",
            "English": "🇺🇸 English", 
            "Mixed": "🌍 हिंदी+English"
        }
        
        return f"{emojis.get(current, '🌐')} | 🔄 {config['total_switches']} switches | ⭐ {config['most_used']} most used"

language_manager = EnhancedLanguageManager()

def switch_to_hindi(user_preference=None):
    return language_manager.switch_language("hindi", user_preference)

def switch_to_english(user_preference=None):
    return language_manager.switch_language("english", user_preference)

def switch_to_mixed():
    return language_manager.switch_language("hindi_english")

def get_current_language():
    return language_manager.get_current_language()

def get_language_status():
    return language_manager.get_language_status()

def get_language_stats():
    return language_manager.get_language_stats()

def auto_detect(text):
    return language_manager.auto_detect_language(text)

# import json
# import os
# import pickle
# from datetime import datetime
# from dotenv import dotenv_values

# class EnhancedLanguageManager:
#     def __init__(self):
#         self.config_file = "Frontend/Files/LanguageConfig.data"
#         self.history_file = "Frontend/Files/LanguageHistory.pkl"
#         self.env_vars = dotenv_values(".env")
#         self.ensure_files()
#         self.language_stats = self.load_stats()
    
#     def ensure_files(self):
#         """Create necessary files"""
#         os.makedirs("Frontend/Files", exist_ok=True)
        
#         if not os.path.exists(self.config_file):
#             default_config = {
#                 "input_language": "hi-IN",
#                 "assistant_voice": "hi-IN-MadhurNeural",
#                 "current_language": "Hindi",
#                 "display_name": "Hindi",
#                 "auto_detect": True,
#                 "preferred_language": "Hindi",
#                 "last_switch": datetime.now().isoformat(),
#                 "switch_count": {"Hindi": 0, "English": 0}
#             }
#             self.save_config(default_config)
    
#     def save_config(self, config):
#         """Save configuration"""
#         with open(self.config_file, "w", encoding="utf-8") as f:
#             json.dump(config, f, indent=2, ensure_ascii=False)
    
#     def get_current_language(self):
#         """Get current language with enhanced info"""
#         config = self.load_config()
        
#         # ⚠️ QUICK FIX APPLIED HERE ⚠️
#         # Ensure switch_count exists and has values
#         if "switch_count" not in config:
#             config["switch_count"] = {"Hindi": 0, "English": 0}
        
#         # Calculate total switches
#         config["total_switches"] = sum(config["switch_count"].values())
        
#         # Find most used language - handle empty/missing case
#         if config["switch_count"] and config["total_switches"] > 0:
#             try:
#                 config["most_used"] = max(config["switch_count"], key=config["switch_count"].get)
#             except:
#                 config["most_used"] = config.get("current_language", "Hindi")
#         else:
#             config["most_used"] = config.get("current_language", "Hindi")
        
#         # Calculate usage percentages
#         config["usage_percentage"] = {}
#         if config["total_switches"] > 0:
#             for lang, count in config["switch_count"].items():
#                 config["usage_percentage"][lang] = (count / config["total_switches"] * 100)
#         else:
#             # Default percentages
#             current = config.get("current_language", "Hindi")
#             config["usage_percentage"][current] = 100
#             for lang in ["Hindi", "English"]:
#                 if lang != current:
#                     config["usage_percentage"][lang] = 0
        
#         return config
    
#     def load_config(self):
#         """Load configuration"""
#         try:
#             with open(self.config_file, "r", encoding="utf-8") as f:
#                 config = json.load(f)
            
#             # Ensure all required keys exist
#             if "switch_count" not in config:
#                 config["switch_count"] = {"Hindi": 0, "English": 0}
            
#             return config
#         except:
#             return self.ensure_files() or self.load_config()
    
#     def switch_language(self, target_language, user_preference=None):
#         """Enhanced language switching with statistics"""
#         languages = {
#             "hindi": {
#                 "input_language": "hi-IN",
#                 "assistant_voice": "hi-IN-MadhurNeural",
#                 "display_name": "Hindi",
#                 "greeting": "नमस्ते! मैं हिंदी में उपलब्ध हूं।",
#                 "farewell": "शुभ रात्रि! फिर मिलेंगे।",
#                 "time_format": "%H:%M",
#                 "date_format": "%d/%m/%Y"
#             },
#             "english": {
#                 "input_language": "en-US",
#                 "assistant_voice": "en-CA-LiamNeural",
#                 "display_name": "English",
#                 "greeting": "Hello! I'm available in English.",
#                 "farewell": "Goodbye! See you soon.",
#                 "time_format": "%I:%M %p",
#                 "date_format": "%B %d, %Y"
#             },
#             "hindi_english": {
#                 "input_language": "hi-IN,en-US",
#                 "assistant_voice": "hi-IN-MadhurNeural",
#                 "display_name": "Mixed",
#                 "greeting": "Hello! नमस्ते! I can understand both Hindi and English.",
#                 "farewell": "Goodbye! अलविदा!",
#                 "time_format": "%H:%M",
#                 "date_format": "%d/%m/%Y"
#             }
#         }
        
#         lang_key = target_language.lower()
        
#         if lang_key in languages:
#             config = self.load_config()
#             old_lang = config.get("current_language", "Hindi")
            
#             # ⚠️ QUICK FIX: Ensure switch_count has the key
#             if old_lang not in config["switch_count"]:
#                 config["switch_count"][old_lang] = 0
            
#             new_lang_display = languages[lang_key]["display_name"]
#             if new_lang_display not in config["switch_count"]:
#                 config["switch_count"][new_lang_display] = 0
            
#             config["switch_count"][old_lang] = config["switch_count"].get(old_lang, 0)
#             config["switch_count"][new_lang_display] = config["switch_count"].get(new_lang_display, 0) + 1
            
#             config.update(languages[lang_key])
#             config["current_language"] = new_lang_display
#             config["last_switch"] = datetime.now().isoformat()
#             config["user_preference"] = user_preference
            
#             self.save_config(config)
#             self.update_system_prompt(new_lang_display)
#             self.save_switch_history(old_lang, new_lang_display)
            
#             return {
#                 "success": True,
#                 "new_language": new_lang_display,
#                 "greeting": languages[lang_key]["greeting"],
#                 "voice": languages[lang_key]["assistant_voice"]
#             }
        
#         return {"success": False, "error": "Language not supported"}
    
#     def save_switch_history(self, from_lang, to_lang):
#         """Save language switch history"""
#         try:
#             history = []
#             if os.path.exists(self.history_file):
#                 with open(self.history_file, "rb") as f:
#                     history = pickle.load(f)
            
#             history.append({
#                 "timestamp": datetime.now().isoformat(),
#                 "from": from_lang,
#                 "to": to_lang,
#                 "duration": None  
#             })
            
#             if len(history) > 1:
#                 prev = history[-2]
#                 curr = history[-1]
#                 prev_time = datetime.fromisoformat(prev["timestamp"])
#                 curr_time = datetime.fromisoformat(curr["timestamp"])
#                 prev["duration"] = (curr_time - prev_time).total_seconds()
            
#             with open(self.history_file, "wb") as f:
#                 pickle.dump(history[-100:], f) 
                
#         except Exception as e:
#             print(f"History save error: {e}")
    
#     def update_system_prompt(self, language_name):
#         """Enhanced system prompts with personality"""
#         username = self.env_vars.get("Username", "Anand Suthar")
#         assistantname = self.env_vars.get("Assistantname", "SPINO")
        
#         prompts = {
#             "Hindi": f"""तुम {assistantname} हो, एक उन्नत AI सहायक जो {username} की मदद करता है।

# विशेषताएँ:
# 1. **बहुभाषी**: हिंदी में प्राथमिक, अंग्रेजी समझ सकते हो
# 2. **वास्तविक समय की जानकारी**: समय, तारीख, समाचार पहुँच
# 3. **संदर्भ जागरूक**: पिछली बातचीत याद रखते हो
# 4. **व्यक्तित्व**: मित्रवत, पेशेवर, मददगार

# नियम:
# - हिंदी में जवाब दो जब तक अंग्रेजी में न कहा जाए
# - स्पष्ट और संक्षिप्त उत्तर दो
# - वास्तविक समय की जानकारी शामिल करो जब प्रासंगिक हो
# - पिछली बातचीत का संदर्भ याद रखो
# - कभी भी "मैं एक AI हूं" न कहो

# उदाहरण:
# प्रश्न: "समय क्या है?"
# उत्तर: "अभी समय रात के 9:30 बजे हैं।"

# प्रश्न: "मौसम कैसा है?"
# उत्तर: "वर्तमान मौसम की जानकारी के अनुसार..." """,
            
#             "English": f"""You are {assistantname}, an advanced AI assistant helping {username}.

# Features:
# 1. **Multilingual**: Primary in English, understands Hindi
# 2. **Real-time info**: Access to time, date, news
# 3. **Context aware**: Remembers previous conversation
# 4. **Personality**: Friendly, professional, helpful

# Rules:
# - Respond in English unless asked to use Hindi
# - Provide clear and concise answers
# - Include real-time information when relevant
# - Remember context from previous conversations
# - Never say "I am an AI"

# Examples:
# Question: "What time is it?"
# Answer: "The current time is 9:30 PM."

# Question: "How's the weather?"
# Answer: "According to current weather information..." """,
            
#             "Mixed": f"""You are {assistantname}, a bilingual AI assistant for {username}.

# 🌟 **Special Abilities**:
# - Understands both Hindi and English seamlessly
# - Auto-detects user's language preference
# - Can code-switch naturally between languages
# - Maintains context across language switches

# 📋 **Response Rules**:
# 1. Respond in the language of the question
# 2. If mixed language query, use the primary language
# 3. Keep answers concise but informative
# 4. Include emojis when appropriate (🎯, ✅, 🔥)
# 5. Remember user preferences across sessions

# 🎯 **Examples**:
# Hindi: "समय बताओ" → "अभी 9:30 बजे हैं ⏰"
# English: "Tell time" → "It's 9:30 PM ⏰"
# Mixed: "Time batao" → "अभी 9:30 बजे हैं (It's 9:30 PM) ⏰" """
#         }
        
#         prompt = prompts.get(language_name, prompts["Hindi"])
#         prompt_file = "Frontend/Files/LanguagePrompt.data"
        
#         with open(prompt_file, "w", encoding="utf-8") as f:
#             f.write(prompt)
    
#     def get_language_stats(self):
#         """Get detailed language statistics"""
#         config = self.get_current_language()
        
#         stats = {
#             "current": config["current_language"],
#             "preferred": config.get("preferred_language", "Hindi"),
#             "auto_detect": config.get("auto_detect", True),
#             "total_switches": config["total_switches"],
#             "switch_counts": config["switch_count"],
#             "usage_percentages": config["usage_percentage"],
#             "most_used": config["most_used"],
#             "last_switch": config["last_switch"],
#             "voice": config["assistant_voice"]
#         }
        
#         try:
#             if os.path.exists(self.history_file):
#                 with open(self.history_file, "rb") as f:
#                     history = pickle.load(f)
#                     stats["recent_switches"] = history[-5:]  
#         except:
#             stats["recent_switches"] = []
        
#         return stats
    
#     def auto_detect_language(self, text):
#         """Auto-detect language from text"""
#         hindi_chars = set("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
#         english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
#         text_chars = set(text)
        
#         hindi_count = len(text_chars.intersection(hindi_chars))
#         english_count = len(text_chars.intersection(english_chars))
        
#         if hindi_count > english_count:
#             return "Hindi"
#         elif english_count > hindi_count:
#             return "English"
#         else:
#             return "Mixed"
    
#     def load_stats(self):
#         """Load and calculate statistics"""
#         return {
#             "total_queries": 0,
#             "language_distribution": {"Hindi": 0, "English": 0, "Mixed": 0},
#             "average_response_time": 0,
#             "user_satisfaction": 0
#         }
    
#     def get_language_status(self):
#         """Enhanced status with emojis"""
#         config = self.get_current_language()
#         current = config["current_language"]
        
#         emojis = {
#             "Hindi": "🇮🇳 हिंदी",
#             "English": "🇺🇸 English", 
#             "Mixed": "🌍 हिंदी+English"
#         }
        
#         return f"{emojis.get(current, '🌐')} | 🔄 {config['total_switches']} switches | ⭐ {config['most_used']} most used"

# language_manager = EnhancedLanguageManager()

# def switch_to_hindi(user_preference=None):
#     return language_manager.switch_language("hindi", user_preference)

# def switch_to_english(user_preference=None):
#     return language_manager.switch_language("english", user_preference)

# def switch_to_mixed():
#     return language_manager.switch_language("hindi_english")

# def get_current_language():
#     return language_manager.get_current_language()

# def get_language_status():
#     return language_manager.get_language_status()

# def get_language_stats():
#     return language_manager.get_language_stats()

# def auto_detect(text):
#     return language_manager.auto_detect_language(text)