import collections
import typing

from BaseClasses import Region, Location, Entrance, RegionType, Shop, TakeAny, UpgradeShop, ShopType


def create_regions(world, player):

    world.regions += [
        create_lw_region(player, 'Menu', None, ['Links House S&Q', 'Sanctuary S&Q', 'Old Man S&Q']),
        create_lw_region(player, 'Light World', ['Mushroom', 'Bottle Merchant', 'Flute Spot', 'Sunken Treasure', 'Purple Chest'],
                         ["Blinds Hideout", "Hyrule Castle Secret Entrance Drop", 'Zoras River', 'Kings Grave Outer Rocks', 'Dam',
                          'Links House', 'Tavern North', 'Chicken House', 'Aginahs Cave', 'Sahasrahlas Hut', 'Kakariko Well Drop', 'Kakariko Well Cave',
                          'Blacksmiths Hut', 'Bat Cave Drop Ledge', 'Bat Cave Cave', 'Sick Kids House', 'Hobo Bridge', 'Lost Woods Hideout Drop', 'Lost Woods Hideout Stump',
                          'Lumberjack Tree Tree', 'Lumberjack Tree Cave', 'Mini Moldorm Cave', 'Ice Rod Cave', 'Lake Hylia Central Island Pier',
                          'Bonk Rock Cave', 'Library', 'Potion Shop', 'Two Brothers House (East)', 'Desert Palace Stairs', 'Eastern Palace', 'Master Sword Meadow',
                          'Sanctuary', 'Sanctuary Grave', 'Death Mountain Entrance Rock', 'Flute Spot 1', 'Dark Desert Teleporter', 'East Hyrule Teleporter', 'South Hyrule Teleporter', 'Kakariko Teleporter',
                          'Elder House (East)', 'Elder House (West)', 'North Fairy Cave', 'North Fairy Cave Drop', 'Lost Woods Gamble', 'Snitch Lady (East)', 'Snitch Lady (West)', 'Tavern (Front)',
                          'Bush Covered House', 'Light World Bomb Hut', 'Kakariko Shop', 'Long Fairy Cave', 'Good Bee Cave', '20 Rupee Cave', 'Cave Shop (Lake Hylia)', 'Waterfall of Wishing', 'Hyrule Castle Main Gate',
                          'Bonk Fairy (Light)', '50 Rupee Cave', 'Fortune Teller (Light)', 'Lake Hylia Fairy', 'Light Hype Fairy', 'Desert Fairy', 'Lumberjack House', 'Lake Hylia Fortune Teller', 'Kakariko Gamble Game', 'Top of Pyramid']),
        create_lw_region(player, 'Death Mountain Entrance', None, ['Old Man Cave (West)', 'Death Mountain Entrance Drop']),
        create_lw_region(player, 'Lake Hylia Central Island', None, ['Capacity Upgrade', 'Lake Hylia Central Island Teleporter']),
        create_cave_region(player, 'Blinds Hideout', 'a bounty of five items', ["Blind\'s Hideout - Top",
                                                                        "Blind\'s Hideout - Left",
                                                                        "Blind\'s Hideout - Right",
                                                                        "Blind\'s Hideout - Far Left",
                                                                        "Blind\'s Hideout - Far Right"]),
        create_cave_region(player, 'Hyrule Castle Secret Entrance', 'a drop\'s exit', ['Link\'s Uncle', 'Secret Passage'], ['Hyrule Castle Secret Entrance Exit']),
        create_lw_region(player, 'Zoras River', ['King Zora', 'Zora\'s Ledge']),
        create_cave_region(player, 'Waterfall of Wishing', 'a cave with two chests', ['Waterfall Fairy - Left', 'Waterfall Fairy - Right']),
        create_lw_region(player, 'Kings Grave Area', None, ['Kings Grave', 'Kings Grave Inner Rocks']),
        create_cave_region(player, 'Kings Grave', 'a cave with a chest', ['King\'s Tomb']),
        create_cave_region(player, 'North Fairy Cave', 'a drop\'s exit', None, ['North Fairy Cave Exit']),
        create_cave_region(player, 'Dam', 'the dam', ['Floodgate', 'Floodgate Chest']),
        create_cave_region(player, 'Links House', 'your house', ['Link\'s House'], ['Links House Exit']),
        create_cave_region(player, 'Chris Houlihan Room', 'I AM ERROR', None, ['Chris Houlihan Room Exit']),
        create_cave_region(player, 'Tavern', 'the tavern', ['Kakariko Tavern']),
        create_cave_region(player, 'Elder House', 'a connector', None, ['Elder House Exit (East)', 'Elder House Exit (West)']),
        create_cave_region(player, 'Snitch Lady (East)', 'a boring house'),
        create_cave_region(player, 'Snitch Lady (West)', 'a boring house'),
        create_cave_region(player, 'Bush Covered House', 'the grass man'),
        create_cave_region(player, 'Tavern (Front)', 'the tavern'),
        create_cave_region(player, 'Light World Bomb Hut', 'a restock room'),
        create_cave_region(player, 'Kakariko Shop', 'a common shop'),
        create_cave_region(player, 'Fortune Teller (Light)', 'a fortune teller'),
        create_cave_region(player, 'Lake Hylia Fortune Teller', 'a fortune teller'),
        create_cave_region(player, 'Lumberjack House', 'a boring house'),
        create_cave_region(player, 'Bonk Fairy (Light)', 'a fairy fountain'),
        create_cave_region(player, 'Bonk Fairy (Dark)', 'a fairy fountain'),
        create_cave_region(player, 'Lake Hylia Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Swamp Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Desert Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Dark Lake Hylia Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Dark Lake Hylia Ledge Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Dark Desert Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Dark Death Mountain Healer Fairy', 'a fairy fountain'),
        create_cave_region(player, 'Chicken House', 'a house with a chest', ['Chicken House']),
        create_cave_region(player, 'Aginahs Cave', 'a cave with a chest', ['Aginah\'s Cave']),
        create_cave_region(player, 'Sahasrahlas Hut', 'Sahasrahla', ['Sahasrahla\'s Hut - Left', 'Sahasrahla\'s Hut - Middle', 'Sahasrahla\'s Hut - Right', 'Sahasrahla']),
        create_cave_region(player, 'Kakariko Well (top)', 'a drop\'s exit', ['Kakariko Well - Top', 'Kakariko Well - Left', 'Kakariko Well - Middle',
                                                                     'Kakariko Well - Right', 'Kakariko Well - Bottom'], ['Kakariko Well (top to bottom)']),
        create_cave_region(player, 'Kakariko Well (bottom)', 'a drop\'s exit', None, ['Kakariko Well Exit']),
        create_cave_region(player, 'Blacksmiths Hut', 'the smith', ['Blacksmith', 'Missing Smith']),
        create_lw_region(player, 'Bat Cave Drop Ledge', None, ['Bat Cave Drop']),
        create_cave_region(player, 'Bat Cave (right)', 'a drop\'s exit', ['Magic Bat'], ['Bat Cave Door']),
        create_cave_region(player, 'Bat Cave (left)', 'a drop\'s exit', None, ['Bat Cave Exit']),
        create_cave_region(player, 'Sick Kids House', 'the sick kid', ['Sick Kid']),
        create_lw_region(player, 'Hobo Bridge', ['Hobo']),
        create_cave_region(player, 'Lost Woods Hideout (top)', 'a drop\'s exit', ['Lost Woods Hideout'], ['Lost Woods Hideout (top to bottom)']),
        create_cave_region(player, 'Lost Woods Hideout (bottom)', 'a drop\'s exit', None, ['Lost Woods Hideout Exit']),
        create_cave_region(player, 'Lumberjack Tree (top)', 'a drop\'s exit', ['Lumberjack Tree'], ['Lumberjack Tree (top to bottom)']),
        create_cave_region(player, 'Lumberjack Tree (bottom)', 'a drop\'s exit', None, ['Lumberjack Tree Exit']),
        create_lw_region(player, 'Cave 45 Ledge', None, ['Cave 45']),
        create_cave_region(player, 'Cave 45', 'a cave with an item', ['Cave 45']),
        create_lw_region(player, 'Graveyard Ledge', None, ['Graveyard Cave']),
        create_cave_region(player, 'Graveyard Cave', 'a cave with an item', ['Graveyard Cave']),
        create_cave_region(player, 'Checkerboard Cave', 'a cave with an item', ['Checkerboard Cave']),
        create_cave_region(player, 'Long Fairy Cave', 'a fairy fountain'),
        create_cave_region(player, 'Mini Moldorm Cave', 'a bounty of five items', ['Mini Moldorm Cave - Far Left', 'Mini Moldorm Cave - Left', 'Mini Moldorm Cave - Right',
                                                                           'Mini Moldorm Cave - Far Right', 'Mini Moldorm Cave - Generous Guy']),
        create_cave_region(player, 'Ice Rod Cave', 'a cave with a chest', ['Ice Rod Cave']),
        create_cave_region(player, 'Good Bee Cave', 'a cold bee'),
        create_cave_region(player, '20 Rupee Cave', 'a cave with some cash'),
        create_cave_region(player, 'Cave Shop (Lake Hylia)', 'a common shop'),
        create_cave_region(player, 'Cave Shop (Dark Death Mountain)', 'a common shop'),
        create_cave_region(player, 'Bonk Rock Cave', 'a cave with a chest', ['Bonk Rock Cave']),
        create_cave_region(player, 'Library', 'the library', ['Library']),
        create_cave_region(player, 'Kakariko Gamble Game', 'a game of chance'),
        create_cave_region(player, 'Potion Shop', 'the potion shop', ['Potion Shop']),
        create_lw_region(player, 'Lake Hylia Island', ['Lake Hylia Island']),
        create_cave_region(player, 'Capacity Upgrade', 'the queen of fairies'),
        create_cave_region(player, 'Two Brothers House', 'a connector', None, ['Two Brothers House Exit (East)', 'Two Brothers House Exit (West)']),
        create_lw_region(player, 'Maze Race Ledge', ['Maze Race'], ['Two Brothers House (West)']),
        create_cave_region(player, '50 Rupee Cave', 'a cave with some cash'),
        create_lw_region(player, 'Desert Ledge', ['Desert Ledge'], ['Desert Palace Entrance (North) Rocks', 'Desert Palace Entrance (West)']),
        create_lw_region(player, 'Desert Ledge (Northeast)', None, ['Checkerboard Cave']),
        create_lw_region(player, 'Desert Palace Stairs', None, ['Desert Palace Entrance (South)']),
        create_lw_region(player, 'Desert Palace Lone Stairs', None, ['Desert Palace Stairs Drop', 'Desert Palace Entrance (East)']),
        create_lw_region(player, 'Desert Palace Entrance (North) Spot', None, ['Desert Palace Entrance (North)', 'Desert Ledge Return Rocks']),
        create_dungeon_region(player, 'Desert Palace Main (Outer)', 'Desert Palace', ['Desert Palace - Big Chest', 'Desert Palace - Torch', 'Desert Palace - Map Chest'],
                              ['Desert Palace Pots (Outer)', 'Desert Palace Exit (West)', 'Desert Palace Exit (East)', 'Desert Palace East Wing']),
        create_dungeon_region(player, 'Desert Palace Main (Inner)', 'Desert Palace', None, ['Desert Palace Exit (South)', 'Desert Palace Pots (Inner)']),
        create_dungeon_region(player, 'Desert Palace East', 'Desert Palace', ['Desert Palace - Compass Chest', 'Desert Palace - Big Key Chest']),
        create_dungeon_region(player, 'Desert Palace North', 'Desert Palace', ['Desert Palace - Boss', 'Desert Palace - Prize'], ['Desert Palace Exit (North)']),
        create_dungeon_region(player, 'Eastern Palace', 'Eastern Palace', ['Eastern Palace - Compass Chest', 'Eastern Palace - Big Chest', 'Eastern Palace - Cannonball Chest',
                                                 'Eastern Palace - Big Key Chest', 'Eastern Palace - Map Chest', 'Eastern Palace - Boss', 'Eastern Palace - Prize'], ['Eastern Palace Exit']),
        create_lw_region(player, 'Master Sword Meadow', ['Master Sword Pedestal']),
        create_cave_region(player, 'Lost Woods Gamble', 'a game of chance'),
        create_lw_region(player, 'Hyrule Castle Courtyard', None, ['Hyrule Castle Secret Entrance Stairs', 'Hyrule Castle Entrance (South)']),
        create_lw_region(player, 'Hyrule Castle Ledge', None, ['Hyrule Castle Entrance (East)', 'Hyrule Castle Entrance (West)', 'Agahnims Tower', 'Hyrule Castle Ledge Courtyard Drop']),
        create_dungeon_region(player, 'Hyrule Castle', 'Hyrule Castle', ['Hyrule Castle - Boomerang Chest', 'Hyrule Castle - Map Chest', 'Hyrule Castle - Zelda\'s Chest'],
                              ['Hyrule Castle Exit (East)', 'Hyrule Castle Exit (West)', 'Hyrule Castle Exit (South)', 'Throne Room']),
        create_dungeon_region(player, 'Sewer Drop', 'a drop\'s exit', None, ['Sewer Drop']),  # This exists only to be referenced for access checks
        create_dungeon_region(player, 'Sewers (Dark)', 'a drop\'s exit', ['Sewers - Dark Cross'], ['Sewers Door']),
        create_dungeon_region(player, 'Sewers', 'a drop\'s exit', ['Sewers - Secret Room - Left', 'Sewers - Secret Room - Middle',
                                         'Sewers - Secret Room - Right'], ['Sanctuary Push Door', 'Sewers Back Door']),
        create_dungeon_region(player, 'Sanctuary', 'a drop\'s exit', ['Sanctuary'], ['Sanctuary Exit']),
        create_dungeon_region(player, 'Agahnims Tower', 'Castle Tower', ['Castle Tower - Room 03', 'Castle Tower - Dark Maze'], ['Agahnim 1', 'Agahnims Tower Exit']),
        create_dungeon_region(player, 'Agahnim 1', 'Castle Tower', ['Agahnim 1'], None),
        create_cave_region(player, 'Old Man Cave', 'a connector', ['Old Man'], ['Old Man Cave Exit (East)', 'Old Man Cave Exit (West)']),
        create_cave_region(player, 'Old Man House', 'a connector', None, ['Old Man House Exit (Bottom)', 'Old Man House Front to Back']),
        create_cave_region(player, 'Old Man House Back', 'a connector', None, ['Old Man House Exit (Top)', 'Old Man House Back to Front']),
        create_lw_region(player, 'Death Mountain', None, ['Old Man Cave (East)', 'Old Man House (Bottom)', 'Old Man House (Top)', 'Death Mountain Return Cave (East)', 'Spectacle Rock Cave', 'Spectacle Rock Cave Peak', 'Spectacle Rock Cave (Bottom)', 'Broken Bridge (West)', 'Death Mountain Teleporter']),
        create_cave_region(player, 'Death Mountain Return Cave', 'a connector', None, ['Death Mountain Return Cave Exit (West)', 'Death Mountain Return Cave Exit (East)']),
        create_lw_region(player, 'Death Mountain Return Ledge', None, ['Death Mountain Return Ledge Drop', 'Death Mountain Return Cave (West)']),
        create_cave_region(player, 'Spectacle Rock Cave (Top)', 'a connector', ['Spectacle Rock Cave'], ['Spectacle Rock Cave Drop', 'Spectacle Rock Cave Exit (Top)']),
        create_cave_region(player, 'Spectacle Rock Cave (Bottom)', 'a connector', None, ['Spectacle Rock Cave Exit']),
        create_cave_region(player, 'Spectacle Rock Cave (Peak)', 'a connector', None, ['Spectacle Rock Cave Peak Drop', 'Spectacle Rock Cave Exit (Peak)']),
        create_lw_region(player, 'East Death Mountain (Bottom)', None, ['Broken Bridge (East)', 'Paradox Cave (Bottom)', 'Paradox Cave (Middle)', 'East Death Mountain Teleporter', 'Hookshot Fairy', 'Fairy Ascension Rocks', 'Spiral Cave (Bottom)']),
        create_cave_region(player, 'Hookshot Fairy', 'fairies deep in a cave'),
        create_cave_region(player, 'Paradox Cave Front', 'a connector', None, ['Paradox Cave Push Block Reverse', 'Paradox Cave Exit (Bottom)', 'Light World Death Mountain Shop']),
        create_cave_region(player, 'Paradox Cave Chest Area', 'a connector', ['Paradox Cave Lower - Far Left',
                                                                      'Paradox Cave Lower - Left',
                                                                      'Paradox Cave Lower - Right',
                                                                      'Paradox Cave Lower - Far Right',
                                                                      'Paradox Cave Lower - Middle',
                                                                      'Paradox Cave Upper - Left',
                                                                      'Paradox Cave Upper - Right'],
                           ['Paradox Cave Push Block', 'Paradox Cave Bomb Jump']),
        create_cave_region(player, 'Paradox Cave', 'a connector', None, ['Paradox Cave Exit (Middle)', 'Paradox Cave Exit (Top)', 'Paradox Cave Drop']),
        create_cave_region(player, 'Light World Death Mountain Shop', 'a common shop'),
        create_lw_region(player, 'East Death Mountain (Top)', None, ['Paradox Cave (Top)', 'Death Mountain (Top)', 'Spiral Cave Ledge Access', 'East Death Mountain Drop', 'Turtle Rock Teleporter', 'Fairy Ascension Ledge']),
        create_lw_region(player, 'Spiral Cave Ledge', None, ['Spiral Cave', 'Spiral Cave Ledge Drop']),
        create_cave_region(player, 'Spiral Cave (Top)', 'a connector', ['Spiral Cave'], ['Spiral Cave (top to bottom)', 'Spiral Cave Exit (Top)']),
        create_cave_region(player, 'Spiral Cave (Bottom)', 'a connector', None, ['Spiral Cave Exit']),
        create_lw_region(player, 'Fairy Ascension Plateau', None, ['Fairy Ascension Drop', 'Fairy Ascension Cave (Bottom)']),
        create_cave_region(player, 'Fairy Ascension Cave (Bottom)', 'a connector', None, ['Fairy Ascension Cave Climb', 'Fairy Ascension Cave Exit (Bottom)']),
        create_cave_region(player, 'Fairy Ascension Cave (Drop)', 'a connector', None, ['Fairy Ascension Cave Pots']),
        create_cave_region(player, 'Fairy Ascension Cave (Top)', 'a connector', None, ['Fairy Ascension Cave Exit (Top)', 'Fairy Ascension Cave Drop']),
        create_lw_region(player, 'Fairy Ascension Ledge', None, ['Fairy Ascension Ledge Drop', 'Fairy Ascension Cave (Top)']),
        create_lw_region(player, 'Death Mountain (Top)', ['Ether Tablet'], ['East Death Mountain (Top)', 'Tower of Hera', 'Death Mountain Drop']),
        create_lw_region(player, 'Spectacle Rock', ['Spectacle Rock'], ['Spectacle Rock Drop']),
        create_dungeon_region(player, 'Tower of Hera (Bottom)', 'Tower of Hera', ['Tower of Hera - Basement Cage', 'Tower of Hera - Map Chest'], ['Tower of Hera Small Key Door', 'Tower of Hera Big Key Door', 'Tower of Hera Exit']),
        create_dungeon_region(player, 'Tower of Hera (Basement)', 'Tower of Hera', ['Tower of Hera - Big Key Chest']),
        create_dungeon_region(player, 'Tower of Hera (Top)', 'Tower of Hera', ['Tower of Hera - Compass Chest', 'Tower of Hera - Big Chest', 'Tower of Hera - Boss', 'Tower of Hera - Prize']),

        create_dw_region(player, 'East Dark World', ['Pyramid'], ['Pyramid Fairy', 'South Dark World Bridge', 'Palace of Darkness', 'Dark Lake Hylia Drop (East)',
                                                           'Hyrule Castle Ledge Mirror Spot', 'Dark Lake Hylia Fairy', 'Palace of Darkness Hint', 'East Dark World Hint', 'Pyramid Hole', 'Northeast Dark World Broken Bridge Pass',]),
        create_dw_region(player, 'Catfish', ['Catfish'], ['Catfish Exit Rock']),
        create_dw_region(player, 'Northeast Dark World', None, ['West Dark World Gap', 'Dark World Potion Shop', 'East Dark World Broken Bridge Pass', 'Catfish Entrance Rock', 'Dark Lake Hylia Teleporter']),
        create_cave_region(player, 'Palace of Darkness Hint', 'a storyteller'),
        create_cave_region(player, 'East Dark World Hint', 'a storyteller'),
        create_dw_region(player, 'South Dark World', ['Stumpy', 'Digging Game'], ['Dark Lake Hylia Drop (South)', 'Hype Cave', 'Swamp Palace', 'Village of Outcasts Heavy Rock', 'Maze Race Mirror Spot',
                                                                                  'Cave 45 Mirror Spot', 'East Dark World Bridge', 'Big Bomb Shop', 'Archery Game', 'Bonk Fairy (Dark)', 'Dark Lake Hylia Shop',
                                                                                  'Bombos Tablet Mirror Spot']),
        create_lw_region(player, 'Bombos Tablet Ledge', ['Bombos Tablet']),
        create_cave_region(player, 'Big Bomb Shop', 'the bomb shop'),
        create_cave_region(player, 'Archery Game', 'a game of skill'),
        create_dw_region(player, 'Dark Lake Hylia', None, ['Lake Hylia Island Mirror Spot', 'East Dark World Pier', 'Dark Lake Hylia Ledge']),
        create_dw_region(player, 'Dark Lake Hylia Central Island', None, ['Ice Palace', 'Lake Hylia Central Island Mirror Spot']),
        create_dw_region(player, 'Dark Lake Hylia Ledge', None, ['Dark Lake Hylia Ledge Drop', 'Dark Lake Hylia Ledge Fairy', 'Dark Lake Hylia Ledge Hint', 'Dark Lake Hylia Ledge Spike Cave']),
        create_cave_region(player, 'Dark Lake Hylia Ledge Hint', 'a storyteller'),
        create_cave_region(player, 'Dark Lake Hylia Ledge Spike Cave', 'a spiky hint'),
        create_cave_region(player, 'Hype Cave', 'a bounty of five items', ['Hype Cave - Top', 'Hype Cave - Middle Right', 'Hype Cave - Middle Left',
                                                                   'Hype Cave - Bottom', 'Hype Cave - Generous Guy']),
        create_dw_region(player, 'West Dark World', ['Frog'], ['Village of Outcasts Drop', 'East Dark World River Pier', 'Brewery', 'C-Shaped House', 'Chest Game', 'Thieves Town', 'Graveyard Ledge Mirror Spot', 'Kings Grave Mirror Spot', 'Bumper Cave Entrance Rock',
                                                       'Skull Woods Forest', 'Village of Outcasts Pegs', 'Village of Outcasts Eastern Rocks', 'Red Shield Shop', 'Dark Sanctuary Hint', 'Fortune Teller (Dark)', 'Dark World Lumberjack Shop']),
        create_dw_region(player, 'Dark Grassy Lawn', None, ['Grassy Lawn Pegs', 'Dark World Shop']),
        create_dw_region(player, 'Hammer Peg Area', ['Dark Blacksmith Ruins'], ['Bat Cave Drop Ledge Mirror Spot', 'Dark World Hammer Peg Cave', 'Peg Area Rocks']),
        create_dw_region(player, 'Bumper Cave Entrance', None, ['Bumper Cave (Bottom)', 'Bumper Cave Entrance Mirror Spot', 'Bumper Cave Entrance Drop']),
        create_cave_region(player, 'Fortune Teller (Dark)', 'a fortune teller'),
        create_cave_region(player, 'Village of Outcasts Shop', 'a common shop'),
        create_cave_region(player, 'Dark Lake Hylia Shop', 'a common shop'),
        create_cave_region(player, 'Dark World Lumberjack Shop', 'a common shop'),
        create_cave_region(player, 'Dark World Potion Shop', 'a common shop'),
        create_cave_region(player, 'Dark World Hammer Peg Cave', 'a cave with an item', ['Peg Cave']),
        create_cave_region(player, 'Pyramid Fairy', 'a cave with two chests', ['Pyramid Fairy - Left', 'Pyramid Fairy - Right']),
        create_cave_region(player, 'Brewery', 'a house with a chest', ['Brewery']),
        create_cave_region(player, 'C-Shaped House', 'a house with a chest', ['C-Shaped House']),
        create_cave_region(player, 'Chest Game', 'a game of 16 chests', ['Chest Game']),
        create_cave_region(player, 'Red Shield Shop', 'the rare shop'),
        create_cave_region(player, 'Dark Sanctuary Hint', 'a storyteller'),
        create_cave_region(player, 'Bumper Cave', 'a connector', None, ['Bumper Cave Exit (Bottom)', 'Bumper Cave Exit (Top)']),
        create_dw_region(player, 'Bumper Cave Ledge', ['Bumper Cave Ledge'], ['Bumper Cave Ledge Drop', 'Bumper Cave (Top)', 'Bumper Cave Ledge Mirror Spot']),
        create_dw_region(player, 'Skull Woods Forest', None, ['Skull Woods First Section Hole (East)', 'Skull Woods First Section Hole (West)', 'Skull Woods First Section Hole (North)',
                                                      'Skull Woods First Section Door', 'Skull Woods Second Section Door (East)']),
        create_dw_region(player, 'Skull Woods Forest (West)', None, ['Skull Woods Second Section Hole', 'Skull Woods Second Section Door (West)', 'Skull Woods Final Section']),
        create_dw_region(player, 'Dark Desert',  None, ['Misery Mire', 'Mire Shed', 'Desert Ledge (Northeast) Mirror Spot', 'Desert Ledge Mirror Spot', 'Desert Palace Stairs Mirror Spot',
                                                'Desert Palace Entrance (North) Mirror Spot', 'Dark Desert Hint', 'Dark Desert Fairy']),
        create_cave_region(player, 'Mire Shed', 'a cave with two chests', ['Mire Shed - Left', 'Mire Shed - Right']),
        create_cave_region(player, 'Dark Desert Hint', 'a storyteller'),
        create_dw_region(player, 'Dark Death Mountain (West Bottom)', None, ['Spike Cave', 'Spectacle Rock Mirror Spot', 'Dark Death Mountain Fairy']),
        create_dw_region(player, 'Dark Death Mountain (Top)', None, ['Dark Death Mountain Drop (East)', 'Dark Death Mountain Drop (West)', 'Ganons Tower', 'Superbunny Cave (Top)',
                                                             'Hookshot Cave', 'East Death Mountain (Top) Mirror Spot', 'Turtle Rock']),
        create_dw_region(player, 'Dark Death Mountain Ledge', None, ['Dark Death Mountain Ledge (East)', 'Dark Death Mountain Ledge (West)', 'Mimic Cave Mirror Spot', 'Spiral Cave Mirror Spot']),
        create_dw_region(player, 'Dark Death Mountain Isolated Ledge', None, ['Isolated Ledge Mirror Spot', 'Turtle Rock Isolated Ledge Entrance']),
        create_dw_region(player, 'Dark Death Mountain (East Bottom)', None, ['Superbunny Cave (Bottom)', 'Cave Shop (Dark Death Mountain)', 'Fairy Ascension Mirror Spot']),
        create_cave_region(player, 'Superbunny Cave (Top)', 'a connector', ['Superbunny Cave - Top', 'Superbunny Cave - Bottom'], ['Superbunny Cave Exit (Top)']),
        create_cave_region(player, 'Superbunny Cave (Bottom)', 'a connector', None, ['Superbunny Cave Climb', 'Superbunny Cave Exit (Bottom)']),
        create_cave_region(player, 'Spike Cave', 'Spike Cave', ['Spike Cave']),
        create_cave_region(player, 'Hookshot Cave', 'a connector', ['Hookshot Cave - Top Right', 'Hookshot Cave - Top Left', 'Hookshot Cave - Bottom Right', 'Hookshot Cave - Bottom Left'],
                           ['Hookshot Cave Exit (South)', 'Hookshot Cave Exit (North)']),
        create_dw_region(player, 'Death Mountain Floating Island (Dark World)', None, ['Floating Island Drop', 'Hookshot Cave Back Entrance', 'Floating Island Mirror Spot']),
        create_lw_region(player, 'Death Mountain Floating Island (Light World)', ['Floating Island']),
        create_dw_region(player, 'Turtle Rock (Top)', None, ['Turtle Rock Drop']),
        create_lw_region(player, 'Mimic Cave Ledge', None, ['Mimic Cave']),
        create_cave_region(player, 'Mimic Cave', 'Mimic Cave', ['Mimic Cave']),

        create_dungeon_region(player, 'Swamp Palace (Entrance)', 'Swamp Palace', None, ['Swamp Palace Moat', 'Swamp Palace Exit']),
        create_dungeon_region(player, 'Swamp Palace (First Room)', 'Swamp Palace', ['Swamp Palace - Entrance'], ['Swamp Palace Small Key Door']),
        create_dungeon_region(player, 'Swamp Palace (Starting Area)', 'Swamp Palace', ['Swamp Palace - Map Chest'], ['Swamp Palace (Center)']),
        create_dungeon_region(player, 'Swamp Palace (Center)', 'Swamp Palace', ['Swamp Palace - Big Chest', 'Swamp Palace - Compass Chest',
                                                                        'Swamp Palace - Big Key Chest', 'Swamp Palace - West Chest'], ['Swamp Palace (North)']),
        create_dungeon_region(player, 'Swamp Palace (North)', 'Swamp Palace', ['Swamp Palace - Flooded Room - Left', 'Swamp Palace - Flooded Room - Right',
                                                                       'Swamp Palace - Waterfall Room', 'Swamp Palace - Boss', 'Swamp Palace - Prize']),
        create_dungeon_region(player, 'Thieves Town (Entrance)', 'Thieves\' Town', ['Thieves\' Town - Big Key Chest',
                                                                            'Thieves\' Town - Map Chest',
                                                                            'Thieves\' Town - Compass Chest',
                                                                            'Thieves\' Town - Ambush Chest'], ['Thieves Town Big Key Door', 'Thieves Town Exit']),
        create_dungeon_region(player, 'Thieves Town (Deep)', 'Thieves\' Town', ['Thieves\' Town - Attic',
                                                                        'Thieves\' Town - Big Chest',
                                                                        'Thieves\' Town - Blind\'s Cell'], ['Blind Fight']),
        create_dungeon_region(player, 'Blind Fight', 'Thieves\' Town', ['Thieves\' Town - Boss', 'Thieves\' Town - Prize']),
        create_dungeon_region(player, 'Skull Woods First Section', 'Skull Woods', ['Skull Woods - Map Chest'], ['Skull Woods First Section Exit', 'Skull Woods First Section Bomb Jump', 'Skull Woods First Section South Door', 'Skull Woods First Section West Door']),
        create_dungeon_region(player, 'Skull Woods First Section (Right)', 'Skull Woods', ['Skull Woods - Pinball Room'], ['Skull Woods First Section (Right) North Door']),
        create_dungeon_region(player, 'Skull Woods First Section (Left)', 'Skull Woods', ['Skull Woods - Compass Chest', 'Skull Woods - Pot Prison'], ['Skull Woods First Section (Left) Door to Exit', 'Skull Woods First Section (Left) Door to Right']),
        create_dungeon_region(player, 'Skull Woods First Section (Top)', 'Skull Woods', ['Skull Woods - Big Chest'], ['Skull Woods First Section (Top) One-Way Path']),
        create_dungeon_region(player, 'Skull Woods Second Section (Drop)', 'Skull Woods', None, ['Skull Woods Second Section (Drop)']),
        create_dungeon_region(player, 'Skull Woods Second Section', 'Skull Woods', ['Skull Woods - Big Key Chest'], ['Skull Woods Second Section Exit (East)', 'Skull Woods Second Section Exit (West)']),
        create_dungeon_region(player, 'Skull Woods Final Section (Entrance)', 'Skull Woods', ['Skull Woods - Bridge Room'], ['Skull Woods Torch Room', 'Skull Woods Final Section Exit']),
        create_dungeon_region(player, 'Skull Woods Final Section (Mothula)', 'Skull Woods', ['Skull Woods - Boss', 'Skull Woods - Prize']),
        create_dungeon_region(player, 'Ice Palace (Entrance)', 'Ice Palace', None, ['Ice Palace Entrance Room', 'Ice Palace Exit']),
        create_dungeon_region(player, 'Ice Palace (Main)', 'Ice Palace', ['Ice Palace - Compass Chest', 'Ice Palace - Freezor Chest',
                                                                  'Ice Palace - Big Chest', 'Ice Palace - Iced T Room'], ['Ice Palace (East)', 'Ice Palace (Kholdstare)']),
        create_dungeon_region(player, 'Ice Palace (East)', 'Ice Palace', ['Ice Palace - Spike Room'], ['Ice Palace (East Top)']),
        create_dungeon_region(player, 'Ice Palace (East Top)', 'Ice Palace', ['Ice Palace - Big Key Chest', 'Ice Palace - Map Chest']),
        create_dungeon_region(player, 'Ice Palace (Kholdstare)', 'Ice Palace', ['Ice Palace - Boss', 'Ice Palace - Prize']),
        create_dungeon_region(player, 'Misery Mire (Entrance)', 'Misery Mire', None, ['Misery Mire Entrance Gap', 'Misery Mire Exit']),
        create_dungeon_region(player, 'Misery Mire (Main)', 'Misery Mire', ['Misery Mire - Big Chest', 'Misery Mire - Map Chest', 'Misery Mire - Main Lobby',
                                                                    'Misery Mire - Bridge Chest', 'Misery Mire - Spike Chest'], ['Misery Mire (West)', 'Misery Mire Big Key Door']),
        create_dungeon_region(player, 'Misery Mire (West)', 'Misery Mire', ['Misery Mire - Compass Chest', 'Misery Mire - Big Key Chest']),
        create_dungeon_region(player, 'Misery Mire (Final Area)', 'Misery Mire', None, ['Misery Mire (Vitreous)']),
        create_dungeon_region(player, 'Misery Mire (Vitreous)', 'Misery Mire', ['Misery Mire - Boss', 'Misery Mire - Prize']),
        create_dungeon_region(player, 'Turtle Rock (Entrance)', 'Turtle Rock', None, ['Turtle Rock Entrance Gap', 'Turtle Rock Exit (Front)']),
        create_dungeon_region(player, 'Turtle Rock (First Section)', 'Turtle Rock', ['Turtle Rock - Compass Chest', 'Turtle Rock - Roller Room - Left',
                                                                             'Turtle Rock - Roller Room - Right'], ['Turtle Rock Pokey Room', 'Turtle Rock Entrance Gap Reverse']),
        create_dungeon_region(player, 'Turtle Rock (Chain Chomp Room)', 'Turtle Rock', ['Turtle Rock - Chain Chomps'], ['Turtle Rock (Chain Chomp Room) (North)', 'Turtle Rock (Chain Chomp Room) (South)']),
        create_dungeon_region(player, 'Turtle Rock (Second Section)', 'Turtle Rock', ['Turtle Rock - Big Key Chest'], ['Turtle Rock Ledge Exit (West)', 'Turtle Rock Chain Chomp Staircase', 'Turtle Rock Big Key Door']),
        create_dungeon_region(player, 'Turtle Rock (Big Chest)', 'Turtle Rock', ['Turtle Rock - Big Chest'], ['Turtle Rock (Big Chest) (North)', 'Turtle Rock Ledge Exit (East)']),
        create_dungeon_region(player, 'Turtle Rock (Crystaroller Room)', 'Turtle Rock', ['Turtle Rock - Crystaroller Room'], ['Turtle Rock Dark Room Staircase', 'Turtle Rock Big Key Door Reverse']),
        create_dungeon_region(player, 'Turtle Rock (Dark Room)', 'Turtle Rock', None, ['Turtle Rock (Dark Room) (North)', 'Turtle Rock (Dark Room) (South)']),
        create_dungeon_region(player, 'Turtle Rock (Eye Bridge)', 'Turtle Rock', ['Turtle Rock - Eye Bridge - Bottom Left', 'Turtle Rock - Eye Bridge - Bottom Right',
                                                                          'Turtle Rock - Eye Bridge - Top Left', 'Turtle Rock - Eye Bridge - Top Right'],
                              ['Turtle Rock Dark Room (South)', 'Turtle Rock (Trinexx)', 'Turtle Rock Isolated Ledge Exit']),
        create_dungeon_region(player, 'Turtle Rock (Trinexx)', 'Turtle Rock', ['Turtle Rock - Boss', 'Turtle Rock - Prize']),
        create_dungeon_region(player, 'Palace of Darkness (Entrance)', 'Palace of Darkness', ['Palace of Darkness - Shooter Room'], ['Palace of Darkness Bridge Room', 'Palace of Darkness Bonk Wall', 'Palace of Darkness Exit']),
        create_dungeon_region(player, 'Palace of Darkness (Center)', 'Palace of Darkness', ['Palace of Darkness - The Arena - Bridge', 'Palace of Darkness - Stalfos Basement'],
                              ['Palace of Darkness Big Key Chest Staircase', 'Palace of Darkness (North)', 'Palace of Darkness Big Key Door']),
        create_dungeon_region(player, 'Palace of Darkness (Big Key Chest)', 'Palace of Darkness', ['Palace of Darkness - Big Key Chest']),
        create_dungeon_region(player, 'Palace of Darkness (Bonk Section)', 'Palace of Darkness', ['Palace of Darkness - The Arena - Ledge', 'Palace of Darkness - Map Chest'], ['Palace of Darkness Hammer Peg Drop']),
        create_dungeon_region(player, 'Palace of Darkness (North)', 'Palace of Darkness', ['Palace of Darkness - Compass Chest', 'Palace of Darkness - Dark Basement - Left', 'Palace of Darkness - Dark Basement - Right'],
                              ['Palace of Darkness Spike Statue Room Door', 'Palace of Darkness Maze Door']),
        create_dungeon_region(player, 'Palace of Darkness (Maze)', 'Palace of Darkness', ['Palace of Darkness - Dark Maze - Top', 'Palace of Darkness - Dark Maze - Bottom', 'Palace of Darkness - Big Chest']),
        create_dungeon_region(player, 'Palace of Darkness (Harmless Hellway)', 'Palace of Darkness', ['Palace of Darkness - Harmless Hellway']),
        create_dungeon_region(player, 'Palace of Darkness (Final Section)', 'Palace of Darkness', ['Palace of Darkness - Boss', 'Palace of Darkness - Prize']),
        create_dungeon_region(player, 'Ganons Tower (Entrance)', 'Ganon\'s Tower', ['Ganons Tower - Bob\'s Torch', 'Ganons Tower - Hope Room - Left', 'Ganons Tower - Hope Room - Right'],
                              ['Ganons Tower (Tile Room)', 'Ganons Tower (Hookshot Room)', 'Ganons Tower Big Key Door', 'Ganons Tower Exit']),
        create_dungeon_region(player, 'Ganons Tower (Tile Room)', 'Ganon\'s Tower', ['Ganons Tower - Tile Room'], ['Ganons Tower (Tile Room) Key Door']),
        create_dungeon_region(player, 'Ganons Tower (Compass Room)', 'Ganon\'s Tower', ['Ganons Tower - Compass Room - Top Left', 'Ganons Tower - Compass Room - Top Right',
                                                                                'Ganons Tower - Compass Room - Bottom Left', 'Ganons Tower - Compass Room - Bottom Right'],
                              ['Ganons Tower (Bottom) (East)']),
        create_dungeon_region(player, 'Ganons Tower (Hookshot Room)', 'Ganon\'s Tower', ['Ganons Tower - DMs Room - Top Left', 'Ganons Tower - DMs Room - Top Right',
                                                                                 'Ganons Tower - DMs Room - Bottom Left', 'Ganons Tower - DMs Room - Bottom Right'],
                              ['Ganons Tower (Map Room)', 'Ganons Tower (Double Switch Room)']),
        create_dungeon_region(player, 'Ganons Tower (Map Room)', 'Ganon\'s Tower', ['Ganons Tower - Map Chest']),
        create_dungeon_region(player, 'Ganons Tower (Firesnake Room)', 'Ganon\'s Tower', ['Ganons Tower - Firesnake Room'], ['Ganons Tower (Firesnake Room)']),
        create_dungeon_region(player, 'Ganons Tower (Teleport Room)', 'Ganon\'s Tower', ['Ganons Tower - Randomizer Room - Top Left', 'Ganons Tower - Randomizer Room - Top Right',
                                                                                 'Ganons Tower - Randomizer Room - Bottom Left', 'Ganons Tower - Randomizer Room - Bottom Right'],
                              ['Ganons Tower (Bottom) (West)']),
        create_dungeon_region(player, 'Ganons Tower (Bottom)', 'Ganon\'s Tower', ['Ganons Tower - Bob\'s Chest', 'Ganons Tower - Big Chest', 'Ganons Tower - Big Key Room - Left',
                                                                          'Ganons Tower - Big Key Room - Right', 'Ganons Tower - Big Key Chest']),
        create_dungeon_region(player, 'Ganons Tower (Top)', 'Ganon\'s Tower', None, ['Ganons Tower Torch Rooms']),
        create_dungeon_region(player, 'Ganons Tower (Before Moldorm)', 'Ganon\'s Tower', ['Ganons Tower - Mini Helmasaur Room - Left', 'Ganons Tower - Mini Helmasaur Room - Right',
                                                                                  'Ganons Tower - Pre-Moldorm Chest'], ['Ganons Tower Moldorm Door']),
        create_dungeon_region(player, 'Ganons Tower (Moldorm)', 'Ganon\'s Tower', None, ['Ganons Tower Moldorm Gap']),
        create_dungeon_region(player, 'Agahnim 2', 'Ganon\'s Tower', ['Ganons Tower - Validation Chest', 'Agahnim 2'], None),
        create_cave_region(player, 'Pyramid', 'a drop\'s exit', ['Ganon'], ['Ganon Drop']),
        create_cave_region(player, 'Bottom of Pyramid', 'a drop\'s exit', None, ['Pyramid Exit']),
        create_dw_region(player, 'Pyramid Ledge', None, ['Pyramid Entrance', 'Pyramid Drop']),
        create_lw_region(player, 'Desert Northern Cliffs'),
        create_dw_region(player, 'Dark Death Mountain Bunny Descent Area')
    ]

    world.initialize_regions()


def create_lw_region(player: int, name: str, locations=None, exits=None):
    return _create_region(player, name, RegionType.LightWorld, 'Light World', locations, exits)


def create_dw_region(player: int, name: str, locations=None, exits=None):
    return _create_region(player, name, RegionType.DarkWorld, 'Dark World', locations, exits)


def create_cave_region(player: int, name: str, hint: str, locations=None, exits=None):
    return _create_region(player, name, RegionType.Cave, hint, locations, exits)


def create_dungeon_region(player: int, name: str, hint: str, locations=None, exits=None):
    return _create_region(player, name, RegionType.Dungeon, hint, locations, exits)


def _create_region(player: int, name: str, type: RegionType, hint: str, locations=None, exits=None):
    ret = Region(name, type, hint, player)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(player, exit, ret))
    for location in locations:
        address, player_address, crystal, hint_text = location_table[location]
        ret.locations.append(Location(player, location, address, crystal, hint_text, ret, player_address))
    return ret


def mark_light_world_regions(world, player: int):
    # cross world caves may have some sections marked as both in_light_world, and in_dark_work.
    # That is ok. the bunny logic will check for this case and incorporate special rules.
    queue = collections.deque(region for region in world.get_regions(player) if region.type == RegionType.LightWorld)
    seen = set(queue)
    while queue:
        current = queue.popleft()
        current.is_light_world = True
        for exit in current.exits:
            if exit.connected_region.type == RegionType.DarkWorld:
                # Don't venture into the dark world
                continue
            if exit.connected_region not in seen:
                seen.add(exit.connected_region)
                queue.append(exit.connected_region)

    queue = collections.deque(region for region in world.get_regions(player) if region.type == RegionType.DarkWorld)
    seen = set(queue)
    while queue:
        current = queue.popleft()
        current.is_dark_world = True
        for exit in current.exits:
            if exit.connected_region.type == RegionType.LightWorld:
                # Don't venture into the light world
                continue
            if exit.connected_region not in seen:
                seen.add(exit.connected_region)
                queue.append(exit.connected_region)


def create_shops(world, player: int):
    cls_mapping = {ShopType.UpgradeShop: UpgradeShop,
                   ShopType.Shop: Shop,
                   ShopType.TakeAny: TakeAny}
    option = world.shop_shuffle[player]
    my_shop_table = dict(shop_table)
    
    num_slots = int(world.shop_shuffle_slots[player])
    
    my_shop_slots = ([True] * num_slots + [False] * (len(shop_table) * 3))[:len(shop_table)*3 - 2] 

    world.random.shuffle(my_shop_slots)

    from Items import ItemFactory
    if 'g' in option or 'f' in option:
        new_basic_shop = world.random.sample(shop_generation_types['default'], k=3)
        new_dark_shop = world.random.sample(shop_generation_types['default'], k=3)
        for name, shop in my_shop_table.items():
            typ, shop_id, keeper, custom, locked, items = shop
            if name == 'Capacity Upgrade':
                pass
            elif name == 'Potion Shop' and not "w" in option:
                pass
            else:
                new_items = world.random.sample(shop_generation_types['default'], k=3)
                if 'f' not in option:
                    if items == _basic_shop_defaults:
                        new_items = new_basic_shop
                    elif items == _dark_world_shop_defaults:
                        new_items = new_dark_shop
                keeper = world.random.choice([0xA0, 0xC1, 0xFF])
                my_shop_table[name] = (typ, shop_id, keeper, custom, locked, new_items)
    
    for region_name, (room_id, type, shopkeeper, custom, locked, inventory) in my_shop_table.items():
        if world.mode[player] == 'inverted' and region_name == 'Dark Lake Hylia Shop':
            locked = True
            inventory = [('Blue Potion', 160), ('Blue Shield', 50), ('Bombs (10)', 50)]
        region = world.get_region(region_name, player)
        shop = cls_mapping[type](region, room_id, shopkeeper, custom, locked)
        region.shop = shop
        world.shops.append(shop)
        for index, item in enumerate(inventory):
            shop.add_inventory(index, *item)
            if region_name == 'Potion Shop' and 'w' not in option:
                pass
            elif region_name == 'Capacity Upgrade':
                pass
            else:
                if my_shop_slots.pop():
                    additional_item = world.random.choice(['Rupees (50)', 'Rupees (100)', 'Rupees (300)'])
                    slot_name = "{} Slot {}".format(shop.region.name, index + 1)
                    loc = Location(player, slot_name, address=shop_table_by_location[slot_name], parent=shop.region)
                    loc.shop_slot = True
                    loc.locked = True
                    loc.item = ItemFactory(additional_item, player)
                    shop.region.locations.append(loc)
                    world.dynamic_locations.append(loc)

                    world.clear_location_cache()


# (type, room_id, shopkeeper, custom, locked, [items])
# item = (item, price, max=0, replacement=None, replacement_price=0)
_basic_shop_defaults = [('Red Potion', 150), ('Small Heart', 10), ('Bombs (10)', 50)]
_dark_world_shop_defaults = [('Red Potion', 150), ('Blue Shield', 50), ('Bombs (10)', 50)]
shop_table = {
    'Cave Shop (Dark Death Mountain)': (0x0112, ShopType.Shop, 0xC1, True, False, _basic_shop_defaults),
    'Red Shield Shop': (0x0110, ShopType.Shop, 0xC1, True, False, [('Red Shield', 500), ('Bee', 10), ('Arrows (10)', 30)]),
    'Dark Lake Hylia Shop': (0x010F, ShopType.Shop, 0xC1, True, False, _dark_world_shop_defaults),
    'Dark World Lumberjack Shop': (0x010F, ShopType.Shop, 0xC1, True, False, _dark_world_shop_defaults),
    'Village of Outcasts Shop': (0x010F, ShopType.Shop, 0xC1, True, False, _dark_world_shop_defaults),
    'Dark World Potion Shop': (0x010F, ShopType.Shop, 0xC1, True, False, _dark_world_shop_defaults),
    'Light World Death Mountain Shop': (0x00FF, ShopType.Shop, 0xA0, True, False, _basic_shop_defaults),
    'Kakariko Shop': (0x011F, ShopType.Shop, 0xA0, True, False, _basic_shop_defaults),
    'Cave Shop (Lake Hylia)': (0x0112, ShopType.Shop, 0xA0, True, False, _basic_shop_defaults),
    'Potion Shop': (0x0109, ShopType.Shop, 0xA0, True, False, [('Red Potion', 120), ('Green Potion', 60), ('Blue Potion', 160)]),
    'Capacity Upgrade': (0x0115, ShopType.UpgradeShop, 0x04, True, True, [('Bomb Upgrade (+5)', 100, 7), ('Arrow Upgrade (+5)', 100, 7)])
}

SHOP_ID_START = 0x400000
shop_table_by_location_id = {SHOP_ID_START + cnt: s for cnt, s in enumerate(
    [item for sublist in [["{} Slot {}".format(name, num + 1) for num in range(3)] for name in shop_table] for item in
     sublist])}
shop_table_by_location_id[(SHOP_ID_START + len(shop_table)*3)] = "Old Man Sword Cave"
shop_table_by_location_id[(SHOP_ID_START + len(shop_table)*3 + 1)] = "Take-Any #1"
shop_table_by_location_id[(SHOP_ID_START + len(shop_table)*3 + 2)] = "Take-Any #2"
shop_table_by_location_id[(SHOP_ID_START + len(shop_table)*3 + 3)] = "Take-Any #3"
shop_table_by_location_id[(SHOP_ID_START + len(shop_table)*3 + 4)] = "Take-Any #4"
shop_table_by_location = {y: x for x, y in shop_table_by_location_id.items()}

shop_generation_types = {
    'default': _basic_shop_defaults + [('Bombs (3)', 20), ('Green Potion', 90), ('Blue Potion', 190), ('Bee', 10), ('Single Arrow', 5), ('Single Bomb', 10)] + [('Red Shield', 500), ('Blue Shield', 50)],
    'potion': [('Red Potion', 150), ('Green Potion', 90), ('Blue Potion', 190)],
    'discount_potion': [('Red Potion', 120), ('Green Potion', 60), ('Blue Potion', 160)],
    'bottle': [('Bee', 10)],
    'time': [('Red Clock', 100), ('Blue Clock', 200), ('Green Clock', 300)],
}

old_location_address_to_new_location_address = {
    0x2eb18: 0x18001b,   # Bottle Merchant
    0x33d68: 0x18001a,   # Purple Chest
    0x2df45: 0x18001d,   # Link's Uncle
    0x2f1fc: 0x180008,   # Sahasrahla
    0x18002a: 0x18001c,  # Black Smith
    0x339cf: 0x180009,   # Sick Kid
    0x33e7d: 0x180019,   # Hobo
    0x180160: 0x18000b,  # Desert Palace - Desert Torch
    0x289b0: 0x180018,   # Master Sword Pedestal
    0xf69fa: 0x180007,   # Old Man
    0x180162: 0x18000d,  # Tower of Hera - Basement Cage
    0x330c7: 0x18000a,   # Stumpy
    0x180161: 0x18000c   # Ganons Tower - Bob's Torch
}


key_drop_data = {
    'Hyrule Castle - Map Guard Key Drop': [0x140036, 0x140037],
    'Hyrule Castle - Boomerang Guard Key Drop': [0x140033, 0x140034],
    'Hyrule Castle - Key Rat Key Drop': [0x14000c, 0x14000d],
    'Hyrule Castle - Big Key Drop': [0x14003c, 0x14003d],
    'Eastern Palace - Dark Square Pot Key': [0x14005a, 0x14005b],
    'Eastern Palace - Dark Eyegore Key Drop': [0x140048, 0x140049],
    'Desert Palace - Desert Tiles 1 Pot Key': [0x140030, 0x140031],
    'Desert Palace - Beamos Hall Pot Key': [0x14002a, 0x14002b],
    'Desert Palace - Desert Tiles 2 Pot Key': [0x140027, 0x140028],
    'Castle Tower - Dark Archer Key Drop': [0x140060, 0x140061],
    'Castle Tower - Circle of Pots Key Drop': [0x140051, 0x140052],
    'Swamp Palace - Pot Row Pot Key': [0x140018, 0x140019],
    'Swamp Palace - Trench 1 Pot Key': [0x140015, 0x140016],
    'Swamp Palace - Hookshot Pot Key': [0x140012, 0x140013],
    'Swamp Palace - Trench 2 Pot Key': [0x14000f, 0x140010],
    'Swamp Palace - Waterway Pot Key': [0x140009, 0x14000a],
    'Skull Woods - West Lobby Pot Key': [0x14002d, 0x14002e],
    'Skull Woods - Spike Corner Key Drop': [0x14001b, 0x14001c],
    'Thieves\' Town - Hallway Pot Key': [0x14005d, 0x14005e],
    'Thieves\' Town - Spike Switch Pot Key': [0x14004e, 0x14004f],
    'Ice Palace - Jelly Key Drop': [0x140003, 0x140004],
    'Ice Palace - Conveyor Key Drop': [0x140021, 0x140022],
    'Ice Palace - Hammer Block Key Drop': [0x140024, 0x140025],
    'Ice Palace - Many Pots Pot Key': [0x140045, 0x140046],
    'Misery Mire - Spikes Pot Key': [0x140054, 0x140055],
    'Misery Mire - Fishbone Pot Key': [0x14004b, 0x14004c],
    'Misery Mire - Conveyor Crystal Key Drop': [0x140063, 0x140064],
    'Turtle Rock - Pokey 1 Key Drop': [0x140057, 0x140058],
    'Turtle Rock - Pokey 2 Key Drop': [0x140006, 0x140007],
    'Ganons Tower - Conveyor Cross Pot Key': [0x14003f, 0x140040],
    'Ganons Tower - Double Switch Pot Key': [0x140042, 0x140043],
    'Ganons Tower - Conveyor Star Pits Pot Key': [0x140039, 0x14003a],
    'Ganons Tower - Mini Helmasaur Key Drop': [0x14001e, 0x14001f]
}

# tuple contents:
# address to write to for item
# address to write to for player getting the item
# can this location drop a crystal
# hint tile/npc text for this location
location_table: typing.Dict[str,
                            typing.Tuple[typing.Optional[typing.Union[int, typing.List[int]]],
                                         typing.Optional[int],
                                         bool,
                                         typing.Optional[str]]] = \
    {'Mushroom': (0x180013, 0x186338, False, 'in the woods'),
     'Bottle Merchant': (0x2eb18, 0x186339, False, 'with a merchant'),
     'Flute Spot': (0x18014a, 0x18633d, False, 'underground'),
     'Sunken Treasure': (0x180145, 0x186354, False, 'underwater'),
     'Purple Chest': (0x33d68, 0x186359, False, 'from a box'),
     "Blind's Hideout - Top": (0xeb0f, 0x1862e3, False, 'in a basement'),
     "Blind's Hideout - Left": (0xeb12, 0x1862e6, False, 'in a basement'),
     "Blind's Hideout - Right": (0xeb15, 0x1862e9, False, 'in a basement'),
     "Blind's Hideout - Far Left": (0xeb18, 0x1862ec, False, 'in a basement'),
     "Blind's Hideout - Far Right": (0xeb1b, 0x1862ef, False, 'in a basement'),
     "Link's Uncle": (0x2df45, 0x18635f, False, 'with your uncle'),
     'Secret Passage': (0xe971, 0x186145, False, 'near your uncle'),
     'King Zora': (0xee1c3, 0x186360, False, 'at a high price'),
     "Zora's Ledge": (0x180149, 0x186358, False, 'near Zora'),
     'Waterfall Fairy - Left': (0xe9b0, 0x186184, False, 'near a fairy'),
     'Waterfall Fairy - Right': (0xe9d1, 0x1861a5, False, 'near a fairy'),
     "King's Tomb": (0xe97a, 0x18614e, False, 'alone in a cave'),
     'Floodgate Chest': (0xe98c, 0x186160, False, 'in the dam'),
     "Link's House": (0xe9bc, 0x186190, False, 'in your home'),
     'Kakariko Tavern': (0xe9ce, 0x1861a2, False, 'in the bar'),
     'Chicken House': (0xe9e9, 0x1861bd, False, 'near poultry'),
     "Aginah's Cave": (0xe9f2, 0x1861c6, False, 'with Aginah'),
     "Sahasrahla's Hut - Left": (0xea82, 0x186256, False, 'near the elder'),
     "Sahasrahla's Hut - Middle": (0xea85, 0x186259, False, 'near the elder'),
     "Sahasrahla's Hut - Right": (0xea88, 0x18625c, False, 'near the elder'),
     'Sahasrahla': (0x2f1fc, 0x186365, False, 'with the elder'),
     'Kakariko Well - Top': (0xea8e, 0x186262, False, 'in a well'),
     'Kakariko Well - Left': (0xea91, 0x186265, False, 'in a well'),
     'Kakariko Well - Middle': (0xea94, 0x186268, False, 'in a well'),
     'Kakariko Well - Right': (0xea97, 0x18626b, False, 'in a well'),
     'Kakariko Well - Bottom': (0xea9a, 0x18626e, False, 'in a well'),
     'Blacksmith': (0x18002a, 0x186366, False, 'with the smith'),
     'Magic Bat': (0x180015, 0x18635e, False, 'with the bat'),
     'Sick Kid': (0x339cf, 0x186367, False, 'with the sick'),
     'Hobo': (0x33e7d, 0x186368, False, 'with the hobo'),
     'Lost Woods Hideout': (0x180000, 0x186348, False, 'near a thief'),
     'Lumberjack Tree': (0x180001, 0x186349, False, 'in a hole'),
     'Cave 45': (0x180003, 0x18634b, False, 'alone in a cave'),
     'Graveyard Cave': (0x180004, 0x18634c, False, 'alone in a cave'),
     'Checkerboard Cave': (0x180005, 0x18634d, False, 'alone in a cave'),
     'Mini Moldorm Cave - Far Left': (0xeb42, 0x186316, False, 'near Moldorms'),
     'Mini Moldorm Cave - Left': (0xeb45, 0x186319, False, 'near Moldorms'),
     'Mini Moldorm Cave - Right': (0xeb48, 0x18631c, False, 'near Moldorms'),
     'Mini Moldorm Cave - Far Right': (0xeb4b, 0x18631f, False, 'near Moldorms'),
     'Mini Moldorm Cave - Generous Guy': (0x180010, 0x18635a, False, 'near Moldorms'),
     'Ice Rod Cave': (0xeb4e, 0x186322, False, 'in a frozen cave'),
     'Bonk Rock Cave': (0xeb3f, 0x186313, False, 'alone in a cave'),
     'Library': (0x180012, 0x18635c, False, 'near books'),
     'Potion Shop': (0x180014, 0x18635d, False, 'near potions'),
     'Lake Hylia Island': (0x180144, 0x186353, False, 'on an island'),
     'Maze Race': (0x180142, 0x186351, False, 'at the race'),
     'Desert Ledge': (0x180143, 0x186352, False, 'in the desert'),
     'Desert Palace - Big Chest': (0xe98f, 0x186163, False, 'in Desert Palace'),
     'Desert Palace - Torch': (0x180160, 0x186362, False, 'in Desert Palace'),
     'Desert Palace - Map Chest': (0xe9b6, 0x18618a, False, 'in Desert Palace'),
     'Desert Palace - Compass Chest': (0xe9cb, 0x18619f, False, 'in Desert Palace'),
     'Desert Palace - Big Key Chest': (0xe9c2, 0x186196, False, 'in Desert Palace'),
     'Desert Palace - Boss': (0x180151, 0x18633f, False, 'with Lanmolas'),
     'Eastern Palace - Compass Chest': (0xe977, 0x18614b, False, 'in Eastern Palace'),
     'Eastern Palace - Big Chest': (0xe97d, 0x186151, False, 'in Eastern Palace'),
     'Eastern Palace - Cannonball Chest': (0xe9b3, 0x186187, False, 'in Eastern Palace'),
     'Eastern Palace - Big Key Chest': (0xe9b9, 0x18618d, False, 'in Eastern Palace'),
     'Eastern Palace - Map Chest': (0xe9f5, 0x1861c9, False, 'in Eastern Palace'),
     'Eastern Palace - Boss': (0x180150, 0x18633e, False, 'with the Armos'),
     'Master Sword Pedestal': (0x289b0, 0x186369, False, 'at the pedestal'),
     'Hyrule Castle - Boomerang Chest': (0xe974, 0x186148, False, 'in Hyrule Castle'),
     'Hyrule Castle - Map Chest': (0xeb0c, 0x1862e0, False, 'in Hyrule Castle'),
     "Hyrule Castle - Zelda's Chest": (0xeb09, 0x1862dd, False, 'in Hyrule Castle'),
     'Sewers - Dark Cross': (0xe96e, 0x186142, False, 'in the sewers'),
     'Sewers - Secret Room - Left': (0xeb5d, 0x186331, False, 'in the sewers'),
     'Sewers - Secret Room - Middle': (0xeb60, 0x186334, False, 'in the sewers'),
     'Sewers - Secret Room - Right': (0xeb63, 0x186337, False, 'in the sewers'),
     'Sanctuary': (0xea79, 0x18624d, False, 'in Sanctuary'),
     'Castle Tower - Room 03': (0xeab5, 0x186289, False, 'in Castle Tower'),
     'Castle Tower - Dark Maze': (0xeab2, 0x186286, False, 'in Castle Tower'),
     'Old Man': (0xf69fa, 0x186364, False, 'with the old man'),
     'Spectacle Rock Cave': (0x180002, 0x18634a, False, 'alone in a cave'),
     'Paradox Cave Lower - Far Left': (0xeb2a, 0x1862fe, False, 'in a cave with seven chests'),
     'Paradox Cave Lower - Left': (0xeb2d, 0x186301, False, 'in a cave with seven chests'),
     'Paradox Cave Lower - Right': (0xeb30, 0x186304, False, 'in a cave with seven chests'),
     'Paradox Cave Lower - Far Right': (0xeb33, 0x186307, False, 'in a cave with seven chests'),
     'Paradox Cave Lower - Middle': (0xeb36, 0x18630a, False, 'in a cave with seven chests'),
     'Paradox Cave Upper - Left': (0xeb39, 0x18630d, False, 'in a cave with seven chests'),
     'Paradox Cave Upper - Right': (0xeb3c, 0x186310, False, 'in a cave with seven chests'),
     'Spiral Cave': (0xe9bf, 0x186193, False, 'in spiral cave'),
     'Ether Tablet': (0x180016, 0x18633b, False, 'at a monolith'),
     'Spectacle Rock': (0x180140, 0x18634f, False, 'atop a rock'),
     'Tower of Hera - Basement Cage': (0x180162, 0x18633a, False, 'in Tower of Hera'),
     'Tower of Hera - Map Chest': (0xe9ad, 0x186181, False, 'in Tower of Hera'),
     'Tower of Hera - Big Key Chest': (0xe9e6, 0x1861ba, False, 'in Tower of Hera'),
     'Tower of Hera - Compass Chest': (0xe9fb, 0x1861cf, False, 'in Tower of Hera'),
     'Tower of Hera - Big Chest': (0xe9f8, 0x1861cc, False, 'in Tower of Hera'),
     'Tower of Hera - Boss': (0x180152, 0x186340, False, 'with Moldorm'),
     'Pyramid': (0x180147, 0x186356, False, 'on the pyramid'),
     'Catfish': (0xee185, 0x186361, False, 'with a catfish'),
     'Stumpy': (0x330c7, 0x18636a, False, 'with tree boy'),
     'Digging Game': (0x180148, 0x186357, False, 'underground'),
     'Bombos Tablet': (0x180017, 0x18633c, False, 'at a monolith'),
     'Hype Cave - Top': (0xeb1e, 0x1862f2, False, 'near a bat-like man'),
     'Hype Cave - Middle Right': (0xeb21, 0x1862f5, False, 'near a bat-like man'),
     'Hype Cave - Middle Left': (0xeb24, 0x1862f8, False, 'near a bat-like man'),
     'Hype Cave - Bottom': (0xeb27, 0x1862fb, False, 'near a bat-like man'),
     'Hype Cave - Generous Guy': (0x180011, 0x18635b, False, 'with a bat-like man'),
     'Peg Cave': (0x180006, 0x18634e, False, 'alone in a cave'),
     'Pyramid Fairy - Left': (0xe980, 0x186154, False, 'near a fairy'),
     'Pyramid Fairy - Right': (0xe983, 0x186157, False, 'near a fairy'),
     'Brewery': (0xe9ec, 0x1861c0, False, 'alone in a home'),
     'C-Shaped House': (0xe9ef, 0x1861c3, False, 'alone in a home'),
     'Chest Game': (0xeda8, 0x18636b, False, 'as a prize'),
     'Bumper Cave Ledge': (0x180146, 0x186355, False, 'on a ledge'),
     'Mire Shed - Left': (0xea73, 0x186247, False, 'near sparks'),
     'Mire Shed - Right': (0xea76, 0x18624a, False, 'near sparks'),
     'Superbunny Cave - Top': (0xea7c, 0x186250, False, 'in a connection'),
     'Superbunny Cave - Bottom': (0xea7f, 0x186253, False, 'in a connection'),
     'Spike Cave': (0xea8b, 0x18625f, False, 'beyond spikes'),
     'Hookshot Cave - Top Right': (0xeb51, 0x186325, False, 'across pits'),
     'Hookshot Cave - Top Left': (0xeb54, 0x186328, False, 'across pits'),
     'Hookshot Cave - Bottom Right': (0xeb5a, 0x18632e, False, 'across pits'),
     'Hookshot Cave - Bottom Left': (0xeb57, 0x18632b, False, 'across pits'),
     'Floating Island': (0x180141, 0x186350, False, 'on an island'),
     'Mimic Cave': (0xe9c5, 0x186199, False, 'in a cave of mimicry'),
     'Swamp Palace - Entrance': (0xea9d, 0x186271, False, 'in Swamp Palace'),
     'Swamp Palace - Map Chest': (0xe986, 0x18615a, False, 'in Swamp Palace'),
     'Swamp Palace - Big Chest': (0xe989, 0x18615d, False, 'in Swamp Palace'),
     'Swamp Palace - Compass Chest': (0xeaa0, 0x186274, False, 'in Swamp Palace'),
     'Swamp Palace - Big Key Chest': (0xeaa6, 0x18627a, False, 'in Swamp Palace'),
     'Swamp Palace - West Chest': (0xeaa3, 0x186277, False, 'in Swamp Palace'),
     'Swamp Palace - Flooded Room - Left': (0xeaa9, 0x18627d, False, 'in Swamp Palace'),
     'Swamp Palace - Flooded Room - Right': (0xeaac, 0x186280, False, 'in Swamp Palace'),
     'Swamp Palace - Waterfall Room': (0xeaaf, 0x186283, False, 'in Swamp Palace'),
     'Swamp Palace - Boss': (0x180154, 0x186342, False, 'with Arrghus'),
     "Thieves' Town - Big Key Chest": (0xea04, 0x1861d8, False, "in Thieves' Town"),
     "Thieves' Town - Map Chest": (0xea01, 0x1861d5, False, "in Thieves' Town"),
     "Thieves' Town - Compass Chest": (0xea07, 0x1861db, False, "in Thieves' Town"),
     "Thieves' Town - Ambush Chest": (0xea0a, 0x1861de, False, "in Thieves' Town"),
     "Thieves' Town - Attic": (0xea0d, 0x1861e1, False, "in Thieves' Town"),
     "Thieves' Town - Big Chest": (0xea10, 0x1861e4, False, "in Thieves' Town"),
     "Thieves' Town - Blind's Cell": (0xea13, 0x1861e7, False, "in Thieves' Town"),
     "Thieves' Town - Boss": (0x180156, 0x186344, False, 'with Blind'),
     'Skull Woods - Compass Chest': (0xe992, 0x186166, False, 'in Skull Woods'),
     'Skull Woods - Map Chest': (0xe99b, 0x18616f, False, 'in Skull Woods'),
     'Skull Woods - Big Chest': (0xe998, 0x18616c, False, 'in Skull Woods'),
     'Skull Woods - Pot Prison': (0xe9a1, 0x186175, False, 'in Skull Woods'),
     'Skull Woods - Pinball Room': (0xe9c8, 0x18619c, False, 'in Skull Woods'),
     'Skull Woods - Big Key Chest': (0xe99e, 0x186172, False, 'in Skull Woods'),
     'Skull Woods - Bridge Room': (0xe9fe, 0x1861d2, False, 'near Mothula'),
     'Skull Woods - Boss': (0x180155, 0x186343, False, 'with Mothula'),
     'Ice Palace - Compass Chest': (0xe9d4, 0x1861a8, False, 'in Ice Palace'),
     'Ice Palace - Freezor Chest': (0xe995, 0x186169, False, 'in Ice Palace'),
     'Ice Palace - Big Chest': (0xe9aa, 0x18617e, False, 'in Ice Palace'),
     'Ice Palace - Iced T Room': (0xe9e3, 0x1861b7, False, 'in Ice Palace'),
     'Ice Palace - Spike Room': (0xe9e0, 0x1861b4, False, 'in Ice Palace'),
     'Ice Palace - Big Key Chest': (0xe9a4, 0x186178, False, 'in Ice Palace'),
     'Ice Palace - Map Chest': (0xe9dd, 0x1861b1, False, 'in Ice Palace'),
     'Ice Palace - Boss': (0x180157, 0x186345, False, 'with Kholdstare'),
     'Misery Mire - Big Chest': (0xea67, 0x18623b, False, 'in Misery Mire'),
     'Misery Mire - Map Chest': (0xea6a, 0x18623e, False, 'in Misery Mire'),
     'Misery Mire - Main Lobby': (0xea5e, 0x186232, False, 'in Misery Mire'),
     'Misery Mire - Bridge Chest': (0xea61, 0x186235, False, 'in Misery Mire'),
     'Misery Mire - Spike Chest': (0xe9da, 0x1861ae, False, 'in Misery Mire'),
     'Misery Mire - Compass Chest': (0xea64, 0x186238, False, 'in Misery Mire'),
     'Misery Mire - Big Key Chest': (0xea6d, 0x186241, False, 'in Misery Mire'),
     'Misery Mire - Boss': (0x180158, 0x186346, False, 'with Vitreous'),
     'Turtle Rock - Compass Chest': (0xea22, 0x1861f6, False, 'in Turtle Rock'),
     'Turtle Rock - Roller Room - Left': (0xea1c, 0x1861f0, False, 'in Turtle Rock'),
     'Turtle Rock - Roller Room - Right': (0xea1f, 0x1861f3, False, 'in Turtle Rock'),
     'Turtle Rock - Chain Chomps': (0xea16, 0x1861ea, False, 'in Turtle Rock'),
     'Turtle Rock - Big Key Chest': (0xea25, 0x1861f9, False, 'in Turtle Rock'),
     'Turtle Rock - Big Chest': (0xea19, 0x1861ed, False, 'in Turtle Rock'),
     'Turtle Rock - Crystaroller Room': (0xea34, 0x186208, False, 'in Turtle Rock'),
     'Turtle Rock - Eye Bridge - Bottom Left': (0xea31, 0x186205, False, 'in Turtle Rock'),
     'Turtle Rock - Eye Bridge - Bottom Right': (0xea2e, 0x186202, False, 'in Turtle Rock'),
     'Turtle Rock - Eye Bridge - Top Left': (0xea2b, 0x1861ff, False, 'in Turtle Rock'),
     'Turtle Rock - Eye Bridge - Top Right': (0xea28, 0x1861fc, False, 'in Turtle Rock'),
     'Turtle Rock - Boss': (0x180159, 0x186347, False, 'with Trinexx'),
     'Palace of Darkness - Shooter Room': (0xea5b, 0x18622f, False, 'in Palace of Darkness'),
     'Palace of Darkness - The Arena - Bridge': (0xea3d, 0x186211, False, 'in Palace of Darkness'),
     'Palace of Darkness - Stalfos Basement': (0xea49, 0x18621d, False, 'in Palace of Darkness'),
     'Palace of Darkness - Big Key Chest': (0xea37, 0x18620b, False, 'in Palace of Darkness'),
     'Palace of Darkness - The Arena - Ledge': (0xea3a, 0x18620e, False, 'in Palace of Darkness'),
     'Palace of Darkness - Map Chest': (0xea52, 0x186226, False, 'in Palace of Darkness'),
     'Palace of Darkness - Compass Chest': (0xea43, 0x186217, False, 'in Palace of Darkness'),
     'Palace of Darkness - Dark Basement - Left': (0xea4c, 0x186220, False, 'in Palace of Darkness'),
     'Palace of Darkness - Dark Basement - Right': (0xea4f, 0x186223, False, 'in Palace of Darkness'),
     'Palace of Darkness - Dark Maze - Top': (0xea55, 0x186229, False, 'in Palace of Darkness'),
     'Palace of Darkness - Dark Maze - Bottom': (0xea58, 0x18622c, False, 'in Palace of Darkness'),
     'Palace of Darkness - Big Chest': (0xea40, 0x186214, False, 'in Palace of Darkness'),
     'Palace of Darkness - Harmless Hellway': (0xea46, 0x18621a, False, 'in Palace of Darkness'),
     'Palace of Darkness - Boss': (0x180153, 0x186341, False, 'with Helmasaur King'),
     "Ganons Tower - Bob's Torch": (0x180161, 0x186363, False, "in Ganon's Tower"),
     'Ganons Tower - Hope Room - Left': (0xead9, 0x1862ad, False, "in Ganon's Tower"),
     'Ganons Tower - Hope Room - Right': (0xeadc, 0x1862b0, False, "in Ganon's Tower"),
     'Ganons Tower - Tile Room': (0xeae2, 0x1862b6, False, "in Ganon's Tower"),
     'Ganons Tower - Compass Room - Top Left': (0xeae5, 0x1862b9, False, "in Ganon's Tower"),
     'Ganons Tower - Compass Room - Top Right': (0xeae8, 0x1862bc, False, "in Ganon's Tower"),
     'Ganons Tower - Compass Room - Bottom Left': (0xeaeb, 0x1862bf, False, "in Ganon's Tower"),
     'Ganons Tower - Compass Room - Bottom Right': (0xeaee, 0x1862c2, False, "in Ganon's Tower"),
     'Ganons Tower - DMs Room - Top Left': (0xeab8, 0x18628c, False, "in Ganon's Tower"),
     'Ganons Tower - DMs Room - Top Right': (0xeabb, 0x18628f, False, "in Ganon's Tower"),
     'Ganons Tower - DMs Room - Bottom Left': (0xeabe, 0x186292, False, "in Ganon's Tower"),
     'Ganons Tower - DMs Room - Bottom Right': (0xeac1, 0x186295, False, "in Ganon's Tower"),
     'Ganons Tower - Map Chest': (0xead3, 0x1862a7, False, "in Ganon's Tower"),
     'Ganons Tower - Firesnake Room': (0xead0, 0x1862a4, False, "in Ganon's Tower"),
     'Ganons Tower - Randomizer Room - Top Left': (0xeac4, 0x186298, False, "in Ganon's Tower"),
     'Ganons Tower - Randomizer Room - Top Right': (0xeac7, 0x18629b, False, "in Ganon's Tower"),
     'Ganons Tower - Randomizer Room - Bottom Left': (0xeaca, 0x18629e, False, "in Ganon's Tower"),
     'Ganons Tower - Randomizer Room - Bottom Right': (0xeacd, 0x1862a1, False, "in Ganon's Tower"),
     "Ganons Tower - Bob's Chest": (0xeadf, 0x1862b3, False, "in Ganon's Tower"),
     'Ganons Tower - Big Chest': (0xead6, 0x1862aa, False, "in Ganon's Tower"),
     'Ganons Tower - Big Key Room - Left': (0xeaf4, 0x1862c8, False, "in Ganon's Tower"),
     'Ganons Tower - Big Key Room - Right': (0xeaf7, 0x1862cb, False, "in Ganon's Tower"),
     'Ganons Tower - Big Key Chest': (0xeaf1, 0x1862c5, False, "in Ganon's Tower"),
     'Ganons Tower - Mini Helmasaur Room - Left': (0xeafd, 0x1862d1, False, "atop Ganon's Tower"),
     'Ganons Tower - Mini Helmasaur Room - Right': (0xeb00, 0x1862d4, False, "atop Ganon's Tower"),
     'Ganons Tower - Pre-Moldorm Chest': (0xeb03, 0x1862d7, False, "atop Ganon's Tower"),
     'Ganons Tower - Validation Chest': (0xeb06, 0x1862da, False, "atop Ganon's Tower"),
     'Ganon': (None, None, False, 'from me'),
     'Agahnim 1': (None, None, False, 'from Ganon\'s wizardry form'),
     'Agahnim 2': (None, None, False, 'from Ganon\'s wizardry form'),
     'Floodgate': (None, None, False, None),
     'Frog': (None, None, False, None),
     'Missing Smith': (None, None, False, None),
     'Dark Blacksmith Ruins': (None, None, False, None),
     'Eastern Palace - Prize': ([0x1209D, 0x53EF8, 0x53EF9, 0x180052, 0x18007C, 0xC6FE], None, True, 'Eastern Palace'),
     'Desert Palace - Prize': ([0x1209E, 0x53F1C, 0x53F1D, 0x180053, 0x180078, 0xC6FF], None, True, 'Desert Palace'),
     'Tower of Hera - Prize': (
         [0x120A5, 0x53F0A, 0x53F0B, 0x18005A, 0x18007A, 0xC706], None, True, 'Tower of Hera'),
     'Palace of Darkness - Prize': (
         [0x120A1, 0x53F00, 0x53F01, 0x180056, 0x18007D, 0xC702], None, True, 'Palace of Darkness'),
     'Swamp Palace - Prize': (
         [0x120A0, 0x53F6C, 0x53F6D, 0x180055, 0x180071, 0xC701], None, True, 'Swamp Palace'),
     'Thieves\' Town - Prize': (
         [0x120A6, 0x53F36, 0x53F37, 0x18005B, 0x180077, 0xC707], None, True, 'Thieves\' Town'),
     'Skull Woods - Prize': (
         [0x120A3, 0x53F12, 0x53F13, 0x180058, 0x18007B, 0xC704], None, True, 'Skull Woods'),
     'Ice Palace - Prize': (
         [0x120A4, 0x53F5A, 0x53F5B, 0x180059, 0x180073, 0xC705], None, True, 'Ice Palace'),
     'Misery Mire - Prize': (
         [0x120A2, 0x53F48, 0x53F49, 0x180057, 0x180075, 0xC703], None, True, 'Misery Mire'),
     'Turtle Rock - Prize': (
         [0x120A7, 0x53F24, 0x53F25, 0x18005C, 0x180079, 0xC708], None, True, 'Turtle Rock')}

lookup_id_to_name = {data[0]: name for name, data in location_table.items() if type(data[0]) == int}
lookup_id_to_name = {**lookup_id_to_name, **{data[1]: name for name, data in key_drop_data.items()}, -1: "cheat console"}
lookup_id_to_name.update(shop_table_by_location_id)
lookup_name_to_id = {name: data[0] for name, data in location_table.items() if type(data[0]) == int}
lookup_name_to_id = {**lookup_name_to_id, **{name: data[1] for name, data in key_drop_data.items()}, "cheat console": -1}
lookup_name_to_id.update(shop_table_by_location)

lookup_vanilla_location_to_entrance = {1572883: 'Kings Grave Inner Rocks', 191256: 'Kings Grave Inner Rocks',
                                       1573194: 'Kings Grave Inner Rocks', 1573189: 'Kings Grave Inner Rocks',
                                       212328: 'Kings Grave Inner Rocks', 60175: 'Blinds Hideout',
                                       60178: 'Blinds Hideout', 60181: 'Blinds Hideout', 60184: 'Blinds Hideout',
                                       60187: 'Blinds Hideout', 188229: 'Hyrule Castle Secret Entrance Drop',
                                       59761: 'Hyrule Castle Secret Entrance Drop', 975299: 'Zoras River',
                                       1573193: 'Zoras River', 59824: 'Waterfall of Wishing',
                                       59857: 'Waterfall of Wishing', 59770: 'Kings Grave', 59788: 'Dam',
                                       59836: 'Links House', 59854: 'Tavern North', 59881: 'Chicken House',
                                       59890: 'Aginahs Cave', 60034: 'Sahasrahlas Hut', 60037: 'Sahasrahlas Hut',
                                       60040: 'Sahasrahlas Hut', 193020: 'Sahasrahlas Hut',
                                       60046: 'Kakariko Well Drop', 60049: 'Kakariko Well Drop',
                                       60052: 'Kakariko Well Drop', 60055: 'Kakariko Well Drop',
                                       60058: 'Kakariko Well Drop', 1572906: 'Blacksmiths Hut',
                                       1572885: 'Bat Cave Drop', 211407: 'Sick Kids House',
                                       212605: 'Hobo Bridge', 1572864: 'Lost Woods Hideout Drop',
                                       1572865: 'Lumberjack Tree Tree', 1572867: 'Cave 45',
                                       1572868: 'Graveyard Cave', 1572869: 'Checkerboard Cave',
                                       60226: 'Mini Moldorm Cave', 60229: 'Mini Moldorm Cave',
                                       60232: 'Mini Moldorm Cave', 60235: 'Mini Moldorm Cave',
                                       1572880: 'Mini Moldorm Cave', 60238: 'Ice Rod Cave',
                                       60223: 'Bonk Rock Cave', 1572882: 'Library', 1572884: 'Potion Shop',
                                       1573188: 'Lake Hylia Island Mirror Spot',
                                       1573186: 'Maze Race Mirror Spot', 1573187: 'Desert Ledge Return Rocks',
                                       59791: 'Desert Palace Entrance (West)',
                                       1573216: 'Desert Palace Entrance (West)',
                                       59830: 'Desert Palace Entrance (West)',
                                       59851: 'Desert Palace Entrance (West)',
                                       59842: 'Desert Palace Entrance (West)',
                                       1573201: 'Desert Palace Entrance (North)', 59767: 'Eastern Palace',
                                       59773: 'Eastern Palace', 59827: 'Eastern Palace', 59833: 'Eastern Palace',
                                       59893: 'Eastern Palace', 1573200: 'Eastern Palace',
                                       166320: 'Master Sword Meadow', 59764: 'Hyrule Castle Entrance (South)',
                                       60172: 'Hyrule Castle Entrance (South)',
                                       60169: 'Hyrule Castle Entrance (South)',
                                       59758: 'Hyrule Castle Entrance (South)',
                                       60253: 'Hyrule Castle Entrance (South)',
                                       60256: 'Hyrule Castle Entrance (South)',
                                       60259: 'Hyrule Castle Entrance (South)', 60025: 'Sanctuary S&Q',
                                       60085: 'Agahnims Tower', 60082: 'Agahnims Tower',
                                       1010170: 'Old Man Cave (West)', 1572866: 'Spectacle Rock Cave',
                                       60202: 'Paradox Cave (Bottom)', 60205: 'Paradox Cave (Bottom)',
                                       60208: 'Paradox Cave (Bottom)', 60211: 'Paradox Cave (Bottom)',
                                       60214: 'Paradox Cave (Bottom)', 60217: 'Paradox Cave (Bottom)',
                                       60220: 'Paradox Cave (Bottom)', 59839: 'Spiral Cave',
                                       1572886: 'Death Mountain (Top)', 1573184: 'Spectacle Rock Mirror Spot',
                                       1573218: 'Tower of Hera', 59821: 'Tower of Hera', 59878: 'Tower of Hera',
                                       59899: 'Tower of Hera', 59896: 'Tower of Hera', 1573202: 'Tower of Hera',
                                       1573191: 'Top of Pyramid', 975237: 'Catfish Entrance Rock',
                                       209095: 'South Dark World Bridge', 1573192: 'South Dark World Bridge',
                                       1572887: 'Bombos Tablet Mirror Spot', 60190: 'Hype Cave',
                                       60193: 'Hype Cave', 60196: 'Hype Cave', 60199: 'Hype Cave',
                                       1572881: 'Hype Cave', 1572870: 'Dark World Hammer Peg Cave',
                                       59776: 'Pyramid Fairy', 59779: 'Pyramid Fairy', 59884: 'Brewery',
                                       59887: 'C-Shaped House', 60840: 'Chest Game',
                                       1573190: 'Bumper Cave (Bottom)', 60019: 'Mire Shed', 60022: 'Mire Shed',
                                       60028: 'Superbunny Cave (Top)', 60031: 'Superbunny Cave (Top)',
                                       60043: 'Spike Cave', 60241: 'Hookshot Cave', 60244: 'Hookshot Cave',
                                       60250: 'Hookshot Cave', 60247: 'Hookshot Cave',
                                       1573185: 'Floating Island Mirror Spot', 59845: 'Mimic Cave',
                                       60061: 'Swamp Palace', 59782: 'Swamp Palace', 59785: 'Swamp Palace',
                                       60064: 'Swamp Palace', 60070: 'Swamp Palace', 60067: 'Swamp Palace',
                                       60073: 'Swamp Palace', 60076: 'Swamp Palace', 60079: 'Swamp Palace',
                                       1573204: 'Swamp Palace', 59908: 'Thieves Town', 59905: 'Thieves Town',
                                       59911: 'Thieves Town', 59914: 'Thieves Town', 59917: 'Thieves Town',
                                       59920: 'Thieves Town', 59923: 'Thieves Town', 1573206: 'Thieves Town',
                                       59803: 'Skull Woods First Section Door',
                                       59848: 'Skull Woods First Section Hole (East)',
                                       59794: 'Skull Woods First Section Hole (West)',
                                       59809: 'Skull Woods First Section Hole (West)',
                                       59800: 'Skull Woods First Section Hole (North)',
                                       59806: 'Skull Woods Second Section Door (East)',
                                       59902: 'Skull Woods Final Section', 1573205: 'Skull Woods Final Section',
                                       59860: 'Ice Palace', 59797: 'Ice Palace', 59818: 'Ice Palace',
                                       59875: 'Ice Palace', 59872: 'Ice Palace', 59812: 'Ice Palace',
                                       59869: 'Ice Palace', 1573207: 'Ice Palace', 60007: 'Misery Mire',
                                       60010: 'Misery Mire', 59998: 'Misery Mire', 60001: 'Misery Mire',
                                       59866: 'Misery Mire', 60004: 'Misery Mire', 60013: 'Misery Mire',
                                       1573208: 'Misery Mire', 59938: 'Turtle Rock', 59932: 'Turtle Rock',
                                       59935: 'Turtle Rock', 59926: 'Turtle Rock',
                                       59941: 'Dark Death Mountain Ledge (West)',
                                       59929: 'Dark Death Mountain Ledge (East)',
                                       59956: 'Dark Death Mountain Ledge (West)',
                                       59953: 'Turtle Rock Isolated Ledge Entrance',
                                       59950: 'Turtle Rock Isolated Ledge Entrance',
                                       59947: 'Turtle Rock Isolated Ledge Entrance',
                                       59944: 'Turtle Rock Isolated Ledge Entrance',
                                       1573209: 'Turtle Rock Isolated Ledge Entrance',
                                       59995: 'Palace of Darkness', 59965: 'Palace of Darkness',
                                       59977: 'Palace of Darkness', 59959: 'Palace of Darkness',
                                       59962: 'Palace of Darkness', 59986: 'Palace of Darkness',
                                       59971: 'Palace of Darkness', 59980: 'Palace of Darkness',
                                       59983: 'Palace of Darkness', 59989: 'Palace of Darkness',
                                       59992: 'Palace of Darkness', 59968: 'Palace of Darkness',
                                       59974: 'Palace of Darkness', 1573203: 'Palace of Darkness',
                                       1573217: 'Ganons Tower', 60121: 'Ganons Tower', 60124: 'Ganons Tower',
                                       60130: 'Ganons Tower', 60133: 'Ganons Tower', 60136: 'Ganons Tower',
                                       60139: 'Ganons Tower', 60142: 'Ganons Tower', 60088: 'Ganons Tower',
                                       60091: 'Ganons Tower', 60094: 'Ganons Tower', 60097: 'Ganons Tower',
                                       60115: 'Ganons Tower', 60112: 'Ganons Tower', 60100: 'Ganons Tower',
                                       60103: 'Ganons Tower', 60106: 'Ganons Tower', 60109: 'Ganons Tower',
                                       60127: 'Ganons Tower', 60118: 'Ganons Tower', 60148: 'Ganons Tower',
                                       60151: 'Ganons Tower', 60145: 'Ganons Tower', 60157: 'Ganons Tower',
                                       60160: 'Ganons Tower', 60163: 'Ganons Tower', 60166: 'Ganons Tower',
                                       0x140037: 'Hyrule Castle Entrance (South)',
                                       0x140034: 'Hyrule Castle Entrance (South)',
                                       0x14000d: 'Hyrule Castle Entrance (South)',
                                       0x14003d: 'Hyrule Castle Entrance (South)',
                                       0x14005b: 'Eastern Palace', 0x140049: 'Eastern Palace',
                                       0x140031: 'Desert Palace Entrance (North)',
                                       0x14002b: 'Desert Palace Entrance (North)',
                                       0x140028: 'Desert Palace Entrance (North)',
                                       0x140061: 'Agahnims Tower', 0x140052: 'Agahnims Tower',
                                       0x140019: 'Swamp Palace', 0x140016: 'Swamp Palace', 0x140013: 'Swamp Palace',
                                       0x140010: 'Swamp Palace', 0x14000a: 'Swamp Palace',
                                       0x14002e: 'Skull Woods Second Section Door (East)',
                                       0x14001c: 'Skull Woods Final Section',
                                       0x14005e: 'Thieves Town', 0x14004f: 'Thieves Town',
                                       0x140004: 'Ice Palace', 0x140022: 'Ice Palace',
                                       0x140025: 'Ice Palace', 0x140046: 'Ice Palace',
                                       0x140055: 'Misery Mire', 0x14004c: 'Misery Mire',
                                       0x140064: 'Misery Mire',
                                       0x140058: 'Turtle Rock', 0x140007: 'Dark Death Mountain Ledge (West)',
                                       0x140040: 'Ganons Tower', 0x140043: 'Ganons Tower',
                                       0x14003a: 'Ganons Tower', 0x14001f: 'Ganons Tower'}

lookup_prizes = {location for location in location_table if location.endswith(" - Prize")}
lookup_boss_drops = {location for location in location_table if location.endswith(" - Boss")}