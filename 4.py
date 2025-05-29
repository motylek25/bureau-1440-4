def f(n):
    reversed_str = str(n)[::-1]
    reversed_num = int(reversed_str)
    return reversed_num
def g(n):
    return f(f(n)) / n
def uniq_g_values():
    uniq_values = set() 
    for n in range(2, 1030):
        if '0' in str(n)[:-1]:  
            continue
        g_n = g(n)
        uniq_values.add(g_n)   
    return len(uniq_values)

result = uniq_g_values()
print(result)  