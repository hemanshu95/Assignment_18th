class PolynomialSolver:
    def F(self,n,L,val):
        k=0
        for i in range(n+1):
            k+=L[i]*(val**i)
        return k
    def fd(self,n,L,val):
        k=0
        for i in range(1,n+1):
            k+=i*L[i]*(val**(i-1))
        return k
    def solver(self,n,L,method):
        if(method=='bisection'):
            print("Enter lower bound of interval containing the root")
            l=int(input())
            print("Enter upper bound of interval containing the root")
            u=int(input())
            print("Enter maximum itertions")
            q=int(input())
            while(abs(self.F(n,L,l)-self.F(n,L,u))>0.00001 and q>0):
                m=(l+u)/2
                if(self.F(n,L,l)*self.F(n,L,m)<0):
                    u=m
                else:
                    l=m
                print (l,u,self.F(n,L,l),self.F(n,L,u))
                q-=1
            return([l,u])
        if(method=='secant'):
            print("Enter lower bound of interval containing the root")
            l=float(input())
            print("Enter upper bound of interval containing the root")
            u=float(input())
            print("Enter maximum itertions")
            q=int(input())
            while(abs(self.F(n,L,l))>0.00001 and q>0):
                f1=self.F(n,L,l)
                f2=self.F(n,L,u)
                l,u=u,u-(((u-l)*f2)/(f2-f1))
                print (l,u,f1,f2)
                q-=1
            return(l)
        if(method=='secantRF'):
            print("Enter lower bound of interval containing the root")
            l=int(input())
            print("Enter upper bound of interval containing the root")
            u=int(input())
            m=l
            print("Enter maximum itertions")
            q=int(input())
            while(abs(self.F(n,L,m))>0.00001 and q>0):
                f1=self.F(n,L,l)
                f2=self.F(n,L,u)
                m=u-(((u-l)*f2)/(f2-f1))
                rp=self.F(n,L,m)
                if(f1*rp<0):
                    u=m
                else:
                    l=m
                print (m)
                q-=1
            return(l)
        if(method=='newtonraphson'):
            print("Enter lower bound of interval containing the root")
            l=int(input())
            print("Enter maximum itertions")
            q=int(input())
            while(abs(self.F(n,L,l))>0.00001 and q>0):
                l=l-self.F(n,L,l)/self.fd(n,L,l)
            return(l)
        else:
            return NULL
    def graph_plot(self,n,L):
        import numpy as np
        import matplotlib.pyplot as plt
        l=float(input("Enter lower bound of interval containing the root : "))
        u=float(input("Enter upper bound of interval containing the root : "))
        E=float(input("Enter the value of E(epsilon) : "))
        x=np.arange(l-1,u+1,E)
        y=[self.F(n,L,i) for i in x]
        plt.plot([0,0],[np.max(y),np.min(y)],'b',[np.max(x),np.min(x)],[0,0],'b')        
        plt.plot(x,y,'k')        
        plt.plot([u,u],[0,self.F(n,L,u)],'g--')
        
        plt.plot(u,self.F(n,L,u),'ro')
        
        plt.plot([l,l],[0,self.F(n,L,l)],'g--')
        plt.plot(l,self.F(n,L,l),'ro')        
        m=(u+l)/2
        while(u-l>E):
            print([u,m,l])
            m=(u+l)/2

            if self.F(n,L,u)*self.F(n,L,m)<0:
                l=m
            elif self.F(n,L,u)*self.F(n,L,m)>0:
                u=m
            else:
                if self.F(n,L,m)==0:
                    l=m
                    u=m
                elif self.F(n,L,u)==0:
                    l=u
                    m=u
                else:
                    m=l
                    u=l
            
            plt.plot([m,m],[0,self.F(n,L,m)],'g--')
            plt.plot(m,self.F(n,L,m),'ro')
        #print([u,m,l])
        #print(u,m,l,self.F(n,L,m))
        plt.plot(m,self.F(n,L,m),'yo')
        plt.xlabel(" X-Axis ")
        plt.ylabel(" Y-Axis ")
        plt.show()

sol=PolynomialSolver()
sol.graph_plot(3,[-1,0,0,1])##for x^3-1 equation

