def get_suggestions(total_emissions, transportation_emissions, electricity_emissions, waste_emissions, diet_emissions):
    suggestions = []

    # Transportation suggestions
    if transportation_emissions > 2:
        suggestions.append("🚗 Consider carpooling, using public transport, or switching to an electric vehicle to reduce emissions.")
    elif transportation_emissions < 1:
        suggestions.append("🚗 Great job! Keep up the sustainable transportation choices.")

    # Electricity suggestions
    if electricity_emissions > 3:
        suggestions.append("💡 Try using energy-efficient appliances, switching to LED lights, or considering solar energy.")
    elif electricity_emissions < 1:
        suggestions.append("💡 Excellent! Keep saving energy with your current habits.")

    # Waste suggestions
    if waste_emissions > 1:
        suggestions.append("🚮 Consider reducing waste, recycling more, and composting organic waste to lower emissions.")
    elif waste_emissions < 0.5:
        suggestions.append("🚮 Keep up the good work! Your waste management efforts are commendable.")

    # Diet suggestions
    if diet_emissions > 4:
        suggestions.append("🍔 Reducing meat consumption or adopting a plant-based diet could significantly cut down your carbon footprint.")
    elif diet_emissions < 2:
        suggestions.append("🍔 Great! You're already making sustainable food choices.")

    # Overall suggestions based on total emissions
    if total_emissions > 10:
        suggestions.append("🌍 Your emissions are high. Consider adopting more sustainable practices across all areas.")
    elif total_emissions < 5:
        suggestions.append("🌍 Well done! You're living sustainably and reducing your carbon footprint.")

    return suggestions
