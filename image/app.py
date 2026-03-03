from datetime import datetime

print("📚 Study Logger Container Started")

study_topic = input("What did you study today? ")

current_time = datetime.now()

log_entry = f"{current_time} - {study_topic}\n"

with open("study_log.txt", "a") as f:
    f.write(log_entry)

print("✅ Study log saved successfully!")
