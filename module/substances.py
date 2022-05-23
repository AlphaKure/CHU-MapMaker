from bs4 import BeautifulSoup
from colorama import Fore

from module.cross import *


def SubstanceTagMaker(FileType: str, NowPart: str, Type: int) -> BeautifulSoup:
    # Type為使用者選擇的值，假設使用者選擇5，為了生成其他選項的空值TAG，假設到6的地方由於輸入Type不同，即可自行生成空值TAG

    global Content  # 文本

    # Reward substances
    if FileType == 'Reward':
        TagNameList = ['', 'ticket', 'trophy', 'chara', '', 'namePlate', 'music',
                       'mapIcon', 'systemVoice', 'avatarAccessory', 'frame']  # 不讓gamePoint skillSeed 碰撞

        # gamePoint-reward
        if NowPart == 'gamePoint':
            if Type == 0:
                _sAmount = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_GamePoint']+Fore.RESET)
            else:
                _sAmount = '0'
            _tGamepoint = tagM('<gamePoint><gamePoint>' +
                               _sAmount+'</gamePoint></gamePoint>')
            return _tGamepoint

        # skillSeed-reward
        elif NowPart == 'skillSeed':
            if Type == 4:
                _sSkillseedId = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedID']+Fore.RESET)
                _sSkillseedcount = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedCount']+Fore.RESET)
                if checkconfig('AutoStr', 'Skill'):
                    _fFInd, _sSkillseedStr = getstr(
                        'name', 'AutoStr', 'Skill', _sSkillseedId)
                    if not _fFInd:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    _sSkillseedStr = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_SkillSeedStr']+Fore.RESET)
            else:
                _sSkillseedId = '-1'
                _sSkillseedStr = 'Invalid'
                _sSkillseedcount = '1'
            _tSkillseed = tagM('<skillSeed><skillSeedName><id>'+_sSkillseedId +
                               '</id><str>'+_sSkillseedStr+'</str><data></skillSeedName></skillSeed>')
            _tSkillseedcount = tagM(
                '<skillSeedCount>'+_sSkillseedcount+'</skillSeedCount>')
            return _tSkillseed, _tSkillseedcount

        # Other-reward 公版
        else:
            if NowPart == TagNameList[Type]:
                Id = input(Fore.GREEN+Content['Cross']['Input']['Input_ID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if checkconfig('AutoStr', TagNameList[Type]):
                    _fFInd, Str = getstr(
                        'name', 'AutoStr', TagNameList[Type], Id)
                    if not _fFInd:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_Str'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><'+NowPart+'Name><id>'+Id+'</id><str>' +
                       Str+'</str><data></'+NowPart+'Name></'+NowPart+'>')
            return Tag

    elif FileType == 'MapBonus':
        TagNameList = ['chara', 'charaWorks', 'skill', 'skillCategory',
                       'music', 'musicGenre', 'musicWorks', 'musicDif', 'musicLv']
        FileNameList = ['chara', 'chara', 'Skill',
                        'Skill', 'music', 'music', 'music', '', '']
        FindKeyList = ['name', 'works', 'name', 'category',
                       'name', 'genreNames', 'worksName', '', '']
        if NowPart == 'musicDif':
            if Type == 7:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Id = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusMusicDif']+Fore.RESET)
                Str = musicDif(int(Id))
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><musicDif><id>' +
                       Id+'</id><str>'+Str+'</str><data /></musicDif></'+NowPart+'>')
            return Tag
        elif NowPart == 'musicLv':
            if Type == 8:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Lv = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusMusicLv']+Fore.RESET)
                if Lv.endswith('+'):
                    Id = str(int(Lv[:-1])*2)
                    Str = 'ID_'+Id
                    Data = 'Lv'+Lv
                else:
                    Id = str(int(Lv)*2-1)
                    Str = 'ID_'+Id
                    Data = 'Lv'+Lv
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
                Data = ''
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><filterLv><id>'+Id +
                       '</id><str>'+Str+'</str><data>'+Data+'</data></filterLv></'+NowPart+'>')
            return Tag
        elif NowPart == 'skillCategory':
            if Type == 3:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Id = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if checkconfig('AutoStr', FileNameList[Type]):
                    _fFind, Str = getstr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], Id)
                    if not _fFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><skillCategory><id>' +
                       Id+'</id><str>'+Str+'</str><data /></skillCategory></'+NowPart+'>')
            return Tag

        elif NowPart == 'musicGenre':
            if Type == 5:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Id = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if checkconfig('AutoStr', FileNameList[Type]):
                    _fFind, Str = getstr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], Id)
                    if not _fFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><genreName><id>' +
                       Id+'</id><str>'+Str+'</str><data /></genreName></'+NowPart+'>')
            return Tag

        elif NowPart == 'musicWorks':
            if Type == 6:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Id = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if checkconfig('AutoStr', FileNameList[Type]):
                    _fFind, Str = getstr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], Id)
                    if not _fFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><worksName><id>' +
                       Id+'</id><str>'+Str+'</str><data /></worksName></'+NowPart+'>')
            return Tag

        else:
            if NowPart == TagNameList[Type]:
                Point = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_MapBonusPoint']+Fore.RESET)
                Id = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerID'].replace(
                    '%TagName%', TagNameList[Type])+Fore.RESET)
                if checkconfig('AutoStr', FileNameList[Type]):
                    _fFind, Str = getstr(
                        FindKeyList[Type], 'AutoStr', FileNameList[Type], Id)
                    if not _fFind:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(Fore.GREEN+Content['Cross']['Input']['Input_MapBonusTriggerStr'].replace(
                        '%TagName%', TagNameList[Type])+Fore.RESET)
            else:
                Point = '1'
                Id = '-1'
                Str = 'Invalid'
            Tag = tagM('<'+NowPart+'><point>'+Point+'</point><'+NowPart+'Name><id>' +
                       Id+'</id><str>'+Str+'</str><data /></'+NowPart+'Name></'+NowPart+'>')
            return Tag
    elif FileType == 'Map':
        if NowPart == 'music':
            _sCourseMusic = input(
                Fore.GREEN+Content['Cross']['Input']['Input_MapHaveTaskTrack']+Fore.RESET).lower()
            if _sCourseMusic == 'n':
                Id = '-1'
                Str = 'Invalid'
                isHard = 'false'
            else:
                Id = input(
                    Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackID']+Fore.RESET)
                if checkconfig('AutoStr', 'music'):
                    _fFInd, Str = getstr('name', 'AutoStr', 'music', Id)
                    if not _fFInd:
                        return SubstanceTagMaker(FileType, NowPart, Type)
                else:
                    Str = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackStr']+Fore.RESET)
                    isHard = input(
                        Fore.GREEN+Content['Cross']['Input']['Input_TaskTrackDifLock']+Fore.RESET).lower()
                    if isHard == 'y':
                        isHard = 'true'
                    else:
                        isHard = 'false'
            return isHard, tagM('<'+NowPart+'Name><id>'+Id+'</id><str>'+Str+'</str><data /></'+NowPart+'Name>')
        else:
            Id = input(
                Fore.GREEN+f'[INFO]Enter the ID of {NowPart}:'+Fore.RESET)
            if checkconfig('AutoStr', NowPart):
                _fFInd, Str = getstr('name', 'AutoStr', NowPart, Id)
                if not _fFInd:
                    return SubstanceTagMaker(FileType, NowPart, Type)
            else:
                Str = input(
                    Fore.GREEN+f'[INFO]Enter the Str of {NowPart}:'+Fore.RESET)
            return tagM('<'+NowPart+'Name><id>'+Id+'</id><str>'+Str+'</str><data /></'+NowPart+'Name>')


def SetContent(data):
    global Content
    Content = data
