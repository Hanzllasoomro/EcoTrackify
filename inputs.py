import streamlit as st

def get_user_inputs():
    st.subheader("🌏 Your Country")
    country = st.selectbox(
        "Select country:", 
        [
            "Pakistan", "USA", "UK", "Canada", "India", "Australia", "China", 
            "Germany", "France", "Brazil", "Japan", "Russia", "Italy", 
            "South Africa", "Mexico", "South Korea", "Saudi Arabia", 
            "Indonesia", "Spain", "Argentina"
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        distance = st.slider("🚗 Daily commenced distance", 0.0, 5000.0)
        electricity = st.slider("💡 Electricity consumption per Day (in kWh)", 0.0, 1000.0)
    with col2:
        waste = st.slider("🚮 Waste generated per Day (in kg)", 0.0, 100.0)
        meals = st.number_input("🍔 Number of meals per Day", 0)

    if distance == 0 or electricity == 0 or waste == 0 or meals == 0:
        st.warning("Please provide non-zero values for accurate results!")

    # Normalize inputs to annual values
    distance = distance * 365
    electricity = electricity * 365
    waste = waste * 365
    meals = meals * 365

    return country, distance, electricity, waste, meals
