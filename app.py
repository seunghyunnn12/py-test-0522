import streamlit as st

st.title("Streamlit 자동 배포 테스트")

name = st.text_input("이름을 입력하세요")
if st.button("확인"):
    st.success(f"{name}님 반가워요! 🎉")
