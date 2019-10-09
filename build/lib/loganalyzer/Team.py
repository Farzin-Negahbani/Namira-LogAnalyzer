from loganalyzer.Agent import *


class Team:
    
    def __init__(self,name,side):
        self.name   = name
        self.side   = side
        self.agents = self.generate_agents()
        
        
        
    def get_result(self):
        result = {"all_kick":[],"all_tackle":[],"true_kick":[],"true_tackle":[]}   
        for agent in self.agents:
            result["all_kick"]+=agent.result["all_kick"]
            result["all_tackle"]+=agent.result["all_tackle"]
            result["true_kick"]+=agent.result["true_kick"]
            result["true_tackle"]+=agent.result["true_tackle"]
        return result

    def generate_agents(self):
        agents=[]
        for i in range (11):
            agents+=[Agent(i+1,self)]
        return agents
    
    def set_agents_data(self,cycle, game):
        for i in range(3,len(cycle)):
            if cycle[i][0][0]==self.side:
                self.agents[cycle[i][0][1]-1].parse_data(cycle[1],cycle[i],game)
        
    def get_agent_data(self,number):
        return self.agents[number-1].get_data()
