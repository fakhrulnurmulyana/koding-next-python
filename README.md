# Price Calculator

A simple price calculator built with Python and CustomTkinter.

The application calculates the final price based on:

* Price
* Quantity
* Discount (%)

## Requirements

* Python 3
* CustomTkinter

Install CustomTkinter with:

```bash
pip install customtkinter
```
and if you use uv, you can run 

```bash
uv run python -m koding_next_python.main
```

## How to Run

Run the application as a Python module from the project directory:

```bash
python -m pricing.main
```
and if you use uv, you can run with

```bash
uv run python -m koding_next_python.main
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
