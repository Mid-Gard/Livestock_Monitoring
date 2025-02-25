import datetime

timestamp = 1683499098
date_time = datetime.datetime.fromtimestamp(timestamp)

print("Date and Time:", date_time.strftime("%Y-%m-%d %H:%M:%S"))
