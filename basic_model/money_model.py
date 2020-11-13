from mesa import Agent, Model
from mesa.time import RandomActivation

class MoneyAgent(Agent):
    # an agent with X monetary units, and a unique id
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    # basic output for each agents' respective step
    def step(self):
        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        print("Agent " + str(self.unique_id) + " has " + str(self.wealth) + " wealth unit(s). Giving agent " + str(other_agent.unique_id) + " one.")
        self.wealth -=1

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

        

# class __main__:
# all_wealth = []
#     #This runs the model 100 times, each model executing 10 steps.
#     for j in range(100):
#         # Run the model
#         model = MoneyModel(10)
#         for i in range(10):
#             model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# plt.hist(all_wealth, bins=range(max(all_wealth)+1)