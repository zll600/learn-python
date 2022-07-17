def bin_to_dec(bin_str: str) -> int:
    """
    Convert binary string to decimal number
    >>> bin_to_dec("0101")
    5
    >>> bin_to_dec("1010")
    10
    >>> bin_to_dec("0")
    0
    >>> bin_to_dec("-0101")
    -5
    >>> bin_to_dec("abc")
    Traceback (most recent call last):
    ...
    ValueError: Non-binary value was passed to the function.
    >>> bin_to_dec(" ")
    Traceback (most recent call last):
    ...
    ValueError: Empty binary string was passed to the function.
    """

    bin_str = str(bin_str).strip()
    if not bin_str:
        raise ValueError("Empty binary string was passed to the function.")
    negative_number = bin_str[0] == '-'
    if negative_number:
        bin_str = bin_str[1:]
    if not all(ch in "01" for ch in bin_str):
        raise ValueError("Non-binary value was passed to the function.")

    decimal_number = 0
    for ch in bin_str:
        decimal_number = 2 * decimal_number + int(ch)

    if negative_number:
        decimal_number *= -1
    return decimal_number
    
if __name__=="__main__":
    import doctest

    doctest.testmod()
