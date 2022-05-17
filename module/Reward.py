from colorama import Fore

from module.cross import *
from module.substances import *

os.system('cls') #避免colorama錯誤

def RewardM(Content):
    if not checkconfig('SavePath','RewardPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']['No_Save_Path'].replace('%now%','Reward')+Fore.RESET)
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
        _sRewardNum=input(Fore.GREEN+Content['Reward']['Input']['Reward_Num']+Fore.RESET)
        _sRewardStr=input(Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%','Reward')+Fore.RESET)
        _tName=tagM('<name><id>'+_sRewardNum+'</id><str>'+_sRewardStr+'</str><data/></name>')
        if len(_sRewardNum)>9:
            print(Fore.RED+Content['Reward']['Error_Msg']['Reward_Num_Out_Of_Range']+Fore.RESET)
            os.system('PAUSE')
            return
        while len(_sRewardNum)!=9:
            _sRewardNum='0'+_sRewardNum
        _tdataName=tagM('<dataName>reward'+_sRewardNum+'</dataName>')
        _dXml.RewardData.append(_tdataName)
        _dXml.RewardData.append(_tName)

        #Menu
        print(Fore.GREEN+Content['Reward']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Reward']['Menu']['Help']+Fore.RESET)
        for i in range(0,11):
            print(Fore.GREEN+Content['Reward']['Menu']['Type_'+str(i)]+Fore.RESET)
        _iType=int(input(Fore.GREEN+'>'+Fore.RESET))
        if _iType>10:
            print(Fore.RED+Content['Cross']['Error_Msg']['Type_Out_Of_Range']+Fore.RESET)
            return
        else:
            _tSubstances=tagM('<substances><list><RewardSubstanceData><type>'+str(_iType)+'</type></RewardSubstanceData></list></substances>')
            _dXml.RewardData.append(_tSubstances)

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
        print(Fore.GREEN+'\n'+Content['Cross']['Output']['Xml_Make_Finish'].replace('%now%','Reward')+Fore.RESET)
        os.system('PAUSE')
        
