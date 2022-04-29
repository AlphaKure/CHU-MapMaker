from colorama import Fore

from cross import *
from substances import *

os.system('cls') #避免colorama錯誤

def Reward_M():
    if not checkconfig('SavePath','RewardPath'):
        print(Fore.RED+'[ERROR] You didn\'t enter save path for reward!'+Fore.RESET)
        os.system('PAUSE')
        return
    else:
        #NEW xml data
        _dXml=tagM('')

        #add datatitle tag
        _tXmlVer=tagM('<?xml version="1.0" encoding="utf-8"?>')
        _tDataTitle=tagM('<RewardData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></RewardData>')
        _dXml.append(_tXmlVer)
        _dXml.append(_tDataTitle)

        #add dataname and name tags
        _sRewardNum=input(Fore.GREEN+'[INFO]Enter custom Rewardnum:'+Fore.RESET)
        _sRewardStr=input(Fore.GREEN+'[INFO]Enter custom Rewardstr:'+Fore.RESET)
        _tName=tagM('<name><id>'+_sRewardNum+'</id><str>'+_sRewardStr+'</str><data/></name>')
        if len(_sRewardNum)>9:
            print(Fore.RED+'[ERROR] Data number should be less than 9 digits!'+Fore.RESET)
            os.system('PAUSE')
            return
        while len(_sRewardNum)!=9:
            _sRewardNum='0'+_sRewardNum
        _tdataName=tagM('<dataName>reward'+_sRewardNum+'</dataName>')
        _dXml.RewardData.append(_tdataName)
        _dXml.RewardData.append(_tName)

        #choose 1 type of Reward
        print(Fore.GREEN+'\n[INFO]What kind of reward that you want to add?'+Fore.RESET)
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
        _iType=int(input(Fore.GREEN+'>'+Fore.RESET))
        if _iType>10:
            print(Fore.RED+'[ERROR] Out of range!'+Fore.RESET)
            return
        else:
            _tSubstances=tagM('<substances><list><RewardSubstanceData><type>'+str(_iType)+'</type></RewardSubstanceData></list></substances>')
            _dXml.RewardData.append(_tSubstances)
            print(Fore.RED+'\n[WARNING]This tool is ONLY add for offical data. If you want to add custom data likes ddsMap or chara, etc. Please add custom data by yourself.')

            #gamepoint reward
            _tGamepoint=SubstanceTagMaker('Reward','gamePoint',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tGamepoint)

            #ticket
            _tTicket=SubstanceTagMaker('Reward','ticket',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tTicket)
        
            #trophy
            _tTrophy=SubstanceTagMaker('Reward','trophy',_iType)        
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tTrophy)
        
            #chara
            _tChara=SubstanceTagMaker('Reward','chara',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tChara)

            #Skillseed
            _tSkillseed,_tSkillseedcount=SubstanceTagMaker('Reward','skillSeed',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tSkillseed)
            _dXml.RewardData.substances.list.RewardSubstanceData.skillSeed.append(_tSkillseedcount) 

            #Nameplate
            _tNameplate=SubstanceTagMaker('Reward','namePlate',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tNameplate)

            #Music
            _tMusic=SubstanceTagMaker('Reward','music',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tMusic)
        
            #Mapicon
            _tMapicon=SubstanceTagMaker('Reward','mapIcon',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tMapicon)

            #Systemvoice
            _tSystemvoice=SubstanceTagMaker('Reward','systemVoice',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tSystemvoice)

            #AvatarAccessory
            _tAvaterAccessory=SubstanceTagMaker('Reward','avatarAccessory',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tAvaterAccessory)

            #Frame
            _tFrame=SubstanceTagMaker('Reward','frame',_iType)
            _dXml.RewardData.substances.list.RewardSubstanceData.append(_tFrame)


        #print(_dXml.prettify()+Fore.RESET)
        _sSavePath=getconfig('SavePath','RewardPath')+'/reward'+_sRewardNum
        if not os.path.isdir(_sSavePath):
            os.mkdir(_sSavePath)
        
        with open(_sSavePath+'/Reward.xml','w',encoding='utf-8')as f:
            f.write(str(_dXml))
            f.close()

        XMLFormat(_sSavePath+'/Reward.xml')
        print(Fore.GREEN+'\nFinish!!!'+Fore.RESET)
        os.system('PAUSE')
        
if __name__=='__main__'and PathChk():
    Reward_M()