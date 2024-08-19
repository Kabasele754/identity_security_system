
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from models.dentity_security_model import IdentitySecurityModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    portrayal["Color"] = agent.color
    return portrayal

grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

chart = ChartModule([{"Label": "Agents", "Color": "Black"}],
                    data_collector_name='datacenter')

model_params = {
    "N_identity": 50,
    "N_security": 10,
    "N_hospital": 5,
    "width": 20,
    "height": 20
}

server = ModularServer(IdentitySecurityModel,
                       [grid, chart],
                       "Identity Security Model",
                       model_params)