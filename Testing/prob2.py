import time



def c_frac(n):
   number = 1;
   thing = (1+(1/1.0))
   fract = 2;
   n-=1
   while(n!=0):
   	fract = 1+1.0/fract
   	n-=1

   number = fract
   return number





num = int(raw_input("Enter n: "))
start = time.time()
print c_frac(num)
end = time.time()

rtime = end-start

print rtime

