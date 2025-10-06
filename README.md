# Agri Decision Assistant

Sistema inteligente de apoio à decisão para agricultura de precisão. Permite avaliar qualidade do solo, precipitação e tipo de cultura, gerando recomendações e visualizações interativas para otimizar manejo agrícola.

---

## Funcionalidades
- Slider de qualidade do solo
- Input de precipitação
- Seleção do tipo de cultura
- Recomendação automática de manejo
- Visualização de dados com gráficos interativos (Plotly)

---

## Tecnologias utilizadas
- Python
- Streamlit (interface web)
- Pandas e NumPy (manipulação de dados)
- Plotly (visualização interativa)
- Scikit-learn (para futuros modelos de ML)

---

## Estrutura do Projeto
agri-decision-assistant/
│
├── data/ # Dados fictícios CSV
├── src/ # Código fonte (main.py, data_loader.py, recommender.py, visualizer.py)
├── models/ # Modelos ML (.pkl)
├── images/ # Screenshots e protótipos
├── requirements.txt # Dependências
├── README.md # Este arquivo
├── LICENSE # MIT License
└── .gitignore # Ignorar arquivos desnecessários

## Como Rodar

1. Criar e ativar ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

## instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

##Rodar Aplicação
streamlit run src/main.py



