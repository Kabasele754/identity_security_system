import mesa
from utils.data_sync import sync_hospital_data


class HospitalAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.births = 0
        self.deaths = 0

    def step(self):
        # Implement hospital behavior
        # For example, randomly generate births and deaths
        if self.random.random() < 0.1:  # 10% chance of a birth
            self.births += 1
        if self.random.random() < 0.05:  # 5% chance of a death
            self.deaths += 1

    def register_events(self):
        # Simuler l'enregistrement des naissances et des décès
        self.births += self.random.randint(0, 5)
        self.deaths += self.random.randint(0, 3)

    @property
    def color(self):
        return "green"
