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
    m = '['
    if len(s1)%2!=0:
        m+=s1
    else:
        m='['
    if len(s2)%2!=0 and len(s1)%2!=0:
        m+=f', {s2}'
    elif len(s2)%2!=0:
        m+=s2
    else:
        m='['
    if len(s3)%2!=0 and (len(s1)%2!=0 or len(s2)%2!=0):
        m+=f', {s3}'
    elif len(s3)%2!=0:
        m+=s3
    else:
        m='['

    m+=']'
    return m 
print(main('5123','45','456'))
