from config import EMISSION_FACTORS, PER_CAPITA_EMISSIONS

def calculate_emissions(country, distance, electricity, waste, meals):
    factors = EMISSION_FACTORS[country]
    transportation = round(factors["Transportation"] * distance / 1000, 2)
    electricity = round(factors["Electricity"] * electricity / 1000, 2)
    waste = round(factors["Waste"] * waste / 1000, 2)
    diet = round(factors["Diet"] * meals / 1000, 2)
    total = round(transportation + electricity + waste + diet, 2)
    return transportation, electricity, waste, diet, total

def calculate_rewards_and_challenges(transportation, electricity, waste, diet, total):
    challenges = []
    rewards = 0
    badges = []

    # Logic for challenges and rewards
    if transportation > 2:
        challenges.append("🚗 Reduce transportation emissions by carpooling.")
    if electricity > 3:
        challenges.append("💡 Use energy-efficient appliances.")
    if waste > 1:
        challenges.append("🚮 Recycle more.")
    if diet > 4:
        challenges.append("🍔 Reduce meat consumption.")

    if total < 5:
        rewards += 20
        badges.append("Sustainability Master")

    return challenges, rewards, badges
