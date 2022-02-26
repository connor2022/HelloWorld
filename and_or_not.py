price = 25
print(price > 10 and price < 50)
#this will be true as the price fulfills both requirements

print(price > 10 and price < 20)
#this is false as it only fulfills one condition

print(price > 50 or price == 25)
#this is true as it fulfills one of the two conditions

print(price > 5 or price == 25)
#this is true even if it fulfills both (it just has to fulfill AT LEAST one)

print(price == 25)

print(not price == 25)
#NOT makes the value of true or false inverted for that specific condition (not the whole line)