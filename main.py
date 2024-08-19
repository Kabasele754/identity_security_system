from models.dentity_security_model import IdentitySecurityModel
import matplotlib.pyplot as plt




def run_simulation():
    model = IdentitySecurityModel(
        N_identity=50,
        N_security=10,
        N_hospital=5,
        width=20,
        height=20
    )

    for i in range(100):
        model.step()

    agent_counts = model.datacenter.get_model_vars_dataframe()
    agent_counts.plot()
    plt.show()


if __name__ == "__main__":
    run_simulation()
