from typing import Tuple
import configparser
import os
import sys

from bs4 import BeautifulSoup as BS
from colorama import Fore
from lxml import etree


def PathCheck() -> bool:
    '''
    ## Check the user path to avoid the problem of not finding the data.
    '''

    global Content 

    NowPath = os.getcwd().lower()
    if not 'chu-mapmaker' in NowPath:
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['SystemPath_Error']+Fore.RESET)
        if sys.platform == 'win32':
            os.system('pause')
        return False
    if NowPath.endswith('\module'):
        os.chdir(NowPath[:-7])
    return True


def TagM(Data: str) -> BS:
    '''
    I am too lazy. LOL.
    '''
    Tag = BS(Data, 'xml')
    return Tag


def GetStr(TargetTag: str, Section: str, Type: str, ItemID: str) -> Tuple[bool, str]:
    '''
    ## Find the ID corresponding to Str program from various paths.

    FindKey: Target Tag Name.
    Section: ini Correspondence Section.
    Type: ini Correspondence name.
    ItemID: To find the ID of the corresponding str.
    '''
    global Content

    Config = configparser.ConfigParser()
    Config.read('config.ini')
    LibraryPath = Config[Section][Type]
    for Dir in os.listdir(LibraryPath):
        if not os.path.isdir(LibraryPath+'/'+Dir):
            continue
        else:
            # Open xml files to find
            with open(LibraryPath+'/'+Dir+'/'+Type+'.xml', 'r', encoding='utf-8')as File:
                XMLData = BS(File.read(), 'xml')
                File.close()
            if XMLData.find(TargetTag).id.string == ItemID:
                return True, XMLData.find(TargetTag).str.string  # Find Success
    print(Fore.RED+Content['Cross']['Error_Msg']
          ['Not_Found_ItemID'].replace('%id%', ItemID)+Fore.RESET)
    if sys.platform == 'win32':
        os.system('pause')
    return False, ' '  # Find Fail


def CheckConfig(Section: str, Type: str) -> bool:
    '''
    ## Used to check if the ini parameter is set or not.

    Section: ini Correspondence Section.
    Type: ini Correspondence name.
    '''
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    if Config[Section][Type]:
        return True
    else:
        return False


def GetConfig(Section: str, Type: str) -> str:
    '''
    ## Used to get ini parameter values.

    Section: ini Correspondence Section.
    Type: ini Correspondence name.
    '''
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    if Section == 'SavePath':
        if Config[Section][Type].endswith('/') or Config[Section][Type].endswith('\\'):
            return Config[Section][Type][:-1]
    return Config[Section][Type]


def XMLFormat(Path: str) -> None:
    '''
    ## Used to format XML.
    '''
    Parser = etree.XMLParser(remove_blank_text=True)
    Tree = etree.parse(Path, Parser)
    Tree.write(Path, pretty_print=True, encoding='utf-8', xml_declaration=True)


def musicDif(InputID: int) -> str:
    '''
    Input id. Return musicDif str.
    '''
    StrList = ['Basic', 'Advanced', 'Expert', 'Master', 'Ultima', 'WorldsEnd']
    return StrList[InputID]


def mapFilter(InputID: str) -> Tuple[str, str]:
    '''
    Input id. Return mapFilter str and data.
    '''
    global Content

    if InputID == '0':
        NewFilterStr = 'Collaboration'
        NewFilterData = 'イベント'
    elif InputID == '1':
        NewFilterStr = 'Current'
        NewFilterData = '現行バージョン'
    elif InputID == '2':
        NewFilterStr = 'Sega'
        NewFilterData = 'ゲキチュウマイ'
    elif InputID == '3':
        NewFilterStr = 'Other'
        NewFilterData = '過去バージョン'
    else:
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['MapFilter_ID_Error']+Fore.RESET)
        if sys.platform == 'win32':
            os.system('pause')
        return
    return NewFilterStr, NewFilterData


def SetContent(Data):
    '''
    Used to get text data.
    '''
    global Content
    Content = Data
