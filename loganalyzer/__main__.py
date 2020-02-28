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
    parser.add_argument("--path", help="Input file path", metavar='<log file without .rcl or .rcg >',
                        required=True, dest='path')
    parser.add_argument(
        "--save_path", help="Output saving path.", metavar='<save_path>', dest='save_path')
    parser.add_argument("--heatmap", help="Show Heatmap of Selected Side", metavar='TEAM_SIDE',
                        dest='heat_map')
    parser.add_argument('--version', action='version', version='1.0.1')
    args = parser.parse_args()
    if args.save_path is None:
        args.save_path = args.path+".log.json"
    return args


def write_to_file(save_path, analyzer):
    # right TEAM
    right_team_data = {
        "rightTeam": analyzer.game.right_team.name,
        "truePass": analyzer.pass_r,
        "intercept": analyzer.intercept_r,
        "onTargetShoot": analyzer.on_target_shoot_r,
        "offTarget": analyzer.off_target_shoot_r,
        "goals": analyzer.game.right_goal,
        "wrongPass": analyzer.intercept_l,
        "passInLength": analyzer.pass_in_length_r,
        "passInWidth": analyzer.pass_in_width_r,
        "passAccuracy": analyzer.pass_accuracy_r,
        "onTargetShoot": analyzer.on_target_shoot_r,
        "shootInLength": analyzer.shoot_in_length_r,
        "shootInWidth": analyzer.shoot_in_width_r,
        "shootAccuracy": analyzer.shoot_accuracy_r,
        "possession": analyzer.possession_r,
        "stamina": analyzer.used_stamina_agents_r,
        "moved": analyzer.team_moved_distance_r,
        "averageDistance10": analyzer.average_distance_10p_r,
        "averageStamina10": analyzer.average_stamina_10p_r,
        "averageStaminaPerDistance10": analyzer.av_st_per_dist_10p_r,
        "staminaPerDistance": analyzer.used_per_distance_r
    }
    # left TEAM
    left_team_data = {
        "leftTeam": analyzer.game.left_team.name,
        "truePass": analyzer.pass_l,
        "Intercept": analyzer.intercept_l,
        "onTargetShoot": analyzer.on_target_shoot_l,
        "offTarget": analyzer.off_target_shoot_l,
        "goals": analyzer.game.left_goal,
        "wrongPass": analyzer.intercept_r,
        "passinLength": analyzer.pass_in_length_l,
        "passInWidth": analyzer.pass_in_width_l,
        "passAccuracy": analyzer.pass_accuracy_l,
        "onTargetShoot": analyzer.on_target_shoot_l,
        "shootInLength": analyzer.shoot_in_length_l,
        "shootInWidth": analyzer.shoot_in_width_l,
        "shootAccuracy": analyzer.shoot_accuracy_l,
        "possession": analyzer.possession_l,
        "stamina": analyzer.used_stamina_agents_l,
        "moved": analyzer.team_moved_distance_l,
        "averageDistance10": analyzer.average_distance_10p_l,
        "averageStamina10": analyzer.average_stamina_10p_l,
        "averageStaminaPerDistance10": analyzer.av_st_per_dist_10p_l,
        "staminaPerDistance": analyzer.used_per_distance_r
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
        "gameResult": {analyzer.game.left_team.name: analyzer.game.left_goal,
                       analyzer.game.right_team.name: analyzer.game.right_goal},
        "rightTeam": right_team_data,
        "leftTeam": left_team_data
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
