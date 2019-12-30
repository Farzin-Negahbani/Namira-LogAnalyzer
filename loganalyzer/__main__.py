import sys
import os
import argparse
import json
from loganalyzer.Game import *
from loganalyzer.Parser import *
from loganalyzer.Analyzer import *
# from Parser import *
# from Game import *
# from Analyzer import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Input file path",
                        required=True, dest='path')
    parser.add_argument(
        "--save_path", help="Output saving path.", dest='save_path')
    parser.add_argument("--heatmap", help="Show Heatmap",
                        dest='heat_map')
    parser.add_argument('--version', action='version', version='1.0.0')
    args = parser.parse_args()
    if args.save_path is None:
        args.save_path = args.path+".log.json"
    return args


def write_to_file(save_path, analyzer):
    # right TEAM
    right_team_data = {
        "Right Team": analyzer.game.right_team.name,
        "True Pass:": analyzer.pass_r,
        "Intercept:": analyzer.intercept_r,
        "on_target_shoot:": analyzer.on_target_shoot_r,
        "off_targ": analyzer.off_target_shoot_r,
        "Goals :": analyzer.game.right_goal,
        "Wrong Pass:": analyzer.intercept_l,
        "Pass in Lenght:": analyzer.pass_in_length_r,
        "Pass in Width:": analyzer.pass_in_width_r,
        "Pass Accuracy:": analyzer.pass_accuracy_r,
        "on_target_shoot:": analyzer.on_target_shoot_r,
        "off_targ": analyzer.off_target_shoot_r,
        "Shoot in Lenght": analyzer.shoot_in_length_r,
        "Shoot in Width": analyzer.shoot_in_width_r,
        "Shoot Accuracy": analyzer.shoot_accuracy_r,
        "Possession": analyzer.possession_r,
        "Stamina": analyzer.used_stamina_agents_r,
        "moved": analyzer.team_moved_distance_r,
        "Average Distance 10": analyzer.average_distance_10p_r,
        "Average Stamina 10": analyzer.average_stamina_10p_r,
        "Average Stamina Per distance 10": analyzer.av_st_per_dist_10p_r,
        "Stamina per ": analyzer.used_per_distance_r
    }
    # left TEAM
    left_team_data = {
        "Left Team": analyzer.game.left_team.name,
        "True Pass:": analyzer.pass_l,
        "Intercept:": analyzer.intercept_l,
        "on_target_shoot:": analyzer.on_target_shoot_l,
        "off_targ": analyzer.off_target_shoot_l,
        "Goals :": analyzer.game.left_goal,
        "Wrong Pass:": analyzer.intercept_r,
        "Pass in Lenght:": analyzer.pass_in_length_l,
        "Pass in Width:": analyzer.pass_in_width_l,
        "Pass Accuracy:": analyzer.pass_accuracy_l,
        "on_target_shoot:": analyzer.on_target_shoot_l,
        "off_targ": analyzer.off_target_shoot_l,
        "Shoot in Lenght": analyzer.shoot_in_length_l,
        "Shoot in Width": analyzer.shoot_in_width_l,
        "Shoot Accuracy": analyzer.shoot_accuracy_l,
        "Possession": analyzer.possession_l,
        "Stamina": analyzer.used_stamina_agents_l,
        "moved": analyzer.team_moved_distance_l,
        "Average Distance 10": analyzer.average_distance_10p_l,
        "Average Stamina 10": analyzer.average_stamina_10p_l,
        "Average Stamina Per distance 10": analyzer.av_st_per_dist_10p_l,
        "Stamina per ": analyzer.used_per_distance_r
    }

    ball_in_region_percentage = {}
    for region in analyzer.regions:
        ball_in_region_percentage[region.name] = region.ball_in_region_cycles

    # Agent_regions
    # owner_cycles    : cycles player is ball owner in the region
    # position_cycles : cycles player is in the region
    right_team_regions_data = {}
    for agent in analyzer.game.right_team.agents:
        agent_data = {}
        for region in agent.regions:
            agent_data[region.name] = {
                "ownerCycles": region.owner_cycles, "positionCycles": region.position_cycles}
        right_team_regions_data[agent.number] = agent_data
    left_team_regions_data = {}
    for agent in analyzer.game.left_team.agents:
        agent_data = {}
        for region in agent.regions:
            agent_data[region.name] = {
                "ownerCycles": region.owner_cycles, "positionCycles": region.position_cycles}
        left_team_regions_data[agent.number] = agent_data
    right_team_data['regionData'] = right_team_regions_data
    left_team_data['regionData'] = left_team_regions_data

    data = {
        "Game Result": {analyzer.game.left_team.name: analyzer.game.left_goal,
                        analyzer.game.right_team.name: analyzer.game.right_goal},
        "right_team": right_team_data,
        "left_team": left_team_data
    }

    with open(save_path, 'w') as outfile:
        json.dump(data, outfile)


def main():
    args = parse_args()
    path = args.path
    save_path = args.save_path
    parser = Parser(path)
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()
    write_to_file(save_path, analyzer)

    # Drawing Heatmap of the game

    if args.heat_map is not None:
        analyzer.draw_heatmap(right_team=True, left_team=True)
