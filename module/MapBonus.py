from colorama import Fore

from module.cross import *
from module.substances import *

os.system('cls') #避免colorama錯誤

def MapBonusM(Content):
    if not checkconfig('SavePath','MapBonusPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']['No_Save_Path'].replace('%now%','MapBonus')+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        #NEW xml data
        _dXml=tagM('')

        #add datatitle tag
        _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
        _tDataTitle=tagM('<MapBonusData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapBonusData>')
        _dXml.append(_tXmlVer)
        _dXml.append(_tDataTitle)

        #add dataname and name tags
        _sMapBonusNum=input(Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%','MapBonus')+Fore.RESET)
        _sMapBonusStr=input(Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%','MapBonus')+Fore.RESET)
        _tName=tagM('<name><id>'+_sMapBonusNum+'</id><str>'+_sMapBonusStr+'</str><data/></name>')
        if len(_sMapBonusNum)>8:
            print(Fore.RED+Content['Cross']['Error_Msg']['Num_Out_of_range'].replace('%now%','MapBonus')+Fore.RESET)
            os.system('PAUSE')
            return
        while len(_sMapBonusNum)!=8:
            _sMapBonusNum='0'+_sMapBonusNum
        _tdataName=tagM('<dataName>mapBonus'+_sMapBonusNum+'</dataName>')
        _dXml.MapBonusData.append(_tdataName)
        _dXml.MapBonusData.append(_tName)

        _tSubstances=tagM('<substances><list></list></substances>')
        _dXml.MapBonusData.append(_tSubstances)

        _iCount=0
        _fFinish=False
        while not _fFinish:
            #choose 1 type of trigger
            print(Fore.RED+Content['MapBonus']['Output']['Counter'].replace('%num%',str(_iCount))+Fore.RESET)
            print(Fore.GREEN+Content['MapBonus']['Menu']['Title']+Fore.RESET)
            print(Fore.GREEN+Content['MapBonus']['Menu']['Help']+Fore.RESET)
            for i in range(0,10):
                print(Fore.GREEN+Content['MapBonus']['Menu']['Type_'+str(i)]+Fore.RESET)
            _iType=int(input(Fore.GREEN+'>'+Fore.RESET))
            if _iType>9:
                print(Fore.RED+Content['Cross']['Error_Msg']['Type_Out_Of_Range']+Fore.RESET)
                return
            elif _iType==9:
                _fFinish=True
            else:
                _tMapBonusSubstanceData=tagM('<MapBonusSubstanceData><type></type></MapBonusSubstanceData>')
                
                #將type轉為正確值
                _tMapBonusSubstanceData.MapBonusSubstanceData.type.string=str(_iType)
            
                #chara
                _tChara=SubstanceTagMaker('MapBonus','chara',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tChara)

                #charaWorks
                _tCharaWorks=SubstanceTagMaker('MapBonus','charaWorks',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tCharaWorks)

                #skill
                _tSkill=SubstanceTagMaker('MapBonus','skill',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tSkill)

                #skillCategory
                _tSkillCategory=SubstanceTagMaker('MapBonus','skillCategory',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tSkillCategory)

                #music
                _tMusic=SubstanceTagMaker('MapBonus','music',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tMusic)

                #musicGenre
                _tMusicGenre=SubstanceTagMaker('MapBonus','musicGenre',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tMusicGenre)

                #musicWorks
                _tMusicWorks=SubstanceTagMaker('MapBonus','musicWorks',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tMusicWorks)

                #musicDif
                _tMusicDif=SubstanceTagMaker('MapBonus','musicDif',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tMusicDif)

                #musicLv
                _tMusicLv=SubstanceTagMaker('MapBonus','musicLv',_iType)
                _tMapBonusSubstanceData.MapBonusSubstanceData.append(_tMusicLv)
                
                _dXml.MapBonusData.substances.list.append(_tMapBonusSubstanceData)
                if _iCount==3:
                    _fFinish=True
                else:
                    _iCount=_iCount+1

        #print(_dXml.prettify())
        _sSavePath=getconfig('SavePath','MapBonusPath')+'/MapBonus'+_sMapBonusNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/MapBonus.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/MapBonus.xml')
        print(Fore.GREEN+Content['Cross']['Output']['Xml_Make_Finish'].replace('%now%','MapBonus')+Fore.RESET)
        os.system('PAUSE')

