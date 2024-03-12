class Person: # Parent class
  nama = 'test'

class Employee(Person): # child class
  gaji = 1000
  id = 123
  
person1 = Person()
employee1 = Employee()

print('nama dari person', person1.nama)
print('nama dari employee', employee1.nama)
print('gaji dari employee',employee1.gaji)
print('id dari employee',employee1.id)
#print('gaji dari person',person1.gaji)
