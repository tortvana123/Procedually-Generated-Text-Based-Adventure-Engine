# "Procedually Generated" Text Based Adventure Engine
A GUI game engine for a procedually generatated text adventure, which is intended to take place in a "dungeon" type enviroment.

## Required third party modules:
* ruamel.yaml for YAML support (Game Data)
* appjar for simple GUI (needs TKinter as the master library)


## Roadmap:
### Done:
* Implement the YAML data loading. **_✓_**
* Implement a title screen **_✓_**
### In Progress:
* Implement the "rooms" system.
 * Basic room naming and descriptions. **_✓_**
 * Moving between rooms
 * YAML file
  * Add possible room properties/actions. (Has monster, has item, shop etc.)
  * Add a few room descriptions with accociated properties and room specific options.
### Future:
* Implement a door key system and a inventory for keys. (a keyring?)
* Implement character stats.
* Implement item inventory and character item slots.
* Implement active and passive dangers. (Active: Monsters etc.; Passive: Traps etc.)

