def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def main():
    decimal = int(input("Masukkan bilangan desimal: "))
    print("Bilangan biner:", decimal_to_binary(decimal))
    print("Bilangan oktal:", decimal_to_octal(decimal))
    print("Bilangan heksadesimal:", decimal_to_hexadecimal(decimal))

if __name__ == "__main__":
    main()
