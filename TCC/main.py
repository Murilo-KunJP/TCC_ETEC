import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

@st.dialog("Alerta!")
def login_validation(usr, passw):
    if usr == '' or passw == '':
        st.error('Por favor, entre com seu usuário e senha.')
    else:
        st.success('Login feito com sucesso!')

if st.user.is_logged_in:
    st.switch_page("pages/main1.py")

with st.form('sign_in'):
    st.title('Sign In')
    st.caption('Entre com o nome de usuário e senha')
    st.divider()
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type='password')
    submit_btn = st.form_submit_button(label="Enviar", type="primary", use_container_width=True)

    if not st.user.is_logged_in:
        google_btn = st.form_submit_button(label="Use sua Conta do Google", use_container_width=True, icon=':material/mail:')

    col1, col2, col3, col4 = st.columns(4)
    with col3:
        remember_box = st.checkbox('Salvar usuário')
    with col4:
        st.html('<p style="margin-top:8px"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Esqueci a senha</a></p>')
    st.divider()
    create_acc_btn = st.form_submit_button(label="Criar uma Conta", use_container_width=True)

if submit_btn:
    login_validation(username, password)

if 'google_btn' in dir() and google_btn:
    st.login()
