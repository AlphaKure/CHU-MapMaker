from colorama import Fore
from cross import *

def MapAreaM():
    
    #建立Xml資料
    _dXml=tagM('')

    #add data title
    _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
    _tTitle=tagM('<MapAreaData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapAreaData>')
    _dXml.append(_tXmlVer)
    _dXml.append(_tTitle)

    #netOpenName


    #add dataname ,name and netOpenName tags
    _tNetOpenName=tagM('<netOpenName><id>2100</id><str>v2_05 00_0</str><data /></netOpenName>')
    _sMapAreaNum=input(Fore.GREEN+'[INFO]Enter custom MapAreanum:'+Fore.RESET)
    _sMapAreaStr=input(Fore.GREEN+'[INFO]Enter custom MapAreastr:'+Fore.RESET)
    _tName=tagM('<name><id>'+_sMapAreaNum+'</id><str>'+_sMapAreaStr+'</str><data/></name>')
    if len(_sMapAreaNum)>8:
        print(Fore.RED+'[ERROR] Data number should be less than 8 digits!'+Fore.RESET)
        os.system('PAUSE')
        return
    while len(_sMapAreaNum)!=8:
        _sMapAreaNum='0'+_sMapAreaNum
    _tDataName=tagM('<dataName>mapArea'+_sMapAreaNum+'</dataName>')
    _dXml.MapAreaData.append(_tDataName)
    _dXml.MapAreaData.append(_tNetOpenName)
    _dXml.MapAreaData.append(_tName)

    #mapBonus tag
    _sMapBonusId=input(Fore.GREEN+'[INFO]Enter the mapBonus ID.'+Fore.RESET)
    if checkconfig('AutoStr','mapBonus'):
        _fFInd,_sMapBonusStr=getstr('name','AutoStr','mapBonus',_sMapBonusId)
        if not _fFInd:
            return
    else:
        _sMapBonusStr=input(Fore.GREEN+'[INFO] Enter the mapBonus Str.'+Fore.RESET)
    _tMapBonusName=tagM('<mapBonusName><id>'+_sMapBonusId+'</id><str>'+_sMapBonusStr+'</str><data /></mapBonusName>')
    _dXml.MapAreaData.append(_tMapBonusName)

    #add MapBoost tags
    _sMapAreaBoostType=input(Fore.GREEN+'Do you want to enable boost?(y/n)'+Fore.RESET).lower()
    if _sMapAreaBoostType=='y':
        _sMapAreaBoostType='1'
        _sMapAreaBoostMultiple=str(int(float(input(Fore.GREEN+'Enter boost multiplier (ex:1.2)'+Fore.RESET))*10))
    else:
        _sMapAreaBoostType='0'
        _sMapAreaBoostMultiple='10'

    _tMapAreaBoostType=tagM('<mapAreaBoostType>'+_sMapAreaBoostType+'</mapAreaBoostType>')
    _tMapAreaBoostMultiple=tagM('<mapAreaBoostMultiple>'+_sMapAreaBoostMultiple+'</mapAreaBoostMultiple>')
    _dXml.MapAreaData.append(_tMapAreaBoostType)
    _dXml.MapAreaData.append(_tMapAreaBoostMultiple)


    #ShortenData
    _tShorteningGridCountList=tagM('<shorteningGridCountList></shorteningGridCountList>')
    _dXml.MapAreaData.append(_tShorteningGridCountList)

    for i in range(0,8):
        _tMapAreaGridShorteningData=tagM('<MapAreaGridShorteningData><count>'+str(i)+'</count></MapAreaGridShorteningData>')
        _dXml.MapAreaData.shorteningGridCountList.append(_tMapAreaGridShorteningData)
    
    _iCount=0
    _fShortenFlag=True
    for _Tag in  _dXml.find_all('MapAreaGridShorteningData'):
        if _fShortenFlag:
            _sCount=input(Fore.GREEN+f'[INFO]Enter the ShortenData of index {_iCount}(Enter -1 to exit.Fill with 0)'+Fore.RESET)
            if _sCount=='-1':
                _fShortenFlag=False
                _Tag.count.string='0'
            else:
                _Tag.count.string=_sCount
            _iCount+=1
        else:
            _Tag.count.string='0'
    
    #grid
    _iEndindex=int(input(Fore.GREEN+'Enter this MapArea end point.'+Fore.RESET))
    #Start point
    _tMapAreaGridData=tagM('<grids><MapAreaGridData><index>0</index><displayType>1</displayType><type>1</type><exit /><entrance /><reward><rewardName><id>-1</id><str>Invalid</str><data /></rewardName></reward></MapAreaGridData></grids>')
    _dXml.MapAreaData.append(_tMapAreaGridData)

    while True:
        print(Fore.RED+'[WARNING]This side only supports small official rewards, such as game points, etc. Please don\'t enter chara and other rewards to avoid unpredictable errors.'+Fore.RESET)
        _sRewardindex=input(Fore.GREEN+'Enter this MapArea reward points.(Enter -1 Finish add )'+Fore.RESET)
        if _sRewardindex=='-1':
            break
        elif int(_sRewardindex)>_iEndindex or int(_sRewardindex)<=0:
            print(Fore.RED+'[ERROR]Out of range!'+Fore.RESET)
        else:
            _sRewardId=input(Fore.GREEN+'[INFO] Input Reward Id.'+Fore.RESET)
            if checkconfig('AutoStr','reward'):
                _fFInd,_sRewardStr=getstr('name','AutoStr','reward',_sMapBonusId)
                if not _fFInd:
                    return
            else:
                _sRewardStr=input(Fore.GREEN+'[INFO] Enter the mapBonus Str.'+Fore.RESET)
            _tMapAreaGridData=tagM('<MapAreaGridData><index>'+_sRewardindex+'</index><displayType>3</displayType><type>3</type><exit /><entrance /><reward><rewardName><id>'+_sRewardId+'</id><str>'+_sRewardStr+'</str><data /></rewardName></reward></MapAreaGridData>')
            _dXml.MapAreaData.grids.append(_tMapAreaGridData)

    #End Point
    _tMapAreaGridData=tagM('<MapAreaGridData><index>'+str(_iEndindex)+'</index><displayType>2</displayType><type>2</type><exit /><entrance /><reward><rewardName><id>-1</id><str>Invalid</str><data /></rewardName></reward></MapAreaGridData>')
    _dXml.MapAreaData.grids.append(_tMapAreaGridData)


    #print(_dXml.prettify())
    if not checkconfig('SavePath','MapAreaPath'):
        print(Fore.RED+'[ERROR] You didn\'t enter save path for MapArea!'+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        _sSavePath=getconfig('SavePath','MapAreaPath')+'/MapArea'+_sMapAreaNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/MapArea.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/MapArea.xml')
        print(Fore.GREEN+'\nFinish!!!'+Fore.RESET)
        os.system('PAUSE')


if __name__=='__main__':
    MapAreaM()