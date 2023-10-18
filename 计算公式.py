import math
x=eval(input())
radians=math.radians(65)
y=math.cos(radians)+((20*x+math.e**x)/math.sqrt(1+x**4))-math.log(6.5*x)
print(f"f({x:.2f})={y:.3f}")
