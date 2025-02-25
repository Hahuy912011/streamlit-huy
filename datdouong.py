import streamlit as st

st.set_page_config(page_title="Web đặt đồ uống", layout="wide")

do_uong_list = ["Trà sữa", "Cà phê", "Nước ép cam", "Sinh tố bơ", "Nước dừa", "Soda chanh", "Matcha đá xay", "Sữa đậu nành"]
duong_list = ["Đường cát trắng", "Đường nâu", "Đường phèn", "Đường thốt nốt", "Đường mía", "Đường ăn kiêng"]
thach_list = ["Thạch rau câu", "Thạch dừa", "Thạch sương sáo", "Thạch pudding", "Thạch nha đam", "Thạch hạt é", "Thạch trân châu"]

thong_tin_hoa_don = ""

st.title("Đặt đồ uống")

with st.form(key="str", clear_on_submit=False):
    do_uong = st.selectbox("Bạn muốn đặt đồ uống gì", do_uong_list)
    duong = st.selectbox("Bạn muốn thêm loại đường gì cho đồ uống", duong_list)
    thach = st.selectbox("Bạn muốn thêm loại thạch nào cho đồ uống", thach_list)
    so_luong = st.slider("Bạn muốn đặt bao nhiêu cốc", min_value=1, max_value=100, value=1)

    submitted = st.form_submit_button("Đặt")

    if submitted:
        thong_tin_hoa_don = f"### Hóa đơn đặt hàng\n- **Đồ uống:** {do_uong}\n- **Đường:** {duong}\n- **Thạch:** {thach}\n- **Số lượng:** {so_luong} cốc"
        st.markdown(thong_tin_hoa_don)
        st.success("Chọn đồ uống thành công!")

if thong_tin_hoa_don:
    st.download_button("Tải xuống hóa đơn", thong_tin_hoa_don, file_name="hoa_don.txt")
