import streamlit as st
from streamlit import streamlit 

st.title  ('Cadastro do cliente')

nome = st.text_input ('Digite o nome do cliente')
endereço = st.text_input ('Digite o endereço')
dt_nas = st.date_input('Escolha a data de Nascimento')
password = st.text_input("Digite sua senha forte", type="password")
senha = st.text_input("Digite sua senha: ")

tipo_cliente = st.selectbox('Tipo do cliente', 
                            ["Pessoa física", "Pessoa jurídica"])
cadastrar = st.button('Cadastrar cliente')

if cadastrar:
    with open ('Cliente.csv','a', encoding='utf8') as arquivo:
        arquivo.write(f'{nome},{endereço},{dt_nas},{senha},{tipo_cliente}')
        st.success('Cadastro do viadin concedido.')
    
if len(senha) < 4:
    print("Precisa de uma senha forte")


# lembrando que precisa estar no arquivo
# para rodar: streamlit run pagina.py