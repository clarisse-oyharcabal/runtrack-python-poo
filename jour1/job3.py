#job3
class Operation :
    def __init__ (self,a,b):
        self.nombre1, self.nombre2 = a, b
    def addition(self):
            return(self.nombre1 + self.nombre2)
exemple = Operation (12,3)
print (f"Le resultat est : {exemple.addition()} ")