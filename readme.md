# Bank Account Management System

This is a simple Python project that simulates a basic bank account management system. The project includes two main classes, `Cliente` and `Conta`, which represent a client and a bank account, respectively. The system allows for deposits, withdrawals, and balance checks.

## Features

- Create a client with a name and phone number
- Create a bank account for the client
- Deposit money into the account
- Withdraw money from the account
- Display account balance

## Project Structure

```plaintext
.
├── cliente.py  # Contains the Cliente class
├── conta.py    # Contains the Conta class
└── main.py     # The main script to run the program

### Installation
git clone https://github.com/tsukishikawa/PyCharm.git

### Usage
To run the project, execute the main.py file:
 python main.py

### Example Usage

# Create a client and a bank account
c1 = Cliente("João", "114444-2222")
conta = Conta(c1.nome, 1222)

# Perform operations
conta.deposita(100)
conta.saque(50)
conta.extrato()