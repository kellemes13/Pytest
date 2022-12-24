timeout /t 100

:TEST Py
@echo ============= gen  linux bin !!!!===============
cd C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\build
python test.py 
@echo===========gen git diff script===================
cd ..
git status > gitdiff.txt
python build\ProcessDiff.py
copy uploadftp.bat  build\WinSCPPortable
@echo ============= bin Xfer to FTP !!!!==============
rem WinSCPPortable\WinSCP.com /script=WinSCPPortable\test.bat
cd build
WinSCPPortable\WinSCP.com /script=WinSCPPortable\uploadftp.bat
set /p input=enter:
