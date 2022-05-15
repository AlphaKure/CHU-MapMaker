from colorama import Fore

from module.cross import *

os.system('cls') #避免colorama錯誤

def EventM(Content):

    if not checkconfig('SavePath','EventPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']['No_Save_Path'].replace('%now%','Event')+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        #建立Xml資料
        _dXml=tagM('')

        #add data title
        _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
        _tTitle=tagM('<EventData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></EventData>')
        _dXml.append(_tXmlVer)
        _dXml.append(_tTitle)

        #add dataname ,name and netOpenName tags
        _tNetOpenName=tagM('<netOpenName><id>2100</id><str>v2_05 00_0</str><data /></netOpenName>')
        _sEventNum=input(Fore.GREEN+Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%','Event')+Fore.RESET)
        _sEventStr=input(Fore.GREEN+Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%','Event')+Fore.RESET)
        if not _sEventStr.endswith('  |マップフラグ1'):
            _sEventStr=_sEventStr+'  |マップフラグ1'
        _tName=tagM('<name><id>'+_sEventNum+'</id><str>'+_sEventStr+'</str><data/></name>')
        if len(_sEventNum)>8:
            print(Fore.RED+Content['Cross']['Error_Msg']['Num_Out_of_range'].replace('%now%','Event')+Fore.RESET)
            os.system('PAUSE')
            return
        while len(_sEventNum)!=8:
            _sEventNum='0'+_sEventNum
        _tDataName=tagM('<dataName>mapArea'+_sEventNum+'</dataName>')
        _dXml.EventData.append(_tDataName)
        _dXml.EventData.append(_tNetOpenName)
        _dXml.EventData.append(_tName)

        #ddsBannerTag
        if input(Fore.GREEN+Content['Event']['Input']['AddDdsBanner']+Fore.RESET).lower()=='y':
            _sDdsBannerId=input(Fore.GREEN+Content['Event']['Input']['DdsBannerID']+Fore.RESET)
            if checkconfig('AutoStr','ddsBanner'):
                _fFInd,_sDdsBannerStr=getstr('name','AutoStr','ddsBanner',_sDdsBannerId)
                if not _fFInd:
                    return
            else:
                _sDdsBannerStr=input(Fore.GREEN+Content['Event']['Input']['DdsBannerStr']+Fore.RESET)
        else:
            _sDdsBannerId='-1'
            _sDdsBannerStr='Invalid'
        _dXml.EventData.append(tagM('<ddsBannerName><id>'+_sDdsBannerId+'</id><str>'+_sDdsBannerStr+'</str><data /></ddsBannerName>'))

        #OtherTag add
        _dXml.EventData.append(tagM('<periodDispType>1</periodDispType>'))
        _dXml.EventData.append(tagM('<alwaysOpen>true</alwaysOpen>'))
        _dXml.EventData.append(tagM('<teamOnly>false</teamOnly>'))
        _dXml.EventData.append(tagM('<isKop>false</isKop>'))
        _dXml.EventData.append(tagM('<priority>0</priority>'))

        #substances tag
        _sMapId=input(Fore.GREEN+Content['Event']['Input']['MapID']+Fore.RESET)
        if checkconfig('AutoStr','map'):
            _fFInd,_sMapStr=getstr('name','AutoStr','map',_sMapId)
            if not _fFInd:
                return
        else:
            _sMapStr=input(Fore.GREEN+Content['Event']['Input']['MapStr']+Fore.RESET)
        _tSubstamces=tagM('<substances><type>2</type><flag><value>0</value></flag><information><informationType>0</informationType><informationDispType>0</informationDispType><mapFilterID><id>-1</id><str>Invalid</str><data /></mapFilterID><courseNames><list /></courseNames><text /><image><path /></image><movieName><id>-1</id><str>Invalid</str><data /></movieName><presentNames><list /></presentNames></information><map><tagText /><mapName><id>'+_sMapId+'</id><str>'+_sMapStr+'</str><data /></mapName><musicNames><list /></musicNames></map><music><musicType>0</musicType><musicNames><list /></musicNames></music><advertiseMovie><firstMovieName><id>-1</id><str>Invalid</str><data /></firstMovieName><secondMovieName><id>-1</id><str>Invalid</str><data /></secondMovieName></advertiseMovie><recommendMusic><musicNames><list /></musicNames></recommendMusic><release><value>0</value></release><course><courseNames><list /></courseNames></course><quest><questNames><list /></questNames></quest><duel><duelName><id>-1</id><str>Invalid</str><data /></duelName></duel><changeSurfBoardUI><value>0</value></changeSurfBoardUI><avatarAccessoryGacha><avatarAccessoryGachaName><id>-1</id><str>Invalid</str><data /></avatarAccessoryGachaName></avatarAccessoryGacha><rightsInfo><rightsNames><list /></rightsNames></rightsInfo><battleReward><battleRewardName><id>-1</id><str>Invalid</str><data /></battleRewardName></battleReward></substances>')
        _dXml.EventData.append(_tSubstamces)

        #print(_dXml.prettify())
        _sSavePath=getconfig('SavePath','EventPath')+'/Event'+_sEventNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        with open(_sSavePath+'/Event.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/Event.xml')
        print(Fore.GREEN+Content['Cross']['Output']['Xml_Make_Finish'].replace('%now%','Event')+Fore.RESET)
        os.system('PAUSE')
