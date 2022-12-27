def Trapezoid(a,b,f):
    n = 100
    def trapezoid(f,a,b,n=100):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))

Trapezoid(3,6,lambda x : 2*(x+1)**2)
Trapezoid(3,6,lambda x : 3*(x+2)**2)
Trapezoid(4,8,lambda x : 4*(x+3)**2)
Trapezoid(4,8,lambda x : 5*(x+4)**2)
Trapezoid(5,10,lambda x : 6*(x+5)**2)
Trapezoid(5,10,lambda x : 7*(x-1)**2)
Trapezoid(6,12,lambda x : 8*(x-2)**2)
Trapezoid(6,12,lambda x : 9*(x-3)**2)
Trapezoid(7,14,lambda x : 10*(x-4)**2)
Trapezoid(7,14,lambda x : 11*(x-5)**2)

