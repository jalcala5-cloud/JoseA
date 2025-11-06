#!/usr/bin/env python3
import os
import time
import datetime
import calendar

# --- Define reminders ---
reminders = {
    "2025-12-06": ["Team meeting at 10:00 AM", "Doctor appointment at 3:30 PM"],
    "2025-12-14": ["Project review", "Dinner with Alex"]
}

def clear_screen():
    os.system("clear")

def show_calendar():
    clear_screen()
    today = datetime.date.today()
    yy, mm = today.year, today.month

    # Print the calendar
    cal = calendar.TextCalendar(firstweekday=0)
    cal_str = cal.formatmonth(yy, mm)

    print(f"\n📅 Real-Time Calendar — {today.strftime('%B %Y')}")
    print("-" * 40)

    # Highlight today's date
    cal_str = cal_str.replace(f"{today.day:2d}", f"\033[95m[{today.day:2d}]\033[0m")

    print(cal_str)

    # Show reminders
    key = today.strftime("%Y-%m-%d")
    print("📝 Reminders for Today:")
    if key in reminders:
        for item in reminders[key]:
            print(f"  • {item}")
    else:
        print("  No reminders today.")

# --- Main Loop ---
while True:
    show_calendar()
    time.sleep(1)
