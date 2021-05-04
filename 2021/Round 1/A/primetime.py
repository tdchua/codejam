def prod_over_list(mylist):
  prod = 1
  for a in mylist:
    prod *= a

  return prod


def generate_combinations(hand_sum, hand_prod):
  global my_deck
  global answer_present
  global answer
  global max_sum
  global dp_memo

  if(len(hand_sum) == 0):
    return

  else:
    my_sum = sum(hand_sum)
    prod = prod_over_list(hand_prod)
    # print(my_sum, prod)
    dp_memo[my_sum][prod] = 'Y'

    if(my_sum == prod):
      if(answer < my_sum):
        answer = my_sum

    idx = 0
    while(idx < len(hand_sum)):
      hand_sum_copy = hand_sum.copy()
      hand_prod_copy = hand_prod.copy()
      hand_prod_copy.append(hand_sum_copy.pop(idx))
      hand_prod_copy_prod = prod_over_list(hand_prod_copy)
      hand_sum_copy_sum = sum(hand_sum_copy)


      if(prod_over_list(hand_prod_copy) < max_sum):
        if(dp_memo[hand_sum_copy_sum][hand_prod_copy_prod] == 'N'):
          generate_combinations(hand_sum_copy, hand_prod_copy)
        # else:
        #   print("DP!")

      idx += 1

  return answer




if __name__ == "__main__":

  testcase = 1
  testcases = int(input())


  while(testcase <= testcases):

    lines = int(input())
    my_deck = []
    answer_present = False
    answer = 0

    for a in range(lines):
      P, N = input().split()
      # print(P, N)
      my_deck += [int(P) for i in range(int(N))]

    dp_memo = [['N' for i in range(prod_over_list(my_deck))] for j in range(sum(my_deck))]
    # print(len(dp_memo), len(dp_memo[0]))

    # print(my_deck)
    max_sum = sum(my_deck)
    # print(sum_of_inputs)

    hand_sum = my_deck.copy()
    hand_prod = []

    idx = 0
    while(idx < len(hand_sum)):
      hand_sum_copy = hand_sum.copy()
      hand_prod_copy = hand_prod.copy()
      hand_prod_copy.append(hand_sum_copy.pop(idx))
      # print(hand_sum_copy)
      # print(hand_prod_copy)

      generate_combinations(hand_sum_copy, hand_prod_copy)

      idx += 1

    print("Case #%d: %d" % (testcase, answer))
    testcase += 1
