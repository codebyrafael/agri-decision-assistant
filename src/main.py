import streamlit as st
from src.data_loader import load_data
from src.recommender import recommend_actions
from src.visualizer import plot_soil_quality, plot_rainfall

st.set_page_config(page_title="Agri Decision Assistant", layout="wide")

st.title("Agri Decision Assistant")
st.markdown("Sistema inteligente de apoio à decisão para agricultura de precisão.")

# Carregar dados
soil_df, weather_df, crops_df = load_data()

# Inputs do usuário
soil_quality = st.slider("Qualidade do Solo", 0.0, 1.0, 0.7)
rainfall = st.number_input("Chuva Média (mm)", 0, 500, 120)
crop_type = st.selectbox("Tipo de Cultura", ["Milho", "Soja", "Trigo"])

# Gerar recomendação
if st.button("Gerar Recomendação"):
    result = recommend_actions(soil_quality, rainfall, crop_type)
    st.success(result)

# Visualizações
st.header("Visualização de Dados")
st.subheader("Qualidade do Solo")
st.plotly_chart(plot_soil_quality(soil_df))

st.subheader("Precipitação")
st.plotly_chart(plot_rainfall(weather_df))
