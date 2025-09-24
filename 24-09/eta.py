data_nascita = input("inserisci data nascita formato gg/mm/aaaa: ")
oggi = input("inserisci data di oggi formato gg/mm/aaaa: ")

gn, mn, an = [int(i) for i in data_nascita.split("/")]
go, mo, ao = [int(i) for i in oggi.split("/")]

eta = ao - an

if mn > mo or (mn == mo and gn > go):
    eta -= 1 

print(eta)