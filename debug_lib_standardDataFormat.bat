@echo off
cd .\dist
cls
call .\lib_standardDataFormat.py >debug.log
call .\lib_standardDataFormat.py
pause
