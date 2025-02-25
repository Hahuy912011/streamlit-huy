import streamlit as st
import random

st.title("Dự báo thời tiết")

# Khởi tạo session state để lưu lịch sử tìm kiếm và trạng thái xác nhận thông tin
if "history" not in st.session_state:
    st.session_state.history = []
if "info_confirmed" not in st.session_state:
    st.session_state.info_confirmed = False

# Nhập thông tin người dùng
user_location = st.text_input("Bạn sống khu vực nào?", "")
user_name = st.text_input("Bạn tên là gì?", "")
interest_location = st.text_input("Bạn quan tâm đến thời tiết ở đâu?", "")

if st.button("Xác nhận thông tin"):
    if user_location and user_name and interest_location:
        st.success("Nhập thông tin thành công")
        st.session_state.info_confirmed = True
    else:
        st.warning("Bạn cần nhập đầy đủ thông tin")
        st.session_state.info_confirmed = False

# Chọn khu vực lớn
regions = {
    "Miền Bắc": ["Hà Nội", "Hải Phòng", "Lào Cai", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Cao Bằng", "Điện Biên", "Hà Giang", "Hà Nam", "Hòa Bình", "Hưng Yên", "Lai Châu", "Lạng Sơn", "Nam Định", "Ninh Bình", "Phú Thọ", "Quảng Ninh", "Sơn La", "Thái Bình", "Thái Nguyên", "Tuyên Quang", "Vĩnh Phúc", "Yên Bái"],
    "Miền Trung": ["Đà Nẵng", "Huế", "Nha Trang", "Thanh Hóa", "Nghệ An", "Hà Tĩnh", "Quảng Bình", "Quảng Trị", "Quảng Nam", "Quảng Ngãi", "Bình Định", "Phú Yên", "Khánh Hòa", "Kon Tum", "Gia Lai", "Đắk Lắk", "Đắk Nông", "Lâm Đồng"],
    "Miền Nam": ["TP. Hồ Chí Minh", "Cần Thơ", "Vũng Tàu", "Bình Phước", "Bình Dương", "Đồng Nai", "Tây Ninh", "Bình Thuận", "Long An", "Đồng Tháp", "An Giang", "Tiền Giang", "Vĩnh Long", "Bến Tre", "Trà Vinh", "Sóc Trăng", "Bạc Liêu", "Cà Mau", "Kiên Giang"]
}
selected_region = st.selectbox("Chọn khu vực lớn", list(regions.keys()))
selected_city = st.selectbox("Chọn tỉnh/thành phố", regions[selected_region])

# Random thời tiết từng khu vực
def generate_weather(region):
    weather_data = {
        "Miền Bắc": {"Nhiệt độ": random.randint(10, 20), "Độ ẩm": random.randint(60, 90), "Mô tả": "Trời rét, có sương mù", "Tốc độ gió": random.uniform(1, 5)},
        "Miền Trung": {"Nhiệt độ": random.randint(20, 30), "Độ ẩm": random.randint(50, 80), "Mô tả": "Nắng ấm, có gió nhẹ", "Tốc độ gió": random.uniform(2, 6)},
        "Miền Nam": {"Nhiệt độ": random.randint(25, 35), "Độ ẩm": random.randint(50, 70), "Mô tả": "Trời nóng, có mưa rào nhẹ", "Tốc độ gió": random.uniform(3, 7)}
    }
    return weather_data.get(region, {})

# Hình ảnh
weather_images = {
    "Trời rét, có sương mù": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRU3xgr1PkEqWgQsUDHYBLwrUZdvSQR7wryA&s",
    "Nắng ấm, có gió nhẹ": "https://hoanghamobile.com/tin-tuc/wp-content/uploads/2024/06/anh-mat-troi.jpg",
    "Trời nóng, có mưa rào nhẹ": "https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/474094yvh/anh-nen-mua-roi-full-hd-dep_041327958.jpg"
}

if st.button("Xem dự báo"):
    if st.session_state.info_confirmed:
        weather = generate_weather(selected_region)
        st.subheader(f"Thời tiết tại {selected_city}")
        st.write(f"Nhiệt độ: {weather['Nhiệt độ']}°C")
        st.write(f"Độ ẩm: {weather['Độ ẩm']}%")
        st.write(f"Mô tả: {weather['Mô tả']}")
        st.write(f"Tốc độ gió: {weather['Tốc độ gió']:.1f} m/s")
        
        # Hiển thị hình ảnh thời tiết
        if weather['Mô tả'] in weather_images:
            st.image(weather_images[weather['Mô tả']], caption=weather['Mô tả'], use_container_width=True)
        
        # Lưu lịch sử tìm kiếm
        st.session_state.history.append({
            "Khu vực": selected_region,
            "Thành phố": selected_city,
            "Nhiệt độ": weather['Nhiệt độ'],
            "Độ ẩm": weather['Độ ẩm'],
            "Mô tả": weather['Mô tả'],
            "Tốc độ gió": weather['Tốc độ gió']
        })
    else:
        st.warning("Bạn cần nhập đầy đủ thông tin trước khi xem dự báo thời tiết")

# Hiển thị thông tin người dùng bên cnahj
st.sidebar.header("Thông tin người sử dụng")
st.sidebar.write(f"**Tên:** {user_name}")
st.sidebar.write(f"**Khu vực sinh sống:** {user_location}")
st.sidebar.write(f"**Khu vực quan tâm:** {interest_location}")

#Hiện lịch sử xem thời tiết
st.sidebar.header("Lịch sử xem thời tiết")
if len(st.session_state.history) > 0:
    for i, record in enumerate(st.session_state.history):
        with st.sidebar.expander(f"Lịch sử {i+1}: {record['Thành phố']}"):
            st.write(f"Khu vực: {record['Khu vực']}")
            st.write(f"Nhiệt độ: {record['Nhiệt độ']}°C")
            st.write(f"Độ ẩm: {record['Độ ẩm']}%")
            st.write(f"Mô tả: {record['Mô tả']}")
            st.write(f"Tốc độ gió: {record['Tốc độ gió']:.1f} m/s")
