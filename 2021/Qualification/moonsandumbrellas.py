
import sys
def help_cody(mystring): #With the help of analysis tab
  global X
  global Y
  global memo

  if(len(mystring) <= 1):
    return 0
  else:
    if(mystring in memo):
      # print("DP: ", mystring)
      return memo[mystring]
    else:
      mylist = list(mystring)
      C_string = mylist.copy()
      J_string = mylist.copy()

      if(mystring[0] == '?'):
        C_string[0] = 'C'
        J_string[0] = 'J'
        C_string = "".join(C_string)
        J_string = "".join(J_string)
        memo[mystring] = min(help_cody(C_string), help_cody(J_string))
        return memo[mystring]
      else:
        if(mystring[0] == mystring[1]): #Same characters for the first two.
          memo[mystring] = help_cody(mystring[1:])
          return memo[mystring]
        else: #Different Characters
          if((mystring[0], mystring[1]) == ('C','J')):
            memo[mystring] = X + help_cody(mystring[1:])
            return memo[mystring]
          if((mystring[0], mystring[1]) == ('J','C')):
            memo[mystring] = Y + help_cody(mystring[1:])
            return memo[mystring]
          if(mystring[1] == '?'):
            C_string[1] = 'C'
            J_string[1] = 'J'
            C_string = "".join(C_string)
            J_string = "".join(J_string)
            memo[mystring] = min(help_cody(C_string), help_cody(J_string))
            return memo[mystring]


if __name__ == "__main__":
  sys.setrecursionlimit(10**6)
  testcase = int(input())
  for test in range(1, testcase+1):

   X, Y, mystring = input().split()
   X = int(X) #Cost for CJ
   Y = int(Y) #Cost for JC
   memo = {}
   print("Case #" + str(test) + ": " + str(help_cody(mystring)))
