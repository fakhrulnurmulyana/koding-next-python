# Price Calculator

A simple price calculator built with Python and CustomTkinter.

The application calculates the final price based on:

* Price
* Quantity
* Discount (%)

## Project Structure

```text
pricing/
├── main.py
├── gui.py
└── pricing.py
```

### `pricing.py`

Contains the calculation logic.

```python
def calculate(price, discount, quantity):
    total = price * quantity
    discount_amount = total * discount / 100
    final_price = total - discount_amount

    return final_price
```

### `gui.py`

Contains the graphical user interface (GUI) using CustomTkinter.

The user enters the price, quantity, and discount, then clicks **Calculate** to see the final price.

### `main.py`

Runs the application.

## Requirements

* Python 3
* CustomTkinter

Install CustomTkinter with:

```bash
pip install customtkinter
```

## How to Run

Run the application as a Python module from the project directory:

```bash
python -m pricing.main
```

## Example

If:

```text
Price     = 100000
Quantity  = 2
Discount  = 10%
```

The calculation is:

```text
Total           = 100000 × 2 = 200000
Discount        = 10% × 200000 = 20000
Final Price     = 200000 - 20000 = 180000
```

The application will display:

```text
Final Price: Rp. 180000
```
