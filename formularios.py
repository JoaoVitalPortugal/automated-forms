#--------------IMPORTS----------------
import requests as r
import streamlit as st

WEBHOOK_URL = ""
#---------------IMPORTS---------------

#---------------FAZENDO SITE--------------------------------------
st.title("seja bem vindo aos feedbacks da Tux company!")

nome = st.text_input("Qual o seu nome completo?")
idade = st.number_input("Quaç a sua idade?")
tem_experiencia = st.selectbox("Tem experiencia?", ["Sim", "Não"])
tempo = "n/a"
email = st.text_input("Qual o seu email? ")

if tem_experiencia == "Sim":
    tempo = st.text_input("Quanto tempo?")
else:
    st.text("ok!")
#---------------FAZENDO SITE--------------------------------------
#------------------------CRIANDO ARQUIVO--------------------------
filename = f"form{nome.replace(" ", "_")}.txt"
send = st.button("Enviar")
if send:
    if not "@" in email or not "." in email:
        st.warning("Email invalido!")
        st.stop()
    st.success("Formulario enviado com sucesso!")
    with open(filename, "w") as f: 
        f.write(f"""
nome: {nome}
idade: {idade}
tem experiencia: {tem_experiencia}
tempo: {tempo}
email: {email}
""")

    with open(filename, "rb") as f:
        r.post(
            WEBHOOK_URL,
            data={"content": "📩 Novo formulário recebido"},
            files={"file": f}
    )
elif Exception:
    print(Exception)
#------------------------CRIANDO ARQUIVO--------------------------


