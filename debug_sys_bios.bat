@echo off
cd .\dist
cls
call .\sys_bios.py >debug.log
call .\sys_bios.py
pause