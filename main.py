from person import Person

if __name__=='__main__':
    person4 = Person('John')
    print(person4.name)

    person4.name = 'John'
    print(person4.name)

    person4.walk()
    person4.info()

    person2 = Person('Bakyt')
    person2.walk()
