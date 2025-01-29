from person import Person

if __name__ == '__main__':
     person1 = Person()
     person1.surname = 'Fff'
     print(person1.age)
     person1.info()

     person1 = Person('Aibek')
     person1.info()

     person2 = Person('Bbbb', 'Dddd', 25)
     person2.info()

     person3 = Person('dddd', 'eeee', gender='male')
     person3.walk()


