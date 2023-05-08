# 48
def e_48():
    # Variaveis
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    seq = [a]
    i = 0

    # Codigo
    while max(seq) < b:
        p4 = seq[i]+4
        m2 = seq[i]-2
        if i % 2 == 0 and p4 < b:
            seq.append(p4)
            i += 1
        elif i % 2 != 0 and m2 < b:
            seq.append(m2)
            i += 1
        else:
            return seq


def e_49():
    num = int(input('Digite o valor: '))
    div = []
    for i in range(1, num+1):
        if (num % i) == 0:
            div.append(i)
    print(sum(div))