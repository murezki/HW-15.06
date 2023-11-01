def align_strings(strings):
    max_len = max(len(s) for s in strings)
    aligned_strings = [s.rjust(max_len, "*") for s in strings]
    return aligned_strings


leee = input().split()
result = align_strings(leee)
print(" ".join(result))



