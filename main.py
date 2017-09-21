def calcolo(x,y,op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y

print("Ciao! Calcolatrice davvero poco furba 1.0 XD\n ")

val1 = input("Primo valore: ")
val1 = int(val1)
val2 = input("Secondo valore: ")
val2 = int(val2)
operazione = input("Operazione(+ - * /): ")

risultato =calcolo(val1,val2,operazione)
print(risultato)

