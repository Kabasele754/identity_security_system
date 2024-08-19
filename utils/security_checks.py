def calculate_risk_score(data, security_level):
    # Calcul plus détaillé du score de risque
    base_score = len(data) * security_level
    if 'last_updated' in data:
        # Augmenter le score si les données n'ont pas été mises à jour récemment
        time_since_update = data['last_updated']
        base_score += time_since_update * 2
    return base_score

def log_security_alert(agent_id, risk_score):
    # Simuler l'enregistrement des alertes de sécurité dans un fichier de log
    with open('security_alerts.log', 'a') as log_file:
        log_file.write(f"Alerte de sécurité: Agent ID {agent_id}, Score de risque {risk_score}\n")


def perform_security_check(data, security_level):
    # Simuler une vérification de sécurité plus complexe
    risk_score = calculate_risk_score(data, security_level)
    if risk_score  > 50:
        print(f"Alerte de sécurité pour l'ID {data.get('id', 'Unknown')} - Score de risque: {risk_score}")
        log_security_alert(data.get('id', 'Unknown'), risk_score)
    return risk_score