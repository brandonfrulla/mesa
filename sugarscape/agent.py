#!/usr/bin/env python3

from mesa import Agent
import numpy as np

class Critter(Agent):
    "An agent with random initial sugar, metabolism, age, and vision."

    init_max = 0

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        Critter.max_id = max(Critter.init_max, unique_id)
        self.vision = np.random.choice(range(1,6))
        self.metabolism = np.random.choice(range(1,4))
        self.max_age = np.random.choice(range(15,35))
        self.sugar = np.random.choice(range(35,65)) 
        self.age = 0

    def step(self):
        self.sugar -= self.metabolism

        if self.sugar <= 0:
            self._die_starvation()

        # only exe if aging is 'on', otherwise skip
        if self.model.aging == True:
            self.age += 1

            if self.age >= self.max_age:
                self._die_age()   

    def _die_starvation(self):
        print("Agent " + str(self.unique_id) +" died from hunger.")
        self.model.schedule.remove(self)

        if self.model.repop:
            self.repopulate()
        
    def _die_age(self):
        print("Agent " + str(self.unique_id) +" died from old age.")
        self.model.schedule.remove(self)
        
        if self.model.repop:
            self.repopulate()

    def repopulate(self):
        replacement = Critter(Critter.max_id + 1, self.model)

        # if _last_will is self.model._last_will=True, 'spawn' would get leftover sugar. Think real-world estates
        if self.model._last_will and self.sugar >= 1:
            replacement.sugar += self.sugar

        self.model.schedule.add(replacement)