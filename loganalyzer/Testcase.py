# -*- coding: utf-8 -*-

from loganalyzer.Parser import *
from loganalyzer.Game import *
from loganalyzer.Analyzer import *


parser = Parser('Data/20190213193824-Namira_4-vs-CYRUS2018_312')

game = Game(parser)

analyzer = Analyzer(game)
analyzer.analyze()

print("Right Team :"+analyzer.game.right_team.name + "\n")
print("Game result :"+analyzer.status_r)
print("Goals :"+str(analyzer.game.right_goal))
print("True Pass:"+str(analyzer.pass_r))
print("Wrong Pass:"+str(analyzer.intercept_l))
print("Pass in Lenght:"+str(analyzer.pass_in_length_r))
print("Pass in Width:"+str(analyzer.pass_in_width_r))
print("Pass Accuracy:"+str(analyzer.pass_accuracy_r))
print("on_target_shoot:"+str(analyzer.on_target_shoot_r))
print("off_target_shoot:"+str(analyzer.off_target_shoot_r))
print("Shoot in Lenght:"+str(analyzer.shoot_in_length_r))
print("Shoot in Width:"+str(analyzer.shoot_in_width_r))
print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_r))
print("Possession:"+str(analyzer.possession_r))
print("Stamina Usage:"+str(analyzer.used_stamina_agents_r))
print("moved Distance:"+str(analyzer.team_moved_distance_r))
print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_r))
print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_r))
print("Average Stamina Per distance 10 Player: " +
      str(analyzer.av_st_per_dist_10p_r))
print("Stamina per Distance:"+str(analyzer.used_per_distance_r)+"\n"+"\n")


print("Left Team :"+analyzer.game.left_team.name+"\n")
print("Game result :"+analyzer.status_l)
print("Goals :"+str(analyzer.game.left_goal))
print("Wrong Pass:"+str(analyzer.intercept_r))
print("Pass in Lenght:"+str(analyzer.pass_in_length_l))
print("Pass in Width:"+str(analyzer.pass_in_width_l))
print("Pass Accuracy:"+str(analyzer.pass_accuracy_l))
print("on_target_shoot:"+str(analyzer.on_target_shoot_l))
print("off_target_shoot:"+str(analyzer.off_target_shoot_l))
print("Shoot in Lenght:"+str(analyzer.shoot_in_length_l))
print("Shoot in Width:"+str(analyzer.shoot_in_width_l))
print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_l))
print("Possession:"+str(analyzer.possession_l))
print("Stamina Usage:"+str(analyzer.used_stamina_agents_l))
print("moved Distance:"+str(analyzer.team_moved_distance_l))
print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_l))
print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_l))
print("Average Stamina Per distance 10 Player: " +
      str(analyzer.av_st_per_dist_10p_l))
print("Stamina per Distance:"+str(analyzer.used_per_distance_l)+"\n")


for region in analyzer.regions:
    print("Ball in Region Percentage", region.name,
          " ", region.ball_in_region_cycles)

print("\nRight Team Regions Data")

# Agent_regions
# owner_cycles    : cycles player is ball owner in the region
# position_cycles : cycles player is in the region
for agent in game.right_team.agents:
    for region in agent.regions:
        print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
              str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))

print("\nLeft Team Regions Data")
for agent in game.left_team.agents:
    for region in agent.regions:
        print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
              str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))

# Drawing Heatmap of the game
heatmap = analyzer.draw_heatmap(right_team=True, left_team=True)
