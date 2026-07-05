import streamlit as st

st.title("Link Button Demo")

st.link_button(
    "Visit GitHub",
    "https://github.com"
)

st.link_button(
    "Visit Google",
    "https://google.com"
)


st.page_link("pages/demo.py",label="Checklink")


st.image(
    "https://s.yimg.com/fz/api/res/1.2/9ks_X1DHsNXvDbkNeeEmcw--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD00MTI7cHhvZmY9NTA7cHlvZmY9MTAwO3E9ODA7c3M9MTt3PTM4OA--/https://i.pinimg.com/736x/a8/08/35/a808353507aa0bd01a6812a412240758.jpg",
    caption="Python Logo",
    width=400
)


st.markdown("`print('Hello')`")


st.markdown("""
| Skill | Level |
|-------|-------|
| Python | ⭐⭐⭐⭐⭐ |
| SQL | ⭐⭐⭐⭐ |
| Streamlit | ⭐⭐⭐ |
""")

st.logo("python.png")


st.badge("New")

st.badge("AI")

st.badge("Python")