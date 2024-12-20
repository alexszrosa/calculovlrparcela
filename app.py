import streamlit as st

st.title("Cálculo do Valor do tratamento")

st.divider()

Vlr_Servico = st.number_input("Digite o valor do serviço: ")

st.divider()

Taxa = st.number_input("Digite a Taxa: ")

st.divider()

Prazo = st.number_input("Digite o prazo: ")

st.divider()

if Prazo > 1:
    Vlr_parcela = (Vlr_Servico+(Vlr_Servico*Taxa/100))/Prazo
    Vlr = st.write(f"O valor de cada parcela R${Vlr_parcela:.2f} ")
    st.balloons()
else:
    "Digite o prazo maior que zero"
st.divider()