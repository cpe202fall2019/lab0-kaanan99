def weight_on_planets():
   # write your code here
   x = int(input("What do you weigh on earth? "))
   mw = x * .38
   jw = x * 2.34
   print("\nOn Mars you would weigh", mw, "pounds.\nOn Jupiter you would weigh", jw, "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
