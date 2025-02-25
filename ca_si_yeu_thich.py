import streamlit as st

tinh_cach = {"Con mèo":"Bạn là người độc lập, bí ẩn, và có xu hướng thích không gian riêng. Bạn có thể là người thông minh, nhẹ nhàng nhưng cũng rất quyết đoán khi cần thiết.",
             "Con chó":"Bạn là người đáng tin cậy, thân thiện, luôn sẵn sàng giúp đỡ và có lòng trung thành sâu sắc với bạn bè và gia đình.",
             "Con sư tử":"Bạn có thể là người tự tin, quyết đoán, và có khả năng lãnh đạo. Người khác có thể nhìn nhận bạn như một người có sức ảnh hưởng và luôn đứng vững trong những tình huống khó khăn.",
             "Con ngựa":"Bạn có thể là người yêu thích sự tự do, luôn tìm kiếm sự phát triển cá nhân và có năng lượng dồi dào. Bạn cũng có thể là người rất chăm chỉ và bền bỉ trong công việc.",
             "Thiên nga":"Bạn là người tao nhã, điềm đạm và có sức hút đặc biệt. Bạn có thể cũng là người có vẻ ngoài thanh thoát, nhưng lại rất mạnh mẽ bên trong."}

st.set_page_config(page_title = "dvnoigiveban", page_icon = ":dog:", layout = "wide" )

st.title("Hãy chọn con vật yếu thích của bạn")
col1, col2, col3, col4, col5 = st.columns(5)

with st.sidebar:
    image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqJ-F0XUATEzBA9XOB6CRTrKimJy1tf39Fhg&s"
    st.image(image, caption = "Alan Walker")
    st.write("Tên : Alan Olav Walker")
    st.write("Nghệ danh : Alan Walker")
    st.write("Alan Walker là một nhà sản xuất âm nhạc và DJ người Anh - Na Uy, nổi bật với phong cách âm nhạc điện tử. Anh sinh năm 1997 tại Anh, nhưng gia đình anh chuyển đến Na Uy khi anh còn nhỏ. Alan Walker bắt đầu sự nghiệp âm nhạc vào năm 2012 và nhanh chóng gây được sự chú ý với các bản nhạc nổi tiếng như Faded, Alone, và Sing Me to Sleep.Faded là bản hit lớn nhất của anh, phát hành vào năm 2015, đạt hàng tỷ lượt xem trên YouTube và trở thành một trong những bài hát nổi tiếng nhất thế giới. Phong cách âm nhạc của Alan Walker kết hợp giữa thể loại progressive house, electro house, và future bass.Ngoài sự nghiệp âm nhạc, hình ảnh đặc trưng của Alan Walker là chiếc áo hoodie và mặt nạ, điều này giúp anh giữ được sự kín đáo và cũng tạo nên một thương hiệu cá nhân độc đáo. Alan Walker đã đạt được nhiều giải thưởng và thành công quốc tế, được biết đến như một trong những DJ và nhà sản xuất trẻ nổi bật nhất trong ngành công nghiệp âm nhạc điện tử.")



st.title("Bài hát yêu thích")
st.write("Ignite")
audio = "AW.mp3"
st.audio(audio, format = "audio/mp3")
st.title("MV yêu thích")
st.write("IGNITE")
video = "https://www.youtube.com/watch?v=zrwTYozyzYA"
st.video(video, format = "video/mp4")



st.write("Con vật bạn chọn là con")

with col1:
    b1 = st.button("Con mèo")
with col2:
    b2 = st.button("Con chó")
with col3:
    b3 = st.button("Con sư tử")
with col4:
    b4 = st.button("Con ngựa")
with col5:
    b5 = st.button("Thiên nga")

if b1:
    with st.expander("Con mèo"):
        st.write(tinh_cach["Con mèo"])
if b2:
    with st.expander("Con chó"):
        st.write(tinh_cach["Con chó"])
if b3:
    with st.expander("Con sư tử"):
        st.write(tinh_cach["Con sư tử"])
if b4:
    with st.expander("Con ngựa"):
        st.write(tinh_cach["Con ngựa"])
if b5:
    with st.expander("Thiên nga"):
        st.write(tinh_cach["Thiên nga"])

with st.sidebar:
    st.title("Trắc nghiệm tính cách")
    if b1:
        st.write("Con vật bạn chọn là con mèo")
    if b2:
        st.write("Con vật bạn chọn là con chó")
    if b3:
        st.write("Con vật bạn chọn là con sư tử")
    if b4:
        st.write("Con vật bạn chọn là con ngựa")
    if b5:
        st.write("Con vật bạn chọn là thiên nga")


anh_meo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtrIHdPTonPL-h4e1khZzEUutvBAJbhegxKQ&s"
st.image(anh_meo, caption = "Mèo")

anh_cho = "https://cellphones.com.vn/sforum/wp-content/uploads/2024/05/anh-cho-58.jpg"
st.image (anh_cho, caption = "Chó")

anh_sutu = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPG27C21ebSokxRNRhX60vv5-2cjcPLlvSA&s"
st.image (anh_sutu, caption = "Sư tử")

anh_ngua = "https://png.pngtree.com/thumb_back/fh260/background/20230424/pngtree-beautiful-horse-galloping-by-the-water-with-mountain-scenery-over-its-image_2559567.jpg"
st.image (anh_ngua, caption = "Ngựa")

anh_thien_nga = "https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/473528tck/image-88-hinh-anh-con-thien-ngade-thuong-dang-yeu-thoi-gian-qua-167636952559531.jpg"
st.image (anh_thien_nga, caption = "Thiên nga")

st.audio(3s.mp3, format="audio/mp3")