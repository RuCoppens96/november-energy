import pandas as pd


class EnergyConsumption:
    def __init__(self, history, default_consumption_pattern):
        self.history = history
        self.default_consumption_pattern = default_consumption_pattern
        self.consumption = pd.DataFrame(columns=['month', 'consumption'])
        self.consumpion_total = 0
        self.consumption_pattern = pd.DataFrame(columns=['month', 'pattern'])
