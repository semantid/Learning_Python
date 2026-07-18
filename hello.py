def Celsius_to_Fahrenheit(c):
    return (c * 9/5) + 32

def Fahrenheit_to_Celsius(f):
    return (f - 32) * 5/9

def main():
    print (" Temperature converter")
    

while True:

    choice=input("Temperature type Celsius or Fahrenheight (C or F): ").strip().upper()

    if choice=="QUIT":
        print("Good Bye!")
        break 
             
    elif choice== "C":
        temp=float(input("Enter temperature in Celcius: "))
        result=Celsius_to_Fahrenheit(temp)
        print(f"{temp} C is {result:.2f} F")

    elif choice=="F":
         temp=float(input("Enter temperature in Fahrenheight:  "))
         result=Fahrenheit_to_Celsius(temp)
         print(f"{temp} F is {result:.2f} C")         
      
    else:
        print("Invalid choice, please enetr C or F.")

if __name__ == "__main__":
    main()        