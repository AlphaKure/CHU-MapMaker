from colorama import Fore

from cross import *
from substances import *


def MapBonusM():

    #NEW xml data
    _dXml=tagM('')

    #add datatitle tag
    _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
    _tDataTitle=tagM('<MapBonusData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapBonusData>')
    _dXml.append(_tXmlVer)
    _dXml.append(_tDataTitle)

    #add dataname and name tags
    _sMapBonusNum=input(Fore.GREEN+'[INFO]Enter custom MapBonusnum:'+Fore.RESET)
    _sMapBonusStr=input(Fore.GREEN+'[INFO]Enter custom MapBonusstr:'+Fore.RESET)
    _tName=tagM('<name><id>'+_sMapBonusNum+'</id><str>'+_sMapBonusStr+'</str><data/></name>')
    if len(_sMapBonusNum)>8:
        print(Fore.RED+'[ERROR] Data number should be less than 8 digits!'+Fore.RESET)
        os.system('PAUSE')
        return
    while len(_sMapBonusNum)!=8:
        _sMapBonusNum='0'+_sMapBonusNum
    _tdataName=tagM('<dataName>mapBonus'+_sMapBonusNum+'</dataName>')
    _dXml.MapBonusData.append(_tdataName)
    _dXml.MapBonusData.append(_tName)

    _tSubstances=tagM('<substances><list></list></substances>')
    _dXml.MapBonusData.append(_tSubstances)

    #新增四個MapBonusSubstancesData
    for i in range(0,4):
        _tMapBonusSubstanceData=tagM('<MapBonusSubstanceData><type>'+str(i*10)+'</type></MapBonusSubstanceData>')
        _dXml.MapBonusData.substances.list.append(_tMapBonusSubstanceData)

    _iCount=0
    _fFinish=False
    for NowTag in _dXml.find_all('MapBonusSubstanceData'):
        if not _fFinish:
            #choose 1 type of trigger
            print(Fore.RED+f'\n[WARNING]You can set up to 4 Bonuses, you have currently set {_iCount}.'+Fore.RESET)
            print(Fore.GREEN+'\n[INFO]What kind of bonus condiction that you want to add?')
            print(Fore.WHITE+'[0]Enter 0: chara')
            print(Fore.WHITE+'[1]Enter 1: charawork')
            print(Fore.WHITE+'[2]Enter 2: skill')
            print(Fore.WHITE+'[3]Enter 3: skillCategory')
            print(Fore.WHITE+'[4]Enter 4: music')
            print(Fore.WHITE+'[5]Enter 5: musicGenre')
            print(Fore.WHITE+'[6]Enter 6: musicWorks')
            print(Fore.WHITE+'[7]Enter 7: musicDif')
            print(Fore.WHITE+'[8]Enter 8: musicLv')
            print(Fore.RED+'[9]Enter 9: Finish!'+Fore.RESET)
            _iType=int(input(Fore.GREEN+'>'++Fore.RESET))
            if _iType>9:
                print(Fore.RED+'[ERROR] Out of range!'+Fore.RESET)
                return
            elif _iType==9:
                _fFinish=True
                NowTag.decompose()
            else:
                print(Fore.RED+'\n[WARNING]This tool is ONLY add for offical data. If you want to add custom data likes ddsMap or chara, etc. Please add custom data by yourself.'+Fore.RESET)
                #將type轉為正確值
                NowTag.type.string=str(_iType)
            
                #chara
                _tChara=SubstanceTagMaker('MapBonus','chara',_iType)
                NowTag.append(_tChara)

                #charaWorks
                _tCharaWorks=SubstanceTagMaker('MapBonus','charaWorks',_iType)
                NowTag.append(_tCharaWorks)

                #skill
                _tSkill=SubstanceTagMaker('MapBonus','skill',_iType)
                NowTag.append(_tSkill)

                #skillCategory
                _tSkillCategory=SubstanceTagMaker('MapBonus','skillCategory',_iType)
                NowTag.append(_tSkillCategory)

                #music
                _tMusic=SubstanceTagMaker('MapBonus','music',_iType)
                NowTag.append(_tMusic)

                #musicGenre
                _tMusicGenre=SubstanceTagMaker('MapBonus','musicGenre',_iType)
                NowTag.append(_tMusicGenre)

                #musicWorks
                _tMusicWorks=SubstanceTagMaker('MapBonus','musicWorks',_iType)
                NowTag.append(_tMusicWorks)

                #musicDif
                _tMusicDif=SubstanceTagMaker('MapBonus','musicDif',_iType)
                NowTag.append(_tMusicDif)

                #musicLv
                _tMusicLv=SubstanceTagMaker('MapBonus','musicLv',_iType)
                NowTag.append(_tMusicLv)
                
        #多餘刪除
        else:
            NowTag.decompose()

        _iCount=_iCount+1

    #print(_dXml.prettify())
    if not checkconfig('SavePath','MapBonusPath'):
        print(Fore.RED+'[ERROR] You didn\'t enter save path for MapBonus!'+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        _sSavePath=getconfig('SavePath','MapBonusPath')+'/MapBonus'+_sMapBonusNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/MapBonus.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/MapBonus.xml')
        print(Fore.GREEN+'\nFinish!!!'+Fore.RESET)
        os.system('PAUSE')

if __name__=='__main__':
    MapBonusM()
