import streamlit as st

st.set_page_config(page_title="Thực đơn yêu thích", layout="wide")

khai_vi_list = ["Gỏi cuốn", "Chả giò", "Bánh xèo", "Súp măng","Bruschetta","Phô mai que chiên","Salad rong biển","Sashimi cá hồi, cá ngừ"]
mon_chinh_list = ["Cơm tấm sườn nướng", "Phở bò", "Gà kho gừng", "Mì xào hải sản","Bò bít tết sốt tiêu đen","Mỳ Carbonara","Cơm lươn","Vịt quay Bắc Kinh"]
trang_mieng_list = ["Chè khoai dẻo", "Kem trái cây", "Bánh flan", "Trái cây tươi","Mochi nhân đậu đỏ","Dango","Chè mè đen"]

so_ban = st.slider("Chọn số bàn của bạn",min_value=1,max_value=20,value=1)

if 'costumer' not in st.session_state:
    st.session_state.costumer = []  

with st.form(key="str", clear_on_submit=True):
    st.title("Đây là form tạo thực đơn yêu thích của bạn:")
    
    khai_vi = st.multiselect("Món khai vị ưa thích của bạn?", khai_vi_list)
    mon_chinh = st.multiselect("Món chính ưa thích của bạn?", mon_chinh_list)
    trang_mieng = st.multiselect("Món tráng miệng ưa thích của bạn?", trang_mieng_list)
    agree = st.checkbox("Tôi đồng ý với thực đơn trên")
    submited = st.form_submit_button("Gửi lên")
    
    if submited:
        if khai_vi and mon_chinh and trang_mieng and agree and so_ban:
            st.session_state.costumer.append({
                "Số bàn": so_ban,
                "Khai vị": khai_vi,
                "Món chính": mon_chinh,
                "Tráng miệng": trang_mieng
            })
            st.success("Nhập thông tin thành công")
        else:
            st.warning("Bạn cần nhập đầy đủ thông tin")

count_costumer = len(st.session_state.costumer)
if count_costumer > 0:
    st.write(f"Hiện tại có {count_costumer} thực đơn đã được tạo.")
    for i, data in enumerate(st.session_state.costumer):
        with st.expander(f"Thực đơn {i+1} - Bàn số {data['Số bàn']}"):
            st.write(f"Thực đơn {i+1} - Bàn số{data["Số bàn"]}")

            st.write("Khai vị:")
            for item in data["Khai vị"]:
                st.write(f"-{item}")

            st.write("Món chính:")
            for item in data["Món chính"]:
                st.write(f"-{item}")

            st.write("Tráng miệng:")
            for item in data["Tráng miệng"]:
                st.write(f"-{item}")