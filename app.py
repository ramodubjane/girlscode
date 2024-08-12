import streamlit as st

# Page navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Monitor Water Quality", "Data Analysis"])

if page == "Home":
    import home
    home.show()
elif page == "Monitor Water Quality":
    import monitor_water_quality
    monitor_water_quality.show()
elif page == "Data Analysis":
    import data_analysis
    data_analysis.show()
