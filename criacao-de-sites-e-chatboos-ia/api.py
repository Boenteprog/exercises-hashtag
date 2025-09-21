# titulo 
# input do chat
# a cada mensagem enviada: 
 # mostra a mensagem que o usuário enviou no chat 
 # enviar essa mensagem para IA responder 
 # aparece na tela a resposta da IA 

import streamlit as st
from openai import OpenAI

#modelo = OpenAI(api_key="")

#Titulo 
st.write("# Mano Texaco - IA Helper") 

#session_state = memoria do streamlit 
if not "list_msg" in st.session_state:
    st.session_state["list_msg"] = []  

session_state = {"list_msg": []}


for gl_call in st.session_state["list_msg"]:
    user = gl_call["role"]
    content = gl_call["content"]
    st.chat_message(user).write(content)


#Caixa de Texto - Mensagem do Usuario 
mensagem_txt = st.chat_input()

# Apenas emite mensagem se algo for enviado (evitar aparecer none)
if mensagem_txt: 

    #Criando caixa de usuario  
    st.chat_message("user").write(mensagem_txt)
    gl_call = {"role": "user", "content": mensagem_txt}
    st.session_state["list_msg"].append(gl_call)
    
    #
    #resposta_ia = modelo.chat.completions.create(
    #    messages=st.session_state["list_msg"],
    #    model="gpt-3.5-turbo"
    #)

    send = "Voce quis dizer " + mensagem_txt + "?"

    #Criando caixa de IA 
    st.chat_message("assistent").write(send)
    ia_call = {"role": "assistent", "content": send}
    st.session_state["list_msg"].append(ia_call)



    