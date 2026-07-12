def generate_reminders(risk):
    reminders = []

    reminders.append("💧 Drink at least 2–3 liters of water daily.")
    reminders.append("😴 Sleep for 7–8 hours every night.")
    reminders.append("🚶 Walk for at least 30 minutes daily.")

    if risk == "High":
        reminders.append("🩺 Schedule a doctor consultation within the next few days.")
        reminders.append("🩸 Monitor your blood glucose regularly.")
    elif risk == "Medium":
        reminders.append("📅 Get a blood glucose test within the next month.")
        reminders.append("🥗 Follow a balanced, low-sugar diet.")
    else:
        reminders.append("✅ Maintain your healthy lifestyle.")
        reminders.append("📅 Get a routine health check every year.")

    return reminders