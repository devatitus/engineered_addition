from decimal import Decimal, InvalidOperation

# HOW TO RUN THE CODE
# 1. Install Python
# 2. Open CMD
# 3. Run: python engineered_addition.py
# 4. Enjoy the engineered Addition System :)

class NumberParserError(Exception):
    """Custom error raised when a number or word cannot be parsed."""


# -------------------------------------
# Words to Numbers Mapping
# -------------------------------------
NUM_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}


def word_to_number(word):
    """Convert words like 'twenty five' → 25"""
    try:
        parts = word.lower().split()
        total = 0
        for p in parts:
            if p not in NUM_WORDS:
                raise NumberParserError(f"Invalid number word: {word}")
            total += NUM_WORDS[p]
        return Decimal(total)
    except Exception:
        raise NumberParserError(f"Invalid number word: {word}")


# -------------------------------------
# Number Parser
# -------------------------------------
def parse_number(value):
    """
    Convert input to Decimal.
    Accepts int, float, numeric string.
    """
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise NumberParserError(f"Invalid number: {value}")


# -------------------------------------
# READ VALUES FROM FILE (Option 3)
# -------------------------------------
def read_file_values(filename):
    values = []
    try:
        with open(filename, "r") as f:
            for line in f:
                raw = line.strip()

                if not raw:  
                    continue  # skip empty lines

                try:
                    # Try number parsing
                    num = parse_number(raw)
                    values.append(num)
                except NumberParserError:
                    # Try word parsing
                    try:
                        num = word_to_number(raw)
                        values.append(num)
                    except NumberParserError:
                        print(f"[SKIPPED INVALID] {raw}")
                        continue

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return None

    return values


# -------------------------------------
# Core Addition Function
# -------------------------------------
def add_numbers(numbers):
    total = Decimal(0)
    for num in numbers:
        total += num
    return total


# -------------------------------------
# Manual Input (Option 1 & 2)
# -------------------------------------
def get_user_values(limit, mode):
    values = []

    for i in range(limit):
        user_input = input(f"Enter value {i+1}: ")

        try:
            if mode == 1:
                values.append(parse_number(user_input))
            else:
                values.append(word_to_number(user_input))

        except NumberParserError as e:
            print(f"[ERROR] {e}")
            return None

    return values


# -------------------------------------
# MAIN
# -------------------------------------
if __name__ == "__main__":
    print("=== Engineered Addition System ===")
    print("1. Enter Numbers Manually")
    print("2. Enter Words Manually")
    print("3. Read Values from File")

    try:
        mode = int(input("Choose option (1 / 2 / 3): "))
        if mode not in [1, 2, 3]:
            raise ValueError("Invalid option.")
    except ValueError:
        print("[ERROR] Please choose 1, 2, or 3.")
        exit(1)

    # Option 3 → Read from file
    if mode == 3:
        filename = input("Enter file name (e.g., values.txt): ")
        values = read_file_values(filename)

        if values:
            total = add_numbers(values)
            print("\nValid Values Count:", len(values))
            print("Total Sum =", float(total))
        exit(0)

    # For Option 1 & 2
    try:
        limit = int(input("How many inputs? "))
        if limit <= 0:
            raise ValueError("Limit must be positive.")
    except ValueError:
        print("[ERROR] Enter valid number for limit.")
        exit(1)

    values = get_user_values(limit, mode)

    if values is not None:
        total = add_numbers(values)
        print("\nValues:", values)
        print("Total =", float(total))
