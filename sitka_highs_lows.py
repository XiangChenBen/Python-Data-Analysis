import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open("data/death_valley_2018_simple.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''#show header and index
    for index,column_header in enumerate(header_row,start=0):
        print(index,column_header)'''

    # acqurie highest/lowest temperature and date from csv
    highs, lows, dates  = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        #solve the missing data
        try:
            low = int(row[5])
            high = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)

# draw highs
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates,highs, c="red",alpha =0.5)
ax.plot(dates,lows, c="blue",alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

# set the parameter for graph
ax.set_title("2018 Daily Highest & lowest Temperature", fontsize=24)
ax.set_xlabel("Date", fontsize=16)
fig.autofmt_xdate() #显示倾斜的日期标签
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)
plt.show()