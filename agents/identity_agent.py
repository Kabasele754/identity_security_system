import mesa
from utils.data_sync import sync_identity_data


class IdentityAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.data = {"id": unique_id, "name": f"Person_{unique_id}"}

    def step(self):
        self.update_data()
        sync_identity_data(self)

    def update_data(self):
        # Simuler la mise à jour des données d'identité
        self.data["last_updated"] = self.model.schedule.steps



    @property
    def color(self):
        return "blue"