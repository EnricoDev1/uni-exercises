def sum_digits(n):
    if n <= 10:
        return n
    
    sum = n % 10 + sum_digits(n // 10)
    
    if sum > 10:
        return sum % 10 + sum_digits(sum // 10)
    else:
        return n % 10 + sum_digits(n // 10)

def main():
    print(sum_digits(int(input("Inserisci un numero intero: "))))

if __name__ == "__main__":
    main()