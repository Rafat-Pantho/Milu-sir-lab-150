for i in range(int(input())):
    n, k = map(int, input().split())

    base_string = ''.join(chr(97 + i) for i in range(k))

    # Repeat the base string until length n is reached
    result_string = (base_string * (n // k)) + base_string[:n % k]
    
    print(result_string)