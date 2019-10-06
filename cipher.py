letters = input()
symbols = input()

dict_ls = {}
dict_sl = {}

for i in range(len(letters)):
    dict_ls[letters[i]] = symbols[i]
    dict_sl[symbols[i]] = letters[i]

text = list(input())
cipher = list(input())

res_text = []
for let in text:
    if let in dict_ls:
        res_text.append(dict_ls[let])
    else:
        res_text.append(let)
text = ''.join(res_text)
print(text)

res_cipher = []
for sym in cipher:
    if sym in dict_sl:
        res_cipher.append(dict_sl[sym])
    else:
        res_cipher.append(sym)
cipher = ''.join(res_cipher)
print(cipher)