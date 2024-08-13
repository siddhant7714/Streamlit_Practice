import streamlit as st
import pandas as pd
import numpy as np
import time as t

# Set up the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Centered Title using st.markdown with HTML
st.markdown("<h1 style='text-align: center;'>Welcome Home Sir!</h1>", unsafe_allow_html=True)


#Displaying image
st.image("aqua-azure-iron-man-wallpaper.jpg", caption="Jarvis here", width=800)


# Other Streamlit components
st.title("This is Jarvis! How may I help you?")
st.header("Header")
st.subheader("Subheader")
st.write("This is a write function.")
st.markdown("**Bold Markdown Text**")
st.markdown(":moon:")
st.latex(r'''
    \frac{a}{b}
''')

# Input widgets
name = st.text_input("Enter your name")
text_area = st.text_area("Enter some text")
number = st.number_input("Enter a number", min_value=0)
slider = st.slider("Select a value", 0, 100)
option = st.selectbox("Choose an option", ["Option 1", "Option 2"])
multi_option = st.multiselect("Select multiple options", ["Option A", "Option B"])
choice = st.radio("Choose one", ["Choice 1", "Choice 2"])
is_checked = st.checkbox("Check me out!")
file = st.file_uploader("Upload a file")
date = st.date_input("Select a date")
time = st.time_input("Select a time")
color = st.color_picker("Pick a color")

# Sidebar content
with st.sidebar:
    st.header("Sidebar")
    st.text_input('Enter your mail')
    st.text_input("Password")
    st.text_input("Enter Your API key!")

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# Expander for additional content
with st.expander("More Info"):
    st.write("Expanded content")

# Progress bar and spinner
progress_bar = st.progress(90)
with st.spinner("Loading..."):
    t.sleep(2)

# Celebratory effects
st.balloons()
st.snow()

# DataFrame creation and display
data = pd.DataFrame(np.random.randn(50, 2), columns=["x", "y"])
st.dataframe(data)  # Display DataFrame with interactive features
st.table(data)      # Display DataFrame as a static table

# Display charts
st.line_chart(data)  # Display a line chart
st.bar_chart(data)   # Display a bar chart

# Display a map with randomly generated location data
data_with_location = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, 50),
    'lon': np.random.uniform(-180, 180, 50)
})
st.map(data_with_location)  # Display a map with location data
