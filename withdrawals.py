def withdraw(account, amount):
    if account['balance'] <= 0:
        return "Withdrawal amount must be greater Zero"
    
    if amount > account["balance"]:
        return f"Insufficint balance."
    

    account['balance'] -= amount
    return f"Withdrawal successifully. Your Account balance is KSH {account["balance"]:.2f}"

