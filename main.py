# -*- coding : utf-8-*-
# pyinstaller -F D:\DeskTop\CHU-MapMaker\main.py  --icon D:\DeskTop\CHU-MapMaker\favicon.ico
# pipreqs . --encoding=utf8 --force
import os
import sys
from typing import Dict

import art
import ujson
from colorama import Fore

import module


def GetContent(Lang)->Dict|bool:
    '''
    ## This program is used to read text json files.
    Transfer the text data into other modules.
    '''
    try:
        with open('./lang/'+Lang+'.json', 'r', encoding='utf-8')as File:
            Content = ujson.loads(File.read())
            module.substances.SetContent(Content) # To substances
            module.cross.SetContent(Content) # To cross
            return Content
    except:
        print(Fore.RED+'This language is not supported!'+Fore.RESET)
        return False


def Main():
    '''
    ## Main Program
    '''

    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear') # For Linux

    
    # Content read
    Content = GetContent(module.cross.GetConfig('lang', 'lang'))
    if Content == False:
        if sys.platform == 'win32':
            os.system('pause') # Fail
        return
    while True:
        # logo
        art.tprint('CHU-MapMaker')
        print(Fore.GREEN+Content['Cross']['Menu']['Welcome']+'\n'+Fore.RESET)
        print(Fore.GREEN+Content['Cross']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Cross']['Menu']['Help']+Fore.RESET)
        for Num in range(0, 6):
            print(Fore.GREEN+Content['Cross']['Menu']
                  ['Type_'+str(Num)]+Fore.RESET)
        Command = int(input(Fore.GREEN+'>'+Fore.RESET))
        if Command > 5:
            continue
        elif Command == 5:
            print(Fore.GREEN+'[INFO] See you next time!'+Fore.RESET)
            if sys.platform == 'win32':
                os.system('pause')
            return
        elif Command == 0:
            module.Reward.RewardM(Content) # Call Reward
        elif Command == 1:
            module.MapBonus.MapBonusM(Content) # Call MapBonus
        elif Command == 2:
            module.MapArea.MapAreaM(Content) # Call MapArea
        elif Command == 3:
            module.Map.MapM(Content) # Call Map
        elif Command == 4:
            module.Event.EventM(Content) # Call Event


if __name__ == '__main__' and module.cross.PathCheck():
    Main()
