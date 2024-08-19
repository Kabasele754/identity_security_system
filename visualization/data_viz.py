import matplotlib.pyplot as plt

def plot_population_data(model):
    agent_counts = model.datacenter.get_model_vars_dataframe()
    plt.figure(figsize=(10, 5))
    plt.plot(agent_counts.index, agent_counts["Agents"])
    plt.title("Nombre total d'agents au fil du temps")
    plt.xlabel("Étapes")
    plt.ylabel("Nombre d'agents")
    plt.show()

def plot_hospital_data(model):
    hospital_data = model.datacenter.get_agent_vars_dataframe()
    births = hospital_data[hospital_data["Births"] > 0]["Births"]
    deaths = hospital_data[hospital_data["Deaths"] > 0]["Deaths"]

    plt.figure(figsize=(10, 5))
    plt.plot(births.index.get_level_values('Step'), births, label='Naissances')
    plt.plot(deaths.index.get_level_values('Step'), deaths, label='Décès')
    plt.title("Naissances et décès enregistrés par les hôpitaux")
    plt.xlabel("Étapes")
    plt.ylabel("Nombre d'événements")
    plt.legend()
    plt.show()