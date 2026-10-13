
from withdrawals import withdraw

account = {
    "owner": 'Alex',
    'balance': 1000.00
}

print(f"Account owner: {account['owner']}")
print(f"Starting balance: KSH {account['balance']}")

result = withdraw(account, 250.00)
print(result)
print(f"Fnal balance: KSH {account['balance']:.2f}")