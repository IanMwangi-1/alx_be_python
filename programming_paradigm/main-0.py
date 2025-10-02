import sys
import json
import os
from bank_account import BankAccount

STATE_FILE = "account_state.json"
DEFAULT_START_BALANCE = 100.0

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"balance": DEFAULT_START_BALANCE}
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"balance": DEFAULT_START_BALANCE}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main():
    state = load_state()
    account = BankAccount(state.get("balance", DEFAULT_START_BALANCE))

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        state["balance"] = account.account_balance
        save_state(state)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            state["balance"] = account.account_balance
            save_state(state)
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
