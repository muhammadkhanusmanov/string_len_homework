def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s)%2==0:
        i = len(s)//2
        m = s[i]+s[i+1]
    else:
        i = (len(s)+1)//2
        m = s[i]
    return m 
