@echo off
cd /d "%~dp0"
title UF2404 - Laboratorio interactivo
where py >nul 2>nul
if %errorlevel%==0 (
  py server.py
) else (
  python server.py
)
pause
