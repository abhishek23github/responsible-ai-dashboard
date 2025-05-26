@echo off 

REM Activate virtual environment
call venv\Scripts\activate

REM Launch Streamlit app for LLM Prompt/Response
start cmd /k "streamlit run ui/ui_streamlit.py"

REM Launch Streamlit app for Dashboard/Visulization
start cmd /k "streamlit run ui/visualize.py"

exit