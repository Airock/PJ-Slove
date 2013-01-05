myfile = open("names.txt", 'r')
st = myfile.read()
vec = st.split(',')
vec.sort()
#vec=['"A"','"B"']
idx = 0
rst = 0
for i in vec:
    idx += 1
    subtotal = 0
    for j in i[1:-1]:
        subtotal += ord(j) - ord('A') + 1
    rst += idx * subtotal
print rst
