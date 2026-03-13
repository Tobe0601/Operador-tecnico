#Suma basica
def add(a, b):
    return a + b

print(add(2, 3))

#Conversor de horas a minutos
def hours_to_minutes (hours):
    return hours * 60

print(hours_to_minutes(5))

#Identificar si un numero esta en un rango entre dos numeros mas
def is_between(x, low, high):
    return low <= x <= high

print(is_between(5, 1, 10))
print(is_between(15, 1, 10))

#Calculando el area de un circulo
import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(3))


#Multiplicando
def multiply(a, b):
    return a * b

print(multiply(4, 6))
print(multiply(10, 3))

#Salario Anual

def yearly_salary(hourly_rate, hours_per_week):
    weekly = hourly_rate * hours_per_week
    yearly = weekly * 52
    return yearly
print(yearly_salary(20,40))