def separate_even_odd(numbers):
    """
    Return a dictionary with keys 'even' and 'odd' containing lists of even and odd integers.
    Preserves the original order.
    """
    
    if numbers is None:
        return {"even": [], "odd": []}
    
    evens = []
    odds = []

    for n in numbers:
        try:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        except TypeError:
            # Skip non-integer values
            continue
    return { "even": evens, "odd": odds }

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print(separate_even_odd(sample))
