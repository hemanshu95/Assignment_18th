__author__ = 'hemanshu'
import numpy as np
import matplotlib.pyplot as plt
class LPsolver:
    def __init__(self):
        self.x=None
        self.a=None
        self.b=None
        self.c=None
        self.n=None
        self.m=None
        self.B=None
        self.S=None
        self.maxpos=None
        self.minpos=None
        self.BC=None

    def init_the_table(self,objective,constraints_value,constraints):
        self.x=np.array([0]*10,float)
        self.a=np.array(objective,float)
        self.b=np.array(constraints_value,float)
        self.c=np.array(constraints,float)
        self.n=np.size(self.a)
        self.m=np.size(self.b)
        self.B=np.array([0]*self.m,float)
        self.S=np.array([[0]*self.m]*self.m,float)
        for i in range(self.m):
            self.S[i][i]=1
        self.maxpos=np.array([0]*(self.m+self.n),float)
        self.minpos=np.array([0]*self.m,float)
        self.BC=np.array([0]*self.m,float)
        for i in range(self.m):
            self.BC[i]=i+self.n


    def solve(self,option, objective,constraints_value, constraints):
        self.init_the_table(objective,constraints_value,constraints)
        
        flag=0
        final_sum=0
        while flag==0:
            for i in range(self.n):
                self.maxpos[i]=self.a[i]
                for j in range(self.m):
                    self.maxpos[i]=self.maxpos[i]-(self.c[j][i]*self.B[j])
                
            for i in range(self.m):
                self.maxpos[i+self.n]=0
                for j in range(self.m):
                    self.maxpos[i+self.n]=self.maxpos[i+self.n]-(self.S[j][i]*self.B[j])
                 
            vm=np.array([0]*self.m,float)
           
            vi=np.argmax(self.maxpos)
            max_pos_v=np.max(self.maxpos)


            if max_pos_v<=0:
                return final_sum
            if vi<self.n:
                for i in range(self.m):
                    vm[i]=self.c[i][vi]


            min_pos_v=0
            for i in range(self.m):
                if vm[i]>0:
                    self.minpos[i]=self.b[i]/vm[i]
                else:
                    self.minpos[i]=self.b[i]*float('inf')

            try :
                min_pos_v=min([i for i in self.minpos if i >0 ])
            except:
                return final_sum
            mp_index=np.where(self.minpos==min_pos_v)[0][0]
            self.BC[mp_index]=vi

            if vi<self.n:
                self.B[mp_index]=self.a[vi]
                self.x[vi]=self.b[mp_index]
            else:
                self.B[mp_index]=0
            final_sum=0
            for i in range(self.n):
                print(self.x[i])
                final_sum=final_sum+(self.x[i]*self.a[i])
            print()
            factor1=0
            if vi<self.n:
                factor1=self.c[mp_index][vi]
            else:
                factor1=self.S[mp_index][vi-self.n]
            for i in range(self.n):
                self.c[mp_index][i]=self.c[mp_index][i]/factor1
            for i in range(self.m):
                self.S[mp_index][i]=self.S[mp_index][i]/factor1
            self.b[mp_index]=self.b[mp_index]/factor1

            if vi<self.n:
                for i in range(self.m):
                    if i!=mp_index:
                        factor1=self.c[i][vi]

                        for j in range(self.n):
                          
                            self.c[i][j]=self.c[i][j]-(factor1*self.c[mp_index][j])
                        for j in range(self.m):
                            
                            self.S[i][j]=self.S[i][j]-(factor1*self.S[mp_index][j])
                        self.b[i]=self.b[i]-(factor1*self.b[mp_index])
                        
            else:
                for i in range(self.m):
                    if i!=mp_index:
                       
                        factor1=self.S[i][vi-self.n]

                        for j in range(self.n):
                            
                            self.c[i][j]=self.c[i][j]-(factor1*self.c[mp_index][j])

                        for j in range(self.m):
                           
                            self.S[i][j]=self.S[i][j]-(factor1*self.S[mp_index][j])
                        self.b[i]=self.b[i]-(factor1*self.b[mp_index])
               

            if vi<self.n:
                self.B[mp_index]=self.a[vi]
                self.x[vi]=self.b[mp_index]
            else:
                self.B[mp_index]=0
            final_sum=0
            for i in range(self.m):
                if self.BC[i]<self.n:
                    self.x[self.BC[i]]=self.b[i]

            for i in range(self.n):
                print(self.x[i])
                final_sum=final_sum+(self.x[i]*self.a[i])
            print()
    def graph_plot(self,objective,constraints_value,constraints):
        self.a=np.array(objective,float)
        self.b=np.array(constraints_value,float)
        self.c=np.array(constraints,float)
        self.m=np.size(self.b)
        x1=0
        x=None
        y=None
        X=None
        Y=None
        TY=None
        Common=[(1,1)]
        min1=self.b[0]/self.c[0][0]
        max1=self. b[0]/self.c[0][0]

        for i in range(self.m):
            x1=self.b[i]/(self.c[i][0])
            if x1<min1:
                min1=x1
            if x1>max1:
                max1=x1
        if min1>0:
            max1=min1
        if max1<0:
            max1=-1*max1
        min1=0
        #print(max1,min1)
        flag=2
        L=[(0,0)]

        #print("vgdysubj",x1)
        X=np.arange(min1,max1,0.0001)

        Y=np.array([(self.b[0]-(self.c[0][0]*k))/self.c[0][1] for k in X])
        plt.plot(X,Y)
        for i in range(1,self.m):
            y=np.array([(self.b[i]-(self.c[i][0]*k))/self.c[i][1] for k in X])
            plt.plot(X,y)
            flag=2
        for j in range(np.size(X)):
                if y[j]<Y[j]:
                    Y[j]=y[j]
                    if flag!=0:
                        Common.append((X[j],y[j]))
                    flag=0
                else:
                    if flag!=1:
                        Common.append((X[j],y[j]))
                    flag=1
        for i in range(np.size(X)):
            L.append((X[i],Y[i]))

        for k in Common:
            if k not in L:
                Common.remove(k)
        max1=round((self.a[0]*Common[0][0])+((self.a[1]*Common[0][1])),4)
        for i in Common:
            if max1<round((self.a[0]*i[0])+((self.a[1]*i[1])),4):
                max1=round((self.a[0]*i[0])+((self.a[1]*i[1])),4)
        plt.show()
        plt.plot([0.02]*np.size(X),Y,X,[0.02]*np.size(Y),X,Y)
        print(max1)
        plt.show()
        return max1








sol=LPsolver()
max_val=sol.graph_plot([3,2],[18,42,24],[[2,1],[2,3],[3,1]])
#solution=sol.sol('Simplex',[1,3],[10,5,4],[[1,2],[1,0],[0,1]])
#print(solution)

