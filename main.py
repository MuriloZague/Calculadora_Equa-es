def resolver_equacao(a, b, c):

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2*a)
        x2 = (-b - delta ** 0.5) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return "Nao existe raiz real"

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))
  
print(resolver_equacao(a, b, c))
