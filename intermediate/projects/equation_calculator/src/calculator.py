"""
calculator.py
Core logic for evaluating expressions and solving equations.
"""

import re
import math


class EquationCalculator:
    """Handles evaluation of expressions and solving of equations."""

    # ------------------------------------------------------------------
    # Expression evaluator
    # ------------------------------------------------------------------
    def evaluate(self, expression: str) -> dict:
        """
        Evaluate a mathematical expression.
        Supports variables declared inline, e.g. '2 + 3 * x, x=5'.

        Returns a dict with 'success', 'result', and optional 'error'.
        """
        try:
            # Split expression and variable assignments  e.g. "2*x + 1, x=3"
            parts = [p.strip() for p in expression.split(",")]
            expr = parts[0]
            variables = {}

            for part in parts[1:]:
                if "=" in part:
                    var, val = part.split("=")
                    variables[var.strip()] = float(val.strip())

            # Replace ^ with ** for Python exponentiation
            expr = expr.replace("^", "**")

            # Safe evaluation context
            safe_env = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
            safe_env.update(variables)

            result = eval(expr, {"__builtins__": {}}, safe_env)  # noqa: S307
            return {"success": True, "result": result}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    # ------------------------------------------------------------------
    # Linear equation solver  (ax + b = c  →  x = (c - b) / a)
    # ------------------------------------------------------------------
    def solve_linear(self, equation: str) -> dict:
        """
        Solve a linear equation of the form: ax + b = c
        Example input: '2x + 3 = 7'

        Returns a dict with 'success', 'result', and optional 'error'.
        """
        try:
            equation = equation.replace(" ", "").replace("^1", "")
            if "=" not in equation:
                return {"success": False, "error": "Equation must contain '='"}

            lhs, rhs = equation.split("=")
            rhs_val = float(rhs)

            # Parse terms on the left side: coefficients of x and constant
            # Matches patterns like: 2x, -x, +3, -5, x
            pattern = r"([+-]?\d*\.?\d*)[xX]|([+-]?\d+\.?\d*)"
            matches = re.findall(pattern, lhs)

            a = 0.0  # coefficient of x
            b = 0.0  # constant term

            for x_coeff, const in matches:
                if x_coeff:
                    coeff = x_coeff.replace("+", "") or "1"
                    coeff = "-1" if coeff == "-" else coeff
                    a += float(coeff)
                elif const:
                    b += float(const)

            if a == 0:
                return {"success": False, "error": "No variable found in equation."}

            x = (rhs_val - b) / a
            return {"success": True, "result": f"x = {x}"}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    # ------------------------------------------------------------------
    # Quadratic equation solver  (ax² + bx + c = 0)
    # ------------------------------------------------------------------
    def solve_quadratic(self, equation: str) -> dict:
        """
        Solve a quadratic equation of the form: ax^2 + bx + c = 0
        Example input: 'x^2 - 5x + 6 = 0'

        Returns a dict with 'success', 'result', and optional 'error'.
        """
        try:
            equation = equation.replace(" ", "")
            if "=" not in equation:
                return {"success": False, "error": "Equation must contain '='"}

            lhs, rhs = equation.split("=")
            rhs_val = float(rhs)

            def _parse_coeff(text: str) -> float:
                """Return numeric coefficient; '' or '+' → 1, '-' → -1."""
                text = text.replace("+", "").strip()
                if text in ("", ):
                    return 1.0
                if text == "-":
                    return -1.0
                return float(text)

            # --- coefficient of x^2 ---
            a = 0.0
            for m in re.finditer(r"([+-]?\d*\.?\d*)[xX]\^2", lhs):
                a += _parse_coeff(m.group(1))

            # --- coefficient of x (not followed by ^) ---
            b = 0.0
            for m in re.finditer(r"([+-]?\d*\.?\d*)[xX](?!\^)", lhs):
                b += _parse_coeff(m.group(1))

            # --- constant term: digits NOT preceded or followed by x/X ---
            c = 0.0
            for m in re.finditer(r"(?<![xX\d\^])([+-]?\d+\.?\d*)(?![xX\d\^])", lhs):
                c += float(m.group(1))
            c -= rhs_val

            if a == 0:
                return {"success": False, "error": "Coefficient 'a' is 0; not a quadratic equation."}

            discriminant = b**2 - 4 * a * c

            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                return {"success": True, "result": f"x₁ = {x1:.4f}, x₂ = {x2:.4f}"}
            elif discriminant == 0:
                x = -b / (2 * a)
                return {"success": True, "result": f"x = {x:.4f} (double root)"}
            else:
                real = -b / (2 * a)
                imag = math.sqrt(-discriminant) / (2 * a)
                return {
                    "success": True,
                    "result": f"x₁ = {real:.4f} + {imag:.4f}i, x₂ = {real:.4f} - {imag:.4f}i (complex roots)",
                }
        except Exception as exc:
            return {"success": False, "error": str(exc)}
