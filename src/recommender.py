def recommend_actions(soil_quality, rainfall, crop_type):
    """
    Gera recomendações agrícolas com base na qualidade do solo,
    precipitação e tipo de cultura.
    """
    if soil_quality < 0.5:
        return "Aplicar correção de solo e reavaliar fertilidade."
    elif rainfall < 50:
        return "Planejar irrigação suplementar."
    elif crop_type.lower() == "milho":
        return "Aplicar nitrogênio em 2 etapas durante o crescimento."
    else:
        return "Condições ideais, seguir manejo atual."
