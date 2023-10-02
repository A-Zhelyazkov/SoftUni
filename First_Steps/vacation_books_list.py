pages = int(input("Pages: "))
pages_per_hour = int(input("Pages per hour: "))
days_to_read = int(input("Days left to read: "))
total_time_to_read = pages / pages_per_hour
needed_hours_daily = total_time_to_read / days_to_read
print(int(needed_hours_daily))
