class Person:
    def __init__(self, name: str, surname: str, date_birth: tuple):
        self._name = name
        self._surname = surname
        self._date_birth = date_birth

    def age(self, curr_date):
        age = curr_date[2] - self._date_birth[2]

        if self._date_birth[1] > curr_date[1] or (curr_date[1] == self._date_birth[1] and self._date_birth[0] > curr_date[0]):
            age -= 1 

        return age 

    def describe(self):
        return f"Nome: {self._name}\nSurname: {self._surname}\nAge: {self._date_birth}"
    
def main():
    persone = []

    for i in range(3):
        nome = input(f"Inserisci nome persona numero {i + 1}: ")
        cognome = input(f"Inserisci cognome persona numero {i + 1}: ")
        data = tuple([int (x) for x in input(f"Inserisci data nascita in formato gg/mm/aaaa: ").split("/")])
        persone.append(Person(nome, cognome, data))

    print("-------------------------------------------------------")
    while True:
        curr_date = input(f"Inserisci data corrente in formato gg/mm/aaaa: ")
        if not curr_date:
            break
        
        curr_date = tuple([int (x) for x in curr_date.split("/")])

        for p in persone:
            if p.age(curr_date) >= 18:
                print(p.describe())        

if __name__ == "__main__":  
    main()