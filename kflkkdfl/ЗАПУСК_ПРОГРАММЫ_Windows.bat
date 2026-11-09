@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  python "app_v02_готовая.py"
) else (
  py "app_v02_готовая.py"
)
if errorlevel 1 pause
