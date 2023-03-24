import streamlit as st

st.set_page_config(
    page_title="Portofolio Data Science",
    page_icon = "👌"
)


st.write('<style>h1 { font-size: 40px; }</style>', unsafe_allow_html=True)
st.title("Welcome to My Project Data Science 😎")

# Display image from URL
st.image("https://tech.kipmi.or.id/wp-content/uploads/2021/11/data-science.jpeg", caption="Data Sience")

st.header("Hello nama saya Bayuzen 👌")
st.write("hari ini saya akan membuat sebuah porotofolio data science terkait price Prediction")