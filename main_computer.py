from computer import Computer

if __name__=='__main__':
    computer1=Computer("Asus", "Vivobook", "I3", 8)
    computer1.display_info()
    computer1.awesome()

    computer2=Computer('Apple', 'Macbook Air', 'M1',8)
    computer2.display_info()
    computer2.awesome()

    computer3=Computer('Acer','Nitro V','I5')
    computer3.display_info()
    computer3.awesome()


    n=int(input('Enter the number of computers:'))
    computers = []
    for i in range (n):
        print(f"\nEnter details for Computer {i + 1}:")
        computer4=Computer(input('brand: '), input('model: '),input('processor: '),int(input('RAM in GB: ')))
        computers.append(computer4)


    i=0
    for comp in computers:
        print(f'\nDetails of {i + 1}-computer ')
        print(comp)
        comp.display_info()
        comp.awesome()
        i+=1


