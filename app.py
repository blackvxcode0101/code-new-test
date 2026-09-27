import streamlit as st

st.title("Meu primeiro site")

nome = st.text_input("Qual seu nome?")
idade = st.number_input("Agora digite sua idade", min_value=0, max_value=120, step=1)
altura = st.text_input("Informe sua altura")
cor_de_pele = st.text_input("Informe sua cor de pele")

if st.button("Enviar"):
    st.write(f"Olá, {nome}!")
    st.write(f"Você tem {idade} anos")
    st.write(f"No próximo ano você terá {idade + 1} anos")
    st.write(f"Sua altura é {altura}")
    st.write(f"Sua cor de pele é {cor_de_pele}")
    
    st.success(f"Seu nome é {nome}, sua idade é {idade}, sua altura é {altura}, e sua cor de pele é {cor_de_pele}.")
    
