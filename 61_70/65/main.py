import traceback

try:
    1 / 0  # Causes ZeroDivisionError
except Exception:
    error_trace = traceback.format_exc()  # Get the full error traceback as a string
    print("Captured Traceback:\n", error_trace)

    traceback.print_exc()  # Prints the full traceback