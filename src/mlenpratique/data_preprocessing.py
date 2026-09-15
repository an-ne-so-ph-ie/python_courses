
def peek(name, n=5, width=160):
    """Print the first raw lines of a text file, separators visible."""
    with open(name, encoding="utf-8") as f:
        for _ in range(n):
            print(repr(f.readline()[:width]))