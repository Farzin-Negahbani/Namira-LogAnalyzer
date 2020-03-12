# Namira Log-Analyzer

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
    sudo apt-get install python3 python3-pip python3-setuptools python3-numpy python3-matplotlib

### Installation
    git clone https://github.com/Farzin-Negahbani/Namira_LogAnalyzer.git
    cd Namira_LogAnalyzer
Then you can do one of the following methods:
#### Method 1
    sudo python3 ./setup.py install
#### Method 2
    pip install .

### Uninstall
    pip uninstall loganalyzer

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
#### Default Regions 
<p align="center">    
  <img width="400" height="280" src="https://github.com/Farzin-Negahbani/Namira_LogAnalyzer/blob/master/Img/default_regions.jpeg">
</p>

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

## Publication

If you found this work useful in your research, please give credits to the authors by citing:

- Asali, E., Negahbani, F., Tafazzol, S., Maghareh, M.S., Bahmeie, S., Barazandeh, S., Mirian, S., & Moshkelgosha, M. (2018). Namira Soccer 2 D Simulation Team Description Paper 2018. [PDF](https://archive.robocup.info/Soccer/Simulation/2D/TDPs/RoboCup/2018/Namira_SS2D_RC2018_TDP.pdf)
- Asali, E., Moravej, A., Akbarpoor, S., Asali, O., Katebzadeh, M., Tafazol, S., ... & Haghighi, A. B. (2017). Persian Gulf Soccer 2D Simulation Team Description Paper 2017. In The 21th annual RoboCup International Symposium, Japan, Nagoya. [PDF](https://www.robocup2017.org/file/symposium/soccer_sim_2D/TDP_PersianGulf.pdf)

### Todo

- [ ] Adding pass and shoot lenght attributes
