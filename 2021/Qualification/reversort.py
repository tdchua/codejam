def reversort(mylist):

  sorted_list = sorted(mylist)
  cost = 0

  for i in range(len(mylist)-1):
    min_number = sorted_list[i]
    j = mylist.index(min_number)
    cost += j - i + 1

    list_to_reverse = mylist[i:j+1]
    list_to_reverse.reverse()
    mylist[i:j+1] = list_to_reverse

    # print(mylist)



  return cost


if __name__ == "__main__":

   testcase = int(input())
   for test in range(1, testcase+1):

     filler = input()
     mylist = [int(a) for a in input().split()]

     print("Case #" + str(test) + ": " + str(reversort(mylist)))
