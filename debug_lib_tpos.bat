@echo off
cd .\dist
cls
call .\lib_tpos.py >debug.log
call .\lib_tpos.py
pause
