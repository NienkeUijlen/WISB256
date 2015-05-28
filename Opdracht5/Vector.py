class Vector:
    
    """ Vector in R^n
    eigenschappen : dimensie(int), scalairen(int)     """
    
    __slots__ = ('_dimensie','lijst')
    
    def __init__(self,n,scalair=0):
        self._dimensie = n
        if type(scalair)==int or type(scalair)==float:
            self.lijst = n*[scalair]
        else:
            self.lijst=list(scalair)

    def __str__(self):
        vector=str()
        for i in range(self._dimensie):
            vector += str(self.lijst[i]) + "\n" 
        return(vector)
    
    def lincomb(self,other,alpha,beta):
        w = Vector(other._dimensie)
        w.lijst = []
        for i in range(w._dimensie):
            w.lijst.append(float(alpha)*float(self.lijst[i])+float(beta)*float(other.lijst[i]))
        return(w)
    
    def scalar(self,alpha):
        w = self.lincomb(self,alpha,0)
        return(w)
    
#    def scalar(self,alpha):
#        w = Vector(self._dimensie)
#        w.lijst = []
#        for i in range(w._dimensie):
#            w.lijst.append(float(alpha)*float(self.lijst[i]))
#        return(w)
        
    def inner(self,other):
        w = []
        for i in range(self._dimensie):
            w.append(float(self.lijst[i])*float(other.lijst[i]))
        while len(w)>1:
            w[0]=w[0]+w[1]
            del(w[1])
        return(w[0])
        
#    def norm(self):
#        w = Vector(1)
#        w.lijst = []
#        for i in range(self._dimensie):
#            w.lijst.append(float(self.lijst[i])*float(self.lijst[i]))
#        while len(w.lijst)>1:
#            w.lijst[0]=w.lijst[0]+w.lijst[1]
#            del(w.lijst[1])
#        if len(w.lijst)==1:
#            w.lijst[0]=int(w.lijst[0])**0.5
#        return(w)
    
    
    def norm(self):
        w = self.inner(self)
        z = w**0.5
        return(z)