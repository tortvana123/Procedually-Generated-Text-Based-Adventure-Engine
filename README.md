# "Procedually Generated" Text Based Adventure Engine
A GUI game engine for a procedually generatated text adventure, which is intended to take place in a "dungeon" type enviroment.

## Required third party modules:
* ruamel.yaml for YAML support (Game Data)
* appjar for simple GUI (needs TKinter as the master library)

## To-do list:
* ~~Redo the YAML import with try/except~~ (If/else makes more sense in this case)

## Roadmap:
### Done:
* Implement the YAML data loading. **_✓_**
* Implement a title screen **_✓_**
* ~~Implement room generation as a seperate function **_✓_**~~
  * Implement room generation into the Room class. **_✓_**

### In Progress:
* Implement the "rooms" system.
 * Basic room naming and descriptions. **_✓_**
 * Dropdown list for actions (WIP)
 * YAML file
   * Add possible room properties/actions. (Has monster, has item, shop, can you move to the next room? etc.)
   * Add a few room descriptions with accociated properties and room specific options.
### Future:
* Implement a door key system and a inventory for keys. (a keyring?)
* Implement character stats.
* Implement item inventory and character item slots.
* Implement active and passive dangers. (Active: Monsters etc.; Passive: Traps etc.)

