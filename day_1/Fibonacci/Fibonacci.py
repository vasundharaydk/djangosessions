def Fibonacci_series(num):
    a,b = 0,1
    fibonaci = [0]
    if num <= 0:
      return 0
    elif num == 1:
      return 1
    else:
      for i  in range(1,num):
        a,b=b,a+b
        fibonaci.append(b)
      return fibonaci
