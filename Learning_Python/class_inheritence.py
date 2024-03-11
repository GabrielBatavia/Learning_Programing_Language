class Person: # Parent class
  nama = 'test'

class Employee(Person): # child class
  gaji = 1000
  
person1 = Person()
employee1 = Employee()

print('nama dari person', person1.nama)
print('nama dari employee', employee1.nama)
print('gaji dari employee',employee1.gaji)
#print('gaji dari person',person1.gaji)