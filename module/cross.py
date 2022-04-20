from bs4 import BeautifulSoup as BS
from lxml import etree
import configparser
import os

def tagM(data:str):
    _tag=BS(data,'xml')
    return _tag

def getstr(findkey:str,section:str,type:str,itemid:str):
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
    print(f'[ERROR]Not find {itemid}')
    os.system('pause')
    return False,' '

def checkconfig(section:str,type:str):
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    if _Config[section][type]:
        return True
    else:
        return False
    
def getconfig(section:str,type:str):
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    if section=='SavePath':
        if _Config[section][type].endswith('/')or  _Config[section][type].endswith('\\'):
            return  _Config[section][type][:-1]
    return  _Config[section][type]


def XMLFormat(path:str):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(path, parser)
    tree.write(path, pretty_print=True,encoding='utf-8',xml_declaration=True)

    
def musicDif(id:int):
    StrList=['Basic','Advanced','Expert','Master','Ultima','WorldsEnd']
    return StrList[id]
