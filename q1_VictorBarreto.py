acc_balance = 1000

check_account = lambda state : (print("Check account") or "Check account") if state == "start" else print("State not valid for this operation") or "State not valid for this operation"

withdraw = lambda state, value : print("Withdraw") or attempt_withdraw(value) if state == "Check account" else print("State not valid for this operation") or "State not valid for this operation"

attempt_withdraw = lambda value : (print("Withdraw not allowed") or acc_balance) if (acc_balance - value) < 0 else print("Withdraw amount") or update_account_balance("Withdraw amount", -value)

deposit = lambda state, value : print("Deposit") or update_account_balance("Deposit", value) if state == "Check account" else print("State not valid for this operation") or "State not valid for this operation"

update_account_balance = lambda state, value : print("Update account balance") or (acc_balance + value) if (state == "Withdraw amount" or state == "Deposit") else print("State not valid for this operation") or acc_balance

print("Antes: " + str(acc_balance))

acc_balance = deposit(check_account("start"), 500)

print("Depois: " + str(acc_balance))
