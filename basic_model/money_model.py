from mesa import Agent, Model
from mesa.time import RandomActivation

class MoneyAgent(Agent):
    # an agent with X monetary units, and a unique id
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    # basic output for each agents' respective step
    def step(self):
        print("Hi, I am agent " + str(self.unique_id) + ", and I currently have " 
        + str(self.wealth) + " wealth unit(s).")

class MoneyModel(Model):
    # a model with N number of agents
    def __init__(self, num):
        self.num_agents = num
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()