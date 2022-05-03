from typing import Tuple
from bs4 import BeautifulSoup as BS
from colorama import Fore
from lxml import etree
import configparser
import os

def PathChk()->bool:
    _NowPath=os.getcwd().lower()
    if not 'chu-mapmaker' in _NowPath:
        print(Fore.RED+'[ERROR]System Path Error!'+Fore.RESET)
        os.system('pause')
        return False
    if _NowPath.endswith('\module'):
        os.chdir(_NowPath[:-7])
    return True

#我超懶
def tagM(data:str)->BS:
    _Tag=BS(data,'xml')
    return _Tag

def getstr(findkey:str,section:str,type:str,itemid:str)->Tuple[bool,str]:
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    _LibraryPath=_Config[section][type]
    for _dir in os.listdir(_LibraryPath):
        if not os.path.isdir(_LibraryPath+'/'+_dir):
            continue
        else:
            with open(_LibraryPath+'/'+_dir+'/'+type+'.xml','r',encoding='utf-8')as f:
                _dXml=BS(f.read(),'xml')
                f.close()
            if _dXml.find(findkey).id.string==itemid:
                return True,_dXml.find(findkey).str.string
    print(Fore.RED+f'[ERROR]Not find {itemid}'+Fore.RESET)
    os.system('pause')
    return False,' '

def checkconfig(section:str,type:str)->bool:
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    if _Config[section][type]:
        return True
    else:
        return False
    
def getconfig(section:str,type:str)->str:
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    if section=='SavePath':
        if _Config[section][type].endswith('/')or  _Config[section][type].endswith('\\'):
            return  _Config[section][type][:-1]
    return  _Config[section][type]


def XMLFormat(path:str)->None:
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(path, parser)
    tree.write(path, pretty_print=True,encoding='utf-8',xml_declaration=True)

    
def musicDif(id:int)->str:
    StrList=['Basic','Advanced','Expert','Master','Ultima','WorldsEnd']
    return StrList[id]

def mapFilter(id:str)->Tuple[str,str]:
    if id=='0':
        NewFilterStr='Collaboration'
        NewFilterData='イベント'
    elif id=='1':
        NewFilterStr='Current'
        NewFilterData='現行バージョン'
    elif id=='2':
        NewFilterStr='Sega'
        NewFilterData='ゲキチュウマイ'
    elif id=='3':
        NewFilterStr='Other'
        NewFilterData='過去バージョン'
    else:
        print(Fore.RED+'[ERROR]ID ERROR!'+Fore.RESET)
        os.system('pause')
        return
    return NewFilterStr,NewFilterData