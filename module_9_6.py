def all_variants(text):
    for j in range(len(text)):
        for i in range(len(text)- j):
            yield text[i:i+j+1]
a = all_variants("abc")
for i in a:
    print(i)