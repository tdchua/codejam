#For Codejam 2019
#Foregone Solution





if __name__ == "__main__":


  for case in range(int(input())): #Testcases

    number = int(input())
    my_new_number = []
    for a in str(number):
      if(a == '4'):
        my_new_number.append('2')
      else:
        my_new_number.append(a)

    my_new_number = "".join(my_new_number)
    diff = number - int(my_new_number)
    print("Case #" + str(case + 1) + ": " + str(diff) + " " + str(my_new_number))
