import streamlit as st

name = st.text_input("Họ và tên:" "Nhập tên của bạn vào đây")
birth = st.text_input("Ngày tháng năm sinh: " ,"Ngày / tháng / năm")
fav_subject = st.text_input("Môn học yêu thích: " )
hobby = st.text_input("Sở thích: ")

st.title("Giới thiệu bản thân")

st.write(f"Họ và tên:{name}")
st.write(f"Ngày tháng năm sinh:{birth}")
st.write(f"Môn học yêu thích:{fav_subject}")
st.write(f"Sở thích:{hobby}")