
while True:
    # average client per day
    day_c = int(input("average client per day : "))
    average_cartons = float(input("average cartons sold per day : "))
    net_profit = float(input("net profit per shoes : "))
    shoes_per_carton = int(input("number of shoes present in one carton : "))

    # estimated outcomes
    daily_Nprofit = net_profit * shoes_per_carton * day_c
    weekly_Nprofit = daily_Nprofit * 6
    month_Nprofit = weekly_Nprofit * 4


    estimated_tax_monthly = month_Nprofit * 0.18

    # estimated expense
    rent = 500000
    sanitation = 3000
    security = 5000
    advertizing = 50000
    other_expenses = 500000

    total_expense = rent + sanitation + security + advertizing + other_expenses

    total_net_monthly_profit = month_Nprofit - total_expense
    #total_net_monthly_profit = month_Nprofit
    annually_Nprofit = total_net_monthly_profit * 12
    in_five_years = annually_Nprofit * 5
    print("setimated daily net profit : ", daily_Nprofit)
    print("setimated weekly net profit : ", weekly_Nprofit)
    print("setimated monthly net profit : ", total_net_monthly_profit)
    print("setimated annually net profit : ", annually_Nprofit)

    print("setimated 5 years period net profit : ", in_five_years)
