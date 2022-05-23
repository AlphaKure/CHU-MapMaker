from colorama import Fore

from module.cross import *
from module.substances import *


def MapM(Content):
    '''
    ## Used to create Map.xml
    '''
    if not CheckConfig('SavePath', 'MapPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'Map')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
        return
    else:
        # Create XML data
        XMLData = TagM('')

        # add data title
        TagXMLVer = TagM('<?xml version="1.0" encoding="utf-8"?>')
        TagTitle = TagM(
            '<MapData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapData>')
        XMLData.append(TagXMLVer)
        XMLData.append(TagTitle)

        # add dataname ,name and netDispPeriod tags
        MapNum = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%', 'Map')+Fore.RESET)
        MapStr = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'Map')+Fore.RESET)
        TagName = TagM('<name><id>'+MapNum+'</id><str>' +
                       MapStr+'</str><data/></name>')
        if len(MapNum) > 8:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Num_Out_of_range'].replace('%now%', 'Map')+Fore.RESET)
            if sys.platform == 'win32':
                os.system('PAUSE')
            return
        while len(MapNum) != 8:
            MapNum = '0'+MapNum
        TagNetDispPeriod = TagM('<netDispPeriod>false</netDispPeriod>')
        TagDataName = TagM('<dataName>map'+MapNum+'</dataName>')

        XMLData.MapData.append(TagDataName)
        XMLData.MapData.append(TagNetDispPeriod)
        XMLData.MapData.append(TagName)

        # maptype setup default=2(Maybe wrong) infinit map=1
        IsMapInfinit = input(
            Fore.GREEN+Content['Map']['Input']['IsMapInfinit']+Fore.RESET).lower()
        if IsMapInfinit == 'y':
            IsMapInfinit = '1'
        else:
            IsMapInfinit = '2'

        TagMapType = TagM('<mapType>'+IsMapInfinit+'</mapType>')
        XMLData.MapData.append(TagMapType)

        # mapFilter setting
        print(Fore.GREEN+Content['Map']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Map']['Menu']['Help']+Fore.RESET)
        for Num in range(0, 4):
            print(Fore.GREEN+Content['Map']['Menu']
                  ['Type_'+str(Num)]+Fore.RESET)
        MapFilterId = input(Fore.GREEN+'>'+Fore.RESET)
        MapFilterStr, MapFilterData = mapFilter(MapFilterId)
        TagMapFilterID = TagM('<mapFilterID><id>'+MapFilterId+'</id><str>' +
                              MapFilterStr+'</str><data>'+MapFilterData+'</data></mapFilterID>')
        XMLData.MapData.append(TagMapFilterID)

        # Other useless tag add
        XMLData.MapData.append(
            TagM('<categoryName><id>0</id><str>設定なし</str><data /></categoryName>'))
        XMLData.MapData.append(
            TagM('<timeTableName><id>-1</id><str>Invalid</str><data /></timeTableName>'))
        XMLData.MapData.append(TagM('<stopPageIndex>0</stopPageIndex>'))
        XMLData.MapData.append(TagM(
            '<stopReleaseEventName><id>-1</id><str>Invalid</str><data /></stopReleaseEventName>'))
        XMLData.MapData.append(TagM('<priority>0</priority>'))

        # add infos tag
        XMLData.MapData.append(TagM('<infos></infos>'))

        # add MapDataAreaInfo
        while True:
            MapDataAreaInfo = TagM('<MapDataAreaInfo></MapDataAreaInfo>')

            # mapArea
            TagMapArea = SubstanceTagMaker('Map', 'mapArea', 0)
            MapDataAreaInfo.MapDataAreaInfo.append(TagMapArea)

            # ddsMap
            TagDDSMap = SubstanceTagMaker('Map', 'ddsMap', 0)
            MapDataAreaInfo.MapDataAreaInfo.append(TagDDSMap)

            # music
            IsHard, TagMusic = SubstanceTagMaker('Map', 'music', 0)
            MapDataAreaInfo.MapDataAreaInfo.append(TagMusic)

            # reward
            TagReward = SubstanceTagMaker('Map', 'reward', 0)
            MapDataAreaInfo.MapDataAreaInfo.append(TagReward)

            # isHard
            MapDataAreaInfo.MapDataAreaInfo.append(
                TagM('<isHard>'+IsHard+'</isHard>'))

            #Page and index
            Page = input(
                Fore.GREEN+Content['Map']['Input']['MapAreaPage']+Fore.RESET)
            Index = input(
                Fore.GREEN+Content['Map']['Input']['MapAreaIndex']+Fore.RESET)
            if int(Index) > 8:
                print(Fore.RED+Content['Map']['Error_Msg']
                      ['Index_Out_Of_Range']+Fore.RESET)
            else:
                MapDataAreaInfo.MapDataAreaInfo.append(
                    TagM('<pageIndex>'+Page+'</pageIndex>'))
                MapDataAreaInfo.MapDataAreaInfo.append(
                    TagM('<indexInPage>'+Index+'</indexInPage>'))

                # requiredAchievementCount
                RequiredAchievementCount = input(
                    Fore.GREEN+'[INFO]Required Achievement Count.(Not enable enter->0)'+Fore.RESET)
                MapDataAreaInfo.MapDataAreaInfo.append(TagM(
                    '<requiredAchievementCount>'+RequiredAchievementCount+'</requiredAchievementCount>'))

                # gauge
                TagGauge = SubstanceTagMaker('Map', 'gauge', 0)
                MapDataAreaInfo.MapDataAreaInfo.append(TagGauge)

                XMLData.MapData.infos.append(MapDataAreaInfo)

            if input(Fore.GREEN+Content['Map']['Input']['Continue']+Fore.RESET).lower() == 'n':
                break

        # print(_dXml.prettify())
        SavePath = GetConfig('SavePath', 'MapPath')+'/map'+MapNum
        if not os.path.isdir(SavePath):
            os.mkdir(SavePath)

        with open(SavePath+'/Map.xml', 'w', encoding='utf-8')as File:
            File.write(str(XMLData))
            File.close()

        XMLFormat(SavePath+'/Map.xml')
        print(Fore.GREEN+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'Map')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
