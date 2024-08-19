import mesa
from agents.identity_agent import IdentityAgent
from agents.security_agent import SecurityAgent
from agents.hospital_agent import HospitalAgent


class IdentitySecurityModel(mesa.Model):
    def __init__(self, N_identity, N_security, N_hospital, width, height):
        super().__init__()
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.current_id = 0  # Initialize current_id

        # Create agents
        self.create_agents(IdentityAgent, N_identity)
        self.create_agents(SecurityAgent, N_security)
        self.create_agents(HospitalAgent, N_hospital)

        self.datacenter = mesa.DataCollector(
            model_reporters={"Agents": lambda m: m.schedule.get_agent_count()},
            agent_reporters={
                "Data": lambda a: len(a.data) if hasattr(a, 'data') else 0,
                "Births": lambda a: a.births if isinstance(a, HospitalAgent) else 0,
                "Deaths": lambda a: a.deaths if isinstance(a, HospitalAgent) else 0
            }
        )

    def create_agents(self, AgentType, N):
        for i in range(N):
            a = AgentType(self.next_id(), self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            self.schedule.add(a)

    def step(self):
        self.datacenter.collect(self)
        self.schedule.step()

    def next_id(self):
        self.current_id += 1
        return self.current_id

    def get_grid(self):
        grid = [[[] for _ in range(self.grid.width)] for _ in range(self.grid.height)]
        for cell in self.grid.coord_iter():
            cell_content, x, y = cell
            for agent in cell_content:
                grid[y][x].append(agent)
        return grid