import streamlit as st

tinh_cach = {"Con mèo": "Bạn là người độc lập, bí ẩn, và có xu hướng thích không gian riêng. Bạn có thể là người thông minh, nhẹ nhàng nhưng cũng rất quyết đoán khi cần thiết.",
             "Con chó": "Bạn là người đáng tin cậy, thân thiện, luôn sẵn sàng giúp đỡ và có lòng trung thành sâu sắc với bạn bè và gia đình.",
             "Con sư tử": "Bạn có thể là người tự tin, quyết đoán, và có khả năng lãnh đạo. Người khác có thể nhìn nhận bạn như một người có sức ảnh hưởng và luôn đứng vững trong những tình huống khó khăn.",
             "Con ngựa": "Bạn có thể là người yêu thích sự tự do, luôn tìm kiếm sự phát triển cá nhân và có năng lượng dồi dào. Bạn cũng có thể là người rất chăm chỉ và bền bỉ trong công việc.",
             "Thiên nga": "Bạn là người tao nhã, điềm đạm và có sức hút đặc biệt. Bạn có thể cũng là người có vẻ ngoài thanh thoát, nhưng lại rất mạnh mẽ bên trong."}

st.set_page_config(page_title="dvnoigiveban", page_icon=":dog:", layout="wide")

st.title("Hãy chọn con vật yếu thích của bạn")
col1, col2, col3, col4, col5 = st.columns(5)

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

anh_meo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtrIHdPTonPL-h4e1khZzEUutvBAJbhegxKQ&s"
anh_cho = "https://cellphones.com.vn/sforum/wp-content/uploads/2024/05/anh-cho-58.jpg"
anh_sutu = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPG27C21ebSokxRNRhX60vv5-2cjcPLlvSA&s"
anh_ngua = "https://png.pngtree.com/thumb_back/fh260/background/20230424/pngtree-beautiful-horse-galloping-by-the-water-with-mountain-scenery-over-its-image_2559567.jpg"
anh_thien_nga = "https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/473528tck/image-88-hinh-anh-con-thien-ngade-thuong-dang-yeu-thoi-gian-qua-167636952559531.jpg"

if b1:
    audio_meo = "meo.mp3"
    st.audio(audio_meo, format = "audio/mp3")
    video = "https://www.youtube.com/watch?v=oFGz1kcRPfY"
    st.video(video)

if b2:
    audio_cho = "cho.mp3"
    st.audio(audio_cho, format = "audio/mp3")
    video = "https://www.youtube.com/watch?v=AGV-2RHDeZI"
    st.video(video)

if b3:
    audio_sutu = "sutu.mp3"
    st.audio(audio_sutu, format = "audio/mp3")
    video = "https://www.youtube.com/watch?v=e8S7pT1YwtE"
    st.video(video)

if b4:
    audio_ngua = "ngua.mp3"
    st.audio(audio_ngua, format = "audio/mp3")
    video = "https://www.youtube.com/watch?v=ALq1eyTX4HU"
    st.video(video)

if b5:
    video = "https://www.youtube.com/watch?v=ApZxHm-MLyc"
    st.video(video)

with st.sidebar:
    if b1:
        st.write("Con vật bạn chọn là con mèo")
        with st.expander("Con mèo"):
            st.write(tinh_cach["Con mèo"])
            st.image(anh_meo, caption="Mèo")
    if b2:
        st.write("Con vật bạn chọn là con chó")
        with st.expander("Con chó"):
            st.write(tinh_cach["Con chó"])
            st.image(anh_cho, caption="Chó")
    if b3:
        st.write("Con vật bạn chọn là con sư tử")
        with st.expander("Con sư tử"):
            st.write(tinh_cach["Con sư tử"])
            st.image(anh_sutu, caption="Sư tử")
    if b4:
        st.write("Con vật bạn chọn là con ngựa")
        with st.expander("Con ngựa"):
            st.write(tinh_cach["Con ngựa"])
            st.image(anh_ngua, caption="Ngựa")
    if b5:
        st.write("Con vật bạn chọn là thiên nga")
        with st.expander("Thiên nga"):
            st.write(tinh_cach["Thiên nga"])
            st.image(anh_thien_nga, caption="Thiên nga")
