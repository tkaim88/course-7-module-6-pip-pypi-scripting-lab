from datetime import datetime
import os


def generate_log(data):
    # STEP 1: Validate input
    # Ensure the provided data is a list
    if not isinstance(data, list):
        raise ValueError("log_data must be a list")

    # STEP 2: Generate a filename with today's date
    # Example: log_20260613.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to the file
    # Each entry is written on its own line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return filename so tests can verify it
    return filename