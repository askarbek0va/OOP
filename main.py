from computer import Computer

if __name__=='__main__':
    computer1=Computer("Asus", "Vivobook", "I3", "8GB")
    computer1.display_info()
    computer1.awesome()

    computer2=Computer('Apple', 'Macbook Air', 'M1','8GB')
    computer2.display_info()
    computer2.awesome()

    computer3=Computer('Acer','Nitro V','I5')
    computer3.display_info()
    computer3.awesome()

    n=int(input('Give the number of computers:'))
    computers = []
    for i in range (n):
        computer4=Computer(input('brand: '), input('model: '),input('processor: '))
        computer4.display_info()
        computer4.awesome()

        computers.append(computer4)

    print(computers)

