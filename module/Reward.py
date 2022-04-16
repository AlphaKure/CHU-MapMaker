from bs4 import BeautifulSoup as BS
import lxml
import configparser
from colorama import Fore

from cross import *

def Reward_M():

    #NEW xml data
    _dXml=tagM('')
    #add datatitle tag
    _tDataTitle=tagM('<RewardData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></RewardData>')
    _dXml.append(_tDataTitle)

    #add dataname and name tags
    _sRewardNum=input(Fore.GREEN+'[INFO]Enter custom Rewardnum:')
    _sRewardStr=input(Fore.GREEN+'[INFO]Enter custom Rewardstr:')
    _tName=tagM('<name><id>'+_sRewardNum+'</id><str>'+_sRewardStr+'</str><data/></name>')
    while len(_sRewardNum)!=9:
        _sRewardNum='0'+_sRewardNum
    _tdataName=tagM('<dataName>reward'+_sRewardNum+'</dataName>')
    _dXml.RewardData.append(_tdataName)
    _dXml.RewardData.append(_tName)

    #choose 1 type of Reward
    print(Fore.GREEN+'\n[INFO]What kind of reward that you want to add?')
    print(Fore.WHITE+'[0]Enter 0: gamePoint')
    print(Fore.WHITE+'[1]Enter 1: ticket')
    print(Fore.WHITE+'[2]Enter 2: trophy')
    print(Fore.WHITE+'[3]Enter 3: chara')
    print(Fore.WHITE+'[4]Enter 4: skillseed')
    print(Fore.WHITE+'[5]Enter 5: nameplate')
    print(Fore.WHITE+'[6]Enter 6: music')
    print(Fore.WHITE+'[7]Enter 7: mapicon')
    print(Fore.WHITE+'[8]Enter 8: systemvoice')
    print(Fore.WHITE+'[9]Enter 9: avatarAccessory')
    print(Fore.WHITE+'[10]Enter 10: frame')
    _iType=int(input(Fore.GREEN+'>'))
    if _iType>10:
        print(Fore.RED+'[ERROR] Out of range!'+Fore.RESET)
        return
    else:
        _tSubstances=tagM('<substances><list><RewardSubstanceData><type>'+str(_iType)+'</type></RewardSubstanceData></list></substances>')
        _dXml.RewardData.append(_tSubstances)
        print(Fore.RED+'\n[WARNING]This tool is ONLY add for offical data. If you want to add custom data likes ddsMap or chara, etc. Please add custom data by yourself.')

        #gamepoint reward
        if _iType==0:
            _sAmount=input(Fore.GREEN+'[INFO]Enter amount of gamePoint that you want to add:')
        else:
            _sAmount='0'
        _tGamepoint=tagM('<gamePoint><gamePoint>'+_sAmount+'</gamePoint></gamePoint>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tGamepoint)


        #ticket
        if _iType==1:
            _sTicketId=input(Fore.GREEN+'[INFO]Enter id of ticket that you want to give:')
            if checkconfig('AutoStr','Ticket'):
                _fFInd,_sTicketStr=getstr('Ticket',_sTicketId)
                if not _fFInd:
                    return
            else:
                _sTicketStr=input(Fore.GREEN+'[INFO]Enter str of ticket that you want to give:')
        else:
            _sTicketId='-1'
            _sTicketStr='Invalid'
        _tTicket=tagM('<ticket><ticketName><id>'+_sTicketId+'</id><str>'+_sTicketStr+'</str><data></ticketName></ticket>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tTicket)
        
        #trophy
        if _iType==2:
            _sTrophyId=input(Fore.GREEN+'[INFO]Enter id of trophy that you want to give:')
            if checkconfig('AutoStr','Trophy'):
                _fFInd,_sTrophyStr=getstr('Trophy',_sTrophyId)
                if not _fFInd:
                    return
            else:
                _sTrophyStr=input(Fore.GREEN+'[INFO]Enter str of trophy that you want to give:')
        else:
            _sTrophyId='-1'
            _sTrophyStr='Invalid'
        
        _tTrophy=tagM('<trophy><trophyName><id>'+_sTrophyId+'</id><str>'+_sTrophyStr+'</str><data></trophyName></trophy>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tTrophy)
        
        #chara
        if _iType==3:
            _sCharaId=input(Fore.GREEN+'[INFO]Enter id of chara that you want to give:')
            if checkconfig('AutoStr','Chara'):
                _fFInd,_sCharaStr=getstr('Ticket',_sCharaId)
                if not _fFInd:
                    return
            else:
                _sCharaStr=input(Fore.GREEN+'[INFO]Enter str of chara that you want to give:')
        else:
            _sCharaId='-1'
            _sCharaStr='Invalid'
        _tChara=tagM('<chara><charaName><id>'+_sCharaId+'</id><str>'+_sCharaStr+'</str><data></charaName></chara>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tChara)

        #Skillseed
        if _iType==4:
            _sSkillseedId=input(Fore.GREEN+'[INFO]Enter id of skillseed that you want to give:')
            _sSkillseedcount=input(Fore.GREEN+'[INFO]Enter count of skillseed that you want to give:')
            if checkconfig('AutoStr','Skillseed'):
                _fFInd,_sSkillseedStr=getstr('Skillseed',_sSkillseedId)
                if not _fFInd:
                    return
            else:
                _sSkillseedStr=input(Fore.GREEN+'[INFO]Enter str of skillseed that you want to give:')
        else:
            _sSkillseedId='-1'
            _sSkillseedStr='Invalid'
            _sSkillseedcount='1'
        _tSkillseed=tagM('<skillSeed><skillSeedName><id>'+_sSkillseedId+'</id><str>'+_sSkillseedStr+'</str><data></skillSeedName></skillSeed>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tSkillseed)
        _tSkillseedcount=tagM('<skillSeedCount>'+_sSkillseedcount+'</skillSeedCount>')
        _dXml.RewardData.substances.list.RewardSubstanceData.skillSeed.append(_tSkillseedcount)
        

        #Nameplate
        if _iType==5:
            _sNameplateId=input(Fore.GREEN+'[INFO]Enter id of nameplate that you want to give:')
            if checkconfig('AutoStr','Nameplate'):
                _fFInd,_sNameplateStr=getstr('Nameplate',_sNameplateId)
                if not _fFInd:
                    return
            else:
                _sNameplateStr=input(Fore.GREEN+'[INFO]Enter str of nameplate that you want to give:')
        else:
            _sNameplateId='-1'
            _sNameplateStr='Invalid'
        _tNameplate=tagM('<namePlate><namePlateName><id>'+_sNameplateId+'</id><str>'+_sNameplateStr+'</str><data></namePlateName></namePlate>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tNameplate)

        #Music
        if _iType==6:
            _sMusicId=input(Fore.GREEN+'[INFO]Enter id of music that you want to give:')
            if checkconfig('AutoStr','Music'):
                _fFInd,_sMusicStr=getstr('Music',_sMusicId)
                if not _fFInd:
                    return
            else:
                _sMusicStr=input(Fore.GREEN+'[INFO]Enter str of music that you want to give:')
        else:
            _sMusicId='-1'
            _sMusicStr='Invalid'
        _tMusic=tagM('<music><musicName><id>'+_sMusicId+'</id><str>'+_sMusicStr+'</str><data></musicName></music>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tMusic)
        
        #Mapicon
        if _iType==7:
            _sMapiconId=input(Fore.GREEN+'[INFO]Enter id of mapicon that you want to give:')
            if checkconfig('AutoStr','Mapicon'):
                _fFInd,_sMapiconStr=getstr('Mapicon',_sMapiconId)
                if not _fFInd:
                    return
            else:
                _sMapiconStr=input(Fore.GREEN+'[INFO]Enter str of mapicon that you want to give:')
        else:
            _sMapiconId='-1'
            _sMapiconStr='Invalid'
        _tMapicon=tagM('<mapIcon><mapIconName><id>'+_sMapiconId+'</id><str>'+_sMapiconStr+'</str><data></mapIconName></mapIcon>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tMapicon)

        #Systemvoice
        if _iType==8:
            _sSystemvoiceId=input(Fore.GREEN+'[INFO]Enter id of systemvoice that you want to give:')
            if checkconfig('AutoStr','Systemvoice'):
                _fFInd,_sSystemvoiceStr=getstr('Systemvoice',_sSystemvoiceId)
                if not _fFInd:
                    return
            else:
                _sSystemvoiceStr=input(Fore.GREEN+'[INFO]Enter str of systemvoice that you want to give:')
        else:
            _sSystemvoiceId='-1'
            _sSystemvoiceStr='Invalid'
        _tSystemvoice=tagM('<systemVoice><systemVoiceName><id>'+_sSystemvoiceId+'</id><str>'+_sSystemvoiceStr+'</str><data></systemVoiceName></systemVoice>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tSystemvoice)

        #AvatarAccessory
        if _iType==9:
            _sAvatarAccessoryId=input(Fore.GREEN+'[INFO]Enter id of avataraccessory that you want to give:')
            if checkconfig('AutoStr','AvatarAccessory'):
                _fFInd,_sAvatarAccessoryStr=getstr('AvatarAccessory',_sAvatarAccessoryId)
                if not _fFInd:
                    return
            else:
                _sAvatarAccessoryStr=input(Fore.GREEN+'[INFO]Enter str of avataraccessory that you want to give:')
        else:
            _sAvatarAccessoryId='-1'
            _sAvatarAccessoryStr='Invalid'
        _tAvaterAccessory=tagM('<avatarAccessory><avatarAccessoryName><id>'+_sAvatarAccessoryId+'</id><str>'+_sAvatarAccessoryStr+'</str><data></avatarAccessoryName></avatarAccessory>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tAvaterAccessory)

        #Frame
        if _iType==10:
            _sFrameId=input(Fore.GREEN+'[INFO]Enter id of frame that you want to give:')
            if checkconfig('AutoStr','Frame'):
                _fFInd,_sFrameStr=getstr('Frame',_sFrameId)
                if not _fFInd:
                    return
            else:
                _sFrameStr=input(Fore.GREEN+'[INFO]Enter str of frame that you want to give:')
        else:
            _sFrameId='-1'
            _sFrameStr='Invalid'
        _tFrame=tagM('<frame><frameName><id>'+_sFrameId+'</id><str>'+_sFrameStr+'</str><data></frameName></frame>')
        _dXml.RewardData.substances.list.RewardSubstanceData.append(_tFrame)


    print(_dXml.prettify()+Fore.RESET)
    if not checkconfig('SavePath','RewardPath'):
        print(Fore.RED+'[ERROR] You didn\'t enter save path for reward!'+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        _sSavePath=getconfig('SavePath','RewardPath')+'/reward'+_sRewardNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/Reward.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

if __name__=='__main__':
    Reward_M()