# 🤖 SPINO AI - Intelligent Voice Assistant

<div align="center">

![SPINO AI Logo](Frontend/Graphics/images/Spino.gif)
*A multilingual AI assistant with image generation capabilities*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-brightgreen)](https://github.com/anand880441-source/SPINO-AI)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/anand880441-source/SPINO-AI)

*Multilingual • AI-Powered • Voice-Controlled • Image Generation*

</div>

## ✨ Features

### 🎤 **Voice Control**
- Real-time speech recognition
- Natural voice responses
- Voice command control (pause/resume/stop)
- Multilingual support (Hindi/English)

### 🖼️ **AI Image Generation**
- Generate images from text descriptions
- Uses HuggingFace AI models (Stable Diffusion)
- 4 images generated concurrently
- Automatic saving and opening
- Fallback models for reliability

### 🤖 **Smart Automation**
- Open/close applications
- Web search (Google, YouTube)
- System controls (volume, mute)
- Content writing (applications, letters, code)
- YouTube music playback

### 🌐 **Multilingual Interface**
- Real-time language switching
- Hindi and English support
- Context-aware responses
- Language usage tracking

### 💻 **Advanced Capabilities**
- Real-time web search
- Chat with multiple AI models (Groq, Gemini)
- File operations and management
- GUI with animated interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Windows OS (optimized for Windows 10/11)
- Microphone and speakers

### Installation

1. **Clone the repository**

git clone https://github.com/anand880441-source/SPINO-AI.git
cd SPINO-AI


## 🔧 Configuration

### API Keys Required:
1. **Groq API** - For AI conversations (up to 4 keys for load balancing)
2. **Gemini API** - Alternative AI model
3. **HuggingFace API** - For image generation

### Optional Features:
- Local Ollama support (for offline AI)
- Multiple Groq keys for rate limit handling
- Custom voice models

## 🎨 Features in Detail

### **Image Generation Pipeline:**
1. Voice command → "generate image of X"
2. Text processing → Clean prompt
3. HuggingFace API → Multiple model fallback
4. Image generation → 4 concurrent images
5. File handling → Save to Data/ folder
6. Automatic opening → Default image viewer

### **Voice Control System:**
- Real-time speech-to-text
- Command classification
- Context-aware responses
- Multilingual TTS engine
- Voice command interrupts

### **Automation Engine:**
- Application detection (desktop/web)
- System command execution
- File operations
- Web automation
- Content generation

## 📊 Performance

- **Response Time:** < 2 seconds for most commands
- **Image Generation:** 15-30 seconds for 4 images
- **Accuracy:** > 90% command recognition
- **Languages:** Hindi & English (easily extensible)

## 🔄 Development

### Adding New Features:
1. Add command handler in `Automation.py`
2. Update `Model.py` for command classification
3. Extend `TranslateAndExecute()` function
4. Test with voice commands

### Adding New Language:
1. Update `LanguageManager.py`
2. Add language prompts in `Chatbot.py`
3. Add TTS support for the language
4. Update GUI translations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for AI inference API
- **HuggingFace** for image generation models
- **Google** for Gemini AI
- **OpenAI** for inspiration
- **Python community** for amazing libraries

## 📞 Support

For issues, feature requests, or questions:
- Open an [Issue](https://github.com/anand880441-source/SPINO-AI/issues)
- Check existing discussions
- Review the documentation

---

<div align="center">

**Made with ❤️ by [Anand Suthar](https://github.com/anand880441-source)**

*"AI that understands, speaks, and creates"*

⭐ **Star this repo if you find it useful!** ⭐

</div>