def per16(n):
    res = ''
    while n > 0:
        res += str(n % 16)
        n //= 16
    return int(res[::-1])