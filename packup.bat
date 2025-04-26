pyinstaller --hidden-import=live2d.v3 -D --windowed --icon=moeroid.ico Main.py -y

copy .\moeroid.ico .\dist\Main\moeroid.ico
