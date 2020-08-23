#Q->2
#using try to avoid failing or crashing in run the program
try:
    # try to convert input data into float type
    n = float(input("Enter the point > "))
    # checking entered data range if in ranger 0 to 20 it will check if not printing a warning
    if n <= 20:
        if n < 10 :
            print('Failed')
        elif 10 <= n < 15:
            print('Not bad')
        elif 15 <= n < 18:
            print('Good')
        else:
            print('Excellent')
    else:
        print("Point can't be grater than 20")
except:
    print("There's an error in data type")