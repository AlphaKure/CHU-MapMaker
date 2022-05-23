from colorama import Fore

from module.cross import *


def EventM(Content):
    '''
    ## Used to create Event.xml
    '''
    if not CheckConfig('SavePath', 'EventPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'Event')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
        return
    else:
        # Create a XML data.
        XMLData = TagM('')

        # add data title
        TagXmlVer = TagM('<?xml version="1.0" encoding="utf-8"?>')
        TagTitle = TagM(
            '<EventData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></EventData>')
        XMLData.append(TagXmlVer)
        XMLData.append(TagTitle)

        # add dataname ,name and netOpenName tags
        TagNetOpenName = TagM(
            '<netOpenName><id>2100</id><str>v2_05 00_0</str><data /></netOpenName>')
        EventNum = input(
            Fore.GREEN+Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%', 'Event')+Fore.RESET)
        EventStr = input(
            Fore.GREEN+Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'Event')+Fore.RESET)
        if not EventStr.endswith('  |マップフラグ1'):
            EventStr = EventStr+'  |マップフラグ1'
        TagName = TagM('<name><id>'+EventNum+'</id><str>' +
                      EventStr+'</str><data/></name>')
        if len(EventNum) > 8:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Num_Out_of_range'].replace('%now%', 'Event')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
            return
        while len(EventNum) != 8:
            EventNum = '0'+EventNum
        TagDataName = TagM('<dataName>mapArea'+EventNum+'</dataName>')
        XMLData.EventData.append(TagDataName)
        XMLData.EventData.append(TagNetOpenName)
        XMLData.EventData.append(TagName)

        # ddsBannerTag
        if input(Fore.GREEN+Content['Event']['Input']['AddDdsBanner']+Fore.RESET).lower() == 'y':
            DDSBannerId = input(
                Fore.GREEN+Content['Event']['Input']['DdsBannerID']+Fore.RESET)
            if CheckConfig('AutoStr', 'ddsBanner'):
                IsFInd, DDSBannerStr = GetStr(
                    'name', 'AutoStr', 'ddsBanner', DDSBannerId)
                if not IsFInd:
                    return
            else:
                DDSBannerStr = input(
                    Fore.GREEN+Content['Event']['Input']['DdsBannerStr']+Fore.RESET)
        else:
            DDSBannerId = '-1'
            DDSBannerStr = 'Invalid'
        XMLData.EventData.append(TagM('<ddsBannerName><id>'+DDSBannerId +
                               '</id><str>'+DDSBannerStr+'</str><data /></ddsBannerName>'))

        # OtherTag add
        XMLData.EventData.append(TagM('<periodDispType>1</periodDispType>'))
        XMLData.EventData.append(TagM('<alwaysOpen>true</alwaysOpen>'))
        XMLData.EventData.append(TagM('<teamOnly>false</teamOnly>'))
        XMLData.EventData.append(TagM('<isKop>false</isKop>'))
        XMLData.EventData.append(TagM('<priority>0</priority>'))

        # substances tag
        MapID = input(
            Fore.GREEN+Content['Event']['Input']['MapID']+Fore.RESET)
        if CheckConfig('AutoStr', 'map'):
            IsFInd, MapStr = GetStr('name', 'AutoStr', 'map', MapID)
            if not IsFInd:
                return
        else:
            MapStr = input(
                Fore.GREEN+Content['Event']['Input']['MapStr']+Fore.RESET)
        TagSubstances = TagM('<substances><type>2</type><flag><value>0</value></flag><information><informationType>0</informationType><informationDispType>0</informationDispType><mapFilterID><id>-1</id><str>Invalid</str><data /></mapFilterID><courseNames><list /></courseNames><text /><image><path /></image><movieName><id>-1</id><str>Invalid</str><data /></movieName><presentNames><list /></presentNames></information><map><tagText /><mapName><id>'+MapID+'</id><str>'+MapStr +
                            '</str><data /></mapName><musicNames><list /></musicNames></map><music><musicType>0</musicType><musicNames><list /></musicNames></music><advertiseMovie><firstMovieName><id>-1</id><str>Invalid</str><data /></firstMovieName><secondMovieName><id>-1</id><str>Invalid</str><data /></secondMovieName></advertiseMovie><recommendMusic><musicNames><list /></musicNames></recommendMusic><release><value>0</value></release><course><courseNames><list /></courseNames></course><quest><questNames><list /></questNames></quest><duel><duelName><id>-1</id><str>Invalid</str><data /></duelName></duel><changeSurfBoardUI><value>0</value></changeSurfBoardUI><avatarAccessoryGacha><avatarAccessoryGachaName><id>-1</id><str>Invalid</str><data /></avatarAccessoryGachaName></avatarAccessoryGacha><rightsInfo><rightsNames><list /></rightsNames></rightsInfo><battleReward><battleRewardName><id>-1</id><str>Invalid</str><data /></battleRewardName></battleReward></substances>')
        XMLData.EventData.append(TagSubstances)

        # print(_dXml.prettify())
        SavePath = GetConfig('SavePath', 'EventPath')+'/Event'+EventNum
        if not os.path.isdir(SavePath):
            os.mkdir(SavePath)
        with open(SavePath+'/Event.xml', 'w', encoding='utf-8')as File:
            File.write(str(XMLData))
            File.close()

        XMLFormat(SavePath+'/Event.xml')
        print(Fore.GREEN+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'Event')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
