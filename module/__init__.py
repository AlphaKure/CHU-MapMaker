import module.Reward as Reward
import module.MapBonus as MapBonus
import module.MapArea as MapArea
import module.Map as Map
import module.Event as Event
import module.cross as cross


def ReadConfig(section,type):
    return cross.getconfig(section,type)