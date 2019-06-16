import itertools


# def trim(to_trim, list, score, max_score):
#   score += 1
#
#   for a in range(1, len(list)):
#     my_copy_list = list[:]
#     if(to_trim[0] in a or to_trim[1] in a):
#       my_copy_list.remove(a)
#
#   for a in range(score, len(my_copy_list)):
#     copy_of_my_copy = my_copy_list[:]
#     new_score = trim(a, copy_of_my_copy, score, max_score)
#
#   if(max_score < score):
#     max_score = score
#
#   return max_score

if __name__ == "__main__":

  for case in range(1, int(input()) + 1):
    my_list = []

    for a in range(int(input())):
      word = input()
      my_list.append(word)

    my_combi = list(itertools.combinations(my_list, 2))
    approved_combi = []
    for a in my_combi:
      if(len(a[0]) > len(a[1])):
        for b in range(len(a[0])):
          if(a[0][b] in a[1]):
            for c in range(len(a[1])):
              if(a[0][b] == a[1][c]):
                if(len(a[0]) - b == len(a[1]) - c):
                  if(a[0][b:] == a[1][c:]):
                    approved_combi.append(a)
      else:
        for b in range(len(a[1])):
          if(a[1][b] in a[0]):
            for c in range(len(a[0])):
              if(a[1][b] == a[0][c]):
                if(len(a[1]) - b == len(a[0]) - c):
                  if(a[1][b:] == a[0][c:]):
                    approved_combi.append(a)
    my_set = list(set(approved_combi))

    filtered_set = []
    for a in my_set:
      copy_my_set = my_set[:]
      copy_my_set.remove(a)
      filtered_set.append(a)
      for b in copy_my_set:
        if(
      trim(a, copy_my_set, 0, 0)

    print(set(approved_combi))
    print(len(set(approved_combi)) * 2)
    # print("Case #" + str(case) + ": POSSIBLE")
