# Q->6

money = 11600900

bill_1000 = money // 1000
money     = money % 1000
bill_500  = money // 500
money     = money % 500
bill_200  = money // 200
money     = money % 200
bill_100  = money // 100
money     = money % 100

print(bill_1000,"->(1000 bill),",bill_500,"->(500 bill),",bill_200,"->(200 bill) and", bill_100,"->(100 bill)")

