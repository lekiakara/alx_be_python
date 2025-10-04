# robust_division_calculator.py

def safe_divide(numerator, denominator):
    
    try:
        # Try converting inputs to float
        num = (numerator)
        den = (denominator)

        # Try dividing
        result = num / den
        return f"Result: {result}"   # formatted to 2 decimal places

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Non-numeric input provided."
  
   