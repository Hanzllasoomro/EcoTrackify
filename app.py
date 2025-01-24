import streamlit as st
from inputs import get_user_inputs
from calculations import calculate_emissions, calculate_rewards_and_challenges
from visualizations import plot_emissions_pie
from suggestions import get_suggestions
from config import PER_CAPITA_EMISSIONS
from footer import display_footer

# Page Setup
st.set_page_config(layout="wide", page_title="EcoTrackify", page_icon="🌍")
st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #A5D6A7   ; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# Header
st.markdown(
    """
    <style>
        .header {
            background-color: #2C3E50;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        .header h1 {
            font-family: 'Roboto', sans-serif;
            font-size: 2.5em;
            margin: 0;
        }
        .header p {
            font-size: 1.2em;
            margin: 5px 0;
        }
    </style>
    <div class="header">
        <h1>EcoTrackify</h1>
        <p>Track, reduce, and manage your carbon footprint 🌱</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# User Inputs
country, distance, electricity, waste, meals = get_user_inputs()

if st.button("Calculate CO2 emissions"):
    # Calculations
    transportation, electricity, waste, diet, total = calculate_emissions(
        country, distance, electricity, waste, meals
    )

    # Display Results
    st.subheader("Results")
    st.metric("Your Total CO2 emissions", f"{total} tonnes per year")

    per_capita = PER_CAPITA_EMISSIONS[country]
    st.warning(
        f"CO2 emissions per capita in {country} are {per_capita} tonnes per person. "
        f"Your emissions are {round((total / per_capita) * 100, 2)}% of the per capita average."
    )

    # Visualization
    plot_emissions_pie(transportation, electricity, waste, diet)

    # Suggestions
    suggestions = get_suggestions(total, transportation, electricity, waste, diet)

    if suggestions:
        st.subheader("💡 Actionable Suggestions to Reduce Your Carbon Footprint:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

    # Rewards and Challenges
    challenges, rewards, badges = calculate_rewards_and_challenges(
        transportation, electricity, waste, diet, total
    )

    if challenges:
        st.subheader("Challenges")
        for challenge in challenges:
            st.write(f"- {challenge}")

    if rewards > 0:
        st.subheader("🏆 Your Rewards")
        st.write(f"You've earned {rewards} points!")

    if badges:
        st.subheader("🎖️ Your Badges")
        for badge in badges:
            st.write(f"- {badge}")

# Footer
display_footer()
