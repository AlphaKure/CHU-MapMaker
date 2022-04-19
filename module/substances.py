from colorama import Fore

from cross import *

def SubstanceTagMaker(FileType:str,NowPart:str,Type:int):
    #Reward substances
    if FileType=='Reward':
        TagNameList=['','ticket','trophy','chara','','namePlate','music','mapIcon','systemVoice','avatarAccessory','frame'] #不讓gamePoint skillSeed 碰撞

        #gamePoint-reward
        if NowPart=='gamePoint':
            if Type==0:
                _sAmount=input(Fore.GREEN+'[INFO]Enter amount of gamePoint that you want to add:')
            else:
                _sAmount='0'
            _tGamepoint=tagM('<gamePoint><gamePoint>'+_sAmount+'</gamePoint></gamePoint>')
            return _tGamepoint
        
        #skillSeed-reward
        elif NowPart=='skillSeed':
            if Type==4:
                _sSkillseedId=input(Fore.GREEN+'[INFO]Enter id of skillseed that you want to give:')
                _sSkillseedcount=input(Fore.GREEN+'[INFO]Enter count of skillseed that you want to give:')
                if checkconfig('AutoStr','Skill'):
                    _fFInd,_sSkillseedStr=getstr('name','AutoStr','Skill',_sSkillseedId)
                    if not _fFInd:
                        return
                else:
                    _sSkillseedStr=input(Fore.GREEN+'[INFO]Enter str of skillseed that you want to give:')
            else:
                _sSkillseedId='-1'
                _sSkillseedStr='Invalid'
                _sSkillseedcount='1'
            _tSkillseed=tagM('<skillSeed><skillSeedName><id>'+_sSkillseedId+'</id><str>'+_sSkillseedStr+'</str><data></skillSeedName></skillSeed>')
            _tSkillseedcount=tagM('<skillSeedCount>'+_sSkillseedcount+'</skillSeedCount>')
            return _tSkillseed,_tSkillseedcount

        #Other-reward 公版    
        else:
            if NowPart==TagNameList[Type]:
                Id=input(Fore.GREEN+f'[INFO]Enter id of {TagNameList[Type]} that you want to give:')
                if checkconfig('AutoStr',TagNameList[Type]):
                    _fFInd,Str=getstr('name','AutoStr',TagNameList[Type],Id)
                    if not _fFInd:
                        return
                else:
                    Str=input(Fore.GREEN+f'[INFO]Enter str of {TagNameList[Type]} that you want to give:')
            else:
                Id='-1'
                Str='Invalid'
            Tag=tagM('<'+NowPart+'><'+NowPart+'Name><id>'+Id+'</id><str>'+Str+'</str><data></'+NowPart+'Name></'+NowPart+'>')
            return Tag

    elif FileType=='MapBonus':
        TagNameList=['chara','charaWorks','skill','skillCategory','music','musicGenre','musicWorks','musicDif','musicLv','']
        FileNameList=['chara','chara','Skill','Skill','music','music','music','','','']
        FindKeyList=['name','works','name','category','name','genreNames','worksName','','','']
        if NowPart=='musicDif':
            if Type==7:
                Point=input(Fore.GREEN+'[INFO]Enter how many bonus step you want to give.')
                Id=input(Fore.GREEN+f'[INFO]Enter Trigger musicDif Id(ex:Basic->0).')
                Str=musicDif(int(Id))
            else:
                Point='1'
                Id='-1'
                Str='Invalid'
            Tag=tagM('<'+NowPart+'><point>'+Point+'</point><'+NowPart+'Name><id>'+Id+'</id><str>'+Str+'</str><data /></'+NowPart+'Name></'+NowPart+'>')
            return Tag
        elif NowPart=='musicLv':
            if Type==8:
                Point=input(Fore.GREEN+'[INFO]Enter how many bonus step you want to give.')
                Lv=input(Fore.GREEN+f'[INFO]Enter Trigger Lv (ex:14+->14+).')
                if Lv.endswith('+'):
                    Id=str(int(Lv[:-1])*2)
                    Str='ID_'+str(Id)
                    Data='Lv'+str(Lv)+'+'
                else:
                    Id=str(int(Lv)*2-1)
                    Str='ID_'+str(Id)
                    Data='Lv'+Lv
            else:
                Point='1'
                Id='-1'
                Str='Invalid'
                Data=''
            Tag=tagM('<'+NowPart+'><point>'+Point+'</point><filterLv><id>'+Id+'</id><str>'+Str+'</str><data>'+Data+'</data></filterLv></'+NowPart+'>')
            return Tag



        else:
            if NowPart==TagNameList[Type]:
                Point=input(Fore.GREEN+'[INFO]Enter how many bonus step you want to give.')
                Id=input(Fore.GREEN+f'[INFO]Enter Trigger {TagNameList[Type]} Id.')
                if checkconfig('AutoStr',FileNameList[Type]):
                    _fFind,Str=getstr(FindKeyList[Type],'AutoStr',FileNameList[Type],Id)
                    if not _fFind:
                        return
                else:
                    Str=input(Fore.GREEN+f'[INFO]Enter Trigger {TagNameList[Type]} Str.')
            else:
                Point='1'
                Id='-1'
                Str='Invalid'
            Tag=tagM('<'+NowPart+'><point>'+Point+'</point><'+NowPart+'Name><id>'+Id+'</id><str>'+Str+'</str><data /></'+NowPart+'Name></'+NowPart+'>')
            return Tag
