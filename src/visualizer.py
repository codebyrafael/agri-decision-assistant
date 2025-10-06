import plotly.express as px

def plot_soil_quality(soil_df):
    """
    Cria gráfico de qualidade do solo por área.
    """
    fig = px.bar(soil_df, x='field', y='quality', title='Qualidade do Solo por Área')
    return fig

def plot_rainfall(weather_df):
    """
    Cria gráfico de precipitação média por região.
    """
    fig = px.line(weather_df, x='region', y='rainfall', title='Precipitação Média')
    return fig
