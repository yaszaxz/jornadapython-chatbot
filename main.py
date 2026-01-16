import streamlit as st
#Importar somente a integração da api da OpenAI
from openai import OpenAI

#Definir o modelo da IA
modeloIA = OpenAI(api_key='')

#Título da página
st.write('# IA sem crédito')

#Condicional para criar a lista de mensagem apenas uma vez
#Lista para salvar as mensagens
if not 'listaMensagens' in st.session_state:
    st.session_state['listaMensagens'] = []

#Campo de chat com placeholder
textoUsuario = st.chat_input('Digite a sua mensagem...')

#Loop para exibir as mensagens na tela
for mensagem in st.session_state['listaMensagens']:
    #Definir quem mandou a mensagem e qual é a mensagem
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)


#Condicional para não ficar exibindo 'none' na mensagem
if (textoUsuario):
    #Mensagens do usuário
    st.chat_message('user').write(textoUsuario)
    mensagemUsuario = {'role': 'user', 'content': textoUsuario}
    st.session_state['listaMensagens'].append(mensagemUsuario)

    #Mensagens da IA (deixar uma resposta fixa pq não tem crédito)
    resposta = 'Você disse: ' + textoUsuario
    st.session_state['listaMensagens'].append(resposta)
    st.chat_message('assistant').write(resposta)
    #resposta = modeloIA.chat.completions.create(messages=st.session_state['listaMensagens'], model='gpt-4o')    
    #textoResposta = resposta.choices[0].message.content
    #st.chat_message('assistant').write(textoResposta)
    #mensagemIa = {'role': 'assistant', 'content': textoResposta}
    #st.session_state['listaMensagens'].append(mensagemIa)