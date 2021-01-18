@echo off & title %~nx0 & color 0A & mode 160

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
echo Checking for Python...
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
echo Now opening the download URL.
start "" "https://www.python.org/downloads/windows/"
echo Press any key to continue after you have successfully installed. Remember to add python to PATH.
pause >nul
goto :DOES_PYTHON_EXIST

:PYTHON_DOES_EXIST
for /f "delims=" %%V in ('python -V') do @set ver=%%V
set ver2="%ver:~7,3%"
if %ver2% == "3.7" (goto :right_version) else (goto :wrong_version)

:wrong_version
echo Wrong Python version installed. You have %ver%, you need Python 3.7
echo Now opening the download URL.
start "" "https://www.python.org/downloads/windows/"
echo Press any key to continue after you have successfully installed. Remember to add python to PATH.
pause >nul
goto :DOES_PYTHON_EXIST

:right_version
echo Congrats, %ver% is installed...
goto :run_game

:run_game
echo Launching game...
python Engine.py
pause
goto :EOF
