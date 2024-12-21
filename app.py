import streamlit as st

st.title("Cálculo do Valor do Tratamento")

st.divider()

Vlr_Servico = st.number_input("Digite o valor do serviço: ")

st.divider()

Taxa = st.number_input("Digite a Taxa: ")

st.divider()

Prazo = st.number_input("Digite o prazo: ")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("Juros Simples")
    if Prazo > 1:
        Vlr_parcela = (Vlr_Servico+(Vlr_Servico*Taxa/100))/Prazo
        Vlrs = st.write(f"O valor de cada parcela R${Vlr_parcela:.2f} ")
        st.balloons()
    else:
        "Digite o prazo maior que zero"

with col2:
    st.header("Juros Compostos")
    if Prazo > 1:
        Taxac = (1+Taxa/100) ** Prazo
        Vlr_parcelac = (Vlr_Servico*Taxac)/(int(Taxa)/100+Prazo)
        Vlrc = st.write(f"O valor de cada parcela R${Vlr_parcelac:.2f} ")
        st.balloons()
    else:
        "Digite o prazo maior que zero"     

st.divider()