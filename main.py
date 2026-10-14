
from withdrawals import withdraw
from deposits import deposit

account = {
    'owner': "Alex",
    "balance": 1000.00,
    "transactions":[]
}

print(f"Starting ballance: KSh {account['balance']:.2f}")

print()

withdraw_result = withdraw(account, 250.00)
print(withdraw_result)

deposit_result = deposit(account, 200)
print(deposit_result)

failed_result = withdraw(account, 2000.00)
print(failed_result)


print("\nTransaction history:")

for transaction in account["transactions"]:
    print(
    f"{transaction['type']}: "
    f"KSH {transaction['amount']:.2f}"
    )

print(f"\nFunal balance: KSH {account['balance']:.2f}")