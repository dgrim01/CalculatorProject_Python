def calc(operation, a=None, b=None):

    try:
        # Check if 'a' is a valid number
        if a is not None and not isinstance(a, (int, float)):
            raise ValueError(f'Invalid number "{a}"')

        # Check if 'b' is a valid number
        if b is not None and not isinstance(b, (int, float)):
            raise ValueError(f'Invalid number "{b}"')

        if operation == "+" or operation == "add":
            return a if b is None else a + b
        elif operation == "*" or operation == "mul":
            return a if b is None else a * b
        elif operation == "/" or operation == "div":
            if b is None:
                return a
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return a / b
        elif operation == "-" or operation == "sub":
            return -a if b is None else a - b
        elif operation == "%" or operation == "mod":
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a if b is None else a % b
        elif operation == "^" or operation == "pow":
            return a if b is None else a ** b
        else:
            raise Exception(f'Invalid operator "{operation}" ')

    except ValueError as ve:
        return f"{str(ve)}"
    except ZeroDivisionError as zde:
        return f"{str(zde)}"
    except Exception as e:
        return f"{str(e)}"


# Evaluate each expression
def eval(expression):
    try:

        if not isinstance(expression, list):
            return f'Failed to evaluate "{expression}"'
        if len(expression) < 1 or len(expression) > 3:
            return f'Failed to evaluate "{expression}"'

        op = expression[0]
        a = expression[1] if len(expression) > 1 else None
        b = expression[2] if len(expression) > 2 else None

        if isinstance(a, list):
            a = eval(a)
        if isinstance(b, list):
            b = eval(b)

        return calc(op, a, b)
    except IndexError:
        return "Error: Expression is incomplete"
    except Exception as e:
        return f"Error: {e}"
