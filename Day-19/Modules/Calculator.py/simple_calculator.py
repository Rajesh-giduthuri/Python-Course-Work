import addition,subtraction,multiplication,division,power

unlimited=tuple(map(int,input("Enter the values for unlimited addition : ").split()))

print("addition of 2 values:",addition.addition_2positional(10,20)) 
print("addition of n values:",addition.addition_unlimited(unlimited))
print("subtraction of 2 values:",subtraction.subtraction(10,20))
print("multiplication of n values:",multiplication.multiplication(10,20))
print("modulo_division of 2 values:",division.modulo_division(10,20))
print("floor_division of 2 values:",division.floor_division(10,20))
print("normal_division of 2 values:",division.normal_division(10,20))
print("power of 2 values:",power.power(2,2))

#output:
#addition of 2 values: 30
#addition of n values: 150 
#subtraction of 2 values: -10
#multiplication of n values: 200
#modulo_division of 2 values: 10
#floor_division of 2 values: 0
#normal_division of 2 values: 0.5