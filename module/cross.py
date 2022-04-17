from base64 import encode
from encodings import utf_8
from bs4 import BeautifulSoup as BS
from lxml import etree
import configparser
import os

def tagM(data:str):
    _tag=BS(data,'xml')
    return _tag

def getstr(type:str,itemid:str):
    '''
    This is for reward
    '''
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    _LibraryPath=_Config['AutoStr'][type]
    for _dir in os.listdir(_LibraryPath):
        if not os.path.isdir(_LibraryPath+'/'+_dir):
            continue
        else:
            with open(_LibraryPath+'/'+_dir+'/'+type+'.xml','r',encoding='utf-8')as f:
                _dXml=BS(f.read(),'xml')
                f.close()
            if _dXml.find('name').id.string==itemid:
                return True,_dXml.find('name').str.string
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
    return _Config[section][type]

def XMLFormat(path:str):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(path, parser)
    tree.write(path, pretty_print=True,encoding='UTF-8')

    
    
