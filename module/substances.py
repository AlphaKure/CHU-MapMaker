from bs4 import BeautifulSoup
from colorama import Fore

from module.cross import *


def SubstanceTagMaker(FileType: str, NowPart: str, Type: int) -> BeautifulSoup:
    '''
    ## Used to generate substances tag

    Type is the value selected by the user.
    Assuming that the user enters 5(Type), the tag guided by 5 will be generated normally.
    While other tags will be automatically generated with a null tag to satisfy the format because of the different Type.
    Type為使用者選擇的值，假設使用者選擇5，為了生成其他選項的空值Tag，假設到6的地方由於輸入Type不同，即可自行生成空值TAG
    '''
    global Content  # 文本

    # Reward substances
    if FileType == 'Reward':
        TagNameList = ['', 'ticket', 'trophy', 'chara', '', 'namePlate', 'music',
                       'mapIcon', 'systemVoice', 'avatarAccessory', 'frame']  # TagName[0] and TagName[4] are set to null to avoid conflict.

        # gamePoint-reward
        if NowPart == 'gamePoint':
            if Type == 0:
                PointAmount = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_GamePoint']+Fore.RESET)
            else:
                PointAmount = '0'
            TagGamepoint = TagM('<gamePoint><gamePoint>' +
                               PointAmount+'</gamePoint></gamePoint>')
            return TagGamepoint

        # skillSeed-reward
        elif NowPart == 'skillSeed':
            if Type == 4:
                SkillSeedID = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedID']+Fore.RESET)
                SkillSeedCount = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedCount']+Fore.RESET)
                if CheckConfig('AutoStr', 'Skill'):
                    IsFind, SkillSeedStr = GetStr(
                        'name', 'AutoStr', 'Skill', SkillSeedID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    SkillSeedStr = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedStr']+Fore.RESET)
            else:
                SkillSeedID = '-1'
                SkillSeedStr = 'Invalid'
                SkillSeedCount = '1'
            TagSkillSeed = TagM('<skillSeed><skillSeedName><id>'+SkillSeedID +
                                '</id><str>'+SkillSeedStr+'</str><data></skillSeedName></skillSeed>')
            TagSkillSeedcount = TagM(
                '<skillSeedCount>'+SkillSeedCount+'</skillSeedCount>')
            return TagSkillSeed, TagSkillSeedcount

        # Other-Reward
        else:
            if NowPart == TagNameList[Type]:
                InputID = input(Fore.GREEN+Content['Cross']['Input']['Input_ID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if CheckConfig('AutoStr', TagNameList[Type]):
                    IsFind, Str = GetStr(
                        'name', 'AutoStr', TagNameList[Type], InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_Str'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><'+NowPart+'Name><id>'+InputID+'</id><str>' +
                       Str+'</str><data></'+NowPart+'Name></'+NowPart+'>')
            return Tag

    elif FileType == 'MapBonus':
        TagNameList = ['chara', 'charaWorks', 'skill', 'skillCategory',
                       'music', 'musicGenre', 'musicWorks', 'musicDif', 'musicLv']
        FileNameList = ['chara', 'chara', 'Skill',
                        'Skill', 'music', 'music', 'music', '', '']  # Leave blank for the same reason as in line 21
        FindKeyList = ['name', 'works', 'name', 'category',
                       'name', 'genreNames', 'worksName', '', '']  # Leave blank for the same reason as in line 21

        # musicDif-MapBonus
        if NowPart == 'musicDif':
            if Type == 7:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                InputID = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusMusicDif']+Fore.RESET)
                Str = musicDif(int(InputID))
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><musicDif><id>' +
                       InputID+'</id><str>'+Str+'</str><data /></musicDif></'+NowPart+'>')
            return Tag
        # musicLv-MapBonus
        elif NowPart == 'musicLv': 
            if Type == 8:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Lv = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusMusicLv']+Fore.RESET)
                if Lv.endswith('+'):
                    InputID = str(int(Lv[:-1])*2)
                    Str = 'ID_'+InputID
                    Data = 'Lv'+Lv
                else:
                    InputID = str(int(Lv)*2-1)
                    Str = 'ID_'+InputID
                    Data = 'Lv'+Lv
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
                Data = ''
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><filterLv><id>'+InputID +
                       '</id><str>'+Str+'</str><data>'+Data+'</data></filterLv></'+NowPart+'>')
            return Tag
        # skillCategory-MapBonus
        elif NowPart == 'skillCategory':
            if Type == 3:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                InputID = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if CheckConfig('AutoStr', FileNameList[Type]):
                    IsFind, Str = GetStr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><skillCategory><id>' +
                       InputID+'</id><str>'+Str+'</str><data /></skillCategory></'+NowPart+'>')
            return Tag

        # musicGenre-MapBonus
        elif NowPart == 'musicGenre':
            if Type == 5:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                InputID = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if CheckConfig('AutoStr', FileNameList[Type]):
                    IsFind, Str = GetStr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><genreName><id>' +
                       InputID+'</id><str>'+Str+'</str><data /></genreName></'+NowPart+'>')
            return Tag

        # musicWorks-MapBonus
        elif NowPart == 'musicWorks':
            if Type == 6:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                InputID = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if CheckConfig('AutoStr', FileNameList[Type]):
                    IsFind, Str = GetStr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><worksName><id>' +
                       InputID+'</id><str>'+Str+'</str><data /></worksName></'+NowPart+'>')
            return Tag

        # Other-MapBonus
        else:
            if NowPart == TagNameList[Type]:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                InputID = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if CheckConfig('AutoStr', FileNameList[Type]):
                    IsFind, Str = GetStr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                InputID = '-1'
                Str = 'Invalid'
            Tag = TagM('<'+NowPart+'><point>'+Point+'</point><'+NowPart+'Name><id>' +
                       InputID+'</id><str>'+Str+'</str><data /></'+NowPart+'Name></'+NowPart+'>')
            return Tag
    elif FileType == 'Map':
        # music-Map
        if NowPart == 'music':
            EnableCourseMusic = input(
                Fore.GREEN+Content['Cross']['Input']['Input_MapHaveTaskTrack']+Fore.RESET).lower()
            if EnableCourseMusic == 'n':
                InputID = '-1'
                Str = 'Invalid'
                IsHard = 'false'
            else:
                InputID = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackID']+Fore.RESET)
                if CheckConfig('AutoStr', 'music'):
                    IsFind, Str = GetStr('name', 'AutoStr', 'music', InputID)
                    if not IsFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackStr']+Fore.RESET)
                    IsHard = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackDifLock']+Fore.RESET).lower()
                    if IsHard == 'y':
                        IsHard = 'true'
                    else:
                        IsHard = 'false'
            return IsHard, TagM('<'+NowPart+'Name><id>'+InputID+'</id><str>'+Str+'</str><data /></'+NowPart+'Name>')
        #Other-Reward
        else:
            InputID = input(
                Fore.GREEN+f'[INFO]Enter the ID of {NowPart}:'+Fore.RESET)
            if CheckConfig('AutoStr', NowPart):
                IsFind, Str = GetStr('name', 'AutoStr', NowPart, InputID)
                if not IsFind:
                    return SubstanceTagMaker(FileType, NowPart, Type)
            else:
                Str = input(
                    Fore.GREEN+f'[INFO]Enter the Str of {NowPart}:'+Fore.RESET)
            return TagM('<'+NowPart+'Name><id>'+InputID+'</id><str>'+Str+'</str><data /></'+NowPart+'Name>')


def SetContent(data):
    global Content
    Content = data
