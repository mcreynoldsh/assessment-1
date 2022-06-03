
#function which takes in an item's cost and the amount paid as arguments and returns a string giving the optimal amount of change owed
def optimal_change(item_cost,amount_paid):
    change_amount = amount_paid - item_cost
    change_list = []    
    unique_list = []
    change_output = f"The optimal change for an item that costs ${'{:.2f}'.format(item_cost)} with an amout paid of ${'{:.2f}'.format(amount_paid)} is " #start of every output string with formatting for correct display of cents decimal places
    #dictionary with bill-name keyed to monetary amount it represents 
    money_conv = {           
        '$100 bill': 100,
        '$50 bill': 50,
        '$20 bill': 20,
        '$10 bill': 10,
        '$5 bill': 5,
        '$1 bill': 1,
        'quarter': .25,
        'dime': .10,
        'nickel': .05,
        'penny': .01
    }

    #statements to account for edge cases where not enough money given or exact change
    if change_amount == 0:
        change_output += "nothing! You gave exact change."
    elif change_amount < 0:
        change_output += "nothing! You owe us more money."

    #loop for converting change_amount using dictionary and adding bill-names into new list. Uses round to account for floating point errors
    for x in money_conv:
        while change_amount >= money_conv[x]:
            change_list.append(x)
            change_amount -= money_conv[x]
            change_amount = round(change_amount,2)

    #loop for building list of unique bill names        
    for k in change_list:
        if unique_list.count(k) == 0:
            unique_list.append(k)
  
    #loop to build output string using each unique bill-name and their count in change_list
    for change in unique_list:

        if(len(unique_list)>1 and len(unique_list)-1 == unique_list.index(change)):
            change_output += "and "
        
        if change_list.count(change) > 1 and change == 'penny':
            change_output += f"{change_list.count(change)} pennies"     
        elif change_list.count(change) > 1:
            change_output += f"{change_list.count(change)} {change}s"     
        else:
            change_output += f"{change_list.count(change)} {change}"
       
        if(len(unique_list)-1 == unique_list.index(change)):
            change_output += "."
        else:
            change_output += ", "    

    return change_output
