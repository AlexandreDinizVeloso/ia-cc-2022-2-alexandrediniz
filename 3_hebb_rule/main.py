entry = []
archive = open('num.txt', 'r')

for line in archive:
    vector_entry = line.split(',')
    entry.append(vector_entry)

w = []

for i in range(len(entry[0]) - 1):
    w.append(0)

outp = []

for i in range(len(entry)):
    outp.append(entry[i][len(entry[i]) - 1])

for i in range(len(entry)):
    x = []
    
    for j in range(len(entry[i]) - 1):
        x.append(entry[i][j])
        y = outp[i]
        w[j] = w[j] + (int(x[j]) * int(y))

    print('\nAs entradas são: ', x, 'As saidas são: ', outp[i], 'Os pesos são', w)
