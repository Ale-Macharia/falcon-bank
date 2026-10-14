
def withdraw(account, amount):
    if amount <= 0:
        return "Withdrawal amount must be greater than zero."
    
    if amount > account['balance']:
        return "insufficient balance"
    
    account["balance"] -= amount

    transaction = {
        "type": "withdrawal",
        "amount": amount
    }

    account["transactions"].append(transaction)
    
    return f"Withdrawal successful. new balance: Ksh {account["balance"]:.2f}"