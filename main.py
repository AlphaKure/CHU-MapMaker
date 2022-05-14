import module

import pyfiglet
import ujson
from colorama import Fore
import os

def GetContent(lang):
    try:
        with open('lang/'+lang+'.json','r',encoding='utf-8')as f:
            return ujson.loads(f.read())
    except:
        print(Fore.RED+'This language is not supported!'+Fore.RESET)
        return ''


def Main():

    os.system('cls')
    #content read
    Content=GetContent(module.cross.getconfig('lang','lang'))
    if Content=='':
        os.system('pause')
        return
    while True:
        #logo
        print(pyfiglet.figlet_format("CHU-MapMaker",font="slant"))
        print(Fore.GREEN+Content['Cross']['Menu']['Welcome']+'\n'+Fore.RESET)
        print(Fore.GREEN+Content['Cross']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Cross']['Menu']['Help']+Fore.RESET)
        for i in range(0,6):
            print(Fore.GREEN+Content['Cross']['Menu']['Type_'+str(i)]+Fore.RESET)
        Cmd=int(input(Fore.GREEN+'>'+Fore.RESET))
        if Cmd>5:
            continue
        elif Cmd==5:
            print(Fore.GREEN+'[INFO] See you next time!'+Fore.RESET)
            os.system('pause')
            return
        elif Cmd==0:
            module.Reward.RewardM(Content)
        elif Cmd==1:
            module.MapBonus.MapBonusM(Content)
        elif Cmd==2:
            module.MapArea.MapAreaM(Content)
        elif Cmd==3:
            module.Map.MapM(Content)
        elif Cmd==4:
            module.Event.EventM(Content)



if __name__=='__main__'and module.cross.PathChk():
    Main()