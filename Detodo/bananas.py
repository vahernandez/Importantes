DataInputs = input().split()
 
CostFirstBanana = int(DataInputs[0])
initialNumberDollars = int(DataInputs[1])
NumberOfBananas = int(DataInputs[2])
 
PriceNeeded = 0
 
for i in range(NumberOfBananas+1) :
    priceOfBanana = i*CostFirstBanana
    PriceNeeded += priceOfBanana
 
AmountBorrowedDollars = PriceNeeded - initialNumberDollars
 
if AmountBorrowedDollars < 0:
    AmountBorrowedDollars = 0
 
print(AmountBorrowedDollars)