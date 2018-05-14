@echo off
python -m pip install --upgrade pip
pip install selenium
for /f "delims=" %%F in ('where python') do set pythonLoc=%%F
for /f "delims=" %%F in ('cd') do set geckopath=%%F\dependencies
for %%A in ("%pythonLoc%") do set pyScriptsFolder=%%~dpAScripts
echo.Copying geckodriver.exe from: %geckopath% to %pyScriptsFolder%
copy %geckopath%\geckodriver.exe %pyScriptsFolder%\geckodriver.exe
echo.Ready to run tool! (Hopefully anyways)
pause