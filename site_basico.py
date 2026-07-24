import streamlit as st

st.title  ('Cadastro do cliente')

nome = st.text_input ('Digite o nome do cliente')
endereço = st.text_input ('Digite o endereço')
dt_nas = st.date_input('Escolha a data de Nascimento')
password = st.text_input("Digite sua senha forte", type="password")
tipo_cliente = st.selectbox('Tipo do cliente', 
                            ["Pessoa física", "Pessoa jurídica"])
cadastrar = st.button('Cadastrar cliente')

if cadastrar:
    with open ('Cliente.csv','a', encoding='utf8') as arquivo:
        arquivo.write(f'{nome},{endereço},{dt_nas},{tipo_cliente}')
        st.success('Cliente cadastrado com sucesso.')
    




