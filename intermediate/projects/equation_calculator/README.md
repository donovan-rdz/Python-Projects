# Equation Calculator

A Python command-line tool that evaluates mathematical expressions and solves linear and quadratic equations.

---

## Features

- **Expression Evaluator** – Compute any math expression (supports variables)
- **Linear Equation Solver** – Solves equations of the form `ax + b = c`
- **Quadratic Equation Solver** – Solves `ax² + bx + c = 0`, including complex roots

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/donovan-rdz/Python-Projects.git
cd Python-Projects/intermediate/projects/equation-calculator

# Run the program
py main.py
```

No external dependencies required — uses Python's standard library only.

---

## Usage Examples

| Input | Output |
|-------|--------|
| `2 + 3 * x, x=5` | `17` |
| `2x + 3 = 7` | `x = 2.0` |
| `x^2 - 5x + 6 = 0` | `x₁ = 3.0, x₂ = 2.0` |
| `x^2 + 1 = 0` | `x₁ = 0 + 1i, x₂ = 0 - 1i` |

---

## Running Tests

```bash
py -m unittest discover tests
```

---

## Concepts Practiced

- OOP with classes and methods
- Regular expressions (`re` module)
- `math` module
- Error handling with `try/except`
- Unit testing with `unittest`
