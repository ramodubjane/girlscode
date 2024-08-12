import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_dummy_filter_data(num_filters=10):
    np.random.seed(0)
    data = {
        'Filter_ID': range(1, num_filters + 1),
        'Contaminant_Level': np.random.normal(loc=5, scale=2, size=num_filters),
        'Filter_Status': np.random.choice(['Good', 'Needs Replacement'], size=num_filters)
    }
    return pd.DataFrame(data)

def show():
    st.title('Data Analysis')

    df = generate_dummy_filter_data()

    st.subheader('Contaminant Levels Analysis')
    fig, ax = plt.subplots()
    sns.histplot(df['Contaminant_Level'], kde=True, ax=ax)
    ax.set_title('Distribution of Contaminant Levels')
    st.pyplot(fig)

    st.subheader('Filter Status Distribution')
    st.bar_chart(df['Filter_Status'].value_counts())
