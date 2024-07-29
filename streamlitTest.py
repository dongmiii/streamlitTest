import streamlit as st

st.title('streamlitTEST')
st.header('header')
st.subheader('subheader')
st.code('a=1')
st.markdown('이것은 **마크다운**입니다')

code = '''

def hello():
    print('hello')

'''
st.code(code)