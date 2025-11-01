@echo off
cd /d "%~dp0"
call .my_env/bin/activate
python3 src/main.py