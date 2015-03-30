class Interpolate:
    
    def solve(self,A,B,method):
        if(method=="newton"):
            return (self.Newton(A,B))
        else:
            return (self.Lagrange(A,B))
    
    def Lagrange(self,A,B):                                                
       
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(A)                                                           
        w=(-1*A[0],1)                                                      
        for i in range(1,n):
            w=P.polymul(w,(-1*A[i],1))                                    
        result=array([0.0 for i in range(len(w)-1)])                    
        derivative=P.polyder(w)                                             
        for i in range(n):
            result+=(P.polydiv(w,(-1*A[i],1))[0]*B[i])/P.polyval(A[i],derivative)   
        return(list(result)) 
        
    def Newton(self,A,B):                                                   
       
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(A)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=B[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(A[j+i]-A[j])
        res=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*A[0],1)                                               

            for j in range(1,i):
                prod=P.polymul(prod,(-1*A[j],1))                              
            res=P.polyadd(res,array(prod)*mat[0][i])                  
        return (list(res))
    def graph_plot(self,x_values,y_values):
        import numpy as np
        import matplotlib.pyplot as plt
        L=self.solve(x_values,y_values,"lagrange")
        n=len(x_values)
        def F(x):
            k=0
            for i in range(n):
                k+=L[i]*(x**i)
            return k
        a=float(input("Enter lower limit of x in graph : "))
        b=float(input("Enter upper limit of x in graph : "))
        c=float(input("Enter lower limit of y in graph : "))
        d=float(input("Enter upper limit of y in graph : "))
        x=np.arange(a,b,0.001)
        y=[F(i) for i in x]        
        plt.plot([0,0],[max(d,np.max(y)),min(c,np.min(y))],'b',[np.max(x),np.min(x)],[0,0],'b')
        
        
        plt.plot(x,y,'k')
        plt.plot(x_values,y_values,'ro')
        
        for i in range(len(x_values)):
            plt.text(x_values[i],y_values[i],"  ({},{}) ".format(x_values[i],y_values[i]))        
        plt.show()


apx=Interpolate()                                                          
for method in ["newton","lagrange"]:
    sol=apx.solve([1,2,3],[0,-1,0],method)
    print(sol)
apx.graph_plot([1,2,3],[0,-1,0])
               
    

   
