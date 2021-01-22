#!/usr/bin/env python3

import csv
import sys
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
import numpy as np

from agent import Critter



class Scape(Model):

    def __init__(self, N, aging=True, repop=True, _last_will=True):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.num_steps = 0
        self.aging = aging
        self.repop = repop
        self._last_will = _last_will

        # Create agents
        for i in range(self.num_agents):
            a = Critter(i, self)
            self.schedule.add(a)

    def step(self):
        self.num_steps += 1
        self.schedule.step()