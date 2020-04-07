import pandas as pd
orders = pd.read_csv("task1data.txt")
sell_orders = orders[orders.OrderType == "Sell"]
max_order = sell_orders[sell_orders.Price==sell_orders.Price.max()]
print(max_order)
