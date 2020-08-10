# convierte los .ui del qt designer a .py
cd uis || exit
pyuic5 ui_main_window.ui -o ui_main_window.py
echo Done
