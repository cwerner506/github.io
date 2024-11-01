test_list = ["hello", "racecar", "world"]
palindromes = []

for i in range(len(test_list)):
    x = list(test_list[i])
    x.reverse()
    rev_str = ''.join(x)
    if test_list[i] == rev_str:
        palindromes.append(test_list[i])
print(palindromes)