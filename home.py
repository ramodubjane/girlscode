import streamlit as st

def show():
    # Display the logo
    st.image("images/logo.jpeg", width=300)

    # App title and description
    st.title("Welcome to AquaGuard")
    st.write("""
    AquaGuard is dedicated to ensuring access to clean and safe water for all. Using cutting-edge technology, we monitor and manage water quality to address the global water crisis.
    
    Navigate through the app using the sidebar to explore our features, including real-time water quality monitoring and in-depth data analysis.
    """)