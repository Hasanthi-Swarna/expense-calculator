"""
Expense Calculator v2.0
Pure Python — no external dependencies.
Features: transaction history, monthly/weekly reports with terminal charts, CSV export
"""

import csv
import os
from collections import defaultdict


# ─────────────────────────────────────────────
# Data Layer
# ─────────────────────────────────────────────

transactions = []   # list of dicts: {type, amount, description}


def add_transaction(tx_type: str, amount: float, description: str) -> None:
    transactions.append({
        "type":        tx_type,   # "credit" or "debit"
        "amount":      amount,
        "description": description,
    })


# ─────────────────────────────────────────────
# Analysis
# ─────────────────────────────────────────────

def summary_stats() -> dict:
    income   = sum(t["amount"] for t in transactions if t["type"] == "credit")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "debit")
    return {
        "income":   round(income, 2),
        "expenses": round(expenses, 2),
        "balance":  round(income - expenses, 2),
        "count":    len(transactions),
    }


# ─────────────────────────────────────────────
# Terminal Bar Chart
# ─────────────────────────────────────────────

def terminal_bar(value: float, max_value: float, width: int = 20, char: str = "█") -> str:
    if max_value == 0:
        return ""
    filled = int(round(value / max_value * width))
    return char * filled


def print_breakdown() -> None:
    """Show income vs expenses as a simple terminal bar chart."""
    s = summary_stats()
    max_val = max(s["income"], s["expenses"]) or 1

    print(f"\n  {'Category':<12}  {'Amount':>12}  Chart")
    print(f"  {'─'*12}  {'─'*12}  {'─'*22}")
    print(f"  {'Income':<12}  ₹{s['income']:>11,.2f}  {terminal_bar(s['income'],   max_val, 20, '▓')}")
    print(f"  {'Expenses':<12}  ₹{s['expenses']:>11,.2f}  {terminal_bar(s['expenses'], max_val, 20, '░')}")
    print(f"\n  ▓ = Income   ░ = Expenses")


# ─────────────────────────────────────────────
# CSV Export
# ─────────────────────────────────────────────

def export_transactions_csv(path: str = "transactions_export.csv") -> str:
    if not transactions:
        return ""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["type", "amount", "description"])
        writer.writeheader()
        writer.writerows(transactions)
    return path


# ─────────────────────────────────────────────
# CLI Helpers
# ─────────────────────────────────────────────

def _get_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= 0:
                print("  ⚠  Amount must be positive. Try again.")
                continue
            return val
        except ValueError:
            print("  ⚠  Invalid number. Please enter a numeric value.")


def _get_choice(prompt: str, valid: list) -> str:
    while True:
        val = input(prompt).strip().lower()
        if val in valid:
            return val
        print(f"  ⚠  Please enter one of: {', '.join(valid)}")


# ─────────────────────────────────────────────
# Menu Handlers
# ─────────────────────────────────────────────

def handle_add_transaction() -> None:
    print("\n  ══════════  Add Transaction  ══════════")
    tx_type = _get_choice("  Type [c = Credit (received) / d = Debit (spent)]: ", ["c", "d"])
    tx_type = "credit" if tx_type == "c" else "debit"
    amount  = _get_float("  Amount (₹): ")
    desc    = input("  Description (optional): ").strip() or "—"

    add_transaction(tx_type, amount, desc)

    sign = "+" if tx_type == "credit" else "-"
    print(f"\n  ✅  Recorded: {sign}₹{amount:.2f}  |  {desc}")


def handle_summary() -> None:
    print("\n  ══════════  Summary  ══════════")
    if not transactions:
        print("  No transactions yet.")
        return

    s = summary_stats()
    print(f"  Total Transactions : {s['count']}")
    print(f"  Total Income       : ₹{s['income']:,.2f}")
    print(f"  Total Expenses     : ₹{s['expenses']:,.2f}")
    print(f"  {'─'*38}")
    label = "🟢 Profit" if s["balance"] >= 0 else "🔴 Loss"
    print(f"  Net Balance ({label}) : ₹{abs(s['balance']):,.2f}")
    print_breakdown()


def handle_recent() -> None:
    print("\n  ══════════  All Transactions  ══════════")
    if not transactions:
        print("  No transactions yet.")
        return

    print(f"\n  {'#':<4}  {'Type':<7}  {'Amount':>10}  Description")
    print(f"  {'─'*4}  {'─'*7}  {'─'*10}  {'─'*25}")
    for i, t in enumerate(transactions, 1):
        sign  = "+" if t["type"] == "credit" else "-"
        label = "Credit" if t["type"] == "credit" else "Debit "
        print(f"  {i:<4}  {label:<7}  {sign}₹{t['amount']:>9,.2f}  {t['description']}")


def handle_export() -> None:
    print("\n  ══════════  Export Transactions  ══════════")
    if not transactions:
        print("  No transactions to export.")
        return

    path = export_transactions_csv()
    print(f"  ✅  {len(transactions)} transactions exported → {os.path.abspath(path)}")


# ─────────────────────────────────────────────
# Main Loop
# ─────────────────────────────────────────────

def main_menu() -> None:
    print("""
  ╔══════════════════════════════════════╗
  ║     💰  Expense Calculator  v2.0     ║
  ╚══════════════════════════════════════╝

    [1]  Add Transaction
    [2]  View Summary & Chart
    [3]  View All Transactions
    [4]  Export to CSV
    [0]  Exit
    """)


def run() -> None:
    handlers = {
        "1": handle_add_transaction,
        "2": handle_summary,
        "3": handle_recent,
        "4": handle_export,
    }

    while True:
        main_menu()
        choice = input("  Select option: ").strip()

        if choice == "0":
            print("\n  👋  Goodbye!\n")
            break
        elif choice in handlers:
            handlers[choice]()
        else:
            print("\n  ⚠  Invalid choice. Please enter 0–4.")


if __name__ == "__main__":
    run()
