import matplotlib.pyplot as plt
import streamlit as st

def plot_emissions_pie(transportation, electricity, waste, diet):
    labels = ["Transportation", "Electricity", "Waste", "Diet"]
    values = [transportation, electricity, waste, diet]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    if all(v == 0 for v in values):
        st.warning("No emissions data to display.")
        return

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors)
    ax.axis('equal')
    st.pyplot(fig, use_container_width=False)
