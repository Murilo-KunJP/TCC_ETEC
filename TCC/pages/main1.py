import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

if not st.user.is_logged_in:
    st.switch_page("main.py")

st.write(f"Bem vindo(a), {st.user.name}!")

if st.button("Log out"):
    st.logout()
    st.switch_page("main.py")
