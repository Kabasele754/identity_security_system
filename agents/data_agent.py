import mesa
import datetime

class DataAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.data = {
            'id': unique_id,
            'last_updated': datetime.datetime.now(),
            'information': "Some sensitive information"
        }

    def step(self):
        # Simuler une mise à jour des données
        if self.random.random() < 0.1:  # 10% de chance de mise à jour
            self.data['last_updated'] = datetime.datetime.now()
            self.data['information'] = f"Updated information at {self.data['last_updated']}"