from datetime import datetime, timedelta

def calculate_week_day(last_period_date):
    last_period_date = datetime.strptime(last_period_date, '%d.%m.%Y')
    current_date = datetime.now()
    
    pregnancy_weeks = (current_date - last_period_date).days // 7
    remaining_days = (current_date - last_period_date).days % 7
    
    print("Pregnancy Weeks:", pregnancy_weeks, "weeks and", remaining_days, "days")
    print("Baby is", (current_date - last_period_date).days, "days old")
    
    due_date = last_period_date + timedelta(days=280)
    remaining_days_count = (due_date - current_date).days
    
    print("Estimated Due Date:", due_date.strftime('%d.%m.%Y'))
    print("Remaining Days:", remaining_days_count, "days")

last_period_date = input("Enter the last period date in DD.MM.YYYY format: ")
calculate_week_day(last_period_date)