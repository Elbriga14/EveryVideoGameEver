import json
import random
import io

databaseRoot = "GamesDB/"
libs = [
#("TestGames.json", "Test")
("3DSGames.json", "3DS"),
("32XGames.json", "32X"),
("AmigaCD32Games.json", "Amiga CD 32"),
("AmstradCPCGames.json", "AmstradCPC"),
("AppleIIGames.json", "Apple II"),
("ArcadeGames.json", "Arcade"),
("Atari5200Games.json", "Atari5200"),
("Atari7800Games.json", "Atari7800"),
("AtariLynxGames.json", "Atari Lynx"),
("DOSGames.json", "DOS"),
("DreamcastGames.json", "Dreamcast"),
("DSGames.json", "DS"),
("FamicomCDGames.json", "FamicomCD"),
("FMTownsGames.json", "FMTowns"),
("GamecubeGames.json", "Gamecube"),
("GameGearGames.json", "GameGear"),
("GBAGames.json", "GBA"),
("GBCGames.json", "GBC"),
("GBGames.json", "GB"),
("GizmondoGames.json", "Gizmondo"),
("IntellivisionGames.json", "Intellivision"),
("ItchIOGames.json", "Itch.io"),
("MagnavoxOdysseyGames.json", "Magnavox Odyssey"),
("MasterSystemGames.json", "MasterSystem"),
("MSXGames.json", "MSX"),
("N64Games.json", "N64"),
("NeoGeoGames.json", "Neo-Geo"),
("NeoGeoPocketColorGames.json", "Neo-Geo Pocket Color"),
("NESGames.json", "NES"),
("NgageGames.json", "NGage"),
("PC88Games.json", "PC88"),
("PC98Games.json", "PC98"),
("PCEngineGames.json", "PC-Engine"),
("PCFXGames.json", "PCFX"),
("PS1Games.json", "PS1"),
("PS2Games.json", "PS2"),
("PS3Games.json", "PS3"),
("PS4Games.json", "PS4"),
("RobloxGames.json", "Roblox"),
("SegaGenesisGames.json", "SegaGenesis/MegaDrive"),
("SegaPicoGames.json", "Sega Pico"),
("SegaSaturnGames.json", "Sega Saturn"),
("SNESGames.json", "SNES"),
("SteamGames.json", "Steam"),
("SwitchGames.json", "Switch"),
("TRS80Games.json", "TRS80"),
("VectrexGames.json", "Vectrex"),
("VirtualBoyGames.json", "VirtualBoy"),
("WiiGames.json", "Wii"),
("WiiUGames.json", "WiiU"),
("WindowsGames.json", "Windows"),
("WonderswanGames.json", "Wonderswan"),
("X68000Games.json", "X68000"),
("XBOX360Games.json", "Xbox 360"),
("XBOXGames.json", "Xbox"),
("XboxOneGames.json", "XboxOne"),
("ZeeboGames.json", "Zeebo"),
("ZXSpectrumGames.json", "ZXSpectrum")
]

database = []
dbDomaines = ""
for path in libs:
    with open(databaseRoot+path[0], encoding ='utf-8', mode='r') as file:
        database += json.loads(file.read())
        dbDomaines += " - " + path[1]


#Games_Win = open("GamesDB/WindowsGames.json", "r")

#data = json.loads(Games_Win) + json.loads(Games_DOS)
#fmt = '{Game} - {Publisher}'.format(data)
#print(data[50]['Publisher'])
#print(data.items()[2])

#print(data["Age of Empires III"]["Publisher"])
def GetRandGame():
    randI = random.randrange(0, len(database))
    game = database[randI]
    if 'Game' in game:
        if game['Game'] != None:
            gamedata = ""
            gamedata += "**"+game['Game']+"**"+" is a game"
            if 'Dev' in game:
                if game['Dev'] != None:
                    gamedata += " by "+game['Dev']+","
            if 'Year' in game:
                if game['Year']!= None:
                    gamedata += " published in "+"**"+str(game['Year'])+"**"+","
            if 'Publisher' in game:
                if game['Publisher'] != None:
                    gamedata += " published by "+game['Publisher']
            if 'Platform' in game:
                if game['Platform'] != None:
                    gamedata += " for "+game['Platform']
            if 'Genre' in game:
                if game['Genre'] != None:
                    gamedata += " (Genre: "+game['Genre']+")"
            if 'GameLink' in game:
                if game['GameLink'] != None:
                    gamedata += "\n"+ game['GameLink']
                    return gamedata
            if 'DevLink' in game:
                if game['DevLink'] != None:
                    gamedata += "\n"+game['DevLink']
                    return gamedata
            if 'PublisherLink' in game:
                if game['PublisherLink'] != None:
                    gamedata += "\n"+game['PublisherLink']
                    return gamedata
            if 'PlatformLink' in game:
                if game['PlatformLink'] != None:
                    gamedata += "\n"+game['PlatformLink']
                    return gamedata
            return gamedata
    else:
        erreur = "- - - **Error: game with no name in database** - - -"
        print(erreur)
        return(erreur)
        
    #return("**" + game['Game'] + "**" +     " est un jeu de " + "**" + game['Dev'] + "**" +    " publié par " + game['Publisher'] +  " en " + "**" + str(game['Year']) + "**" +    " pour " + game['Platform'] +   ".\n" + game['Link'])

def DataBaseInfo():
        Entries = 0
        for game in database:
            Entries += len(game)
        return (
            "**"+ f'{len(database):,}'+"**" + " games with " + f'{Entries:,}' + " data points.\n"+ 
            "**Platforms:** " + dbDomaines
        )


print (DataBaseInfo())
print(GetRandGame())