from random import randint
from time import sleep

import sys

class CellularAutomata(object):
    def __init__(self, rule, n=20, steps=30):
        self.rule = rule
        self.n = n
        self.steps = steps
        self.ca = []
        for i in range(self.n):
            #self.ca.append(randint(0, 1))
            self.ca.append(0)
        self.ca[n//2] = 1

    def __str__(self):
        representation = ""
        for cell in self.ca:
            representation += str(cell)
        return representation

    def _neighborhood(self, ca, pos):
        left = ca[len(ca) - 1] if pos == 0 else ca[pos - 1]
        right = ca[0] if pos == len(ca) - 1 else ca[pos + 1]
        return [left, ca[pos], right]

    def _behavior(self, neighborhood):
        rule_binary = format(self.rule, "08b")
        rule_binary = rule_binary[::-1]
        bit = 4 * neighborhood[0] + 2 * neighborhood[1] + neighborhood[2]
        return int(rule_binary[bit])

    def iterate(self):
        copy = list(self.ca)
        for i in range(len(self.ca)):
            self.ca[i] = self._behavior(self._neighborhood(copy, i))

def main():
    ca = CellularAutomata(rule=110, n=100, steps=50)
    for i in range(ca.steps):
        print(ca)
        ca.iterate()
        sleep(.25)

if __name__ == "__main__":
    main()
