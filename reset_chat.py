import json
import os
import shutil

def reset_all():
    print("🔄 Resetting SPINO AI data...")
    
    chatlog_file = r"Data\ChatLog.json"
    if os.path.exists(chatlog_file):
        os.remove(chatlog_file)
        print("✅ Deleted ChatLog.json")
    
    chatbot_file = r"Data\Chatbot.json"
    if os.path.exists(chatbot_file):
        os.remove(chatbot_file)
        print("✅ Deleted Chatbot.json")
    
    config_file = "Frontend/Files/LanguageConfig.data"
    if os.path.exists(config_file):
        os.remove(config_file)
        print("✅ Deleted LanguageConfig.data")
    
    prompt_file = "Frontend/Files/LanguagePrompt.data"
    if os.path.exists(prompt_file):
        os.remove(prompt_file)
        print("✅ Deleted LanguagePrompt.data")
    
    os.makedirs("Frontend/Files", exist_ok=True)
    default_config = {
        "input_language": "hi-IN",
        "assistant_voice": "hi-IN-MadhurNeural",
        "current_language": "Hindi",
        "display_name": "Hindi"
    }
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(default_config, f, indent=2)
    print("✅ Created fresh LanguageConfig.data")
    
    os.makedirs("Data", exist_ok=True)
    with open(chatlog_file, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
    print("✅ Created fresh ChatLog.json")
    
    with open(chatbot_file, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
    print("✅ Created fresh Chatbot.json")
    
    print("\n🎯 Reset complete! Now:")
    print("1. Run Backend/LanguageManager.py once")
    print("2. Then run main.py")
    print("3. Say 'speak in english' to switch to English")

if __name__ == "__main__":
    reset_all()