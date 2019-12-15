# Namira LogAnalyzer
Python Script for parsing and analyzing agent2D soccer simulation rcl and rcg log files. This has been used in [NAMIRA TPAS](https://github.com/Farzin-Negahbani/Namira_TPAS),
a Tournament Planning and Analyzer Software.
## Why is this useful?
- Generating comprehensive data about your team performance on different matches. 
- Evaluating different capabilities of your team .
- Using extracted data to train machine learning algorithm.

## Getting Started

You just need python 3.x! and setuptools running on any OS.
### Pre Installation
##### Ubuntu
    sudo apt-get update
    sudo apt-get install python3 python3-setuptools python3-numpy python3-matplotlib
### Installation
    python3 ./setup.py install
### Uninstall
    python ./setup.py uninstall 

## Capabilities of this analyzer

This analyzer can report following match facts and information:
- Pass
   - Pass Counting 
     - In Width 
     - In Length
     - In 9 determined regions (A, B, ... I)  
     - True Passes 
  - Pass Interception
  - Pass Accuracy 
- Shoot
  - Shoot Counting 
    - In Width 
    - In Length
    - In 9 determined regions (A, B, ... I)
    - On Target Shoots
    - Off Target Shoots
  - Shoot Accuracy 
- Possession 
  - Possession in 9 determined regions (A, B, ... I) for the teams
  - Possession in 9 determined regions for each player (A, B, ... I)
  - Possession of any team or player in any custom region
- Position 
  - Cycles each player is in 9 determined regions (A, B, ... I)
  - Cycles each player is in any of custom regions (A, B, ... I)
- Players' moved distance
- Players' stamina usage
- Players' stamina used per distance
- Game Heatmap of teams
- Kick count
- Tackle count
- Say count
### How to Use
To check how to retrieve data, take a look at **Testcase.py** file. 
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
For any questions or suggestions please feel free to contact or open an issue.
* **[Farzin Negahbani](mailto:farzin.negahbani@gmail.com)** 
* **[Shahryar Bahmai](mailto:shahryarbahmeie@gmail.com)**  
