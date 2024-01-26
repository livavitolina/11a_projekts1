saraksts = [float(sk) if '.' in sk else int(sk) for sk in input("Ievadi skaitļus, atdalot tos ar atstarpi (Decimālskaitļus jāievada ar punktu!): ").split()]
dublikati = False

for i in range(len(saraksts)-1):
	if saraksts[i] == saraksts[i + 1]: 
		dublikati = True
		print(saraksts[i], saraksts[i + 1])

if not dublikati:
	print("Netika atrastas vienādas vērtības!")