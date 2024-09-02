def inverte_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Entrada do usuário
string = input("Informe a string a ser invertida: ")

# Invertendo a string
resultado = inverte_string(string)

print(f"String invertida: {resultado}")