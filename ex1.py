stock_price=[10,20,30,40,50]
# this will give 10
stock_price[0] 
# this will give 40
stock_price[2]

# another example we have stock price from match 4 to march 7
# we will use the dictionaries cz they are theones that can store both key and values

stock_price_withdate={
  "march1":20,
  "march2":30,
  "march3":40,
  "march4":50
}
print(stock_price_withdate.get("march1"))
print(stock_price_withdate.get("march4"))