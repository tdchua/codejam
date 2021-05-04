#1st Test Set : O
#2nd Test Set : X
#3rd Test Set : X

if __name__ == "__main__":

  T, N, Q = map(int, input().split())

  for test in range(T):
    mylist = [i for i in range(4, N+1)]
    mysortedlist = []

    if(len(mysortedlist) == 0): #The first time we're going to ask
      print("1 2 3")
      mid = int(input())
      if(mid == 2):
        mysortedlist = [1, 2, 3]
      if(mid == 1):
        mysortedlist = [2, 1, 3]
      if(mid == 3):
        mysortedlist = [1, 3, 2]

    while(len(mylist) != 0):
      number_to_add = mylist.pop(0)
      i = 0
      j = i + 1
      while(i < len(mysortedlist)-1):
        print(mysortedlist[i], mysortedlist[j], number_to_add)
        mid = int(input())

        if(mid == number_to_add):
          mysortedlist.insert(j, number_to_add)
          break
        elif(mid == mysortedlist[i]):
          mysortedlist.insert(i, number_to_add)
          break
        elif(mid == mysortedlist[j] and j == len(mysortedlist)-1):
          mysortedlist.append(number_to_add)
          break

        i += 1
        j += 1

    mysortedlist = [str(i) for i in mysortedlist]
    print(" ".join(mysortedlist))
    result = input()

    if(result == -1):
      break
