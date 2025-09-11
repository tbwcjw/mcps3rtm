# offsets and values for minecraft ps3 edition
# tbwcjw - MIT 2025
#
# credits:
# PhoenixARC, TheBlackRabbit, Misakiii, 
# MayhemModding, SkullModz, OhItzDiiTz, 
# DublinModz, EternalModz, tbwcjw, et al.


from dataclasses import dataclass, field
from typing import List, Union
from enum import Enum

class Category(Enum):
    MOBS = "Mobs"
    TIME = "Time"
    SKY = "Sky"
    WEATHER = "Weather"
    UTILITIES = "Utilities"
    GRIEF = "Grief"
    CRASH = "Crash"
    MOVEMENT = "Movement"
    XRAY = "X-Ray"
    FUN = "Fun"
    GOD = "God"
    HUD = "GUI"
    PVE = "Combat"

@dataclass
class Offset:
    address: str
    values: dict[str, Union[str, list[str]]]
    display_name: str = ""
    description: str = ""
    categories: List[Category] = field(default_factory=list)


def str_to_hex(input: str) -> list[str]:
    import sys
    print(input)
    return [hex(ord(c)) for c in input]

map = {
"NameChange": Offset(address=["0x3000ABE4", "0x3000AC54", "0x3000ACC4", "0x3000AD34", "0x3000ABA4"], #utilities
                values=str_to_hex, #callable
                display_name="Name Change",
                description="Change your displayed name. Requires relog to take effect.",
                categories=[Category.UTILITIES]), 

"SpawnMobs": Offset(address="0x004619E4", #mobs
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="No Mobs",
                description="Disables spawning of mobs, destroys mobs that players have spawned. Stops mobs from doing damage.",
                categories=[Category.MOBS]), 

"DayNight": Offset(address="0x014C6880", #time
                values={"DAY": "0x3F", "NIGHT": "0x2F"},
                display_name="Day/Night",
                description="Set the time to day or night",
                categories=[Category.TIME]),

"SunMoon": Offset(address="0x00B21F1C", #sky
                values={"REMOVE": ["0x2F", "0x80"], 
                        "4SUNS": ["0x3F", "0xFF"],
                        "MOON_BRIGHT": ["0x4F", "0xFF"],
                        "RESET": ["0x3F", "0x80"]},
                display_name="Sun/Moon",
                description="'Remove' removes the sun and moon. '4suns' creates 4 suns, makes moon brighter. 'moon_bright' maxes moon brightness.",
                categories=[Category.SKY]),

"GameSpeed": Offset(address="0x00C202C9", #time
                values={"+1": "0x60",
                        "+2": "0x70",
                        "+3": "0x80",
                        "+4": "0x90",
                        "+5": "0xF0",
                        "-1": "0x40",
                        "-2": "0x30",
                        "-3": "0x20",
                        "-4": "0x10",
                        "-5": "0x00", 
                        "DEFAULT": "0x50"},
                display_name="Game Speed",
                description="Speed up or slow down the games speed. Effects movement, look controls, mobs, daylight cycle.",
                categories=[Category.TIME]),

"CloudGlitch": Offset(address="0x00B230AD", #sky
                values={"ON": "0x70", "OFF": "0x80"},
                display_name="Cloud Glitch",
                description="Makes clouds move extremely fast, looks glitchy.",
                categories=[Category.SKY]), 

"BlueClouds": Offset(address="0x0038B964", #sky
                values={"ON": "0xFF", "OFF": "0x3D"},
                display_name="Blue Clouds/Fog",
                description="Turns clouds and fog blue.",
                categories=[Category.SKY]), 

"AutoSave": Offset(address="0x00AEEE54", #utilities
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Auto Save",
                description="Enables/disables autosaving",
                categories=[Category.UTILITIES]), 

"AutoSprint": Offset(address="0x00B01EEF", #movement
                values={"ON": "0x00", "OFF": "0x01"},
                display_name="Auto Sprint",
                description="Lock sprint on when sprint started.",
                categories=[Category.MOVEMENT]), 

"EndSky": Offset(address="0x00B22050", #sky
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="End Sky",
                description="Replace the overworld sky with the End world sky.",
                categories=[Category.SKY]), 

"LockGamemode": Offset(address="0x002F03D0", #utilities
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Lock Gamemode",
                        description="Lock Gamemode to current gamemode",
                        categories=[Category.UTILITIES]),

"LockWeather": Offset(address="0x00393E84", #utilities, weather
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Lock Weather",
                        description="Lock weather to current weather",
                categories=[Category.UTILITIES, Category.WEATHER]),

"AntiJoin": Offset(address="0x0098871F", #utilities
                values={"ON": "0x01", "OFF": "0x00"},
                display_name="AntiJoin",
                description="Prevents other players from joining the world",
                categories=[Category.UTILITIES]), 

"CreeperNoGrief": Offset(address="0x001CC827", #grief, mobs
                        values={"ON": "0x00", "OFF": "0x01"},
                        display_name="Creeper No Grief",
                        description="Prevents creepers from destroying blocks. This only works when host options has mob griefing turned off, any you WANT creepers to grief.",
                        categories=[Category.GRIEF, Category.MOBS]),

"CreeperInstantExplode": Offset(address="0x001CCC2C", #mobs
                                values={"ON": "0x40", "OFF": "0x41"},
                                display_name="Creepers Instantly Explode",
                                description="Make creepers explode instantly (on spawn).",
                                categories=[Category.MOBS]),

"CreeperFireExplode": Offset(address="0x001CC894", #mobs
                values={"ON": ["0x39", "0x40", "0x00", "0x10"], 
                        "OFF": ["0x39", "0x40", "0x00", "0x00"]},
                display_name="Creeper Fire Explosion",
                description="Creepers explode and spread fire.",
                categories=[Category.MOBS]),

"CreeperLargeExplode": Offset(address="0x001CC7E0", #grief, mobs
                values={"ON": ["0x42", "0xFF"], 
                        "OFF": ["0x3F", "0x80"]},
                display_name="Creeper Large Explosion",
                description="Creepers have a large (32x32) distruction radius. Causes massive server lag spike. ",
                categories=[Category.GRIEF, Category.MOBS]),

"CreeperMediumExplode": Offset(address="0x001CC7E0", #grief, mobs
                values={"ON": ["0x3F", "0xFF"], 
                        "OFF": ["0x3F", "0x80"]},
                display_name="Creeper Medium Explosion",
                description="Creepers have a 9x9 distruction radius.",
                categories=[Category.GRIEF, Category.MOBS]),

"BigCreeper": Offset(address="0x001CC81C",  #mobs
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Big Creepers",
                        description="Creepers don't die after exploding. Their positions freeze, and you are constantly hurt inside their grief radius.",
                        categories=[Category.MOBS]), 

"TNTNoGrief1": Offset(address="0x00245DEB", #grief
                        values={"ON": "0x00", "OFF": "0x01"},
                        display_name="TNT No Grief (Part 1)",
                        description="Prevents TNT from destroying blocks. (1/2)",
                        categories=[Category.GRIEF]),

"TNTNoGrief2": Offset(address="0x00245DF0", #grief
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="TNT No Grief (Part 2)",
                        description="Prevents TNT from destroying blocks. (2/2)",
                        categories=[Category.GRIEF]),

"TNTDown": Offset(address="0x0051E558", #utilities
                values={"ON": "0x4F", "OFF": "0x3F"},
                display_name="TNT Down",
                description="TNT Disappears, Exposion particles and sound effect still play.",
                categories=[Category.UTILITIES]), 

"TNTSilent": Offset(address="0x00245BE4", #grief
                values={"ON": ["0xFF", "0x60", "0x18", "0x90"], 
                        "OFF": ["0xFF", "0x60", "0x08", "0x90"]},
                display_name="Silent TNT",
                description="Makes TNT explosions silent. The fuse 'hiss' is still audible.",
                categories=[Category.GRIEF]), 

"TNTMoreParticles": Offset(address="0x00245E58", #fun
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="TNT More Particles",
                        description="Makes TNT spawn more particles when exploding. Also seems to break rotation of particles.",
                        categories=[Category.FUN]),

"TNTNoDelay": Offset(address="0x0051E6A0", #grief
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="TNT No Delay",
                        description="Make TNT explode instantly when ignited",
                        categories=[Category.GRIEF]),

"DamageAll": Offset(address="0x0039E2D4", #grief
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Damage All Players",
                description="Damage all players over time, until OFF.",
                categories=[Category.GRIEF]),

"StopAll": Offset(address="0x004668B6", #utilities, grief, movement
                values={"ON": "0x78", "OFF": "0x08"},
                display_name="Stop All Payer Movement",
                description="Stops all player movement until OFF.",
                categories=[Category.GRIEF, Category.UTILITIES, Category.MOVEMENT]),

"NormalMove": Offset(address="0x004668B6", #utilities, movement
                values={"ON": "0x78", "OFF": "0x26"},
                display_name="Normal Movement Speed",
                description="Set movement speed to default.",
                categories=[Category.UTILITIES, Category.MOVEMENT]),

"FastMove1": Offset(address="0x003ABD49", #movement
                        values={"ON": ["0xFF", "0xFF", "0xFF"], 
                                "OFF": ["0x26", "0xAD", "0x89"]},
                        display_name="Fast Movement (1/5)",
                        description="(Slowest) Increase movement speed of all players until off.",
                        categories=[Category.MOVEMENT]),

"FastMove2": Offset(address="0x003AA999", #movement
                        values={"ON": "0x00", "OFF": "0x68"},
                        display_name="Fast Movement (2/5)",
                        description="Increase movement speed of all players until off.",
                        categories=[Category.MOVEMENT]),

"FastMove3": Offset(address="0x003ABD48", #movement
                        values={"ON": ["0x3F", "0xFF", "0x00", "0x01"], 
                                "OFF": ["0x3E", "0x26", "0xAD", "0x89"]},
                        display_name="Fast Movement (3/5)",
                        description="Increase movement speed of all players until off.",
                        categories=[Category.MOVEMENT]),

"FastMove4": Offset(address="0x003AA998", #movement
                        values={"ON": "0x3E", "OFF": "0x3F"},
                        display_name="Fast Movement (4/5)",
                        description="Increase movement speed of all players until off. Breaks some collisions.",
                        categories=[Category.MOVEMENT]),

"FastMove5": Offset(address="0x003ABD48", #movement
                        values={"ON": ["0x41", "0xFF"], 
                                "OFF": ["0x3E", "0x26"]},
                        display_name="Fast Movement (5/5)",
                        description="(Fastest) Increase movement speed of all players until off. Breaks some collisions.",
                        categories=[Category.MOVEMENT]),

"LeftHandAll": Offset(address="0x0151F2F0", #utilities
                        values={"ON": ["0x30", "0x01", "0x87", "0xF0"], 
                                "OFF": [ "0x30", "0x01", "0x87", "0xF8"]},
                        display_name="Left Hand (All players)",
                        description="With empty hand, show left hand. Map in left hand will display on right.",
                        categories=[Category.UTILITIES]),

"NoRunAll": Offset(address="0x00018CE4", #utilities, movement
                        values={"ON": ["0xFF", "0xE0", "0x28", "0x90"], 
                                "OFF": ["0xFF", "0xE0", "0x08", "0x90"]},
                        display_name="No Run (All players)",
                        description="Disallow all players to run",
                        categories=[Category.MOVEMENT, Category.UTILITIES]),

"DisablePortals": Offset(address="0x002379E7", #utilities
                values={"ON": "0x00", "OFF": "0x01"},
                display_name="Disable Portals",
                description="Portals will not work, but do display.",
                categories=[Category.UTILITIES]),

"DirtNetherPortal": Offset(address="0x014C89FE", #utilities
                values={"ON": ["0x14", "0x70"], 
                        "OFF": ["0x5E", "0x70"]},
                display_name="Dirt Nether Portals",
                description="Build Nether Portals out of minecraft:dirt.",
                categories=[Category.UTILITIES]),

"StoneNetherPortal": Offset(address="0x014C89FE", #utiltites
                values={"ON": ["0x11", "0xC0"], 
                        "OFF": ["0x5E", "0x70"]},
                display_name="Stone Nether Portals",
                description="Build Nether Portals out of minecraft:stone (NOT cobblestone).",
                categories=[Category.UTILITIES]),

"DisableChunkLoading": Offset(address="0x00B2437C", #grief, crash, utilities
                        values={"ON": ["0x4E", "0x80", "0x00", "0x20"], 
                                "OFF": ["0xF8", "0x21", "0xFF", "0x71"]},
                        display_name="Disable Chunk Loading",
                        description="New chunks will not load. This can cause crashes, especially when switching between the overworld, nether and end.",
                        categories=[Category.UTILITIES, Category.GRIEF, Category.CRASH]),

"OptimizeChunkLoading": Offset(address="0x00B21C61", #utilities
                        values={"ON": "0xD7", "OFF": "0x30"},
                        display_name="Optimize Chunk Loading",
                        description="New chunks will not load. This can cause crashes, especially when switching between the overworld, nether and end.",
                        categories=[Category.UTILITIES]),

"ExtremeFastBreakAll": Offset(address="0x0010E0C4", #grief
                        values={"ON": ["0xFF", "0xE0", "0x18", "0x90"], 
                                "OFF": ["0xFF", "0xE0", "0x08", "0x90"]},
                        display_name="Extremely Fast Break (All players)",
                        description="All players can break blocks extemely fast, works in survival.",
                        categories=[Category.GRIEF]),

"FastBreakAll": Offset(address="0x0010E0C4", #grief
                        values={"ON": ["0xFF", "0xE0", "0x28", "0x90"], 
                                "OFF": ["0xFF", "0xE0", "0x08", "0x90"]},
                        display_name="Fast Break (All players)",
                        description="All players can break blocks faster, works in survival.",
                        categories=[Category.GRIEF]),

"FastBreak": Offset(address="0x00AEB11C", #grief
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="Fast Break",
                description="Break blocks faster, seemingly only works in creative.",
                categories=[Category.GRIEF]),

"FastWalk": Offset(address="0x003ABD49", #movement
                values={"ON": "0x86", "OFF": "0x26"},
                display_name="Fast Walk",
                description="Increases walking speed",
                categories=[Category.MOVEMENT]),

"BabyPlayer": Offset(address="0x0039F52F", #fun
                values={"ON": "0x01", "OFF": "0x00"},
                display_name="Baby Player",
                description="Makes the player model babby sized.",
                categories=[Category.FUN]),

"SillyWalk": Offset(address="0x002341D0", #fun
                values={"ON": "0xC3", "OFF": "0xC0"},
                display_name="Fast Walk",
                description="Player model does a silly walk. Approved by the Ministry of Silly Walks.",
                categories=[Category.FUN]),
                
"FastBuild": Offset(address="0x00AECE70", #grief
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Fast Build",
                description="Place blocks without delay Only works in survival.",
                categories=[Category.GRIEF]), 

"DriftBoat": Offset(address="0x002278E4", #fun
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="Drift Boats",
                description="Make boats drift",
                categories=[Category.FUN]), 

"BreakBoats": Offset(address="0x000E0F90", #utilities
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="Break Boats",
                description="Boats are no longer rideable.",
                categories=[Category.UTILITIES]), 

"StopXPGain": Offset(address="0x004B00AC", #utilties
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="Stop XP Gain",
                description="Keeps current XP, but cannot gain anymore.",
                categories=[Category.UTILITIES]),

"MaxXP": Offset(address="0x004B0094", #utilities
                values={"ON": ["0x7C", "0xA5", "0x10", "0x14"], 
                        "OFF": ["0x7C", "0xA5", "0x20", "0x14"]},
                display_name="Max XP",
                description="Throw a bottle o' enchanting or collect an experience orb to get the maximum XP level.",
                categories=[Category.UTILITIES]),

"KillAllPlayers": Offset(address="0x00226168", #grief
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Kill All",
                        description="Kills all and players.",
                categories=[Category.GRIEF]),

"GodMode": Offset(address="0x004B2021", #utilities, god
                values={"ON": "0x80", "OFF": "0x20"},
                display_name="God Mode",
                description="Godlike.",
                categories=[Category.UTILITIES, Category.GOD]), 

"DemiGodMode": Offset(address="0x003A4064",  #utilities, god
                        values={"ON": ["0xFF", "0x40", "0x88", "0x90"], 
                                "OFF": ["0xFF", "0x40", "0x08", "0x90"]},
                        display_name="Demi God Mode",
                        description="Demi Godlike.",
                        categories=[Category.UTILITIES, Category.GOD]),

"LightningBolt": Offset(address="0x0098871F", #grief, crash
                        values={"ON": "0x01", "OFF": "0x00"},
                        display_name="Lightning Bolt",
                        description="Spams lightning, only works during stormy weather.",
                        categories=[Category.GRIEF, Category.GOD]), 

"EnableRain": Offset(address="0x00393F8F", #utilities
                        values={"ON": "0x01", "OFF": "0x00"},
                        display_name="Enable Rain",
                        description="Toggles rain. Sometimes needs a manual reset via host options.",
                        categories=[Category.UTILITIES]),

"EntityGodMode": Offset(address="0x003A3F6C", #god
                        values={"ON": "0x40", "OFF": "0x41",},
                        display_name="Entity God Mode",
                        description="Give mobs God Mode",
                        categories=[Category.GOD]),

"NoSlowWeb": Offset(address="0x00234F9F", #utilities
                values={"ON": "0x00", "OFF": "0x01"},
                display_name="Spider Web Slow Movement",
                description="Toggles slow movement through spiders webs",
                categories=[Category.UTILITIES]),

"DisableGravity": Offset(address="0x00246A2C", #utilities
                        values={"ON": "0xFF", "OFF": "0x3F"},
                        display_name="Disable Gravity",
                        description="Stop blocks like gravel from falling.",
                        categories=[Category.UTILITIES]),

"DisableMobEggs": Offset(address="0x005BF34E", #utilties, mobs
                        values={"ON": "0x48", "OFF": "0x08"},
                        display_name="Kill Mob Spawn",
                        description="Prevents mobs from being spawned in with spawn eggs",
                        categories=[Category.UTILITIES, Category.MOBS]), 

"BurnInWater": Offset(address="0x00225EA8", #grief, utilities
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Burn In Water",
                        description="Makes players and entities burn in water.",
                        categories=[Category.UTILITIES, Category.GRIEF]), 

"InfinitePlace": Offset(address="0x0010673F", #grief, utilites
                        values={"ON": "0x00", "OFF": "0x01"},
                        display_name="Infinite Place",
                        description="Infinite block placement in survival, stacks will not descrease.",
                        categories=[Category.UTILITIES, Category.GRIEF]), 

"InfiniteCraft": Offset(address="0x0098871F", #grief, utilities
                        values={"ON": "0x01", "OFF": "0x00"},
                        display_name="Infinite Craft",
                        description="Craft anything in survival without the required materials",
                        categories=[Category.UTILITIES, Category.GRIEF]), 

"InfiniteBreath": Offset(address="0x0039DE28", #utilities
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Infinite Breath",
                        description="Underwater breath never runs out.",
                        categories=[Category.UTILITIES]),

"NoFall": Offset(address="0x003A409C", #utilities
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Disable Fall Damage",
                description="Player doesn't take fall damage",
                categories=[Category.UTILITIES]), 

"GlitchMob": Offset(address="0x00EA89E2", #mob, fun
                values={"ON": "0x18", "OFF": "0x08"},
                display_name="Glitch Out Mobs",
                description="Mobs will catch fire, die, lay on the ground dead.",
                categories=[Category.MOBS, Category.FUN]),

"NoPickup": Offset(address=["0x00310B0C","0x004A3FB8"], #grief, utilities
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="No Pickup",
                description="Prevents the picking up of dropped items",
                categories=[Category.UTILITIES, Category.GRIEF]),

"MaxPickup": Offset(address="0x00310AD4", #grief
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="Max Pickup",
                description="Duplicate dropped items into stacks.",
                categories=[Category.GRIEF]),

"UnlimitedArrows": Offset(address="0x00224B13", #utilities
                        values={"ON": "0x00", "OFF": "0x01"},
                        display_name="Unlimited Arrows",
                        categories=[Category.UTILITIES]),

"RemoveArrows": Offset(address="0x000FB644", #utilities
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Remove Arrows",
                        description="Arrows won't be taken from inventory",
                        categories=[Category.UTILITIES]), #decrement from stack if on

"BlockArrows": Offset(address="0x000FB55C", #utilities
                        values={"ON": "0x80", "OFF": "0x40"},
                        display_name="Block Arrows",
                        description="The velocity of arrows is set to zero. Making arrows impossible to fire.",
                        categories=[Category.UTILITIES]), 

"AirToWater": Offset(address="0x001D7FCC", #grief
                values={"ON": "0x40", 
                        "OFF": "0x41"},
                display_name="Air To Water",
                description="Replaces all air blocks with water.",
                categories=[Category.GRIEF]),

"AutoLadder": Offset(address="0x003A74F3", #utilities
                        values={"ON": "0x01", "OFF": "0x00"},
                        display_name="Auto Ladder",
                        description="Climb blocks like a spider.",
                        categories=[Category.UTILITIES, Category.MOVEMENT]), #climb walls like a spider

"CrouchRun": Offset(address="0x00B0142B", #utilities
                values={"ON": "0x01", "OFF": "0x00"},
                display_name="Crouch and Run",
                description="Makes the player crouch and run, locks crouch on.",
                categories=[Category.UTILITIES]),

"NoEntityCollision": Offset(address="0x000108AC", #utilities, grief
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Full No Collide",
                        description="Player and entities don't collide with objects.",
                        categories=[Category.UTILITIES, Category.XRAY]), #player and entities dont collide with objects

"NoCollisionBypass": Offset(address="0x002271B0", #utilities, grief
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Self No Collide",
                        description="Player doesn't collide with objects, entities do. Also makes dropped items bounce.",
                        categories=[Category.UTILITIES, Category.XRAY]), #bounces dropped items, clip through blocks

"MaxRiptide": Offset(address="0x00217DCF", #utilities
                        values={"ON": "0x08", "OFF": "0x00"},
                        display_name="Max Riptide",
                        description="Maximum level riptide on trident, only useful in water.",
                        categories=[Category.UTILITIES]),

"MakeRain": Offset(address="0x00A9B23E", #weather
                values={"ON": "0x48", "OFF": "0x08"},
                display_name="Make It Rain",
                description="Rain, without other atmospheric/weather effects.",
                categories=[Category.WEATHER]),

"NightVision": Offset(address="0x00A9A6C8", #utilities
                        values={"ON": "0x7F", "OFF": "0x3F"},
                        display_name="Night Vision",
                        description="Increase visibility in the dark.",
                        categories=[Category.UTILITIES]), 

"Levitation": Offset(address="0x003ABDD0", #utilities
                        values={"ON": "0xBF", "OFF": "0x3F"},
                        display_name="Levitate",
                        description="All Entities slowly float toward the heavens",
                        categories=[Category.UTILITIES]), 

"RemoveText": Offset(address="0x007865EC", #utilities, hud
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Remove Text",
                        description="Remove text from GUI elements and menus",
                        categories=[Category.UTILITIES, Category.HUD]),
        
"BreakCamera": Offset(address="0x00A97F34", #fun
                        values={"ON": "0xDF", "OFF": "0x3F"},
                        display_name="Break Camera",
                        description="Remove camera anchors from player, breaking it in a fun way.",
                        categories=[Category.FUN]), 

"BetterTime": Offset(address="0x00A9A6DC", #time
                        values={"ON": "0x0F", "OFF": "0x3F"},
                        display_name="Better Time",
                        description="More atmospheric lighting, better shadows.",
                        categories=[Category.TIME]),

"MoonGravity": Offset(address="0x003ABF88", #fun
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Moon Gravity",
                        description="Slow falling, longer movement momentum rollup, higher jumping.",
                        categories=[Category.FUN, Category.MOVEMENT]),

"WalkInSky": Offset(address="0x00011B00", #utilities, fun
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Walk In The Sky",
                description="Move player to the top Y coordinate, player will be unable to change Y coord.",
                categories=[Category.UTILITIES, Category.MOVEMENT]),

"SkipAlong": Offset(address="0x00A857D1", #fun
                values={"ON": "0x00", "OFF": "0x80"},
                display_name="Skip Along",
                description="Causes players legs to 'skip' while walking.",
                categories=[Category.FUN, Category.MOVEMENT]),

"WallHack": Offset(address="0x00A98F50", #grief, utilities
                values={"ON": "0x3F", "OFF": "0x3D"},
                display_name="Wall Hack",
                description="Look through walls, when close enough to them",
                categories=[Category.UTILITIES, Category.XRAY]),

"Nameplate": Offset(address="0x00AD8158", #utilties
                values={"ON": "0x4C", "OFF": "0x2C"},
                display_name="Nameplate",
                description="Display nameplates for players, and self.",
                categories=[Category.UTILITIES]),

"ActiveNameplate": Offset(address="0x00AD8110", #utilities
                values={"ON": ["0xFF", "0xC0", "0xE0", "0x90"],
                        "OFF": ["0xFF", "0xC0", "0x10", "0x90"]},
                display_name="Activity Nameplate",
                description="When used in conjunction with `Nameplate` command, nameplates will move up and down depending on movement speed.",
                categories=[Category.UTILITIES]), 

"FlatBlocks": Offset(address="0x000924FF", #utilties, hud
                values={"ON": "0x01", "OFF": "0x00"},
                display_name="Flat Blocks",
                description="Blocks in the inventory will appear flat.",
                categories=[Category.UTILITIES, Category.HUD]),


"SuperKnockback": Offset(address="0x003ABF3C", #pve
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Super Knockback",
                        description="Insane amount of knockback on entities. Can break walking functionality. Causes entity lag.",
                categories=[Category.PVE]), #stupid amount of knockback, breaks walking

"ReverseKnockback": Offset(address="0x003A4018", #pve
                values={"ON": ["0xBF", "0x80"],
                        "OFF": ["0x3E", "0xCC"]},
                display_name="Reverse Knockback",
                description="Hitting players or entities will knock them back into you. And they will hit you into them.",
                categories=[Category.PVE]),

"AutoWalk": Offset(address="0x003ABE18", #utilities
                values={"ON": ["0xFF", "0x40"],
                        "OFF": ["0xFF", "0x20"]},
                display_name="Auto Walk",
                description="Walk forever in the direction facing. Stops when flying.",
                categories=[Category.UTILITIES]),

"AntiKnockback": Offset(address="0x003A4018", #pve
                values={"ON": ["0x00", "0x00"],
                        "OFF": ["0x3E", "0xCC"]},
                display_name="Anti Knockback",
                description="Remove's all knockback from you, entities and players.",
                categories=[Category.PVE]),

"NoRun": Offset(address="0x00B022F8", #utilities
                values={"ON": "0x4C", "OFF": "0x2C"},
                display_name="No Running",
                description="Disables running",
                categories=[Category.UTILITIES]), 

"InstantMine": Offset(address="0x00AEB090", #utilties
                        values={"ON": "0xBF", "OFF": "0x3F"},
                        display_name="Instant Mine",
                        description="Break blocks instantly.",
                        categories=[Category.UTILITIES]), 

"InstantKillFire": Offset(address="0x002258F8", #grief
                        values={"ON": ["0x4F", "0x80"], 
                                "OFF": ["0x3F", "0x80"]},
                        display_name="Instant Kill Fire",
                        description="Touching fire instantly kills players and entities",
                        categories=[Category.GRIEF]),

"NoAutoRegen": Offset(address="0x002ADCE8", #utilities
                        values={"ON": [ "0x68", "0x63", "0x00", "0x00"], 
                                "OFF": ["0x68", "0x63", "0x00", "0x01"]},
                        display_name="No Auto Regen",
                        description="No health regeneration",
                        categories=[Category.UTILITIES]),

"DeadScreen": Offset(address="0x003A7654", #fun
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Death Screen",
                        description="Bring up the animated red HUD overlay",
                        categories=[Category.FUN]),

"FloatUp": Offset(address="0x003ABDC8", #fun
                values={"ON": "0x3F", "OFF": "0xBF"},
                display_name="Float Up",
                description="Float to the top Y coord, with increasing momentum.",
                categories=[Category.FUN, Category.MOVEMENT]), 

"InvertPlayer": Offset(address="0x00A99420", #fun
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Invert Player Controls",
                        description="Up is Left, Down is Right, Right is Left, Left is Right... That makes sense, right? left?",
                        categories=[Category.FUN, Category.MOVEMENT]), 

"LockInBlock": Offset(address="0x00389B3C", #utilities
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Lock In Block",
                        description="Lock player movement to block player is on.",
                        categories=[Category.MOVEMENT, Category.UTILITIES]),

"NoFlight": Offset(address="0x00B02368", #utilities
                values={"ON": "0x41", "OFF": "0x40"},
                display_name="No Flight",
                description="Disable flying",
                categories=[Category.UTILITIES, Category.MOVEMENT]), #disable flight

"AntiKick": Offset(address="0x00AEE434", #grief, utilities
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="AntiKick",
                description="Prevent player being kicked from the session. TODO: test this.",
                categories=[Category.UTILITIES]),

"ShowBlockID": Offset(address="0x003097C8", #hud, utilities
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Show Block ID's",
                        description="Show numeric block ID (Format: #0000/00) on tooltips.",
                        categories=[Category.UTILITIES, Category.HUD]), #numeric block id

"ShowBlockName": Offset(address="0x003097B8", #hud, utilities
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Show Block Names",
                        description="Show alphanumeric block name (Format: minecraft:dirt) identifiers on tooltips.",
                         categories=[Category.UTILITIES, Category.HUD]),

"StaticControls": Offset(address="0x00AEFE64", #utilities
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Static Controls",
                        description="Camera and movement speed is static",
                        categories=[Category.UTILITIES]),

"StaticLook": Offset(address="0x00A98FA4", #utilities
                        values={"ON": [ "0xFF", "0xA0", "0x18", "0x90"], 
                                "OFF": ["0xFF", "0xA0", "0x08", "0x90"]},
                        display_name="Static Look Speed",
                        description="Camera movement speed is static.",
                        categories=[Category.UTILITIES]),

"PriviFlight": Offset(address="0x00B02378", #utilities
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Privilieged Flight",
                        description="Whether or not privileged players (op, mod) can fly.",
                        categories=[Category.UTILITIES]), #privileged (op, mod) player flight,

"StuckFlying": Offset(address="0x00B023EC", #utilities
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Stuck Flight",
                description="Disallow falling while flying, keeps the player flying",
                categories=[Category.UTILITIES, Category.MOVEMENT]), 

"CrashSelf": Offset(address="0x00785DBC", #grief, crash
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="(!!) Crash Game for Self",
                description="Crash your game to the XMB. Be careful, data loss is possible.",
                categories=[Category.GRIEF, Category.CRASH]), #crash game to xmb

"CrashOther": Offset(address="0x00AD8320", #grief, crash
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="(!!) Crash Game for Players",
                        description="Crash the game to the XMB for other players. This is a dick move. TODO: Check this works",
                        categories=[Category.GRIEF, Category.CRASH]), 

"SwimGlitch": Offset(address="0x00B0229C", #fun, movement
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Swim Glitch",
                        description="Swim anywhere by going into fast swim, then leaving the water.",
                        categories=[Category.FUN, Category.MOVEMENT]), 

"InvertSwimMovement": Offset(address="0x003ABD44", #fun, movement
                                values={"ON": "0xBC", "OFF": "0x3C"},
                                display_name="Invert Swimming Movement",
                                description="Invert the movement controls while swimming",
                                categories=[Category.FUN, Category.MOVEMENT]),

"DisableSwim": Offset(address="0x0034B8F4", #utilities, movement
                        values={"ON": "0x41", "OFF": "0x40"},
                        display_name="Disable Swimming",
                        description="Disables fast swimming, regular swimming is unaffected.",
                        categories=[Category.UTILITIES, Category.MOVEMENT]),

"JumpForwardSpeed": Offset(address="0x003AA999", #utilties, movement
                        values={"ON": "0xA0", "OFF": "0x68"},
                        display_name="Super Speed (Jumping)",
                        description="Multiplies movement speed (non Y axis) while jumping",
                        categories=[Category.UTILITIES, Category.MOVEMENT]), 

"SuperJump": Offset(address="0x003AA77C", #utilties, movement
                values={"ON": "0x3F", "OFF": "0x3E"},
                display_name="Super Jump",
                description="Fast jumps, doesn't affect height, only affects speed of jumping.",
                categories=[Category.UTILITIES, Category.MOVEMENT]), #quick jumps

"SpaceJump": Offset(address="0x00011ADC", #fun, movement
                values={"ON": "0x40", "OFF": "0x41"},
                display_name="Space Jump",
                description="Jump to the max Y coordinate",
                categories=[Category.FUN, Category.MOVEMENT]), 

"AngledGravity": Offset(address="0x002271F4", #fun, movement
                values={"ON": ["0xFC", "0x80"], 
                        "OFF": ["0xFC", "0x20"]},
                display_name="Angled Gravity",
                description="Makes gravity happen at a 45 degree angle, affects jumping and falling.",
                categories=[Category.FUN, Category.MOVEMENT]),

"MultiJumpNoFallDamage": Offset(address="0x0022790B", #movement, utilities
                                values={"ON": "0x14", "OFF": "0x18"},
                                display_name="MultiJump (No Fall Damage)",
                                description="Allows jumping while in a jump, does not take fall damage.",
                                categories=[Category.UTILITIES, Category.MOVEMENT]),

"MultiJump": Offset(address="0x003B000A", #movement, utilities
                values={"ON": "0x02", "OFF": "0x01"},
                display_name="Multi Jump",
                description="Allow jumping while in a jump.",
                categories=[Category.FUN, Category.MOVEMENT]), 

"HitDistance": Offset(address="0x00233290", 
                values={"FAR": "0xFF", "HALF": "0x7F", "DEFAULT": "0x00"},
                display_name="Hit Distance",
                description="Increase the distance you can hit entities from.",
                categories=[Category.PVE]),

"SpamAttack": Offset(address="0x00AEBED4", 
                        values={"ON": "0xBE", "OFF": "0x3E"},
                        display_name="Spam Attack",
                        description="Holding R2 will cause the player to attack quickly, removes delay.",
                        categories=[Category.PVE]), 
                        
"RemoveWater": Offset(address="0x00225E80", 
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Remove Water",
                        description="TODO: Figure out what this does"),
                        
"XToHit": Offset(address="0x00AEEB83", 
                values={"ON": "0x0F", "OFF": "0x01"},
                display_name="X To Hit",
                description="Pressing X key will trigger the 'Action' button, usually R2.",
                categories=[Category.PVE, Category.UTILITIES]),

"QuickMobs": Offset(address="0x003AFB60", 
                        values={"ON": "0x4F", "OFF": "0x3F"},
                        display_name="Quick Mobs",
                        description="Makes mobs extremely fast.",
                        categories=[Category.MOBS, Category.MOVEMENT]),

"BlockStatic": Offset(address="0x00AE3C3F", 
                        values={"ON": "0x01", "OFF": "0x00"},
                        display_name="Block Static",
                        description="TODO: Figure out what this does"),

"InstantHit": Offset(address="0x00AEBED4", 
                        values={"ON": "0xFF", "OFF": "0x3E"},
                        display_name="Instant Hit",
                        description="TODO: Figure out what this does"),

"WolfRemoveWater": Offset(address="0x006C0630", 
                        values={"ON": "0x40", "OFF": "0x41"},
                        display_name="Wolf Remove Water",
                        description="Stops water from being placed around wolves. TODO: not sure what else this does"), 

"XRay": Offset(address="0x00A99154", #grief, utilities, xray
                values={"ON": ["0xFC", "0x80", "0x30", "0x90"], 
                        "OFF": ["0xFC", "0x60", "0x30", "0x90"]},
                display_name="XRay",
                description="See through structures.",
                categories=[Category.GRIEF, Category.UTILITIES, Category.XRAY]),

"WaterJump": Offset(address="0x003ABD68", #movement
                values={"ON": ["0x3F", "0xF9", "0x99", "0x99"],
                        "OFF": ["0x3F", "0xE9", "0x99", "0x99"]},
                display_name="Jump out of water",
                description="Hold jump in water to propel upwards and jump out of the water with momentum.",
                categories=[Category.MOVEMENT]),

"GunItems": Offset(address="0x014C6880",
                values={"ON": ["0x3F", "0xFF"],
                        "OFF": ["0x3F", "0x80"]},
                display_name="GunItems",
                description="TODO: not sure what this does"),

"Suicide": Offset(address="0x003ABDD0", #utilties
                values={"ON": ["0x3F", "0xFF"],
                        "OFF": ["0x3F", "0xEF"]},
                display_name="Suicide",
                description="Jump flings you to the top of the map at max speed, then down to the bottom of the map at max speed, killing you.",
                categories=[Category.UTILITIES]),    

"ForceThunder": Offset(address="0x00393E34", #weather
                values={"ON": ["0xFF", "0x80"],
                        "OFF": ["0x3F", "0x80"]},
                display_name="Force Thunder",
                description="If the weather is in 'rain' mode, this will force it to be in 'thunder' mode instead.",
                categories=[Category.WEATHER]),

"RainToSnow": Offset(address="0x01310954", #weather
                values={"ON": "0x7E",
                        "OFF": "0x3E"},
                display_name="Rain To Snow",
                description="Makes it snow in non-snow biomes, when its raining. Used in conjunction with ForceThunder it causes an epileptic nightmare.",
                categories=[Category.WEATHER]),

"GlitchedWeather": Offset(address="0x00393E34", #weather, crash
                values={"ON": ["0x4F", "0x80"],
                        "OFF": ["0x3F", "0x80"]},
                display_name="Rainbow Storm",
                description="Works best in Thunder weather mode. Horizon flashes different colors, sky changes colors, particles quadruple, lighting changes. Very glitchy, A great way to lag and crash your came. Changing weather mode while ON will crash game.",
                categories=[Category.WEATHER, Category.CRASH]),

"DisableStars": Offset(address="0x0038C658", #sky
                values={"ON": "0xFF",
                        "OFF": "0x3F"},
                display_name="Disable Stars",
                description="Turn off stars in the night sky",
                categories=[Category.SKY]),


"SkyColor": Offset(address="0x00410734", #sky
                values={"LIGHTGREEN": ["0x40", "0x50"],
                        "GREEN": ["0x41", "0x50"],
                        "PURPLE": ["0x49", "0xC0"],
                        "LAVENDER": ["0x42", "0xC0"],
                        "ORANGE": ["0x43", "0xC0"],
                        "YELLOW": ["0x46", "0xC0"],
                        "FLESH": ["0x00", "0xFF"],
                        "CYAN": ["0x4A", "0xC0"],
                        "BLACK": ["0xFF", "0xFF"],
                        "RESET": ["0x40", "0xC0"],
                },
                display_name="Sky Color",
                description="Change the color of the sky",
                categories=[Category.SKY]),

"GUIColor": Offset(address="0x30DBAD64", #hud
                values={"RED": ["0x3F", "0x80", "0x00", "0x00", "0x4F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00" ],
                        "PURPLE": ["0x3F", "0x80", "0x00", "0x00", "0x1F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00"],
                        "GREEN": [ "0X5F", "0x80", "0x00", "0x00", "0x5F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00" ],
                        "BLUE": ["0x00", "0x80", "0x00", "0x00", "0x8F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00" ],
                        "RESET": ["0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00"],
                },
                display_name="GUI Color",
                description="Change the color of the GUI and HUD.",
                categories=[Category.HUD]),

"HideGUI": Offset(address="0x30DBAD64", #hud, utilities
                values={"ON": ["0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00", "0x00"],
                        "OFF": ["0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00", "0x3F", "0x80", "0x00", "0x00"],
                },
                display_name="Hide GUI",
                description="Hide the GUI, including all menus and HUD.",
                categories=[Category.HUD, Category.UTILITIES]),


"Spectator": Offset(address="0x014C9048", #utilities
                values={"ON": ["0x32", "0x3A", "0x84", "0xC0"],
                        "OFF": ["0x32", "0x39", "0x4B", "0xD0"]},
                display_name="Spectator Mode",
                description="Adds 'spectator mode' to the gamemodes. You can switch to it in Host Options.",
                categories=[Category.UTILITIES]),

"SpectralArrows": Offset(address="0x014C90D4", #pve
                values={"ON": ["0x32", "0x20", "0x8D", "0xA0"],
                        "OFF": ["0x32", "0x1E", "0xAD", "0xA0"]},
                display_name="Spectral Arrows",
                description="Fired arrows become spectral arrows on pickup.",
                categories=[Category.PVE]),

"StopBow": Offset(address="0x000FB4C5", #utilities
                values={"ON": ["0xE0", "0x58"],
                        "OFF": ["0xE0", "0x08"]},
                display_name="Stop Bow",
                description="Bow will not fire.",
                categories=[Category.UTILITIES]),

"ExtremeCamSens": Offset(address="0x00ABA948", #utilities, movement
                values={"ON": ["0x44", "0xFF"],
                        "OFF": ["0x42", "0x48"]},
                display_name="Extreme Camera Sensitivity",
                description="Extreme look control sensitivity.",
                categories=[Category.UTILITIES, Category.MOVEMENT]),

"FastCamSens": Offset(address="0x00ABA948",
                values={"ON": ["0x42", "0xFF"],
                        "OFF": ["0x42", "0x48"]},
                display_name="Fast Camera Sensitivity",
                description="Fast look control sensitivity.",
                categories=[Category.UTILITIES]),

"TeleportKill": Offset(address="0x003AFB60", #grief
                values={"ON": ["0xFF", "0xFF", "0xFF", "0xFF"],
                        "OFF": ["0x3F", "0x7A", "0xE1", "0x48"]},
                display_name="Teleport and Kill",
                description="Teleport all entities and players to you, and kill them.",
                categories=[Category.GRIEF]),

"FastBow": Offset(address="0x000FB4C5", #grief, pve
                values={"ON": ["0xE0", "0x18", "0x18"],
                        "OFF": ["0xE0", "0x08", "0x18"]},
                display_name="Fast Bow",
                description="Bow fires at maximum velocity without fully drawing.",
                categories=[Category.GRIEF, Category.PVE]),

"FloorCam": Offset(address="0x004B1CE0", #fun
                values={"ON": ["0xFC", "0x02", "0x10"],
                        "OFF": ["0xFC", "0x01", "0x10"]},
                display_name="Floor Camera",
                description="Places the camera at the feet of the player",
                categories=[Category.FUN]),

"R3FloorCam": Offset(address="0x004B1D60", #fun
                values={"ON": ["0xFC", "0x00", "0xF8", "0x90"],
                        "OFF": ["0xFC", "0x20", "0xF8", "0x90"]},
                display_name="R3 Floor Camera",
                description="Pressing R3 toggles camera position between feet of the player and normal position.",
                categories=[Category.FUN]),

"MinigameHUD": Offset(address="0x00AD8480", #hud
                values={"ON": ["0x41", "0x82"],
                        "OFF": ["0x40", "0x82"]},
                display_name="Minigame HUD",
                description="Toggles the Minigame HUD GUI. Will crash the game.",
                categories=[Category.HUD]),

"ChestESP": Offset(address="0x00A9C2B4", #xray, utilties, grief
                values={"ON": ["0x3E", "0xFF"],
                        "OFF": ["0x3F", "0x80"]},
                display_name="Chest ESP",
                description="Removes textures from everything except chests.",
                categories=[Category.XRAY, Category.UTILITIES, Category.GRIEF]),
                
"EntityESP1": Offset(address="0x00AD5A5C", #xray, utilties, grief
                values={"ON": ["0x6F", "0xFF"],
                        "OFF": ["0x3F", "0x80"]},
                display_name="Entity ESP (Part 1)",
                description="(1/2) Turn entities and players red.",
                categories=[Category.XRAY, Category.UTILITIES, Category.GRIEF]),

"EntityESP2": Offset(address="0x00AD5B60", #xray, utilties, grief
                values={"ON": "0x41",
                        "OFF": "0x40"},
                display_name="Entity ESP (Part 2)",
                description="(2/2) Turn entities and players red.",
                categories=[Category.XRAY, Category.UTILITIES, Category.GRIEF]),

"NoHitCam": Offset(address="0x00A972B0", #utilities
                values={"ON": ["0x00", "0x00"],
                        "OFF": ["0x40", "0x49"]},
                display_name="No Hit Camera Effect",
                description="Removed the 'shake' effect from the camera when hit.",
                categories=[Category.UTILITIES]),

"AntiAFK": Offset(address="0x002267B0", #utilities
                values={"ON": ["0x3F", "0x80"],
                        "OFF": ["0x00", "0x00"]},
                display_name="Anti AFK",
                description="Slowly moves the player, so can't be kicked for AFK.",
                categories=[Category.UTILITIES]),

"FlingAll": Offset(address="0x002267B0", #grief
                values={"ON": ["0x3F", "0xF0"],
                        "OFF": ["0x00", "0x00", "0x00", "0x00"]},
                display_name="Fling All",
                description="Makes players and entities fly and bounce or 'fling' across the map",
                categories=[Category.GRIEF]),

"NoDamageHit": Offset(address="0x003A3FF0", #grief, pve, utilities
                values={"ON": ["0xFF", "0xFF"],
                        "OFF": ["0x3F", "0x00"]},
                display_name="NoDamageHit",
                description="Take no damage, deal no damage.",
                categories=[Category.GRIEF, Category.PVE, Category.UTILITIES]),

"KillNoDespawn": Offset(address="0x0039F587", #utilities
                values={"ON": "0x00",
                        "OFF": "0x14"},
                display_name="Kill No Despawn Entity",
                description="Killed entities won't despawn.",
                categories=[Category.UTILITIES]),

"KillInstantDespawn": Offset(address="0x0039F587", #utilities
                values={"ON": "0x01",
                        "OFF": "0x14"},
                display_name="Kill Despawn Entity",
                description="Killed entities instantly despawn.",
                categories=[Category.UTILITIES]),

"ShowArmor": Offset(address="0x0090B5F0", #hud, utilities
                values={"ON": ["0x38", "0x80", "0x00", "0x01"],
                        "OFF": ["0x38", "0x80", "0x00", "0x00"]},
                display_name="Show Armor",
                description="Display worn armor on the left hand side of the HUD.",
                categories=[Category.UTILITIES]),

"UFO": Offset(address="0x003ABDD0", #fun
                values={"ON": ["0x3F", "0x00", "0x7A", "0xFF"],
                        "OFF": ["0x3F", "0xEF", "0x5C", "0x29"]},
                display_name="UFO",
                description="No jumping, low gravity, slow fly speed, no fall from flying, all players and entities.",
                categories=[Category.FUN]),

"FOV": Offset(address="0x014C670C", #utilities
                values={"50": ["0x3F", "0xFF", "0xFF"],
                        "75": ["0x3F", "0x70"],
                        "80": ["0x3F", "0x60"],
                        "85": ["0x3F", "0x50"],
                        "90": ["0x3F", "0x40"],
                        "95": ["0x3F", "0x30"],
                        "100": ["0x3F", "0x25"],
                        "105": ["0x3F", "0x20"],
                        "110": ["0x3F", "0x15"],
                        "115": ["0x3F", "0x10"],
                        "RESET": ["0x3F", "0x80", "0x00"]},
                display_name="Field Of View",
                description="Change the player camera FOV.",
                categories=[Category.UTILITIES]),

"DisableRespawn": Offset(address="0x00AF1EE0", #utilities
                values={"OFF": ["0xF8", "0x21", "0xFD", "0x21"], 
                        "ON": ["0x4E", '0x80', "0x00", "0x20"]},
                display_name="Disable Respawning",
                description="If player dies and tries to respawn, they will be stuck at the 'resapwning' screen.",
                categories=[Category.UTILITIES]),

"Brightness": Offset(address="0x00A9C2B5", #utilities
                values={"100": "0xFF",
                        "90":"0xE6",
                        "80": "0xCC",
                        "70": "0xB3",
                        "60": "0x99",
                        "50": "0x80",
                        "40": "0x66",
                        "30": "0x4D",
                        "20": "0x33",
                        "10": "0x1A",
                        "4": "0x0A",
                        "0": "0x00",
                        "RESET": "0x80"},
                display_name="Brightness (%)",
                description="Change the brightness of the game with affecting gamma. 50 is default.",
                categories=[Category.UTILITIES]),

"Smoke": Offset(address="0x00B24177", #utilties, fun
                values={"ON": "0x01",
                        "OFF": "0x00"},
                display_name="Heavy Smoke",
                categories=[Category.UTILITIES, Category.FUN]),
} 

def tabulate(map_data: dict, filename: str):
        headers = ["#", "Command", "Address", "Values", "Description", "Categories"]
        md = "| " + " | ".join(headers) + " |\n"
        md += "| " + " | ".join(["---"] * len(headers)) + " |\n"

        i = 0
        for key, offset in map_data.items():
                i=i+1
                address = ", ".join(offset.address) if isinstance(offset.address, list) else offset.address
                if callable(offset.values):
                        values = "Callable"
                elif isinstance(offset.values, dict):
                        values = ", ".join(f"{k}: {v}" for k, v in offset.values.items())
                else:
                        values = str(offset.values)
                categories = ", ".join(c.value for c in offset.categories)

                md += f"{i} | {key} | {address} | {values} | {offset.description} | {categories} |\n"

        with open(filename, "w", encoding="utf-8") as f:
                f.write(md)

#tabulate(map, "OFFSETS.md")
#print(len(map))