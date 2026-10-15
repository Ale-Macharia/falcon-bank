
def create_account(owner, account_number, initial_balance):
    customer_info = {"name": name, "account_number": account_number, "owner": owner} 

    new_account = {
        'owner': {
            "name": name,
            "account_number": account_number,
            "balance": initial_balance
        }
    }



    if initial_balance <= 0:
        return "your starting amount ust be Greater than 0.00 Ksh"
    
    for ACC in new_account["owner"]:
        Acc = ACC
        
        if account_number == Acc['account_number']:
            return "This account number exists"
        else:
            new_account['owner'].append(customer_info)


    

    

    return new_account

print("Welcome to Falcon Bank. Lets Make you an account: \n")

name = input("\nWhats your name: ")
account_number = int(input("Account number: "))
initial_balance = int(input("Starting amount: "))


customer = create_account(name, account_number, initial_balance)
print(customer)