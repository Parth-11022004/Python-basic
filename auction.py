dict = {
    
}
bool_value = True
while(bool_value):
    name = input("What is ur name:\n")
    amount = int(input("Enter the amount in $\n"))
    dict[name] = amount
    yes_or_no = input("Are there any other bidders? Say 'yes' or 'no'\n")
    if yes_or_no == 'no':
        bool_value = False


   


max_key = None
max_value = -1  


for key in dict:
    value = dict[key]  
    if value > max_value:  
        max_value = value  
        max_key = key      


print(f"The highest bidder is {max_key}")