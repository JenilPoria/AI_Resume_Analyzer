# AI Resume Analyzer

A full-stack application to analyze resumes against job descriptions using LLMs (Groq).

## Features
- **PDF & Text Input**: Upload a PDF resume or paste text directly.
- **AI Analysis**: Extracts insights, alignment scores, strengths, weaknesses, and keywords.
- **Interactive UI**: Built with Streamlit for a smooth user experience.
- **FastAPI Backend**: Robust backend handling the analysis logic.

## Prerequisites
- Python 3.9+
- [Groq API Key](https://console.groq.com/)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd AI_Resume_Analizer
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Setup**:
    Create a `.env` file in the root directory:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    BACKEND_URL=http://127.0.0.1:8000/process
    ```

## Usage

1.  **Start the Backend**:
    ```bash
    uvicorn backend.main:app --reload
    ```

2.  **Start the Frontend** (in a new terminal):
    ```bash
    streamlit run main.py
    ```

3.  Open your browser at `http://localhost:8501`.

## Project Structure
- `backend/`: FastAPI backend and API routes.
- `llm/`: Logic for interacting with Groq LLM.
- `main.py`: Streamlit frontend application.
