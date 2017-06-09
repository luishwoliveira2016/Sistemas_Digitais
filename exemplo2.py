class analisadorLexico():


	def ehVariavel(self, palavra, palavra1):
		if(palavra == "inteiro"):
			return palavra1
		else:
			return False	

	def ehNumero(self, palavra):
		try: 
			palavra = int(palavra)
			return palavra
		except ValueError:	
			return False

	def ehPrint(self, palavra):
		if(palavra == "imprimir"):
			return "print"
		else:
			return False

	def ehIgual(self, palavra):
		if(palavra == "="):
			return "="
		else:
			return False

	def analisa(self):
		entrada = open("inteiro.txt", "r")
		codigo = entrada.read()
		lista = codigo.split()
		saida = open("saida.py", "w")
		linhaCode = ""
		codeOpt = ""
		print(lista)

		for i in range(0, len(lista)-1):
			print ("lc", i, linhaCode)
			if(self.ehVariavel(lista[i], lista[i+1])):
				linhaCode = self.ehVariavel(lista[i], lista[i+1])
			elif(self.ehNumero(lista[i])):
				linhaCode = lista[i]
			elif(self.ehPrint(lista[i])):
				linhaCode = self.ehPrint(lista[i])
			elif(self.ehIgual(lista[i])):
				linhaCode = self.ehIgual(lista[i])
			else:
				linhaCode = ""
			codeOpt += linhaCode + "\n"

		saida.write(codeOpt)
		entrada.close()
		saida.close()


teste = analisadorLexico()
teste.analisa()