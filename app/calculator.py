class Calculator(object):
 
    def add(self, x, y):
        return x + y

    def divide(self, x, y):
    	if y == 0:
			raise Exception("Divisao por zero nao permitida!")		

        return x / y



