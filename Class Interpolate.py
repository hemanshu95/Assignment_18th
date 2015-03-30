import matplotlib.pyplot as plt
class Interpolate:
    
    def solve(self,L,M,xlower,xupper,method):
        if(method=="newton"):
            return (self.Newton(L,M,xlower,xupper))
        else:
            return (self.Lagrange(L,M,xlower,xupper))
    
    def plotgraph(self,y_values, xlower, xupper) :
        def drange(start, stop, step):
            r = start
            while r < stop:
                yield r
                r += step
        from numpy.polynomial import polynomial as P 
        i0=drange(xlower, xupper, 0.1)
        x=[]
        for xd in i0 :
            x.append(xd)
        y=[]
        for x_val in x :
            y.append(P.polyval(x_val, y_values))
        
        plt.plot(x, y,)
        plt.xlabel('values of x')
        plt.ylabel('values of p(x)')
        plt.show()

    def Lagrange(self,L,M,xlower,xupper):                                                
        
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                        
        w=(-1*L[0],1)                                                      
        for i in range(1,n):
            w=P.polymul(w,(-1*L[i],1))                                    
        result=array([0.0 for i in range(len(w)-1)])                    
        derivative=P.polyder(w)                                             
        for i in range(n):
            y_values=(P.polydiv(w,(-1*L[i],1))[0]*M[i])/P.polyval(L[i],derivative)
            self.plotgraph(y_values, xlower, xupper)
            result+=(P.polydiv(w,(-1*L[i],1))[0]*M[i])/P.polyval(L[i],derivative)   
        return(list(result))                                                
    def Newton(self,L,M):                                                   
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=M[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(L[j+i]-L[j])
        result=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*L[0],1)                                               
                                                                            
            for j in range(1,i):
                prod=P.polymul(prod,(-1*L[j],1))                              
            result=P.polyadd(result,array(prod)*mat[0][i])                  
        return (list(result))         
L=[-9,-4,-1,7]

M=[5,2,-2,9]
plt.plot(L,M,'ro')
plt.plot([min(L)-2,max(L)+2],[0,0],'k-')
plt.plot([0,0],[min(M)-2,max(M)+2],'k-')
xlower=int(input('Enter the lower range of x to be plotted:'))
xupper=int(input('Enter the upper range of x to be plotted:'))
method=input('Enter the method - newton/lagrange:')
apx = Interpolate()
l=apx.solve(L,M,xlower,xupper,method)
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
from numpy.polynomial import polynomial as P 
i0=drange(xlower, xupper, 0.1)
x=[]
for xd in i0 :
    x.append(xd)
y=[]
for x_val in x :
    y.append(P.polyval(x_val, l))
import matplotlib.pyplot as plt
plt.plot(x, y,'k',linewidth='3')
plt.xlabel('values of x')
plt.ylabel('values of p(x)')
plt.show()


