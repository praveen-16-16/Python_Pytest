@echo off

echo Checking if virtual environment exists...
if not exist "myenv\Scripts\activate" (
    echo   Creating one Virtual environment...
    python -m venv myenv
)

echo Activating virtual environment...
call myenv\Scripts\activate

echo Installing required packages...
call pip install pytest

echo Running pytest for all arithmetic tests...
call python -m pytest -s -v  

echo Deactivating virtual environment...
call myenv\Scripts\deactivate.bat

pause
