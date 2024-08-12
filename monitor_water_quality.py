import streamlit as st
import pandas as pd
import numpy as np
import folium # type: ignore
from streamlit_folium import st_folium # type: ignore

def generate_dummy_filter_data(num_filters=10):
    np.random.seed(0)
    data = {
        'Filter_ID': range(1, num_filters + 1),
        'Latitude': np.random.uniform(-90, 90, num_filters),
        'Longitude': np.random.uniform(-180, 180, num_filters),
        'Contaminant_Level': np.random.normal(loc=5, scale=2, size=num_filters),
        'Filter_Status': np.random.choice(['Good', 'Needs Replacement'], size=num_filters)
    }
    return pd.DataFrame(data)

def show():
    st.title('Monitor Water Quality')

    df = generate_dummy_filter_data()

    st.subheader('Contaminated Areas')
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=2)

    for _, row in df.iterrows():
        color = 'green' if row['Contaminant_Level'] < 7 else 'red'
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"Filter ID: {row['Filter_ID']}<br>Contaminant Level: {row['Contaminant_Level']:.2f}<br>Status: {row['Filter_Status']}",
            icon=folium.Icon(color=color)
        ).add_to(m)

    st_data = st_folium(m, width=700, height=500)

    st.sidebar.header('Filter Options')
    contaminant_threshold = st.sidebar.slider('Contaminant Level Threshold', min_value=0, max_value=10, value=7)

    filtered_df = df[df['Contaminant_Level'] >= contaminant_threshold]

    st.subheader(f'Filters with Contaminant Levels above {contaminant_threshold}')
    st.write(filtered_df)

    if not filtered_df.empty:
        m_filtered = folium.Map(location=[filtered_df['Latitude'].mean(), filtered_df['Longitude'].mean()], zoom_start=2)

        for _, row in filtered_df.iterrows():
            color = 'green' if row['Contaminant_Level'] < contaminant_threshold else 'red'
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=f"Filter ID: {row['Filter_ID']}<br>Contaminant Level: {row['Contaminant_Level']:.2f}<br>Status: {row['Filter_Status']}",
                icon=folium.Icon(color=color)
            ).add_to(m_filtered)

        st.subheader('Filtered Map of Contaminated Areas')
        st_folium(m_filtered, width=700, height=500)

    else:
        st.write("No filters exceed the selected contaminant level threshold.")
