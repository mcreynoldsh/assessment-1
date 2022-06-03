from optimal_change import optimal_change
#test cases for optimal_change function, including edge/special case values
print(optimal_change(32.50, 42.60)== "The optimal change for an item that costs $32.50 with an amout paid of $42.60 is 1 $10 bill, and 1 dime.")
print(optimal_change(50.53, 10)== "The optimal change for an item that costs $50.53 with an amout paid of $10.00 is nothing! You owe us more money.")
print(optimal_change(26.78, 26.78)== "The optimal change for an item that costs $26.78 with an amout paid of $26.78 is nothing! You gave exact change.")
print(optimal_change(146.32, 300)== "The optimal change for an item that costs $146.32 with an amout paid of $300.00 is 1 $100 bill, 1 $50 bill, 3 $1 bills, 2 quarters, 1 dime, 1 nickel, and 3 pennies.")
print(optimal_change(130, 230)== "The optimal change for an item that costs $130.00 with an amout paid of $230.00 is 1 $100 bill.")
print(optimal_change(136.66, 525)== "The optimal change for an item that costs $136.66 with an amout paid of $525.00 is 3 $100 bills, 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 1 nickel, and 4 pennies.")
print(optimal_change(5.06,5.07)== "The optimal change for an item that costs $5.06 with an amout paid of $5.07 is 1 penny.")