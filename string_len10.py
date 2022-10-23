def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    a = s[-1]+s[-2]+s[-3]
    if s==a:
        m = True
    else:
        m = False
    return m 