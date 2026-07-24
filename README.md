# 🩺 AI Medicine Reminder & Health Assistant (Agentic AI)

An **Agentic AI-powered Medicine Reminder & Health Assistant** built using **LangGraph, LangChain, Ollama, RAG, FAISS, YOLOv8, MCP, and Voice AI**.

This project creates an intelligent healthcare assistant that can understand user queries, provide medicine information, manage reminders, detect medicines from images, and support voice-based interaction.

---

# 🚀 Features

✅ Agentic AI Multi-Agent System  
✅ Medicine Information Assistant  
✅ Medicine Reminder System  
✅ RAG-based Medical Knowledge Retrieval  
✅ FAISS Vector Database  
✅ Medicine Image Detection using YOLOv8  
✅ Voice Assistant  
✅ MCP Tool Integration  
✅ Gradio Dashboard  

---

# 🏗️ System Architecture

```
                              USER
                                |
          -----------------------------------------
          |                  |                    |
          ↓                  ↓                    ↓

     Text Input        Image Input          Voice Input

          |                  |                    |
          ↓                  ↓                    ↓

    LangGraph Agent      YOLOv8 Model      Speech Model
          |              Medicine           Processing
          |              Detection
          |
          ↓

      Router Agent

          |
  ------------------------------------------------
  |                 |              |              |
  ↓                 ↓              ↓              ↓

Reminder Agent  Medicine Agent  Health Agent  Emergency Agent

          |
          ↓

        Ollama LLM + RAG + MCP Tools

          |
          ↓

       Final AI Response

          |
          ↓

       Gradio Dashboard
```

---

# 📂 Project Structure

```
AI-Medicine-Assistant/

│
├── ai-agents/
│   ├── 01-chatbot.ipynb
│   ├── 02-mcp-tools.ipynb
│   ├── 02-mcp-pydantic.ipynb
│   ├── 03-mcp-router.ipynb
│   ├── aup_config.py
│   ├── math_server.py
│   ├── Medicine MCP Server.py
│   └── README.md
│
├── medicine_data/
│   ├── medicine_info.txt
│   └── README.md
│
├── rag/
│   ├── medicine_faiss/
│   │   ├── index.faiss
│   │   └── index.pkl
│   │
│   ├── 00-chatbot-norag.ipynb
│   ├── 01-rag-chunking.ipynb
│   ├── 02-rag-prompts.ipynb
│   ├── 03-rag-pipeline-HyDE.ipynb
│   ├── aup_config.py
│   └── README.md
│
├── training_model/
│   ├── medicine_dataset/
│   │   ├── images/
│   │   │   ├── train/
│   │   │   │   ├── aspirin.jpg
│   │   │   │   └── paracetamol.jpg
│   │   │   │
│   │   │   └── val/
│   │   │       └── paracetamol.jpg
│   │   │
│   │   ├── labels/
│   │   └── data.yaml
│   │
│   ├── runs/
│   │   └── detect/
│   │
│   ├── Medicine Detection using YOLOv8.ipynb
│   ├── medicine.yaml
│   ├── yolov8n.pt
│   └── Voice Assistant.ipynb
│
└── README.md
```

---

# 🛠️ Technologies Used

## AI & LLM

- LangGraph
- LangChain
- Ollama
- Llama 3.1 8B
- MCP (Model Context Protocol)

## Retrieval Augmented Generation

- FAISS Vector Database
- Embeddings
- Medical Knowledge Retrieval

## Computer Vision

- YOLOv8
- OpenCV
- Image Detection

## Voice AI

- Speech Recognition
- Text-to-Speech

## Dashboard

- Gradio

---

# 🤖 AI Agent Architecture

## Router Agent

Classifies user requests and forwards them to the correct agent.

## Medicine Agent

Provides:
- Medicine information
- Uses
- Side effects
- Drug details

Uses:
- LLM
- RAG Pipeline
- FAISS Retrieval

## Reminder Agent

Handles:
- Medicine schedules
- Reminder requests

## Health Agent

Provides general health guidance.

## Emergency Agent

Handles emergency-related queries.

---

# 📚 RAG Pipeline

Folder:

```
rag/
```

RAG improves response accuracy by retrieving information from medical documents.

Workflow:

```
Medicine Documents
        |
        ↓
Text Chunking
        |
        ↓
Embedding Generation
        |
        ↓
FAISS Vector Database
        |
        ↓
Retriever
        |
        ↓
LLM Response
```

Knowledge Source:

```
medicine_data/medicine_info.txt
```

---

# 🔍 Medicine Detection using YOLOv8

YOLOv8 detects medicines from uploaded images.

Workflow:

```
Medicine Image
        |
        ↓
Image Processing
        |
        ↓
YOLOv8 Model
        |
        ↓
Medicine Detection
        |
        ↓
Medicine Information
```

Model:

```
yolov8n.pt
```

---

# 🎙️ Voice Assistant

Voice module provides:

- Voice input
- Speech recognition
- AI response generation
- Voice output

Notebook:

```
training_model/Voice Assistant.ipynb
```

---

# ⚙️ Installation

Create environment:

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

# ▶️ Running Ollama

Check models:

```bash
ollama list
```

Run model:

```bash
ollama run llama3.1:8b
```

Start Ollama:

```bash
ollama serve
```

---

# ▶️ Running Agentic AI

Open:

```
ai-agents/03-mcp-router.ipynb
```

Run all cells.

The LangGraph Medicine Assistant will start.

---

# ▶️ Running RAG System

Open:

```
rag/03-rag-pipeline-HyDE.ipynb
```

Run notebook to retrieve medicine information using FAISS.

---

# ▶️ Running Medicine Detection

Open:

```
training_model/Medicine Detection using YOLOv8.ipynb
```

Run the notebook for medicine image detection.

---

# ▶️ Running Voice Assistant

Open:

```
training_model/Voice Assistant.ipynb
```

Run cells and interact using voice commands.

---

# 📌 Future Improvements

- Real-time medicine reminder notifications
- Mobile application
- User health profile management
- Medicine expiry detection
- Doctor consultation integration
- SOS emergency calling
- Multi-language voice support

---

# ⚠️ Disclaimer

This project is an AI healthcare assistant prototype.

It provides informational support and does not replace professional medical advice, diagnosis, or treatment.

Always consult healthcare professionals for medical decisions.

---

# ⭐ Project Highlights

✔ Agentic AI Healthcare Assistant  
✔ LangGraph Multi-Agent Architecture  
✔ Ollama Local LLM  
✔ RAG + FAISS Medical Retrieval  
✔ MCP Tool Integration  
✔ YOLOv8 Medicine Detection  
✔ Voice Assistant  
✔ Gradio Dashboard  

---

# 🎯 Project Goal

To build an intelligent AI healthcare assistant that combines **Agentic AI, RAG, Computer Vision, and Voice Technology** to provide personalized medicine support and healthcare assistance.
