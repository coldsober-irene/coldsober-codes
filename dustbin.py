
"""from alright import WhatsApp
import pyautogui as pg
from time import sleep

messenger = WhatsApp()

messenger.find_user("250784778722")
messenger.send_picture("19.jpg")
pg.moveTo(1295, 590)
pg.leftClick()


import pandas as pd
import os

new_data_style = pd.DataFrame(
    {
        "column1":[1,2,3,4,5],
        "column2":["irene", "coldsober", "fud", "serevision", "walker"],
        "years":["2000", "2002", "2003", "2007", "1997"]
    }
)
print(new_data_style)
"""

from math import pow

annual_cash = [
    -500000,
    120000,
    90000,
    100000,
    150000,
    140000,
    300000
]

ann2 = [
    -500000,
    80000,
    120000,
    110000,
    250000,
    80000,
    110000
]

disc1 = []
disc2 = []
rate = .14

for i in range(7):
    factor = 1 / pow((1 + rate), i)
    discounted_cash2 = annual_cash[i] * factor
    discounted_cash1 = ann2[i] * factor
    disc2.append(discounted_cash2)
    disc1.append(discounted_cash1)

total_netpv1 = 0.0
total_netpv2 = 0.0
for i in disc1:
    total_netpv1 += i

for i in disc2:
    total_netpv2 += i

print("net pv = ", round(total_netpv1, 3))
print("net pv = ", round(total_netpv2, 3))

profitable_index1 = 1 + (total_netpv1 / 500000)
profitable_index2 = 1 + (total_netpv2 / 500000)

print("profitable_index : ", round(profitable_index1, 2))
print("profitable_index : ", round(profitable_index2, 2))

# ----------------------------------------------------------------------
total_fixed_cost = [15000 for i in range(10)]
total_variable_cost = [0, 8000,
                       15000,
                       "null",
                       "null",
                       25000,
                       "null",
                       34000,
                       45000,
                       61000
                       ]

total_variable_cost[3] = "null"
total_variable_cost[4] = "null"
total_variable_cost[6] = "null"

total_cost = [15000,
              "null",
              30000,
              35000,
              38000,
              "null",
              43000,
              49000,
              60000,
              76000
              ]

total_cost[1] == "null"
total_cost[5] == "null"

output = [i for i in range(0, 10000, 1000)]

average_fixed_cost = []
average_variable_cost = []
average_total_cost = []
marginal_cost = []

#output[8] = "null"
total_fixed_cost[2] = "null"

# find missing values
for i in range(len(output)):
    if total_variable_cost[i] == "null":
        total_variable_cost[i] = total_cost[i] - total_fixed_cost[i]

    if total_cost[i] == "null":
        total_cost[i] = total_variable_cost[i] + total_fixed_cost[i]

    if total_fixed_cost[i] == "null":
        total_fixed_cost[i] = total_cost[i] - total_variable_cost[i]

for i in range(len(output)):
    try:
        av_fixed_cost = total_fixed_cost[i] / output[i]
        average_fixed_cost.append(round(av_fixed_cost, 2))
    except ZeroDivisionError:
        average_fixed_cost.append("NULL")
    try:
        av_variable_cost = total_variable_cost[i] / output[i]
        average_variable_cost.append(round(av_variable_cost, 2))
    except ZeroDivisionError:
        average_variable_cost.append("NULL")
    try:
        total_av_cost = average_fixed_cost[i] + average_variable_cost[i]
        try:
            average_total_cost.append(round(total_av_cost, 2))
        except TypeError:
            average_total_cost.append(total_av_cost)
    except ZeroDivisionError:
        average_total_cost.append("NULL")

print("average_fixed_cost : ", average_fixed_cost)
print("average_variable_cost : ", average_variable_cost)
print("average_total_cost : ", average_total_cost)

