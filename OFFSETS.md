| # | Command | Address | Values | Description | Categories |
| --- | --- | --- | --- | --- | --- |
1 | NameChange | 0x3000ABE4, 0x3000AC54, 0x3000ACC4, 0x3000AD34, 0x3000ABA4 | Callable | Change your displayed name. Requires relog to take effect. | Utilities |
2 | SpawnMobs | 0x004619E4 | ON: 0x41, OFF: 0x40 | Disables spawning of mobs, destroys mobs that players have spawned. Stops mobs from doing damage. | Mobs |
3 | DayNight | 0x014C6880 | DAY: 0x3F, NIGHT: 0x2F | Set the time to day or night | Time |
4 | SunMoon | 0x00B21F1C | REMOVE: ['0x2F', '0x80'], 4SUNS: ['0x3F', '0xFF'], MOON_BRIGHT: ['0x4F', '0xFF'], RESET: ['0x3F', '0x80'] | 'Remove' removes the sun and moon. '4suns' creates 4 suns, makes moon brighter. 'moon_bright' maxes moon brightness. | Sky |
5 | GameSpeed | 0x00C202C9 | +1: 0x60, +2: 0x70, +3: 0x80, +4: 0x90, +5: 0xF0, -1: 0x40, -2: 0x30, -3: 0x20, -4: 0x10, -5: 0x00, DEFAULT: 0x50 | Speed up or slow down the games speed. Effects movement, look controls, mobs, daylight cycle. | Time |
6 | CloudGlitch | 0x00B230AD | ON: 0x70, OFF: 0x80 | Makes clouds move extremely fast, looks glitchy. | Sky |
7 | BlueClouds | 0x0038B964 | ON: 0xFF, OFF: 0x3D | Turns clouds and fog blue. | Sky |
8 | AutoSave | 0x00AEEE54 | ON: 0x40, OFF: 0x41 | Enables/disables autosaving | Utilities |
9 | AutoSprint | 0x00B01EEF | ON: 0x00, OFF: 0x01 | Lock sprint on when sprint started. | Movement |
10 | EndSky | 0x00B22050 | ON: 0x41, OFF: 0x40 | Replace the overworld sky with the End world sky. | Sky |
11 | LockGamemode | 0x002F03D0 | ON: 0x41, OFF: 0x40 | Lock Gamemode to current gamemode | Utilities |
12 | LockWeather | 0x00393E84 | ON: 0x41, OFF: 0x40 | Lock weather to current weather | Utilities, Weather |
13 | AntiJoin | 0x0098871F | ON: 0x01, OFF: 0x00 | Prevents other players from joining the world | Utilities |
14 | CreeperNoGrief | 0x001CC827 | ON: 0x00, OFF: 0x01 | Prevents creepers from destroying blocks. This only works when host options has mob griefing turned off, any you WANT creepers to grief. | Grief, Mobs |
15 | CreeperInstantExplode | 0x001CCC2C | ON: 0x40, OFF: 0x41 | Make creepers explode instantly (on spawn). | Mobs |
16 | CreeperFireExplode | 0x001CC894 | ON: ['0x39', '0x40', '0x00', '0x10'], OFF: ['0x39', '0x40', '0x00', '0x00'] | Creepers explode and spread fire. | Mobs |
17 | CreeperLargeExplode | 0x001CC7E0 | ON: ['0x42', '0xFF'], OFF: ['0x3F', '0x80'] | Creepers have a large (32x32) distruction radius. Causes massive server lag spike.  | Grief, Mobs |
18 | CreeperMediumExplode | 0x001CC7E0 | ON: ['0x3F', '0xFF'], OFF: ['0x3F', '0x80'] | Creepers have a 9x9 distruction radius. | Grief, Mobs |
19 | BigCreeper | 0x001CC81C | ON: 0x41, OFF: 0x40 | Creepers don't die after exploding. Their positions freeze, and you are constantly hurt inside their grief radius. | Mobs |
20 | TNTNoGrief1 | 0x00245DEB | ON: 0x00, OFF: 0x01 | Prevents TNT from destroying blocks. (1/2) | Grief |
21 | TNTNoGrief2 | 0x00245DF0 | ON: 0x40, OFF: 0x41 | Prevents TNT from destroying blocks. (2/2) | Grief |
22 | TNTDown | 0x0051E558 | ON: 0x4F, OFF: 0x3F | TNT Disappears, Exposion particles and sound effect still play. | Utilities |
23 | TNTSilent | 0x00245BE4 | ON: ['0xFF', '0x60', '0x18', '0x90'], OFF: ['0xFF', '0x60', '0x08', '0x90'] | Makes TNT explosions silent. The fuse 'hiss' is still audible. | Grief |
24 | TNTMoreParticles | 0x00245E58 | ON: 0x40, OFF: 0x41 | Makes TNT spawn more particles when exploding. Also seems to break rotation of particles. | Fun |
25 | TNTNoDelay | 0x0051E6A0 | ON: 0x40, OFF: 0x41 | Make TNT explode instantly when ignited | Grief |
26 | DamageAll | 0x0039E2D4 | ON: 0x40, OFF: 0x41 | Damage all players over time, until OFF. | Grief |
27 | StopAll | 0x004668B6 | ON: 0x78, OFF: 0x08 | Stops all player movement until OFF. | Grief, Utilities, Movement |
28 | NormalMove | 0x004668B6 | ON: 0x78, OFF: 0x26 | Set movement speed to default. | Utilities, Movement |
29 | FastMove1 | 0x003ABD49 | ON: ['0xFF', '0xFF', '0xFF'], OFF: ['0x26', '0xAD', '0x89'] | (Slowest) Increase movement speed of all players until off. | Movement |
30 | FastMove2 | 0x003AA999 | ON: 0x00, OFF: 0x68 | Increase movement speed of all players until off. | Movement |
31 | FastMove3 | 0x003ABD48 | ON: ['0x3F', '0xFF', '0x00', '0x01'], OFF: ['0x3E', '0x26', '0xAD', '0x89'] | Increase movement speed of all players until off. | Movement |
32 | FastMove4 | 0x003AA998 | ON: 0x3E, OFF: 0x3F | Increase movement speed of all players until off. Breaks some collisions. | Movement |
33 | FastMove5 | 0x003ABD48 | ON: ['0x41', '0xFF'], OFF: ['0x3E', '0x26'] | (Fastest) Increase movement speed of all players until off. Breaks some collisions. | Movement |
34 | LeftHandAll | 0x0151F2F0 | ON: ['0x30', '0x01', '0x87', '0xF0'], OFF: ['0x30', '0x01', '0x87', '0xF8'] | With empty hand, show left hand. Map in left hand will display on right. | Utilities |
35 | NoRunAll | 0x00018CE4 | ON: ['0xFF', '0xE0', '0x28', '0x90'], OFF: ['0xFF', '0xE0', '0x08', '0x90'] | Disallow all players to run | Movement, Utilities |
36 | DisablePortals | 0x002379E7 | ON: 0x00, OFF: 0x01 | Portals will not work, but do display. | Utilities |
37 | DirtNetherPortal | 0x014C89FE | ON: ['0x14', '0x70'], OFF: ['0x5E', '0x70'] | Build Nether Portals out of minecraft:dirt. | Utilities |
38 | StoneNetherPortal | 0x014C89FE | ON: ['0x11', '0xC0'], OFF: ['0x5E', '0x70'] | Build Nether Portals out of minecraft:stone (NOT cobblestone). | Utilities |
39 | DisableChunkLoading | 0x00B2437C | ON: ['0x4E', '0x80', '0x00', '0x20'], OFF: ['0xF8', '0x21', '0xFF', '0x71'] | New chunks will not load. This can cause crashes, especially when switching between the overworld, nether and end. | Utilities, Grief, Crash |
40 | OptimizeChunkLoading | 0x00B21C61 | ON: 0xD7, OFF: 0x30 | New chunks will not load. This can cause crashes, especially when switching between the overworld, nether and end. | Utilities |
41 | ExtremeFastBreakAll | 0x0010E0C4 | ON: ['0xFF', '0xE0', '0x18', '0x90'], OFF: ['0xFF', '0xE0', '0x08', '0x90'] | All players can break blocks extemely fast, works in survival. | Grief |
42 | FastBreakAll | 0x0010E0C4 | ON: ['0xFF', '0xE0', '0x28', '0x90'], OFF: ['0xFF', '0xE0', '0x08', '0x90'] | All players can break blocks faster, works in survival. | Grief |
43 | FastBreak | 0x00AEB11C | ON: 0x41, OFF: 0x40 | Break blocks faster, seemingly only works in creative. | Grief |
44 | FastWalk | 0x003ABD49 | ON: 0x86, OFF: 0x26 | Increases walking speed | Movement |
45 | BabyPlayer | 0x0039F52F | ON: 0x01, OFF: 0x00 | Makes the player model babby sized. | Fun |
46 | SillyWalk | 0x002341D0 | ON: 0xC3, OFF: 0xC0 | Player model does a silly walk. Approved by the Ministry of Silly Walks. | Fun |
47 | FastBuild | 0x00AECE70 | ON: 0x40, OFF: 0x41 | Place blocks without delay Only works in survival. | Grief |
48 | DriftBoat | 0x002278E4 | ON: 0x41, OFF: 0x40 | Make boats drift | Fun |
49 | BreakBoats | 0x000E0F90 | ON: 0x41, OFF: 0x40 | Boats are no longer rideable. | Utilities |
50 | StopXPGain | 0x004B00AC | ON: 0x41, OFF: 0x40 | Keeps current XP, but cannot gain anymore. | Utilities |
51 | MaxXP | 0x004B0094 | ON: ['0x7C', '0xA5', '0x10', '0x14'], OFF: ['0x7C', '0xA5', '0x20', '0x14'] | Throw a bottle o' enchanting or collect an experience orb to get the maximum XP level. | Utilities |
52 | KillAllPlayers | 0x00226168 | ON: 0x40, OFF: 0x41 | Kills all and players. | Grief |
53 | GodMode | 0x004B2021 | ON: 0x80, OFF: 0x20 | Godlike. | Utilities, God |
54 | DemiGodMode | 0x003A4064 | ON: ['0xFF', '0x40', '0x88', '0x90'], OFF: ['0xFF', '0x40', '0x08', '0x90'] | Demi Godlike. | Utilities, God |
55 | LightningBolt | 0x0098871F | ON: 0x01, OFF: 0x00 | Spams lightning, only works during stormy weather. | Grief, God |
56 | EnableRain | 0x00393F8F | ON: 0x01, OFF: 0x00 | Toggles rain. Sometimes needs a manual reset via host options. | Utilities |
57 | EntityGodMode | 0x003A3F6C | ON: 0x40, OFF: 0x41 | Give mobs God Mode | God |
58 | NoSlowWeb | 0x00234F9F | ON: 0x00, OFF: 0x01 | Toggles slow movement through spiders webs | Utilities |
59 | DisableGravity | 0x00246A2C | ON: 0xFF, OFF: 0x3F | Stop blocks like gravel from falling. | Utilities |
60 | DisableMobEggs | 0x005BF34E | ON: 0x48, OFF: 0x08 | Prevents mobs from being spawned in with spawn eggs | Utilities, Mobs |
61 | BurnInWater | 0x00225EA8 | ON: 0x41, OFF: 0x40 | Makes players and entities burn in water. | Utilities, Grief |
62 | InfinitePlace | 0x0010673F | ON: 0x00, OFF: 0x01 | Infinite block placement in survival, stacks will not descrease. | Utilities, Grief |
63 | InfiniteCraft | 0x0098871F | ON: 0x01, OFF: 0x00 | Craft anything in survival without the required materials | Utilities, Grief |
64 | InfiniteBreath | 0x0039DE28 | ON: 0x41, OFF: 0x40 | Underwater breath never runs out. | Utilities |
65 | NoFall | 0x003A409C | ON: 0x40, OFF: 0x41 | Player doesn't take fall damage | Utilities |
66 | GlitchMob | 0x00EA89E2 | ON: 0x18, OFF: 0x08 | Mobs will catch fire, die, lay on the ground dead. | Mobs, Fun |
67 | NoPickup | 0x00310B0C, 0x004A3FB8 | ON: 0x41, OFF: 0x40 | Prevents the picking up of dropped items | Utilities, Grief |
68 | MaxPickup | 0x00310AD4 | ON: 0x41, OFF: 0x40 | Duplicate dropped items into stacks. | Grief |
69 | UnlimitedArrows | 0x00224B13 | ON: 0x00, OFF: 0x01 |  | Utilities |
70 | RemoveArrows | 0x000FB644 | ON: 0x41, OFF: 0x40 | Arrows won't be taken from inventory | Utilities |
71 | BlockArrows | 0x000FB55C | ON: 0x80, OFF: 0x40 | The velocity of arrows is set to zero. Making arrows impossible to fire. | Utilities |
72 | AirToWater | 0x001D7FCC | ON: 0x40, OFF: 0x41 | Replaces all air blocks with water. | Grief |
73 | AutoLadder | 0x003A74F3 | ON: 0x01, OFF: 0x00 | Climb blocks like a spider. | Utilities, Movement |
74 | CrouchRun | 0x00B0142B | ON: 0x01, OFF: 0x00 | Makes the player crouch and run, locks crouch on. | Utilities |
75 | NoEntityCollision | 0x000108AC | ON: 0x41, OFF: 0x40 | Player and entities don't collide with objects. | Utilities, X-Ray |
76 | NoCollisionBypass | 0x002271B0 | ON: 0x40, OFF: 0x41 | Player doesn't collide with objects, entities do. Also makes dropped items bounce. | Utilities, X-Ray |
77 | MaxRiptide | 0x00217DCF | ON: 0x08, OFF: 0x00 | Maximum level riptide on trident, only useful in water. | Utilities |
78 | MakeRain | 0x00A9B23E | ON: 0x48, OFF: 0x08 | Rain, without other atmospheric/weather effects. | Weather |
79 | NightVision | 0x00A9A6C8 | ON: 0x7F, OFF: 0x3F | Increase visibility in the dark. | Utilities |
80 | Levitation | 0x003ABDD0 | ON: 0xBF, OFF: 0x3F | All Entities slowly float toward the heavens | Utilities |
81 | RemoveText | 0x007865EC | ON: 0x40, OFF: 0x41 | Remove text from GUI elements and menus | Utilities, GUI |
82 | BreakCamera | 0x00A97F34 | ON: 0xDF, OFF: 0x3F | Remove camera anchors from player, breaking it in a fun way. | Fun |
83 | BetterTime | 0x00A9A6DC | ON: 0x0F, OFF: 0x3F | More atmospheric lighting, better shadows. | Time |
84 | MoonGravity | 0x003ABF88 | ON: 0x40, OFF: 0x41 | Slow falling, longer movement momentum rollup, higher jumping. | Fun, Movement |
85 | WalkInSky | 0x00011B00 | ON: 0x40, OFF: 0x41 | Move player to the top Y coordinate, player will be unable to change Y coord. | Utilities, Movement |
86 | SkipAlong | 0x00A857D1 | ON: 0x00, OFF: 0x80 | Causes players legs to 'skip' while walking. | Fun, Movement |
87 | WallHack | 0x00A98F50 | ON: 0x3F, OFF: 0x3D | Look through walls, when close enough to them | Utilities, X-Ray |
88 | Nameplate | 0x00AD8158 | ON: 0x4C, OFF: 0x2C | Display nameplates for players, and self. | Utilities |
89 | ActiveNameplate | 0x00AD8110 | ON: ['0xFF', '0xC0', '0xE0', '0x90'], OFF: ['0xFF', '0xC0', '0x10', '0x90'] | When used in conjunction with `Nameplate` command, nameplates will move up and down depending on movement speed. | Utilities |
90 | FlatBlocks | 0x000924FF | ON: 0x01, OFF: 0x00 | Blocks in the inventory will appear flat. | Utilities, GUI |
91 | SuperKnockback | 0x003ABF3C | ON: 0x41, OFF: 0x40 | Insane amount of knockback on entities. Can break walking functionality. Causes entity lag. | Combat |
92 | ReverseKnockback | 0x003A4018 | ON: ['0xBF', '0x80'], OFF: ['0x3E', '0xCC'] | Hitting players or entities will knock them back into you. And they will hit you into them. | Combat |
93 | AutoWalk | 0x003ABE18 | ON: ['0xFF', '0x40'], OFF: ['0xFF', '0x20'] | Walk forever in the direction facing. Stops when flying. | Utilities |
94 | AntiKnockback | 0x003A4018 | ON: ['0x00', '0x00'], OFF: ['0x3E', '0xCC'] | Remove's all knockback from you, entities and players. | Combat |
95 | NoRun | 0x00B022F8 | ON: 0x4C, OFF: 0x2C | Disables running | Utilities |
96 | InstantMine | 0x00AEB090 | ON: 0xBF, OFF: 0x3F | Break blocks instantly. | Utilities |
97 | InstantKillFire | 0x002258F8 | ON: ['0x4F', '0x80'], OFF: ['0x3F', '0x80'] | Touching fire instantly kills players and entities | Grief |
98 | NoAutoRegen | 0x002ADCE8 | ON: ['0x68', '0x63', '0x00', '0x00'], OFF: ['0x68', '0x63', '0x00', '0x01'] | No health regeneration | Utilities |
99 | DeadScreen | 0x003A7654 | ON: 0x41, OFF: 0x40 | Bring up the animated red HUD overlay | Fun |
100 | FloatUp | 0x003ABDC8 | ON: 0x3F, OFF: 0xBF | Float to the top Y coord, with increasing momentum. | Fun, Movement |
101 | InvertPlayer | 0x00A99420 | ON: 0x40, OFF: 0x41 | Up is Left, Down is Right, Right is Left, Left is Right... That makes sense, right? left? | Fun, Movement |
102 | LockInBlock | 0x00389B3C | ON: 0x40, OFF: 0x41 | Lock player movement to block player is on. | Movement, Utilities |
103 | NoFlight | 0x00B02368 | ON: 0x41, OFF: 0x40 | Disable flying | Utilities, Movement |
104 | AntiKick | 0x00AEE434 | ON: 0x40, OFF: 0x41 | Prevent player being kicked from the session. TODO: test this. | Utilities |
105 | ShowBlockID | 0x003097C8 | ON: 0x40, OFF: 0x41 | Show numeric block ID (Format: #0000/00) on tooltips. | Utilities, GUI |
106 | ShowBlockName | 0x003097B8 | ON: 0x40, OFF: 0x41 | Show alphanumeric block name (Format: minecraft:dirt) identifiers on tooltips. | Utilities, GUI |
107 | StaticControls | 0x00AEFE64 | ON: 0x41, OFF: 0x40 | Camera and movement speed is static | Utilities |
108 | StaticLook | 0x00A98FA4 | ON: ['0xFF', '0xA0', '0x18', '0x90'], OFF: ['0xFF', '0xA0', '0x08', '0x90'] | Camera movement speed is static. | Utilities |
109 | PriviFlight | 0x00B02378 | ON: 0x40, OFF: 0x41 | Whether or not privileged players (op, mod) can fly. | Utilities |
110 | StuckFlying | 0x00B023EC | ON: 0x40, OFF: 0x41 | Disallow falling while flying, keeps the player flying | Utilities, Movement |
111 | CrashSelf | 0x00785DBC | ON: 0x40, OFF: 0x41 | Crash your game to the XMB. Be careful, data loss is possible. | Grief, Crash |
112 | CrashOther | 0x00AD8320 | ON: 0x40, OFF: 0x41 | Crash the game to the XMB for other players. This is a dick move. TODO: Check this works | Grief, Crash |
113 | SwimGlitch | 0x00B0229C | ON: 0x40, OFF: 0x41 | Swim anywhere by going into fast swim, then leaving the water. | Fun, Movement |
114 | InvertSwimMovement | 0x003ABD44 | ON: 0xBC, OFF: 0x3C | Invert the movement controls while swimming | Fun, Movement |
115 | DisableSwim | 0x0034B8F4 | ON: 0x41, OFF: 0x40 | Disables fast swimming, regular swimming is unaffected. | Utilities, Movement |
116 | JumpForwardSpeed | 0x003AA999 | ON: 0xA0, OFF: 0x68 | Multiplies movement speed (non Y axis) while jumping | Utilities, Movement |
117 | SuperJump | 0x003AA77C | ON: 0x3F, OFF: 0x3E | Fast jumps, doesn't affect height, only affects speed of jumping. | Utilities, Movement |
118 | SpaceJump | 0x00011ADC | ON: 0x40, OFF: 0x41 | Jump to the max Y coordinate | Fun, Movement |
119 | AngledGravity | 0x002271F4 | ON: ['0xFC', '0x80'], OFF: ['0xFC', '0x20'] | Makes gravity happen at a 45 degree angle, affects jumping and falling. | Fun, Movement |
120 | MultiJumpNoFallDamage | 0x0022790B | ON: 0x14, OFF: 0x18 | Allows jumping while in a jump, does not take fall damage. | Utilities, Movement |
121 | MultiJump | 0x003B000A | ON: 0x02, OFF: 0x01 | Allow jumping while in a jump. | Fun, Movement |
122 | HitDistance | 0x00233290 | FAR: 0xFF, HALF: 0x7F, DEFAULT: 0x00 | Increase the distance you can hit entities from. | Combat |
123 | SpamAttack | 0x00AEBED4 | ON: 0xBE, OFF: 0x3E | Holding R2 will cause the player to attack quickly, removes delay. | Combat |
124 | RemoveWater | 0x00225E80 | ON: 0x40, OFF: 0x41 | TODO: Figure out what this does |  |
125 | XToHit | 0x00AEEB83 | ON: 0x0F, OFF: 0x01 | Pressing X key will trigger the 'Action' button, usually R2. | Combat, Utilities |
126 | QuickMobs | 0x003AFB60 | ON: 0x4F, OFF: 0x3F | Makes mobs extremely fast. | Mobs, Movement |
127 | BlockStatic | 0x00AE3C3F | ON: 0x01, OFF: 0x00 | TODO: Figure out what this does |  |
128 | InstantHit | 0x00AEBED4 | ON: 0xFF, OFF: 0x3E | TODO: Figure out what this does |  |
129 | WolfRemoveWater | 0x006C0630 | ON: 0x40, OFF: 0x41 | Stops water from being placed around wolves. TODO: not sure what else this does |  |
130 | XRay | 0x00A99154 | ON: ['0xFC', '0x80', '0x30', '0x90'], OFF: ['0xFC', '0x60', '0x30', '0x90'] | See through structures. | Grief, Utilities, X-Ray |
131 | WaterJump | 0x003ABD68 | ON: ['0x3F', '0xF9', '0x99', '0x99'], OFF: ['0x3F', '0xE9', '0x99', '0x99'] | Hold jump in water to propel upwards and jump out of the water with momentum. | Movement |
132 | GunItems | 0x014C6880 | ON: ['0x3F', '0xFF'], OFF: ['0x3F', '0x80'] | TODO: not sure what this does |  |
133 | Suicide | 0x003ABDD0 | ON: ['0x3F', '0xFF'], OFF: ['0x3F', '0xEF'] | Jump flings you to the top of the map at max speed, then down to the bottom of the map at max speed, killing you. | Utilities |
134 | ForceThunder | 0x00393E34 | ON: ['0xFF', '0x80'], OFF: ['0x3F', '0x80'] | If the weather is in 'rain' mode, this will force it to be in 'thunder' mode instead. | Weather |
135 | RainToSnow | 0x01310954 | ON: 0x7E, OFF: 0x3E | Makes it snow in non-snow biomes, when its raining. Used in conjunction with ForceThunder it causes an epileptic nightmare. | Weather |
136 | GlitchedWeather | 0x00393E34 | ON: ['0x4F', '0x80'], OFF: ['0x3F', '0x80'] | Works best in Thunder weather mode. Horizon flashes different colors, sky changes colors, particles quadruple, lighting changes. Very glitchy, A great way to lag and crash your came. Changing weather mode while ON will crash game. | Weather, Crash |
137 | DisableStars | 0x0038C658 | ON: 0xFF, OFF: 0x3F | Turn off stars in the night sky | Sky |
138 | SkyColor | 0x00410734 | LIGHTGREEN: ['0x40', '0x50'], GREEN: ['0x41', '0x50'], PURPLE: ['0x49', '0xC0'], LAVENDER: ['0x42', '0xC0'], ORANGE: ['0x43', '0xC0'], YELLOW: ['0x46', '0xC0'], FLESH: ['0x00', '0xFF'], CYAN: ['0x4A', '0xC0'], BLACK: ['0xFF', '0xFF'], RESET: ['0x40', '0xC0'] | Change the color of the sky | Sky |
139 | GUIColor | 0x30DBAD64 | RED: ['0x3F', '0x80', '0x00', '0x00', '0x4F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'], PURPLE: ['0x3F', '0x80', '0x00', '0x00', '0x1F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'], GREEN: ['0X5F', '0x80', '0x00', '0x00', '0x5F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'], BLUE: ['0x00', '0x80', '0x00', '0x00', '0x8F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'], RESET: ['0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'] | Change the color of the GUI and HUD. | GUI |
140 | HideGUI | 0x30DBAD64 | ON: ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'], OFF: ['0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00', '0x3F', '0x80', '0x00', '0x00'] | Hide the GUI, including all menus and HUD. | GUI, Utilities |
141 | Spectator | 0x014C9048 | ON: ['0x32', '0x3A', '0x84', '0xC0'], OFF: ['0x32', '0x39', '0x4B', '0xD0'] | Adds 'spectator mode' to the gamemodes. You can switch to it in Host Options. | Utilities |
142 | SpectralArrows | 0x014C90D4 | ON: ['0x32', '0x20', '0x8D', '0xA0'], OFF: ['0x32', '0x1E', '0xAD', '0xA0'] | Fired arrows become spectral arrows on pickup. | Combat |
143 | StopBow | 0x000FB4C5 | ON: ['0xE0', '0x58'], OFF: ['0xE0', '0x08'] | Bow will not fire. | Utilities |
144 | ExtremeCamSens | 0x00ABA948 | ON: ['0x44', '0xFF'], OFF: ['0x42', '0x48'] | Extreme look control sensitivity. | Utilities, Movement |
145 | FastCamSens | 0x00ABA948 | ON: ['0x42', '0xFF'], OFF: ['0x42', '0x48'] | Fast look control sensitivity. | Utilities |
146 | TeleportKill | 0x003AFB60 | ON: ['0xFF', '0xFF', '0xFF', '0xFF'], OFF: ['0x3F', '0x7A', '0xE1', '0x48'] | Teleport all entities and players to you, and kill them. | Grief |
147 | FastBow | 0x000FB4C5 | ON: ['0xE0', '0x18', '0x18'], OFF: ['0xE0', '0x08', '0x18'] | Bow fires at maximum velocity without fully drawing. | Grief, Combat |
148 | FloorCam | 0x004B1CE0 | ON: ['0xFC', '0x02', '0x10'], OFF: ['0xFC', '0x01', '0x10'] | Places the camera at the feet of the player | Fun |
149 | R3FloorCam | 0x004B1D60 | ON: ['0xFC', '0x00', '0xF8', '0x90'], OFF: ['0xFC', '0x20', '0xF8', '0x90'] | Pressing R3 toggles camera position between feet of the player and normal position. | Fun |
150 | MinigameHUD | 0x00AD8480 | ON: ['0x41', '0x82'], OFF: ['0x40', '0x82'] | Toggles the Minigame HUD GUI. Will crash the game. | GUI |
151 | ChestESP | 0x00A9C2B4 | ON: ['0x3E', '0xFF'], OFF: ['0x3F', '0x80'] | Removes textures from everything except chests. | X-Ray, Utilities, Grief |
152 | EntityESP1 | 0x00AD5A5C | ON: ['0x6F', '0xFF'], OFF: ['0x3F', '0x80'] | (1/2) Turn entities and players red. | X-Ray, Utilities, Grief |
153 | EntityESP2 | 0x00AD5B60 | ON: 0x41, OFF: 0x40 | (2/2) Turn entities and players red. | X-Ray, Utilities, Grief |
154 | NoHitCam | 0x00A972B0 | ON: ['0x00', '0x00'], OFF: ['0x40', '0x49'] | Removed the 'shake' effect from the camera when hit. | Utilities |
155 | AntiAFK | 0x002267B0 | ON: ['0x3F', '0x80'], OFF: ['0x00', '0x00'] | Slowly moves the player, so can't be kicked for AFK. | Utilities |
156 | FlingAll | 0x002267B0 | ON: ['0x3F', '0xF0'], OFF: ['0x00', '0x00', '0x00', '0x00'] | Makes players and entities fly and bounce or 'fling' across the map | Grief |
157 | NoDamageHit | 0x003A3FF0 | ON: ['0xFF', '0xFF'], OFF: ['0x3F', '0x00'] | Take no damage, deal no damage. | Grief, Combat, Utilities |
158 | KillNoDespawn | 0x0039F587 | ON: 0x00, OFF: 0x14 | Killed entities won't despawn. | Utilities |
159 | KillInstantDespawn | 0x0039F587 | ON: 0x01, OFF: 0x14 | Killed entities instantly despawn. | Utilities |
160 | ShowArmor | 0x0090B5F0 | ON: ['0x38', '0x80', '0x00', '0x01'], OFF: ['0x38', '0x80', '0x00', '0x00'] | Display worn armor on the left hand side of the HUD. | Utilities |
161 | UFO | 0x003ABDD0 | ON: ['0x3F', '0x00', '0x7A', '0xFF'], OFF: ['0x3F', '0xEF', '0x5C', '0x29'] | No jumping, low gravity, slow fly speed, no fall from flying, all players and entities. | Fun |
162 | FOV | 0x014C670C | 50: ['0x3F', '0xFF', '0xFF'], 75: ['0x3F', '0x70'], 80: ['0x3F', '0x60'], 85: ['0x3F', '0x50'], 90: ['0x3F', '0x40'], 95: ['0x3F', '0x30'], 100: ['0x3F', '0x25'], 105: ['0x3F', '0x20'], 110: ['0x3F', '0x15'], 115: ['0x3F', '0x10'], RESET: ['0x3F', '0x80', '0x00'] | Change the player camera FOV. | Utilities |
163 | DisableRespawn | 0x00AF1EE0 | OFF: ['0xF8', '0x21', '0xFD', '0x21'], ON: ['0x4E', '0x80', '0x00', '0x20'] | If player dies and tries to respawn, they will be stuck at the 'resapwning' screen. | Utilities |
164 | Brightness | 0x00A9C2B5 | 100: 0xFF, 90: 0xE6, 80: 0xCC, 70: 0xB3, 60: 0x99, 50: 0x80, 40: 0x66, 30: 0x4D, 20: 0x33, 10: 0x1A, 4: 0x0A, 0: 0x00, RESET: 0x80 | Change the brightness of the game with affecting gamma. 50 is default. | Utilities |
165 | Smoke | 0x00B24177 | ON: 0x01, OFF: 0x00 |  | Utilities, Fun |
