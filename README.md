# Restaurant Billing System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Problem Statement](https://img.shields.io/badge/PS%20No.-45-darkred)
![Status](https://img.shields.io/badge/Status-Completed-success)
![University](https://img.shields.io/badge/Rungta%20International%20Skills%20University-Bhilai-18181b)

A console-based Python application developed to automate restaurant order processing, validate customer inputs, and generate itemized receipts with conditional discounts and Goods and Services Tax (GST).

---

## Table of Contents
- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Menu & Billing Rules](#menu--billing-rules)
- [Technologies Used](#technologies-used)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Test Cases & Verification](#test-cases--verification)
- [Sample Console Output](#sample-console-output)
- [Future Scope](#future-scope)
- [Project & Author Information](#project--author-information)

---

## About the Project

In fast-paced food service counters, manual billing often leads to calculation mistakes, inconsistent tax or discount application, and slower customer checkout. The **Restaurant Billing System** solves this by loading menu prices dynamically from an external file (`menu.txt`), guiding the cashier through an interactive order-entry loop, validating every entry against strict business rules, and outputting a cleanly aligned console receipt.

---

## Key Features

- **Dynamic Menu Loading:** Reads dish names and unit prices from `menu.txt` into a Python dictionary (`O(1)` lookup), with a built-in fallback dictionary for reliability.
- **Interactive Order Loop:** Accepts multiple food and beverage selections until the cashier enters `Generate bill` (or `bill` / `done`).
- **Defensive Input Validation:**
  - Case-insensitive item matching against available menu items.
  - Rejects zero, negative, or non-numeric quantities without crashing.
  - Prevents generating an empty bill before at least one item is added.
- **Smart Order Consolidation:** Automatically merges quantities and line totals if the same item is ordered multiple times within a session.
- **Modular Billing Engine:** Separates subtotal, discount, GST, and grand total computations into dedicated functions.
- **Formatted Receipt Output:** Displays aligned columns for items, quantities, line amounts, discount breakdown, tax, and final payable amount.

---

## Menu & Billing Rules

Configured via `codebase/menu.txt`:

| Item | Unit Price (Rs.) |
| :--- | :---: |
| **Dosa** | 80 |
| **Idli** | 40 |
| **Thali** | 150 |
| **Tea** | 20 |

- **Discount Rule:** A **10% discount** is applied automatically when the subtotal is strictly greater than **Rs. 500** (`subtotal > 500`).
- **Taxation Rule:** **5% GST** is calculated on the net taxable amount *after* deducting any applicable discount.

---

## Technologies Used

| Technology / Concept | Role in Project |
| :--- | :--- |
| **Python 3** | Core programming language and runtime environment |
| **File Handling (`os`)** | Portable loading of `menu.txt` relative to script location |
| **Dictionaries (`dict`)** | Storing menu items and prices for fast lookup |
| **Lists (`list[dict]`)** | Maintaining ordered customer selections and line totals |
| **Loops & Exception Handling** | Continuous order intake and `ValueError` quantity validation |
| **Modular Functions** | Independent functions for subtotal, discount, GST, and grand total |

---

## Repository Structure

```text
Restaurant-Billing-System/
├── codebase/
│   ├── menu.txt                # External menu items and prices
│   └── restaurant_billing.py   # Main Python 3 source code
├── documentation/
│   ├── Project_Report.pdf      # Complete academic project report
│   └── Presentation.pptx       # Project presentation slides
└── README.md                   # Project overview and usage guide
```

---

## How to Run

1. **Ensure Python 3 is installed** on your system:
   ```bash
   python --version
   ```
2. **Clone this repository:**
   ```bash
   git clone https://github.com/ayushkumardubey-art/Restaurant-Billing-System.git
   ```
3. **Navigate to the `codebase` directory:**
   ```bash
   cd Restaurant-Billing-System/codebase
   ```
4. **Execute the program:**
   ```bash
   python restaurant_billing.py
   ```

---

## Test Cases & Verification

| Scenario | Input Provided | Verified Output | Status |
| :--- | :--- | :--- | :---: |
| **Case 1: Normal Input** | `Dosa`, Quantity: `2` | `Dosa x2 added \| Amount: 160` | Pass |
| **Case 2: Boundary Input** | `Tea`, Quantity: `1` → `Generate bill` | `Subtotal: 20 \| Discount: 0.00 \| GST (5%): 1.00 \| Grand Total: 21.00` | Pass |
| **Case 3: Invalid Input** | `Pizza` / Qty: `0` / Qty: `abc` | Rejects unavailable item, zero/negative, and non-numeric quantities | Pass |
| **Case 4: Discount (> 500)** | `Thali` ×4, `Dosa` ×2, `Tea` ×2 → `Generate bill` | `Subtotal: 800 \| Discount (10%): 80.00 \| GST (5%): 36.00 \| Grand Total: 756.00` | Pass |

---

## Sample Console Output

```text
Welcome to the Restaurant Billing System!

========== RESTAURANT MENU ==========
Dosa            Rs. 80
Idli            Rs. 40
Thali           Rs. 150
Tea             Rs. 20
=====================================
Order item (or 'Generate bill'): Thali
Quantity: 4
Thali x4 added | Amount: 600
Order item (or 'Generate bill'): Dosa
Quantity: 2
Dosa x2 added | Amount: 160
Order item (or 'Generate bill'): Tea
Quantity: 2
Tea x2 added | Amount: 40
Order item (or 'Generate bill'): Generate bill

==============================================
               RESTAURANT BILL
==============================================
Thali        x4    = 600
Dosa         x2    = 160
Tea          x2    = 40
----------------------------------------------
Subtotal: 800 | Discount (10%): 80.00
GST (5%): 36.00 | Grand Total: 756.00
==============================================
          Thank you! Visit again.
==============================================
```

---

## Future Scope

- Automatically save generated receipts to a timestamped sales log (`bills_log.txt`).
- Integrate SQLite or MySQL database storage for daily sales analytics.
- Build a graphical point-of-sale (POS) interface using Tkinter or a web framework.
- Add table-wise billing, split payments, and UPI/Card payment tracking.

---

## Project & Author Information

- **Project Title:** Restaurant Billing System
- **Problem Statement:** PS No. 45
- **Subject:** Programming in Python (Session 2026–27)
- **Author:** Ayush Kumar Dubey (`RU-25-11741`)
- **Program:** Bachelor of Computer Application (Artificial Intelligence & Machine Learning)
- **Faculty Guide:** Mr. Shushant Kumar
- **Institution:** School of Information and Technology, Rungta International Skills University, Bhilai, Chhattisgarh