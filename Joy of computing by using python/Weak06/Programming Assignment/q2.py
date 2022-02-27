S = input()

# ******** code to copy start ********

import string

encrypt_msg = ""
lower = string.ascii_lowercase
upper = string.ascii_uppercase

for ch in S:
    if ch in lower:
        index = lower.index(ch)
        encrypt_msg += lower[(index + 24) % 26]
    elif ch in upper:
        index = upper.index(ch)
        encrypt_msg += upper[(index + 23) % 26]
    else:
        encrypt_msg += ch

print(encrypt_msg)

# ******* code to copy end ********