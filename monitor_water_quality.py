import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

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

    # Define the color scale for the markers
    color_scale = [
        [0, "green"], 
        [7, "red"]
    ]

    # Create a pydeck layer for the map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position=["Longitude", "Latitude"],
        get_fill_color="[200, 30, 0, 140]" if "Contaminant_Level" >= 7 else "[0, 200, 0, 140]",
        get_radius=100000,
        radius_scale=1,
        pickable=True
    )

    # Define the map view
    view_state = pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=2,
        pitch=0
    )

    # Create a deck map
    deck_map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/light-v9"
    )

    st.pydeck_chart(deck_map)

    # Sidebar for filtering data
    st.sidebar.header('Filter Options')
    contaminant_threshold = st.sidebar.slider('Contaminant Level Threshold', min_value=0, max_value=10, value=7)

    filtered_df = df[df['Contaminant_Level'] >= contaminant_threshold]

    st.subheader(f'Filters with Contaminant Levels above {contaminant_threshold}')
    st.write(filtered_df)

    if not filtered_df.empty:
        filtered_layer = pdk.Layer(
            "ScatterplotLayer",
            filtered_df,
            get_position=["Longitude", "Latitude"],
            get_fill_color="[200, 30, 0, 140]",
            get_radius=100000,
            radius_scale=1,
            pickable=True
        )

        filtered_deck_map = pdk.Deck(
            layers=[filtered_layer],
            initial_view_state=view_state,
            map_style="mapbox://styles/mapbox/light-v9"
        )

        st.subheader('Filtered Map of Contaminated Areas')
        st.pydeck_chart(filtered_deck_map)

    else:
        st.write("No filters exceed the selected contaminant level threshold.")
