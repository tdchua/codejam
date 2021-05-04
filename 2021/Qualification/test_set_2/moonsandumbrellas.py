
import sys
def help_cody(mystring): #With the help of analysis tab
  global X
  global Y
  global Count

  Count += 1
  print(Count)

  if(len(mystring) <= 1):
    return 0
  else:
    mylist = list(mystring)
    C_string = mylist.copy()
    J_string = mylist.copy()

    if(mystring[0] == '?'):
      C_string[0] = 'C'
      J_string[0] = 'J'
      C_string = "".join(C_string)
      J_string = "".join(J_string)

      return min(help_cody(C_string), help_cody(J_string))
    else:
      if(mystring[0] == mystring[1]): #Same characters for the first two.
        return help_cody(mystring[1:])
      else: #Different Characters
        if((mystring[0], mystring[1]) == ('C','J')):
          return X + help_cody(mystring[1:])
        if((mystring[0], mystring[1]) == ('J','C')):
          return Y + help_cody(mystring[1:])
        if(mystring[1] == '?'):
          C_string[1] = 'C'
          J_string[1] = 'J'
          C_string = "".join(C_string)
          J_string = "".join(J_string)

          return min(help_cody(C_string), help_cody(J_string))


if __name__ == "__main__":
  sys.setrecursionlimit(10**6)
  testcase = int(input())
  for test in range(1, testcase+1):

   X, Y, mystring = input().split()
   X = int(X) #Cost for CJ
   Y = int(Y) #Cost for JC
   Count = 0

   print("Case #" + str(test) + ": " + str(help_cody(mystring)))
