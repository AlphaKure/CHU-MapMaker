from colorama import Fore

from cross import *
from substances import *

def MapM():

     #建立Xml資料
    _dXml=tagM('')

    #add data title
    _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
    _tTitle=tagM('<MapData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapData>')
    _dXml.append(_tXmlVer)
    _dXml.append(_tTitle)

    #add dataname ,name and netDispPeriod tags
    _sMapNum=input(Fore.GREEN+'[INFO]Enter custom Map num:'+Fore.RESET)
    _sMapStr=input(Fore.GREEN+'[INFO]Enter custom Map str:'+Fore.RESET)
    _tName=tagM('<name><id>'+_sMapNum+'</id><str>'+_sMapStr+'</str><data/></name>')
    if len(_sMapNum)>8:
        print(Fore.RED+'[ERROR] Data number should be less than 8 digits!'+Fore.RESET)
        os.system('PAUSE')
        return
    while len(_sMapNum)!=8:
        _sMapNum='0'+_sMapNum
    _tNetDispPeriod=tagM('<netDispPeriod>false</netDispPeriod>')
    _tDataName=tagM('<dataName>map'+_sMapNum+'</dataName>')

    _dXml.MapData.append(_tDataName)
    _dXml.MapData.append(_tNetDispPeriod)
    _dXml.MapData.append(_tName)

    #maptype setup default=2(Maybe wrong) infinit map=1 
    _sIsMapInfinit=input(Fore.GREEN+'[INFO]Is this map infinit?(y/n)'+Fore.RESET).lower()
    if _sIsMapInfinit=='y':
        _sIsMapInfinit='1'
    else:
        _sIsMapInfinit='2'
    
    _tMapType=tagM('<mapType>'+_sIsMapInfinit+'</mapType>')
    _dXml.MapData.append(_tMapType)

    #mapFilter setting
    print(Fore.GREEN+'\n[0]Enter 0: Collaboration \n[1]Enter 1: Current \n[2]Enter 2: Sega \n[3]Enter 3: Other'+Fore.RESET)
    _sMapFilterId=input(Fore.GREEN+'[INFO]Enter custom Map Type:'+Fore.RESET)
    _sMapFilterStr,_sMapFilterData=mapFilter(_sMapFilterId)
    _tMapFilterID=tagM('<mapFilterID><id>'+_sMapFilterId+'</id><str>'+_sMapFilterStr+'</str><data>'+_sMapFilterData+'</data></mapFilterID>')
    _dXml.MapData.append(_tMapFilterID)

    #Other useless tag add
    _dXml.MapData.append(tagM('<categoryName><id>0</id><str>設定なし</str><data /></categoryName>'))
    _dXml.MapData.append(tagM('<timeTableName><id>-1</id><str>Invalid</str><data /></timeTableName>'))
    _dXml.MapData.append(tagM('<stopPageIndex>0</stopPageIndex>'))
    _dXml.MapData.append(tagM('<stopReleaseEventName><id>-1</id><str>Invalid</str><data /></stopReleaseEventName>'))
    _dXml.MapData.append(tagM('<priority>0</priority>'))

    #add infos tag
    _dXml.MapData.append(tagM('<infos></infos>'))

    _iIndex=0 
    _iPage=0

    #add MapDataAreaInfo 
    while True:
        _tMapDataAreaInfo=tagM('<MapDataAreaInfo></MapDataAreaInfo>')

        #mapArea
        _tMapArea=SubstanceTagMaker('Map','mapArea',0)
        _tMapDataAreaInfo.MapDataAreaInfo.append(_tMapArea)

        #ddsMap
        _tddsMap=SubstanceTagMaker('Map','ddsMap',0)
        _tMapDataAreaInfo.MapDataAreaInfo.append(_tddsMap)
        #music
        _sIsHard,_tMusic=SubstanceTagMaker('Map','music',0)
        _tMapDataAreaInfo.MapDataAreaInfo.append(_tMusic)

        #reward
        _tReward=SubstanceTagMaker('Map','reward',0)
        _tMapDataAreaInfo.MapDataAreaInfo.append(_tReward)

        #isHard
        _tMapDataAreaInfo.MapDataAreaInfo.append(tagM('<isHard>'+_sIsHard+'</isHard>'))

        #Page and index
        _tMapDataAreaInfo.MapDataAreaInfo.append(tagM('<pageIndex>'+str(_iPage)+'</pageIndex>'))
        _tMapDataAreaInfo.MapDataAreaInfo.append(tagM('<indexInPage>'+str(_iIndex)+'</indexInPage>'))

        #requiredAchievementCount
        _sRequiredAchievementCount=input(Fore.GREEN+'[INFO]Required Achievement Count.(Not enable enter->0)'+Fore.RESET)
        _tMapDataAreaInfo.MapDataAreaInfo.append(tagM('<requiredAchievementCount>'+_sRequiredAchievementCount+'</requiredAchievementCount>'))

        #gauge
        _tgauge=SubstanceTagMaker('Map','gauge',0)
        _tMapDataAreaInfo.MapDataAreaInfo.append(_tgauge)

        _dXml.MapData.infos.append(_tMapDataAreaInfo)

        if input(Fore.GREEN+'Continue add MapAreaInfo?(y/n)'+Fore.RESET).lower()=='n':
            break

        if _iIndex!=8:
            _iIndex+=1
        else:
            _iIndex=0
            _iPage+=1

    #print(_dXml.prettify())
    if not checkconfig('SavePath','MapPath'):
        print(Fore.RED+'[ERROR] You didn\'t enter save path for Map!'+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        _sSavePath=getconfig('SavePath','MapPath')+'/map'+_sMapNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/Map.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/Map.xml')
        print(Fore.GREEN+'\nFinish!!!'+Fore.RESET)
        os.system('PAUSE')
        
if __name__=='__main__':
    MapM()