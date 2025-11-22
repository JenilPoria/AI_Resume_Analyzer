@echo off
echo Starting FastAPI server...
start cmd /k "uvicorn backend.main:app --reload"

timeout /t 5 >nul

echo Starting Streamlit app...
start cmd /k "streamlit run main.py"
