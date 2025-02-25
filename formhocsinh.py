import streamlit as st

st.set_page_config(page_title="Form nhập học sinh", layout="wide")
# nếu phiên hoạt động không có phiên student

if 'student' not in st.session_state:
    st.session_state.student = [] # phiên hoạt động

with st.form(key="str", clear_on_submit=True):
    st.title("Đây là form tạo học sinh: ")
    name = st.text_input("Nhập tên học sinh: ")
    birthday = st.text_input("Nhập ngày sinh: ")
    submited = st.form_submit_button("Gửi lên")
    if submited:
        if name and birthday:
            st.session_state.student.append(
                {
                    "name": name,
                    "birthday": birthday
                }
            )
            st.success("Nhập thông tin thành công")
        else:
            st.warning("Bạn cần nhập đầy đủ thông tin")
        
count_student = len(st.session_state.student)
if count_student > 0: # nếu có học sinh
    cols = st.columns(count_student)
    
    for i in range(count_student):
        with cols[i]:
            st.write(f"Tên: {st.session_state.student[i]['name']}")
            st.write(f"Ngày sinh: {st.session_state.student[i]['birthday']}")
    

