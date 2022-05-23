from colorama import Fore

from module.cross import *
from module.substances import *


def MapBonusM(Content):
    '''
    ## Used to create MapBonus.xml.
    '''
    if not CheckConfig('SavePath', 'MapBonusPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'MapBonus')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
        return
    else:
        # create xml data
        XMLData = TagM('')

        # add datatitle tag
        TagXMLVer = TagM('<?xml version="1.0" encoding="utf-8"?>')
        TagDataTitle = TagM(
            '<MapBonusData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></MapBonusData>')
        XMLData.append(TagXMLVer)
        XMLData.append(TagDataTitle)

        # add dataname and name tags
        MapBonusNum = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Num'].replace('%now%', 'MapBonus')+Fore.RESET)
        MapBonusStr = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'MapBonus')+Fore.RESET)
        TagName = TagM('<name><id>'+MapBonusNum+'</id><str>' +
                      MapBonusStr+'</str><data/></name>')
        if len(MapBonusNum) > 8:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Num_Out_of_range'].replace('%now%', 'MapBonus')+Fore.RESET)
            if sys.platform == 'win32':
                os.system('PAUSE')
            return
        while len(MapBonusNum) != 8:
            MapBonusNum = '0'+MapBonusNum
        TagDataName = TagM('<dataName>mapBonus'+MapBonusNum+'</dataName>')
        XMLData.MapBonusData.append(TagDataName)
        XMLData.MapBonusData.append(TagName)

        TagSubstances = TagM('<substances><list></list></substances>')
        XMLData.MapBonusData.append(TagSubstances)

        CountOfBonus = 0
        IsFinish = False
        while not IsFinish:
            # choose 1 type of trigger
            print(Fore.RED+Content['MapBonus']['Output']
                  ['Counter'].replace('%num%', str(CountOfBonus))+Fore.RESET)
            print(Fore.GREEN+Content['MapBonus']['Menu']['Title']+Fore.RESET)
            print(Fore.GREEN+Content['MapBonus']['Menu']['Help']+Fore.RESET)
            for Num in range(0, 10):
                print(Fore.GREEN+Content['MapBonus']
                      ['Menu']['Type_'+str(Num)]+Fore.RESET)
            InputType = int(input(Fore.GREEN+'>'+Fore.RESET))
            if InputType > 9:
                print(Fore.RED+Content['Cross']['Error_Msg']
                      ['Type_Out_Of_Range']+Fore.RESET)
                return
            elif InputType == 9:
                IsFinish = True
            else:
                TagMapBonusSubstanceData = TagM(
                    '<MapBonusSubstanceData><type></type></MapBonusSubstanceData>')

                # type
                TagMapBonusSubstanceData.MapBonusSubstanceData.type.string = str(
                    InputType)

                # chara
                TagChara = SubstanceTagMaker('MapBonus', 'chara', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(TagChara)

                # charaWorks
                TagCharaWorks = SubstanceTagMaker(
                    'MapBonus', 'charaWorks', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(
                    TagCharaWorks)

                # skill
                TagSkill = SubstanceTagMaker('MapBonus', 'skill', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(TagSkill)

                # skillCategory
                TagSkillCategory = SubstanceTagMaker(
                    'MapBonus', 'skillCategory', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(
                    TagSkillCategory)

                # music
                TagMusic = SubstanceTagMaker('MapBonus', 'music', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(TagMusic)

                # musicGenre
                TagMusicGenre = SubstanceTagMaker(
                    'MapBonus', 'musicGenre', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(
                    TagMusicGenre)

                # musicWorks
                TagMusicWorks = SubstanceTagMaker(
                    'MapBonus', 'musicWorks', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(
                    TagMusicWorks)

                # musicDif
                TagMusicDif = SubstanceTagMaker('MapBonus', 'musicDif', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(
                    TagMusicDif)

                # musicLv
                TagMusicLv = SubstanceTagMaker('MapBonus', 'musicLv', InputType)
                TagMapBonusSubstanceData.MapBonusSubstanceData.append(TagMusicLv)

                XMLData.MapBonusData.substances.list.append(
                    TagMapBonusSubstanceData)
                if CountOfBonus == 3:
                    IsFinish = True
                else:
                    CountOfBonus = CountOfBonus+1

        # print(_dXml.prettify())
        SavePath = GetConfig('SavePath', 'MapBonusPath') + \
            '/MapBonus'+MapBonusNum
        if not os.path.isdir(SavePath):
            os.mkdir(SavePath)

        with open(SavePath+'/MapBonus.xml', 'w', encoding='utf-8')as File:
            File.write(str(XMLData))
            File.close()

        XMLFormat(SavePath+'/MapBonus.xml')
        print(Fore.GREEN+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'MapBonus')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
