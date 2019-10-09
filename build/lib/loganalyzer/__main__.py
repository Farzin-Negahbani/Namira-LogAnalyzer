import sys
import os
import argparse
from loganalyzer.Game import *
from loganalyzer.Parser import *
from loganalyzer.Analyzer import * 
# from Parser import *
# from Game import * 
# from Analyzer import * 

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Input file path", required=True, dest='path')
    parser.add_argument("--save_path", help="Output saving path.", dest='save_path')
    parser.add_argument('--version', action='version', version='1.0.0')
    args = parser.parse_args()
    if args.save_path is None:
        args.save_path = args.path+".log"
    return args
    
def write_to_file(save_path,analyzer):
    f = open(save_path,'w')
    #right TEAM
    f.writelines("Right Team"+os.linesep)
    f.writelines(analyzer.game.right_team.name+os.linesep)
    f.writelines("True Pass:"+str(analyzer.pass_r )+os.linesep)
    f.writelines("Intercept:"+str(analyzer.intercept_r )+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_r )+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_r )+os.linesep)
    f.writelines("Game result :"+analyzer.status_r+os.linesep)
    f.writelines("Goals :"+str(analyzer.game.right_goal)+os.linesep)
    f.writelines("True Pass:"+str(analyzer.pass_r )+os.linesep)
    f.writelines("Wrong Pass:"+str(analyzer.intercept_l )+os.linesep)
    f.writelines("Pass in Lenght:"+str(analyzer.pass_in_length_r )+os.linesep)
    f.writelines("Pass in Width:"+str(analyzer.pass_in_width_r )+os.linesep)
    f.writelines("Pass Accuracy:"+str(analyzer.pass_accuracy_r)+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_r)+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_r )+os.linesep)
    f.writelines("Shoot in Lenght:"+str(analyzer.shoot_in_length_r )+os.linesep)
    f.writelines("Shoot in Width:"+str(analyzer.shoot_in_width_r )+os.linesep)
    f.writelines("Shoot Accuracy:"+str(analyzer.shoot_accuracy_r)+os.linesep)
    f.writelines("Possession:"+str(analyzer.possession_r)+os.linesep)
    f.writelines("Stamina Usage:"+str(analyzer.used_stamina_agents_r )+os.linesep)
    f.writelines("moved Distance:"+str(analyzer.team_moved_distance_r )+os.linesep)
    f.writelines("Average Distance 10 Player: "+str(analyzer.average_distance_10p_r)+os.linesep)
    f.writelines("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_r)+os.linesep)
    f.writelines("Average Stamina Per distance 10 Player: "+str(analyzer.av_st_per_dist_10p_r )+os.linesep)
    f.writelines("Stamina per Distance:"+str(analyzer.used_per_distance_r )+"\n"+"\n"+os.linesep)
    #left TEAM
    f.writelines(os.linesep)
    f.writelines("Left Team"+os.linesep)
    f.writelines(analyzer.game.left_team.name+os.linesep)
    f.writelines("True Pass:"+str(analyzer.pass_l )+os.linesep)
    f.writelines("Intercept:"+str(analyzer.intercept_l )+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_l )+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_l )+os.linesep)
    f.writelines("Game result :"+analyzer.status_l+os.linesep)
    f.writelines("Goals :"+str(analyzer.game.left_goal)+os.linesep)
    f.writelines("Wrong Pass:"+str(analyzer.intercept_r )+os.linesep)
    f.writelines("Pass in Lenght:"+str(analyzer.pass_in_length_l )+os.linesep)
    f.writelines("Pass in Width:"+str(analyzer.pass_in_width_l )+os.linesep)
    f.writelines("Pass Accuracy:"+str(analyzer.pass_accuracy_l)+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_l )+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_l )+os.linesep)
    f.writelines("Shoot in Lenght:"+str(analyzer.shoot_in_length_l )+os.linesep)
    f.writelines("Shoot in Width:"+str(analyzer.shoot_in_width_l )+os.linesep)
    f.writelines("Shoot Accuracy:"+str(analyzer.shoot_accuracy_l)+os.linesep)
    f.writelines("Possession:"+str(analyzer.possession_l)+os.linesep)
    f.writelines("Stamina Usage:"+str(analyzer.used_stamina_agents_l )+os.linesep)
    f.writelines("moved Distance:"+str(analyzer.team_moved_distance_l )+os.linesep)
    f.writelines("Average Distance 10 Player: "+str(analyzer.average_distance_10p_l)+os.linesep)
    f.writelines("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_l)+os.linesep)
    f.writelines("Average Stamina Per distance 10 Player: "+str(analyzer.av_st_per_dist_10p_l )+os.linesep)
    f.writelines("Stamina per Distance:"+str(analyzer.used_per_distance_l )+os.linesep)

    for region in analyzer.regions:
        f.writelines("Ball in Region Percentage"+" "+str(region.name)+" "+str(region.ball_in_region_cycles)+os.linesep)

    f.writelines(os.linesep)
    f.writelines("Right Team Regions Data"+os.linesep)
    #Agent_regions   
    # owner_cycles    : cycles player is ball owner in the region
    # position_cycles : cycles player is in the region
    for agent in analyzer.game.right_team.agents :
        for region in agent.regions:
            f.writelines(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: "+ str(region.owner_cycles) + "  "+ "position_cycles: "+str(region.position_cycles)+os.linesep)
    f.writelines(os.linesep)
    f.writelines("Left Team Regions Data"+os.linesep)
    for agent in analyzer.game.left_team.agents :
        for region in agent.regions:
            f.writelines(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: "+ str(region.owner_cycles) + "  "+ "position_cycles: "+str(region.position_cycles)+os.linesep)
    f.close()
def main():
    args=parse_args()
    path = args.path
    save_path = args.save_path
    parser = Parser(path)
    game = Game(parser) 
    analyzer = Analyzer(game)
    analyzer.analyze()
    write_to_file(save_path,analyzer)

    #Drawing Heatmap of the game      
    heatmap = analyzer.draw_heatmap(right_team = True, Left_team= True)


