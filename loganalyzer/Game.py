from loganalyzer.Team import *


class Game:

    def __init__(self, parser):
        self.parser = parser
        self.right_goal = 0
        self.left_goal = 0
        self.server_param = {}
        self.right_team = Team(parser.right_team, 'r')
        self.left_team = Team(parser.left_team, 'l')
        self.agent_types = {}
        self.play_modes = {}
        self.ball_pos = {}
        self.play_on_cycles = []
        self.set_game_result()
        self.set_teams_data()

    def set_play_modes(self, cycle, playMode):
        self.play_modes[cycle] = playMode

    def set_ball_position(self, cycle, ball_data):
        self.ball_pos[cycle] = {
            'x': ball_data[1], 'y': ball_data[2], 'Vx': ball_data[3], 'Vy': ball_data[4]}

    def set_game_result(self):
        self.left_goal, self.right_goal = self.parser.data_rcg[-1][0][4:]


    def set_teams_data(self):
        current_play_mode = False
        for cycle in self.parser.data_rcg:
            if cycle[0][0] == 'show':
                if current_play_mode == 'play_on':
                    self.play_on_cycles += [cycle[0][1]]
                self.set_ball_position(cycle[0][1], cycle[0][2])
                self.left_team.set_agents_data(cycle[0], self)
                self.right_team.set_agents_data(cycle[0], self)

            elif cycle[0][0] == 'playmode':
                current_play_mode = cycle[0][2]
                self.set_play_modes(cycle[0][1], cycle[0][2])

            elif cycle[0][0] == 'server_param':
                for i in range(1, len(cycle[0])):
                    self.server_param[cycle[0][i][0]] = cycle[0][i][1]

            elif cycle[0][0] == 'player_type':
                data = {}
                for i in range(2, len(cycle[0])):
                    data[cycle[0][i][0]] = cycle[0][i][1]
                self.agent_types[cycle[0][1][1]] = data

    def get_agent_data(self, side, number):

        if side == 'l':
            return self.left_team.agents[number-1].get_data()
        else:
            return self.right_team.agents[number-1].get_data()

    def get_kickers(self, cycle):
        kickers = []
        for agent in self.left_team.agents+self.right_team.agents:
            if(agent.data[cycle]['is_tackled'] or agent.data[cycle]['is_kicked']):
                kickers.append(agent)
        return kickers

    def get_last_kickers(self, cycle):
        m = 0
        kickers = []
        for agent in (self.left_team.agents+self.right_team.agents):
            if cycle in agent.data:
                if(agent.data[cycle]['last_tackle_cycle'] > m or agent.data[cycle]['lastkickCycle'] > m):
                    if(agent.data[cycle]['last_tackle_cycle'] > agent.data[cycle]['lastkickCycle']):
                        m = agent.data[cycle]['last_tackle_cycle']
                    else:
                        m = agent.data[cycle]['lastkickCycle']
                    kickers.clear()
                    kickers.append(agent)
                elif(agent.data[cycle]['last_tackle_cycle'] == m or agent.data[cycle]['lastkickCycle'] == m):
                    kickers.append(agent)
        return kickers

    def get_play_on_cycles(self):
        return self.play_on_cycles
