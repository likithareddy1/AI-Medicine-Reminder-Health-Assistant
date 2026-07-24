# 🩺 AI Medicine Reminder & Health Assistant (Agentic AI)

An **Agentic AI-powered Healthcare Assistant** that helps users manage medicines through **AI chatbot, voice reminders, medicine image detection, and intelligent medical information retrieval**.

This project combines **LangGraph, LangChain, Ollama LLM, RAG, FAISS, YOLOv8, MCP (Model Context Protocol), Speech Recognition, Text-to-Speech, and Gradio** to build an intelligent medicine assistance system.

---

# 🚀 Features

✅ Agentic AI Multi-Agent System using LangGraph  
✅ AI Medicine Chatbot  
✅ Medicine Information Retrieval using RAG  
✅ FAISS Vector Database  
✅ Medicine Image Detection using YOLOv8  
✅ Voice-Based Medicine Reminder  
✅ Speech Recognition  
✅ Text-to-Speech Response  
✅ MCP Tool Integration  
✅ Ollama Local LLM  
✅ Gradio Interactive Dashboard  

---

# 🎯 Project Objective

The goal of this project is to build an intelligent AI healthcare assistant that helps users:

- Get medicine information
- Understand medicine usage and side effects
- Identify medicines from images
- Set medicine reminders
- Receive voice notifications
- Interact with AI through voice and text

---

# 🏗️ System Architecture

```
                           USER
                             |
        --------------------------------------------
        |                    |                     |
        ↓                    ↓                     ↓

   Text Input          Image Input           Voice Input

        |                    |                     |
        ↓                    ↓                     ↓

   LangGraph             YOLOv8          Speech Recognition
    Agent              Detection          Speech-to-Text

                             |
                             ↓

                       Router Agent

                             |
       ------------------------------------------------
       |                  |             |              |
       ↓                  ↓             ↓              ↓

 Reminder Agent   Medicine Agent  Health Agent  Emergency Agent

       |                  |             |              |
       ------------------------------------------------

                             |
                             ↓

              Ollama LLM + RAG + MCP Tools

                             |
                             ↓

                    Final AI Response

                             |
              --------------------------------
              |                              |
              ↓                              ↓

       Gradio Dashboard              Text-to-Speech

                                             |
                                             ↓

                                  🔊 Voice Reminder
```

---

# 🔄 Voice Medicine Reminder Workflow

```
User Voice Command

        ↓

Speech Recognition

        ↓

Convert Speech to Text

        ↓

LangGraph Router Agent

        ↓

Reminder Agent

        ↓

Extract Medicine Name & Time

        ↓

Create Reminder

        ↓

Scheduled Notification

        ↓

Text-to-Speech

        ↓

🔊 Voice Medicine Reminder
```

Example:

```
User:
"Remind me to take Paracetamol at 9 PM"

AI:
"Reminder set successfully.
I will remind you to take Paracetamol at 9 PM."

At 9 PM:

"Hello!
It is time to take your Paracetamol medicine.
Stay healthy."
```

---

# 🤖 Agent Architecture

## Router Agent

The Router Agent analyzes user requests and routes them to the appropriate agent.

---

## Reminder Agent

Responsible for:

- Creating medicine reminders
- Managing reminder schedules
- Providing voice notifications

---

## Medicine Agent

Responsible for:

- Medicine information
- Usage details
- Side effects
- Drug-related questions

Uses:

- RAG
- FAISS
- Medical knowledge database

---

## Health Agent

Provides general health-related assistance.

---

## Emergency Agent

Handles emergency-related requests.

---

# 📚 RAG Pipeline

The Retrieval Augmented Generation system improves AI responses using medical knowledge.

```
Medicine Documents

        ↓

Text Chunking

        ↓

Embeddings Generation

        ↓

FAISS Vector Database

        ↓

Retriever

        ↓

Ollama LLM

        ↓

Final Answer
```

---

# 🔍 Medicine Detection using YOLOv8

YOLOv8 computer vision model is used to identify medicines from images.

Workflow:

```
Medicine Image

      ↓

YOLOv8 Model

      ↓

Medicine Detection

      ↓

Medicine Name

      ↓

Retrieve Medicine Information
```

---

# 🎙️ Voice Assistant

The voice module provides:

- Speech input
- Speech recognition
- AI response generation
- Voice output

Workflow:

```
Voice Input

    ↓

Speech Recognition

    ↓

AI Processing

    ↓

Response Generation

    ↓

Text-to-Speech

    ↓

Voice Output
```

---

# 🛠️ Technologies Used

## Artificial Intelligence

- LangGraph
- LangChain
- Ollama
- Llama 3.1 8B
- MCP

## Retrieval Augmented Generation

- FAISS
- Sentence Transformers
- Embeddings

## Computer Vision

- YOLOv8
- OpenCV
- Ultralytics

## Voice

- SpeechRecognition
- pyttsx3
- Text-to-Speech

## Interface

- Gradio

---

# 📂 Project Structure

```
AI-Medicine-Reminder-Health-Assistant

│
├── ai-agents
│   │
│   ├── 01-chatbot.ipynb
│   ├── 02-a-mcp-tools.ipynb
│   ├── 02-b-mcp-pydantic.ipynb
│   ├── 03-mcp-router.ipynb
│   ├── Medicine MCP Server.py
│   ├── aup_config.py
│   └── math_server.py
│
├── medicine_data
│   └── medicine_info.txt
│
├── rag
│   │
│   ├── medicine_faiss
│   │   ├── index.faiss
│   │   └── index.pkl
│   │
│   ├── 00.chatbot-norag.ipynb
│   ├── 01.rag-chunking.ipynb
│   ├── 02.rag-prompts.ipynb
│   └── 03.rag-pipeline-HyDE.ipynb
│
├── training_model
│   │
│   ├── Medicine Detection using YOLOv8.ipynb
│   ├── Voice Assistant.ipynb
│   ├── medicine.yaml
│   │
│   └── medicine_dataset
│       ├── images
│       ├── labels
│       └── data.yaml
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/likithareddy1/AI-Medicine-Reminder-Health-Assistant.git
```

Move into project:

```bash
cd AI-Medicine-Reminder-Health-Assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧠 Ollama Setup

Install Ollama.

Download Llama model:

```bash
ollama pull llama3.1:8b
```

Run Ollama:

```bash
ollama serve
```

Check models:

```bash
ollama list
```

---

# ▶️ Running the Project

## Run Agentic AI System

Open:

```
ai-agents/03-mcp-router.ipynb
```

Run all cells.

---

## Run RAG System

Open:

```
rag/03.rag-pipeline-HyDE.ipynb
```

---

## Run Medicine Detection

Open:

```
training_model/Medicine Detection using YOLOv8.ipynb
```

---

## Run Voice Assistant

Open:

```
training_model/Voice Assistant.ipynb
```

---

# ⚡ AMD Compute Usage

This project was developed using AMD GPU compute environment.

AMD ROCm acceleration was used for AI development and experimentation.

AMD compute helps in:

- Running AI model workloads
- Accelerating deep learning experiments
- Supporting local LLM inference
- Training and testing YOLOv8 models

Technologies used:

- AMD ROCm
- PyTorch
- Ollama
- YOLOv8

---

---

# 🔮 Future Improvements

- Mobile application
- Real-time medicine notifications
- Medicine expiry detection
- User health profile
- SOS emergency calling
- Doctor consultation integration
- Multi-language voice support

---

# ⚠️ Disclaimer

This project is an AI healthcare assistant prototype.

It provides informational support and does not replace professional medical advice, diagnosis, or treatment.

Always consult healthcare professionals for medical decisions.

---

# ⭐ Project Highlights

✔ Agentic AI Healthcare Assistant  
✔ LangGraph Multi-Agent System  
✔ Ollama Local LLM  
✔ RAG + FAISS Medical Retrieval  
✔ MCP Tool Integration  
✔ YOLOv8 Medicine Detection  
✔ Voice-Based Medicine Reminder  
✔ Speech AI Integration  
✔ Gradio Dashboard  

---

# 👩‍💻 Team Members

This project was developed as a team effort.

### Team Members

- **Likitha Reddy**  
- **Naveen**  
- **Thahiya**

GitHub:

https://github.com/likithareddy1
