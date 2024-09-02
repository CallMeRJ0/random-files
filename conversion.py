def main():
    type = int(input("1 to convert C to F | 2 to convert F to C \n"))
    
    def f_c():
        fahrenheit = float(input("Enter the fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        celsius = round(celsius, 3)
        print(f"{fahrenheit}°F in fahrenheit is {celsius}°C")   
    def c_f():
        celsius = float(input("Enter the celsius: "))
        fahrenheit = (celsius*9 /5) + 32
        fahrenheit=round(fahrenheit, 3)
        print(f"{celsius}°C in fahrenheit is {fahrenheit}°F")
        return
        
    if type == 1:
        c_f()
    elif type == 2:
        f_c()
    else:
        print("Error")
        quit()
while True:
    main()
