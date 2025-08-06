import pyautogui, webbrowser
from time import sleep
idchannel = '750096327408484403'
idchanneltext = '750142299907948586'
webbrowser.open(f'https://discord.com/channels/{idchannel}/{idchanneltext}')

sleep(5)

with open('Automatizador de canciones/songs.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
       

