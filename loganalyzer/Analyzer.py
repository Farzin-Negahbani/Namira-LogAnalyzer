import math


class Region:

    def __init__(self, top_left, bottom_right, name="Unnamed"):

        self.top_left = top_left
        self.bottom_right = bottom_right
        self.name = name
        self.ball_in_region_cycles = 0

    def in_region(self, x, y):
        '''check if a point (x,y) l  ies in a rectangle
        with upper left corner (x1,y1) and bottom right corner (x2,y2)'''
        if (x > self.top_left[0] and x < self.bottom_right[0] and y > self.top_left[1] and y < self.bottom_right[1]):
            return True
        else:
            return False


class Analyzer:

    def __init__(self, game):

        self.game = game
        self.play_on_cycles = game.get_play_on_cycles()
        self.pass_status = 0  # 0 --> no kick,  1 --> one kicker detected
        self.shoot_status = 0
        self.pass_last_kicker = -1
        self.pass_last_kick_cycle = -1
        self.i = 0
        self.ball_owner = 0

        # Special Regions
        self.regions = []
        self.regions.append(Region((-52.5, -34), (-17.5, -11), "A"))
        self.regions.append(Region((-52.5, -11), (-17.5, 11), "B"))
        self.regions.append(Region((-52.5, 11), (-17.5, 34), "C"))
        self.regions.append(Region((-17.5, -34), (17.5, -11), "D"))
        self.regions.append(Region((-17.5, -11), (17.5, 11), "E"))
        self.regions.append(Region((-17.5, 11), (17.5, 34), "F"))
        self.regions.append(Region((17.5, -34), (52.5, -11), "G"))
        self.regions.append(Region((17.5, -11), (52.5, 11), "H"))
        self.regions.append(Region((17.5, 11), (52.5, 34), "I"))

        # Right TEAM
        self.status_r = 0  # Winner' 'Loser' 'Draw'
        self.pass_r = 0
        self.intercept_r = 0
        self.pass_in_length_r = 0
        self.pass_in_width_r = 0
        self.pass_accuracy_r = 0
        self.shoot_in_length_r = 0
        self.shoot_in_width_r = 0
        self.on_target_shoot_r = 0
        self.off_target_shoot_r = 0
        self.shoot_accuracy_r = 0
        self.possession_r = 0
        self.used_stamina_agents_r = []
        self.team_moved_distance_r = []
        self.used_per_distance_r = []
        self.average_stamina_10p_r = 0
        self.average_distance_10p_r = 0
        self.av_st_per_dist_10p_r = 0

        # Left TEAM
        self.status_l = 0  # Winner' 'Loser' 'Draw'
        self.pass_l = 0
        self.intercept_l = 0
        self.pass_in_length_l = 0
        self.pass_in_width_l = 0
        self.pass_accuracy_l = 0
        self.shoot_in_length_l = 0
        self.shoot_in_width_l = 0
        self.on_target_shoot_l = 0
        self.off_target_shoot_l = 0
        self.shoot_accuracy_l = 0
        self.possession_l = 0
        self.used_stamina_agents_l = []
        self.team_moved_distance_l = []
        self.used_per_distance_l = []
        self.average_stamina_10p_l = 0
        self.average_distance_10p_l = 0
        self.av_st_per_dist_10p_l = 0

    def draw_heatmap(self, right_team=False, left_team=True):
        import numpy as np
        import matplotlib.pyplot as plt

        world = np.zeros((110, 75))

        if(right_team ):
            team =self.game.right_team.agents
        elif(left_team):
            team =self.game.left_team.agents
        # for cycle in self.play_on_cycles:
        for cycle in self.play_on_cycles:
            for agent in team:
                if(agent.number != 1):
                    x = int(round(agent.data[cycle]['x'], 1))+52
                    y = int(round(agent.data[cycle]['y'], 1))+33
                    for i in range(-4,5):
                        for j in range(-4,5):
                            try:
                                world[x+i][y+j] += 5 - abs(j) 
                            except:
                                continue
        fig, ax = plt.subplots()
        ax.set_xticks(np.arange(len([])))
        ax.set_yticks(np.arange(len([])))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        cbarlabel="Relative Frequency"

        im = ax.imshow(np.fliplr(world).T, interpolation='gaussian')
        cbar = ax.figure.colorbar(im, ax=ax )
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
        plt.show()


    def line_intersection(self,line1, line2):
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]
        
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here
        div = det(xdiff, ydiff)
        if div == 0:
           raise Exception('lines do not intersect!')
        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
    
    def update_distance(self, key):
        
        def distance(p1,p2):
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        
        if(key in self.play_on_cycles and (key-1) in self.play_on_cycles):
            for agent in (self.game.right_team.agents + self.game.left_team.agents):
                p1 = (agent.data[key-1]['x'],agent.data[key-1]['y'])
                p2 = (agent.data[key]['x'],agent.data[key]['y'])
                if( distance(p1,p2) < 1.6):
                    agent.moved_distance = agent.moved_distance +distance(p1,p2)
        
                
    def update_parameters(self):
        
        if(self.game.left_goal == self.game.right_goal ):
            self.status_l = "Draw"
            self.status_r = "Draw"
        elif(self.game.left_goal > self.game.right_goal ):
            self.status_l = "Winner"
            self.status_r = "Loser"
        else:
            self.status_r = "Winner"
            self.status_l = "Loser"
        
        for agent in self.game.right_team.agents:
            
            agent.used_stamina = self.game.server_param['stamina_max']+self.game.server_param['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina']
            self.used_stamina_agents_r.append((round(agent.used_stamina,2),agent.number))       
            
            self.team_moved_distance_r.append((round(agent.moved_distance,2),agent.number))
            if(agent.moved_distance !=0):
                self.used_per_distance_r.append((round(agent.used_stamina/agent.moved_distance,1),agent.number))
            
            
        for agent in self.game.left_team.agents:
            
            agent.used_stamina = self.game.server_param['stamina_max']+self.game.server_param['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina']
            self.used_stamina_agents_l.append((round(agent.used_stamina,2),agent.number))       
    
            self.team_moved_distance_l.append((round(agent.moved_distance,2),agent.number))
            if(agent.moved_distance !=0):
                self.used_per_distance_l.append((round(agent.used_stamina/agent.moved_distance,1),agent.number))

        if(self.pass_r+self.intercept_l != 0):
            self.pass_accuracy_r  = round(self.pass_r * 100/(self.pass_r+self.intercept_l),1)
        else:
            self.pass_accuracy_r  = 0
            
        if(self.pass_l+self.intercept_r != 0):
            self.pass_accuracy_l  = round(self.pass_l * 100/(self.pass_l+self.intercept_r),1)
        else:
            self.pass_accuracy_l  = 0
            
        if(self.on_target_shoot_l+self.off_target_shoot_l != 0):
            self.shoot_accuracy_l = round(self.on_target_shoot_l *100/(self.on_target_shoot_l+self.off_target_shoot_l),1)
        else:
            self.shoot_accuracy_l  = 0
            
        if(self.on_target_shoot_r+self.off_target_shoot_r != 0):
            self.shoot_accuracy_r = round(self.on_target_shoot_r *100/(self.on_target_shoot_r+self.off_target_shoot_r),1)
        else:
            self.shoot_accuracy_r  = 0
            
        total                 = self.possession_r+self.possession_l
        if(total!=0):
            self.possession_r     = round(self.possession_r * 100 /(total) ,1)
            self.possession_l     = round(self.possession_l * 100 /(total) ,1)
        else:
            self.possession_r     = 0
            self.possession_l     = 0
        
        s = sum([d.ball_in_region_cycles for d in self.regions])
        for region in self.regions:
            region.ball_in_region_cycles = round(region.ball_in_region_cycles*100/s,1)

        self.average_distance_10p_r = round(sum([d[0] for d in self.team_moved_distance_r if d[1]!=1])/10,1)
        self.average_distance_10p_l = round(sum([d[0] for d in self.team_moved_distance_l if d[1]!=1])/10,1)
        self.average_stamina_10p_r = round(sum([d[0] for d in self.used_stamina_agents_r if d[1]!=1])/10,1)
        self.average_stamina_10p_l = round(sum([d[0] for d in self.used_stamina_agents_l if d[1]!=1])/10,1)

        if(self.average_distance_10p_r !=0):
            self.av_st_per_dist_10p_r  = round(self.average_stamina_10p_r/self.average_distance_10p_r,1)
        
        if(self.average_distance_10p_l !=0):
            self.av_st_per_dist_10p_l  = round(self.average_stamina_10p_l/self.average_distance_10p_l,1)

    def update_possession(self, key):
        
        if(key in self.play_on_cycles and len(self.game.get_last_kickers(key))>0):
           
            for region in self.regions:
                if(region.in_region(self.game.ball_pos[key]['x'],self.game.ball_pos[key]['y'])):
                    region.ball_in_region_cycles +=1
                    break
                    
            for agent in (self.game.right_team.agents +self.game.left_team.agents ):
                for region in agent.regions:
                    if(region.in_region(agent.data[key]['x'],agent.data[key]['y'])):
                        region.position_cycles +=1
                        if(self.game.get_last_kickers(key)[0] == agent):
                            region.owner_cycles +=1
                        break
                    
                
            if(self.game.get_last_kickers(key)[0].team.name == self.game.left_team.name ):
                self.possession_l +=1
                # print("Left Team is ball Owner cycle ",key)
            else:
                # print("Right Team is ball Owner cycle ",key)
                self.possession_r +=1

        
    def check_shoot(self, key):

        if key in self.game.ball_pos:
            if(key not in self.play_on_cycles):
                self.shoot_status = 0
                
            elif( self.shoot_status == 0 and (self.game.ball_pos[key]['Vx']**2 + self.game.ball_pos[key]['Vy']**2)** 0.5  > 2.0 ):
                kickers = self.game.get_kickers(key)
                if(len(kickers)>0 and kickers[0].team.name == self.game.right_team.name and math.hypot(kickers[0].data[key]['x']+51.6,kickers[0].data[key]['y'] )< 20 and self.game.ball_pos[key]['Vx']   ):
                    ball1 = (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2 = (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    if ball1[0]-ball2[0]>0:
                        (x,y) = self.line_intersection((ball1,ball2) , ((-52.6,1),(-52.6,0)) )
                            
                        if(abs(y)<7.5 ):
                            if(abs(y-ball1[1])> abs(x-ball1[0])):
                                self.shoot_in_width_r +=1
                            else:
                                self.shoot_in_length_r +=1
                            # print( "On-Target Shoot", key , kickers[0].number , self.game.right_team.name)
                            self.on_target_shoot_r +=1
                            self.shoot_status       =1

                        elif(abs(y)<16 and abs(y)>9):
                            if(abs(y-ball1[1])> abs(x-ball1[0])):
                                self.shoot_in_width_r +=1
                            else:
                                self.shoot_in_length_r +=1
                            # print( "Off-Target Shoot", key ,kickers[0].number , self.game.right_team.name)
                            self.off_target_shoot_r +=1
                            self.shoot_status       =1
                                                        
                            
                elif(len(kickers)>0 and kickers[0].team.name == self.game.left_team.name and  math.hypot(kickers[0].data[key]['x']-51.6,kickers[0].data[key]['y'] ) < 20 and self.game.ball_pos[key]['Vx']):
                    ball1= (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2= (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    if ball2[0]-ball1[0]>0:
                        (x,y) = self.line_intersection( (ball1,ball2), ((52.6,1),(52.6,0)) )
    
                        if(abs(y)<7.5 ):
                            if(abs(y-ball1[1])> abs(x-ball1[0])):
                                self.shoot_in_width_l +=1
                            else:
                                self.shoot_in_length_l +=1  
                            # print( "On-Target Shoot",key, kickers[0].number , self.game.left_team.name)
                            self.on_target_shoot_l +=1
                            self.shoot_status       =1
                            
                        elif(abs(y)<16 and abs(y)>9):
                            if(abs(y-ball1[1])> abs(x-ball1[0])):
                                self.shoot_in_width_l +=1
                            else:
                                self.shoot_in_length_l +=1  
                            # print( "Off-Target Shooet",key, kickers[0].number , self.game.left_team.name)
                            self.off_target_shoot_l+=1
                            self.shoot_status       =1


    def check_pass(self, key):
        if len(self.game.get_last_kickers(key))>0:
            if(key not in self.play_on_cycles):
                self.pass_status = 0

            elif(self.pass_status == 0):
                self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                self.pass_last_kick_cycle = key
                self.pass_status      = 1

            elif(self.pass_status == 1 ):

                if(self.pass_last_kicker == self.game.get_last_kickers(key)[0] and self.game.get_last_kickers(key)[0].data[key]['is_kicked']):
                    self.pass_status = 1
                    self.pass_last_kick_cycle = key

                elif(self.pass_last_kicker != self.game.get_last_kickers(key)[0]  and  self.pass_last_kicker.team == self.game.get_last_kickers(key)[0].team  ):
                    self.i = self.i+1
                    ball1 = (self.game.ball_pos[self.pass_last_kick_cycle]['x'], self.game.ball_pos[self.pass_last_kick_cycle]['y'])
                    ball2 = (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    if(self.pass_last_kicker.team.name == self.game.right_team.name):
                        self.pass_r += 1
                        if(abs(ball1[0]-ball2[0])>abs(ball1[1]-ball2[1])):
                            self.pass_in_width_r +=1
                        else:
                            self.pass_in_length_r +=1
                    else:
                        self.pass_l += 1    
                        if(abs(ball1[0]-ball2[0])>abs(ball1[1]-ball2[1])):
                            self.pass_in_width_l +=1
                        else:
                            self.pass_in_length_l +=1
                   
                        
                    self.pass_status = 1
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key

                elif(self.pass_last_kicker.team != self.game.get_last_kickers(key)[0].team):
                    if(self.game.get_last_kickers(key)[0].team.name == self.game.right_team.name):
                        self.intercept_r += 1
                    else:
                        self.intercept_l += 1
                    ball1 = (self.game.ball_pos[self.pass_last_kick_cycle]['x'], self.game.ball_pos[self.pass_last_kick_cycle]['y'])
                    ball2 = (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                        
                        
                    self.pass_status = 1
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key


    def analyze(self):
        ''' pass, shoot, pass intercept, shot intercept, possesion ,  '''
        
        for key in range(1,self.play_on_cycles[-1]+1):
            self.check_pass(key)
            self.check_shoot(key)
            self.update_possession(key)
            self.update_distance(key)
        self.update_parameters()