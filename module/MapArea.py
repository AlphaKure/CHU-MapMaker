from colorama import Fore
from module.cross import *


def MapAreaM(Content):
    '''
    ## Used to create MapArea.xml
    '''
    if not CheckConfig('SavePath', 'MapAreaPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'MapArea')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
        return
    else:
        # Create XML data 
        XMLData = TagM('')

        # add data title
        TagXMLVer = TagM('<?xml version="1.0" encoding="utf-8"?>')
        TagTitle = TagM(
            '<MapAreaData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapAreaData>')
        XMLData.append(TagXMLVer)
        XMLData.append(TagTitle)

        # add dataname ,name and netOpenName tags
        TagNetOpenName = TagM(
            '<netOpenName><id>2100</id><str>v2_05 00_0</str><data /></netOpenName>')
        MapAreaNum = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%', 'MapArea')+Fore.RESET)
        MapAreaStr = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'MapArea')+Fore.RESET)
        Name = TagM('<name><id>'+MapAreaNum+'</id><str>' +
                      MapAreaStr+'</str><data/></name>')
        if len(MapAreaNum) > 8:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Num_Out_of_range'].replace('%now%', 'MapBonus')+Fore.RESET)
            if sys.platform == 'win32':
                os.system('PAUSE')
            return
        while len(MapAreaNum) != 8:
            MapAreaNum = '0'+MapAreaNum
        TagDataName = TagM('<dataName>mapArea'+MapAreaNum+'</dataName>')
        XMLData.MapAreaData.append(TagDataName)
        XMLData.MapAreaData.append(TagNetOpenName)
        XMLData.MapAreaData.append(Name)

        # mapBonus tag
        MapBonusID = input(
            Fore.GREEN+Content['MapArea']['Input']['MapBonus_ID']+Fore.RESET)
        if CheckConfig('AutoStr', 'mapBonus'):
            IsFInd, MapBonusStr = GetStr(
                'name', 'AutoStr', 'mapBonus', MapBonusID)
            if not IsFInd:
                return
        else:
            MapBonusStr = input(
                Fore.GREEN+Content['MapArea']['Input']['MapBonus_Str']+Fore.RESET)
        TagMapBonusName = TagM('<mapBonusName><id>'+MapBonusID +
                              '</id><str>'+MapBonusStr+'</str><data /></mapBonusName>')
        XMLData.MapAreaData.append(TagMapBonusName)

        # add MapBoost tags
        MapAreaBoostType = input(
            Fore.GREEN+Content['MapArea']['Input']['Enable_Boost']+Fore.RESET).lower()
        if MapAreaBoostType == 'y':
            MapAreaBoostType = '1'
            MapAreaBoostMultiple = str(int(float(input(
                Fore.GREEN+Content['MapArea']['Input']['Boost_Multiplier']+Fore.RESET))*10))
        else:
            MapAreaBoostType = '0'
            MapAreaBoostMultiple = '10'

        TagMapAreaBoostType = TagM(
            '<mapAreaBoostType>'+MapAreaBoostType+'</mapAreaBoostType>')
        TagMapAreaBoostMultiple = TagM(
            '<mapAreaBoostMultiple>'+MapAreaBoostMultiple+'</mapAreaBoostMultiple>')
        XMLData.MapAreaData.append(TagMapAreaBoostType)
        XMLData.MapAreaData.append(TagMapAreaBoostMultiple)

        # ShortenData
        TagShorteningGridCountList = TagM(
            '<shorteningGridCountList></shorteningGridCountList>')
        XMLData.MapAreaData.append(TagShorteningGridCountList)

        for Num in range(0, 8):
            TagMapAreaGridShorteningData = TagM(
                '<MapAreaGridShorteningData><count>'+str(Num)+'</count></MapAreaGridShorteningData>')
            XMLData.MapAreaData.shorteningGridCountList.append(
                TagMapAreaGridShorteningData)

        CountOfShoortenData = 0
        ShortenFlag = True
        for MapAreaGridShorteningData in XMLData.find_all('MapAreaGridShorteningData'):
            if ShortenFlag:
                ShortenGridCount = input(Fore.GREEN+Content['MapArea']['Input']['ShortenData'].replace(
                    '%Count%', str(CountOfShoortenData))+Fore.RESET)
                if ShortenGridCount == '-1':
                    ShortenFlag = False
                    MapAreaGridShorteningData.count.string = '0'
                else:
                    MapAreaGridShorteningData.count.string = ShortenGridCount
                CountOfShoortenData += 1
            else:
                MapAreaGridShorteningData.count.string = '0'

        # grid
        Endindex = int(
            input(Fore.GREEN+Content['MapArea']['Input']['MapArea_EndIndex']+Fore.RESET))
        # Start point
        TagMapAreaGridData = TagM(
            '<grids><MapAreaGridData><index>0</index><displayType>1</displayType><type>1</type><exit /><entrance /><reward><rewardName><id>-1</id><str>Invalid</str><data /></rewardName></reward></MapAreaGridData></grids>')
        XMLData.MapAreaData.append(TagMapAreaGridData)

        while True:
            RewardIndex = input(
                Fore.GREEN+Content['MapArea']['Input']['Other_Reward_Index']+Fore.RESET)
            if RewardIndex == '-1':
                break
            elif int(RewardIndex) > Endindex or int(RewardIndex) <= 0:
                print(Fore.RED+Content['MapArea']['Error_Msg']
                      ['Other_Reward_Index_Out_Of_Range']+Fore.RESET)
            else:
                RewardID = input(
                    Fore.GREEN+Content['MapArea']['Input']['Other_Reward_ID']+Fore.RESET)
                if CheckConfig('AutoStr', 'reward'):
                    IsFInd, RewardStr = GetStr(
                        'name', 'AutoStr', 'reward', MapBonusID)
                    if not IsFInd:
                        return
                else:
                    RewardStr = input(
                        Fore.GREEN+Content['MapArea']['Input']['Other_Reward_Str']+Fore.RESET)
                TagMapAreaGridData = TagM('<MapAreaGridData><index>'+RewardIndex+'</index><displayType>3</displayType><type>3</type><exit /><entrance /><reward><rewardName><id>' +
                                         RewardID+'</id><str>'+RewardStr+'</str><data /></rewardName></reward></MapAreaGridData>')
                XMLData.MapAreaData.grids.append(TagMapAreaGridData)

        # End Point
        TagMapAreaGridData = TagM('<MapAreaGridData><index>'+str(Endindex) +
                                 '</index><displayType>2</displayType><type>2</type><exit /><entrance /><reward><rewardName><id>-1</id><str>Invalid</str><data /></rewardName></reward></MapAreaGridData>')
        XMLData.MapAreaData.grids.append(TagMapAreaGridData)

        # print(_dXml.prettify())
        SavePath = GetConfig('SavePath', 'MapAreaPath') + \
            '/MapArea'+MapAreaNum
        if not os.path.isdir(SavePath):
            os.mkdir(SavePath)

        with open(SavePath+'/MapArea.xml', 'w', encoding='utf-8')as File:
            File.write(str(XMLData))
            File.close()

        XMLFormat(SavePath+'/MapArea.xml')
        print(Fore.GREEN+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'MapArea')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
