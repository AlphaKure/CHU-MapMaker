from colorama import Fore

from module.cross import *
from module.substances import *


def MapM(Content):
    if not checkconfig('SavePath', 'MapPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'Map')+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        # 建立Xml資料
        _dXml = tagM('')

        # add data title
        _tXmlVer = tagM('<?xml version="1.0" encoding="utf-8"?>')
        _tTitle = tagM(
            '<MapData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapData>')
        _dXml.append(_tXmlVer)
        _dXml.append(_tTitle)

        # add dataname ,name and netDispPeriod tags
        _sMapNum = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%', 'Map')+Fore.RESET)
        _sMapStr = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'Map')+Fore.RESET)
        _tName = tagM('<name><id>'+_sMapNum+'</id><str>' +
                      _sMapStr+'</str><data/></name>')
        if len(_sMapNum) > 8:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Num_Out_of_range'].replace('%now%', 'Map')+Fore.RESET)
            os.system('PAUSE')
            return
        while len(_sMapNum) != 8:
            _sMapNum = '0'+_sMapNum
        _tNetDispPeriod = tagM('<netDispPeriod>false</netDispPeriod>')
        _tDataName = tagM('<dataName>map'+_sMapNum+'</dataName>')

        _dXml.MapData.append(_tDataName)
        _dXml.MapData.append(_tNetDispPeriod)
        _dXml.MapData.append(_tName)

        # maptype setup default=2(Maybe wrong) infinit map=1
        _sIsMapInfinit = input(
            Fore.GREEN+Content['Map']['Input']['IsMapInfinit']+Fore.RESET).lower()
        if _sIsMapInfinit == 'y':
            _sIsMapInfinit = '1'
        else:
            _sIsMapInfinit = '2'

        _tMapType = tagM('<mapType>'+_sIsMapInfinit+'</mapType>')
        _dXml.MapData.append(_tMapType)

        # mapFilter setting
        print(Fore.GREEN+Content['Map']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Map']['Menu']['Help']+Fore.RESET)
        for i in range(0, 4):
            print(Fore.GREEN+Content['Map']['Menu']['Type_'+str(i)]+Fore.RESET)
        _sMapFilterId = input(Fore.GREEN+'>'+Fore.RESET)
        _sMapFilterStr, _sMapFilterData = mapFilter(_sMapFilterId)
        _tMapFilterID = tagM('<mapFilterID><id>'+_sMapFilterId+'</id><str>' +
                             _sMapFilterStr+'</str><data>'+_sMapFilterData+'</data></mapFilterID>')
        _dXml.MapData.append(_tMapFilterID)

        # Other useless tag add
        _dXml.MapData.append(
            tagM('<categoryName><id>0</id><str>設定なし</str><data /></categoryName>'))
        _dXml.MapData.append(
            tagM('<timeTableName><id>-1</id><str>Invalid</str><data /></timeTableName>'))
        _dXml.MapData.append(tagM('<stopPageIndex>0</stopPageIndex>'))
        _dXml.MapData.append(tagM(
            '<stopReleaseEventName><id>-1</id><str>Invalid</str><data /></stopReleaseEventName>'))
        _dXml.MapData.append(tagM('<priority>0</priority>'))

        # add infos tag
        _dXml.MapData.append(tagM('<infos></infos>'))

        # add MapDataAreaInfo
        while True:
            _tMapDataAreaInfo = tagM('<MapDataAreaInfo></MapDataAreaInfo>')

            # mapArea
            _tMapArea = SubstanceTagMaker('Map', 'mapArea', 0)
            _tMapDataAreaInfo.MapDataAreaInfo.append(_tMapArea)

            # ddsMap
            _tddsMap = SubstanceTagMaker('Map', 'ddsMap', 0)
            _tMapDataAreaInfo.MapDataAreaInfo.append(_tddsMap)

            # music
            _sIsHard, _tMusic = SubstanceTagMaker('Map', 'music', 0)
            _tMapDataAreaInfo.MapDataAreaInfo.append(_tMusic)

            # reward
            _tReward = SubstanceTagMaker('Map', 'reward', 0)
            _tMapDataAreaInfo.MapDataAreaInfo.append(_tReward)

            # isHard
            _tMapDataAreaInfo.MapDataAreaInfo.append(
                tagM('<isHard>'+_sIsHard+'</isHard>'))

            #Page and index
            _sPage = input(
                Fore.GREEN+Content['Map']['Input']['MapAreaPage']+Fore.RESET)
            _sIndex = input(
                Fore.GREEN+Content['Map']['Input']['MapAreaIndex']+Fore.RESET)
            if int(_sIndex) > 8:
                print(Fore.RED+Content['Map']['Error_Msg']
                      ['Index_Out_Of_Range']+Fore.RESET)
            else:
                _tMapDataAreaInfo.MapDataAreaInfo.append(
                    tagM('<pageIndex>'+_sPage+'</pageIndex>'))
                _tMapDataAreaInfo.MapDataAreaInfo.append(
                    tagM('<indexInPage>'+_sIndex+'</indexInPage>'))

                # requiredAchievementCount
                _sRequiredAchievementCount = input(
                    Fore.GREEN+'[INFO]Required Achievement Count.(Not enable enter->0)'+Fore.RESET)
                _tMapDataAreaInfo.MapDataAreaInfo.append(tagM(
                    '<requiredAchievementCount>'+_sRequiredAchievementCount+'</requiredAchievementCount>'))

                # gauge
                _tgauge = SubstanceTagMaker('Map', 'gauge', 0)
                _tMapDataAreaInfo.MapDataAreaInfo.append(_tgauge)

                _dXml.MapData.infos.append(_tMapDataAreaInfo)

            if input(Fore.GREEN+Content['Map']['Input']['Continue']+Fore.RESET).lower() == 'n':
                break

        # print(_dXml.prettify())
        _sSavePath = getconfig('SavePath', 'MapPath')+'/map'+_sMapNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)

        with open(_sSavePath+'/Map.xml', 'w', encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/Map.xml')
        print(Fore.GREEN+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'Map')+Fore.RESET)
        os.system('PAUSE')
