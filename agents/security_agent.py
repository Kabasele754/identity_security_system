import mesa
from utils.security_checks import perform_security_check


class SecurityAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.security_level = self.random.randint(1, 5)

    def step(self):
        self.check_nearby_agents()

    def check_nearby_agents(self):
        neighbors = self.model.grid.get_neighbors(
            self.pos,
            moore=True,  # or False, depending on your desired neighborhood type
            include_center=False
        )
        for neighbor in neighbors:
            if hasattr(neighbor, 'data'):
                perform_security_check(neighbor.data, self.security_level)

    @property
    def color(self):
        return "red"