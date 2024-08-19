def sync_hospital_data(agent):
    # Simuler la synchronisation des données de l'hôpital avec d'autres systèmes
    for neighbor in agent.model.grid.get_neighbors(agent.pos, include_center=False):
        if hasattr(neighbor, 'update_hospital_data'):
            neighbor.update_hospital_data(agent.births, agent.deaths)

def sync_identity_data(agent):
    # Synchroniser les données d'identité entre les agents
    neighbors = agent.model.grid.get_neighbors(
        agent.pos,
        moore=True,  # or False, depending on your desired neighborhood type
        include_center=False
    )
    # Implement data synchronization logic
    for neighbor in neighbors:
        if isinstance(neighbor, type(agent)):
            # Sync data between agents of the same type
            agent.data.update(neighbor.data)