def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    if s[0:-1:1]==s[-1:0:-1]:
        return True
    else: return False


print (main ("aka"))