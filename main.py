# Import delle librerie necessarie all'esecuzione del codice
import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# Definisco l'inizio dello studio e la fine
# La fine è definita come la data odierna
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Imposta il titolo nella pagina
st.title('Predizione del futuro andamento del mercato azionario')

# Definisco quali sono le scelte in merito alle azioni su cui effettuare la previsione dell'andamento
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# Definisco lo slider che permetta al'utente di scegliere l'intervallo di anni,
# a decorrere da oggi, da predire dall'algoritmo
n_years = st.slider('Anni di predizione:', 1, 4)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Mostra il caricamento dei dati grezzi	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Dati grezzi')
st.write(data.tail())

# Traccia il grafico dei dati grezzi elaborati in precedenza
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Effettua la predizione dell'andamento mediante Prophet
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Traccia il grafico dell'andamento predetto
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

# TODO Terminare l'aggiornamento della lingua in italiano
# Infatti, alcune di queste righe di codice sono parte di esempi
# provenienti dalle documentazioni di Prophet e Streamlit.