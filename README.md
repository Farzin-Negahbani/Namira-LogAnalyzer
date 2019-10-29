# Namira LogAnalyzer
Python Script for parsing and analyzing agent2D soccer simulation rcl and rcg logs. This used in [NAMIRA TPAS](https://github.com/Farzin-Negahbani/Namira_TPAS)
a Tournament Planning and Analyzer Software.

## Getting Started

You just need python 3.x! and setuptools running on any OS.
### Pre Installation
##### Ubuntu
    sudo apt-get update
    sudo apt-get install python3 python3-setuptools python3-numpy python3-matplotlib
### Installation
    python3 ./setup.py install
<!-- ### Uninstallation
    python ./setup.py uninstall -->
### How To Use?
## Capabilities of this analyzer

This analyzer could report many match facts, a list of them are as follows
- Pass count
  - Pass in Width 
  - Pass in Length
  - Pass Counting in 9 determined regions (A, B, ... I)
  - Pass Accuracy 
  - Pass Interception
  - True Pass 
- Shoot count
  - Shoot in Width 
  - Shoot in Length
  - Shoot Counting in 9 determined regions (A, B, ... I)
  - On Target Shoot
  - Off Target Shoot
  - Shoot Accuracy 
- Possession 
  - Possession in 9 determined regions (A, B, ... I)
  - Possession in 9 determined regions for each player (A, B, ... I)
  - Possession on any custom region
- Position 
  - Cycles players are in 9 determined regions (A, B, ... I)
- Players moved distance
- Players stamina usage
- Players stamina used per distance
- Game heatmap of teams
- Kick count
- Tackle count
- say count
### How to Use
#### As a Script
    loganalyzer --path <log file without .rcl or .rcg >
#### As a Module
    import loganalyzer
    from loganalyzer import Parser
    from loganalyzer import Game
    from loganalyzer import Analyzer
    parser = Parser('path to log file without .rcl or .rcg')
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()
    left_team_pass = analyzer.pass_l 
    left_team_in_target_shoot = analyzer.in_target_shoot_l 
    left_team_agent_1 = game.left_team.agents[0].data 
## Questions
Any questions or suggestions please feel free to contact :
* **[Farzin Negahbani](mailto: farzin.negahbani@gmail.com)** 
* **[Shahryar Bahmai](mailto: shahryarbahmeie@gmail.com)**  
