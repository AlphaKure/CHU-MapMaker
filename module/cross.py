from bs4 import BeautifulSoup as BS
import lxml
import configparser
import os

def tagM(data:str):
    _tag=BS(data,'xml')
    return _tag

def getstr(type:str,itemid:str):
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    _LibraryPath=_Config['AutoStr'][type+'Library']
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

def checkconfig(type:str):
    _Config=configparser.ConfigParser()
    _Config.read('config.ini')
    if _Config['AutoStr'][type+'Library']:
        return True
    else:
        return False
    


if __name__=='__main__':
    getstr('Ticket')
    
    
