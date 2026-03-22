# 💰 Expense Calculator

A Python CLI app to track income and expenses, view a summary with a terminal bar chart, and export transactions to CSV.

---

## Features

- Add credit (received) and debit (spent) transactions with descriptions
- View total income, expenses, and net profit/loss
- Terminal bar chart comparing income vs expenses
- View all transactions in a numbered list
- Export transactions to CSV

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Usage

```bash
python expense_calculator.py
```

### Menu Options

```
[1]  Add Transaction
[2]  View Summary & Chart
[3]  View All Transactions
[4]  Export to CSV
[0]  Exit
```

### Example

```
  ══════════  Add Transaction  ══════════
  Type [c = Credit (received) / d = Debit (spent)]: c
  Amount (₹): 45000
  Description (optional): Monthly Salary

  ✅  Recorded: +₹45000.00  |  Monthly Salary
```

```
  ══════════  Summary  ══════════
  Total Transactions : 3
  Total Income       : ₹45,000.00
  Total Expenses     : ₹15,200.00
  ──────────────────────────────────────
  Net Balance (🟢 Profit) : ₹29,800.00

  Category            Amount  Chart
  ────────────  ────────────  ──────────────────────
  Income        ₹  45,000.00  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  Expenses      ₹  15,200.00  ░░░░░░░

  ▓ = Income   ░ = Expenses
```

---

## Project Structure

```
expense-calculator/
├── expense_calculator.py   # Main application
└── transactions_export.csv # Generated on export
```
