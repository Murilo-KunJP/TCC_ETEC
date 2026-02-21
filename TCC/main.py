import streamlit as st

#Login de Usuário
@st.dialog("Alerta!")
def login_validation(usr, passw):
    if usr == '' or passw == '':
        st.error('Porfavor, entre com seu usuário e senha.')
    else:
        st.success('Login feito com sucesso!')
with st.form('sign_in'):
    st.title('Sign In')
    st.caption('Entre com o nome de usuário e senha')
    st.divider()
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type = 'password')

    submit_btn = st.form_submit_button(label="Enviar", key=None, type="primary", use_container_width= True)
    google_btn = st.form_submit_button(label="Use sua Conta do Google", key=None, type="secondary", use_container_width= True, icon=':material/mail:')
   
    col1, col2, col3, col4 = st.columns(4)
    with col3:
        remember_box = st.checkbox('Salvar usuário')
    with col4:
        forgot_password = st.html('<p style= margin:7px><a href=''>Esqueci a Senha</a></p>')
    create_acc_btn = st.form_submit_button(label="Criar uma Conta", key=None, type="secondary", use_container_width= True)

if submit_btn:
    login_validation(username, password)
