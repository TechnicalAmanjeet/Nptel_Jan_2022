
original_msg = "hii gus How re you I hope you re doing good"
shift = 1

def encode_msg(original_msg, shift):
    encoded_msg = []
    for i in range(len(original_msg)):
        if original_msg[i] != " ":
            encoded_msg.append(chr((ord(original_msg[i]) + shift) % 256))
    print(encoded_msg)
    return "".join(encoded_msg)

def decode_msg(encoded_msg, shift):
    decoded_msg = []
    for i in range(len(encoded_msg)):
        if encoded_msg[i] != " ":
            decoded_msg.append( chr(ord(encoded_msg[i]) - shift) % 256)
    print(decoded_msg)
    return "".join(decoded_msg)


encoded_msg = encode_msg(original_msg, shift)
print(encoded_msg)
decoded_msg = decode_msg(encoded_msg, shift)
