from colorama import Fore

from module.cross import *
from module.substances import *


def RewardM(Content):
    '''
    ## Used to create Reward.xml
    '''
    if not CheckConfig('SavePath', 'RewardPath'):
        print(Fore.RED+Content['Cross']['Error_Msg']
              ['No_Save_Path'].replace('%now%', 'Reward')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
        return
    else:
        # create xml data
        XMLData = TagM('')

        # add datatitle tag
        TagXMLVer = TagM('<?xml version="1.0" encoding="utf-8"?>')
        TagDataTitle = TagM(
            '<RewardData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></RewardData>')
        XMLData.append(TagXMLVer)
        XMLData.append(TagDataTitle)

        # add dataname and name tags
        RewardNum = input(
            Fore.GREEN+Content['Reward']['Input']['Reward_Num']+Fore.RESET)
        RewardStr = input(
            Fore.GREEN+Content['Cross']['Input']['Input_Name'].replace('%now%', 'Reward')+Fore.RESET)
        TagName = TagM('<name><id>'+RewardNum+'</id><str>' +
                      RewardStr+'</str><data/></name>')
        if len(RewardNum) > 9:
            print(Fore.RED+Content['Reward']['Error_Msg']
                  ['Reward_Num_Out_Of_Range']+Fore.RESET)
            if sys.platform == 'win32':
                os.system('PAUSE')
            return
        while len(RewardNum) != 9:
            RewardNum = '0'+RewardNum
        TagDataName = TagM('<dataName>reward'+RewardNum+'</dataName>')
        XMLData.RewardData.append(TagDataName)
        XMLData.RewardData.append(TagName)

        # Menu
        print(Fore.GREEN+Content['Reward']['Menu']['Title']+Fore.RESET)
        print(Fore.GREEN+Content['Reward']['Menu']['Help']+Fore.RESET)
        for Num in range(0, 11):
            print(Fore.GREEN+Content['Reward']
                  ['Menu']['Type_'+str(Num)]+Fore.RESET)
        InputType = int(input(Fore.GREEN+'>'+Fore.RESET))
        if InputType > 10:
            print(Fore.RED+Content['Cross']['Error_Msg']
                  ['Type_Out_Of_Range']+Fore.RESET)
            return
        else:
            TagSubstances = TagM('<substances><list><RewardSubstanceData><type>' +
                                str(InputType)+'</type></RewardSubstanceData></list></substances>')
            XMLData.RewardData.append(TagSubstances)

            # gamepoint reward
            TagGamepoint = SubstanceTagMaker('Reward', 'gamePoint', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagGamepoint)

            # ticket
            TagTicket = SubstanceTagMaker('Reward', 'ticket', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagTicket)

            # trophy
            TagTrophy = SubstanceTagMaker('Reward', 'trophy', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagTrophy)

            # chara
            TagChara = SubstanceTagMaker('Reward', 'chara', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagChara)

            # Skillseed
            TagSkillseed, TagSkillseedcount = SubstanceTagMaker(
                'Reward', 'skillSeed', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagSkillseed)
            XMLData.RewardData.substances.list.RewardSubstanceData.skillSeed.append(
                TagSkillseedcount)

            # Nameplate
            TagNameplate = SubstanceTagMaker('Reward', 'namePlate', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagNameplate)

            # Music
            TagMusic = SubstanceTagMaker('Reward', 'music', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagMusic)

            # Mapicon
            TagMapicon = SubstanceTagMaker('Reward', 'mapIcon', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagMapicon)

            # Systemvoice
            TagSystemvoice = SubstanceTagMaker('Reward', 'systemVoice', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagSystemvoice)

            # AvatarAccessory
            TagAvaterAccessory = SubstanceTagMaker(
                'Reward', 'avatarAccessory', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagAvaterAccessory)

            # Frame
            TagFrame = SubstanceTagMaker('Reward', 'frame', InputType)
            XMLData.RewardData.substances.list.RewardSubstanceData.append(
                TagFrame)

        # print(_dXml.prettify()+Fore.RESET)
        SavePath = GetConfig('SavePath', 'RewardPath')+'/reward'+RewardNum
        if not os.path.isdir(SavePath):
            os.mkdir(SavePath)

        with open(SavePath+'/Reward.xml', 'w', encoding='utf-8')as File:
            File.write(str(XMLData))
            File.close()

        XMLFormat(SavePath+'/Reward.xml')
        print(Fore.GREEN+'\n'+Content['Cross']['Output']
              ['Xml_Make_Finish'].replace('%now%', 'Reward')+Fore.RESET)
        if sys.platform == 'win32':
            os.system('PAUSE')
