# CBPi4 Grouped Actor Plugin

### This Actor plugin can be used to group up to 8 actors into on actor

## Group multiple actors into one actor
- This plugin allows to group up to 8 actors into one actor
- If the Grouped Actor is switched on, all actors that belong to the group will be switched on
- If the power is changed for the grouped actor, all actors that belong to the group will be set to the same power

### Installation:

You can install it directly via pypi.org:	
- sudo pip3 install cbpi4-GroupedActor 

Alternativeley you can install (or clone) it from the GIT Repo. In case of updates, you will find them here first:
- sudo pip3 install https://github.com/avollkopf/cbpi4-GroupedActor/archive/main.zip


## Parameters:

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-groupedActor-setting.png?raw=true)

- Actor 1-8: Actors can be added to the group

## Usage:

- You can add individual Actors to your dashboard
- Add the grouped Actor to your dashboard and enable actions to set power for the actor group
- The example below shows the grouped actor and the two actors that are in the group:

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-actorgroup.png?raw=true)

- If you click on the grouped actor button, both actors in the group will be switched on.

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-actorgroup-active.png?raw=true)

- If you click on the action menu of the grouped actor (3 dots on the right), the actions menu will be opend to set the power

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-actorgroup-actionmenu.png?raw=true)

- If you choose 'Set Power', the corresponding dialog will open and you can set the power for the grouped actor. Hit save.

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-setpower.png?raw=true)

- Once you saved the power setting, the power of the grouped actor and the actors from the group are set to the entered value.

![Settings](https://github.com/avollkopf/cbpi4-GroupedActor/blob/main/cbpi4-groupedActor-power.png?raw=true)

The grouped actor can be alo used in the Kettle Logic plugins that use power settings (e.g. PIDBoil,...)

Changelog:

- 11.05.22: (0.0.5) Updated README (removed cbpi add)
- 07.02.22: (0.0.4) Removal of duplicated mqtt messages
- 06.02.22: (0.0.3) Some minor fixes 
- 26.11.21: (0.0.2) Added power settings to the grouped actor and created README
- 23.07.21: (0.0.1) Initial commit
