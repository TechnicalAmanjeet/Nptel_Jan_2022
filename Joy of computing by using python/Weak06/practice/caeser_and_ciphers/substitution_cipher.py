import string

encode_key_dict = {}

for i in range(len(string.ascii_letters)):
    encode_key_dict[string.ascii_letters[i]] = string.ascii_letters[i - 5]
print(encode_key_dict)

with open("text_msg.txt", 'r') as file:
    encoded_msg = []
    for line in file.readlines():
        for member in line:
            if member in string.ascii_letters:
                encoded_msg.append(encode_key_dict[member])
            else:
                encoded_msg.append(member)
        print(line)
        print("".join(encoded_msg))
    print(encoded_msg)

with open("encoded_msg.txt", 'w') as file:
    file.write("".join(encoded_msg))
