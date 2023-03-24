class MultipleFun():
            def Subfields():
                print("Sub-fields in AI are:")
                print("Machine Learning")
                print("Neural Networks")
                print("Vision")
                print("Robotics")
                print("Speech Processing")
                print("Natural Language Processing")
            
            def OddEven():
                num1 = int(input("Enter a Number:"))
                if((num1%2)==1):
                    print(num1,"is Odd Number")
                else:
                    print(num1, "is Even Number")
            
            def Elegible():
                var = input("Your Gender:")
                num = int(input("Your Age:"))
                if(var == "Male" and num >=21):
                    print("ELIGIBLE")
                elif(var == "Female" and num>=18):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")        
            def Percentage():
                num1 = int(input("Subject1:"))
                num2 = int(input("Subject2:"))
                num3 = int(input("Subject3:"))
                num4 = int(input("Subject4:"))
                num5 = int(input("Subject5:"))
                Total =(num1+num2+num3+num4+num5)
                percentage = Total/5
                print("Total:",Total)
                print("Percentage",percentage)
            def triangle():
                num1 = int(input("Height:"))
                num2 = int(input("Breadth:"))
                print("Area formula: (Height*Breadth)/2")
                Area = (num1*num2)/2
                print("Area of Triangle:",Area)
            def PerimeterTriangle():
                num1 = int(input("Height1:"))
                num2 = int(input("Height2:"))
                num3 = int(input("Breadth:"))
                print("Perimeter formula: Height1+Height2+Breadth")
                perimeter = num1+num2+num3
                print("Perimeter of Triangle: ",perimeter)    