def generate_my_permutations(N, explored, to_explore):
  global permutations

  if(len(to_explore) == 0):
    # print(explored)
    permutations.append(explored)
  else:
    i = 0
    while(i < len(to_explore)):
      to_explore_filtered = to_explore.copy()
      explored_copy = explored.copy()
      explored_copy.append(to_explore_filtered.pop(i))
      generate_my_permutations(N, explored_copy, to_explore_filtered)

      i += 1


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


def find_answer(permutations, C):
  for permutation in permutations:
    if(reversort(permutation.copy()) == C):
      return permutation

  return False




if __name__ == "__main__":

   testcase = int(input())


   for test in range(1, testcase+1):
     permutations = []
     N, C = map(int, input().split())
     to_explore = [num for num in range(1, N+1)]
     i = 0
     while(i < len(to_explore)):
       to_explore_filtered = to_explore.copy()
       explored = [to_explore_filtered.pop(i)]
       #
       # print(to_explore_filtered)
       # print(explored)

       generate_my_permutations(N, explored, to_explore_filtered)
       i += 1

     answer = find_answer(permutations, C)
     if(answer == False):
       print("Case #" + str(test) + ": " + "IMPOSSIBLE")
     else:
       answer = ' '.join(str(a) for a in answer)
       print("Case #" + str(test) + ": " + answer)
