train = []
archive = open('num.txt', 'r')

for line in archive:
    vector_num = line.split(',')
    train.append(vector_num)

w = []

for i in range(len(train[0])-1):
    w.append(0)

exp_outp = []

for i in range(len(train)):
    exp_outp.append(train[i][len(train[i])-1])

w = [0,0,0]
a = 1
t = 0
test = 0
epoch = 0
training = True

while(training):
        epoch += 1
        test = 0
      
        for i in range(len(train)):
            summ = 0
            summ += int(w[2])
            
            for j in range(len(train[i])-1):
                summ += int(train[i][j]) * int(w[j])

            if(summ > t):
                y = 1
            elif((summ >= -t) and (summ <= t)):
                y = 0
            elif(summ < -t):
                y = -1

            if(int(exp_outp[i]) == y):
                test += 1
                if test == 1:
                    training = False
            else:
                leng = len(w)
                for j in range(leng):
                    if j == 2:
                        w[j] = int(w[j]) + (a * int(exp_outp[i]))
                    else:
                        w[j] = int(w[j]) + (a * int(exp_outp[i]) * int(train[i][j]))
            print('\nAs entradas são: ',train[i],'As saídas são: ',exp_output[i],'Os pesos são: ',w)
        epoch += 1
        print('Número de epocas é igual a: '+str(epoch))
