
def deposit(account, amount):
    if amount <= 0:
        return "Deposit must be greatey tham 0"
    
    account['balance'] += amount

    transaction = {
        "type": "deposit",
        "amount": amount
    }

    account["transactions"].append(transaction)
    return f"Deposit successful. New balance: Ksh {account['balance']}"