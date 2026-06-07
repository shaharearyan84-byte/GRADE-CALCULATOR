import streamlit as st

# Page Config
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #dcdcdc;
    font-size: 18px;
    margin-bottom: 30px;
}

.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.grade {
    font-size: 40px;
    font-weight: bold;
    color: #ff4b4b;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    transform: scale(1.03);
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🎓 Student Grade Calculator</div>',
            unsafe_allow_html=True)

st.markdown('<div class="sub-title">Calculate your percentage and grade instantly</div>',
            unsafe_allow_html=True)

# Input Card
with st.container():
    st.subheader("📚 Enter Subject Marks")

    col1, col2 = st.columns(2)

    with col1:
        sub1 = st.number_input("Subject 1", 0, 100)
        sub2 = st.number_input("Subject 2", 0, 100)
        sub3 = st.number_input("Subject 3", 0, 100)

    with col2:
        sub4 = st.number_input("Subject 4", 0, 100)
        sub5 = st.number_input("Subject 5", 0, 100)

# Calculate Button
if st.button("🚀 Calculate Grade"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+ 🌟"
    elif percentage >= 80:
        grade = "A 🎉"
    elif percentage >= 70:
        grade = "B 👍"
    elif percentage >= 60:
        grade = "C 🙂"
    elif percentage >= 50:
        grade = "D 😐"
    else:
        grade = "F ❌"

    st.markdown(f"""
    <div class="result-box">
        <h2>📊 Result</h2>
        <h3>Total Marks: {total}/500</h3>
        <h3>Percentage: {percentage:.2f}%</h3>
        <div class="grade">{grade}</div>
    </div>
    """, unsafe_allow_html=True)

    # Progress Bar
    st.progress(int(percentage))

    # Balloons for Top Grade
    if percentage >= 90:
        st.balloons()