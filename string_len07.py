def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    x=""
    if len(s1)%2==1:
        x+=s1
    else: ""
    if len(s2)%2==1:
        x+=s2
    else: ""
    if len(s3)%2==1:
        x+=s3
    else: ""
    return x

print(main ("qwe", "asd", "zx"))