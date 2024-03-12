import random


MAX_LINES: int = 3
MAX_BET: int = 100
MIN_BET: int = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # symbol holds key and symbol_count holds value
        for _ in range(symbol_count):
            all_symbols.append(symbol)

def deposit():
    while True:
        amount: int = input("What would you like to deposit: $ ")
        if amount.isdigit(): # Negative #'s won't be true
            amount: int = int(amount) # convert to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines: int = input(f"Enter the number of lines to bet on 1 - {str(MAX_LINES)}: ")
        if lines.isdigit():
            lines: int = int(lines)
            if lines in range(1, MAX_LINES + 1):
                break
            else:
                print(f"Must be in range 1 - {str(MAX_LINES)}:")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet: int = input("What would you like to bet on each line? $ ")
        if bet.isdigit():
            bet: int = int(bet)
            if bet in range(MIN_BET, MAX_BET + 1):
                break
            else:
                print(f"Amount must be in range ${str(MIN_BET)} - ${str(MAX_BET)}:")
        else:
            print("Please enter a number.")
    return bet

def main():
    balance: int = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Inadequate Funds, your current balance is ${balance}")
        else:
            break

    print(f"You have a current balance of ${balance}.")
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

main()


# https://www.youtube.com/watch?v=th4OBktqK1I&t=66s&ab_channel=TechWithTim
# 23:54