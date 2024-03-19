from datetime import datetime

# Get current date and time
current_date_time = datetime.now()

# Format the current date as dd/mm/yyyy
current_date = current_date_time.strftime("%d/%m/%Y")

current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)

