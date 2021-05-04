def check_seq(l_idx, r_idx):
  global my_vector

  #Case 1 Left index corresponds to beginning of list
  if(l_idx == 1):
    if(r_idx == len(my_vector)-1): #Right index corresponds to end of list
      print("Case 1")
      my_vector = ['T' for i in range(K+1)]
      return len(my_vector[1:])
    else: #Right index is succeeded by a 'O'
      print("Case 2")
      my_vector[1:r_idx+1] = ['T' for i in range(r_idx)]
      return r_idx
  #Case 2 Right index correspods to end of list
  elif(r_idx == len(my_vector)-1):
    #Left index is preceeded by a 'O'
    print("Case 3")
    my_vector[l_idx:] = ['T' for i in range(r_idx-l_idx+1)]
    return (r_idx - l_idx + 1)
  #Case 3 In between other letters (T, O)
  else:
    if(my_vector[l_idx-1] == 'T' or my_vector[r_idx+1] == 'T'):
      print("Case 4")
      my_vector[l_idx:r_idx+1] = ['T' for i in range(r_idx-l_idx+1)]
      return(r_idx-l_idx+1)
    if((r_idx - l_idx + 1) % 2 == 0): #Even
      print("Case 5")
      my_vector[l_idx:l_idx+((r_idx-l_idx+1)//2)] = ['T' for i in range((r_idx-l_idx+1)//2)]
      return (r_idx - l_idx + 1) // 2
    else:
      print("Case 6")
      my_vector[l_idx:l_idx+((r_idx-l_idx+1)//2)+1] = ['T' for i in range(((r_idx-l_idx+1)//2)+1)]
      return ((r_idx - l_idx + 1) // 2) + 1


if __name__ == "__main__":

  testcases = int(input())
  for test in range(1, testcases+1):

    N, K = map(int, input().split())
    # print(N, K)

    my_vector = ['X' for i in range(K+1)]

    P = list(map(int, input().split()))
    for Pi in P:
      my_vector[Pi] = 'O'

    # print(my_vector)


    #Let's first find the longest segment of X's.
    answer_count = 0
    seq = 0
    streak = False
    l_idx = 0
    r_idx = 0

    max_l_idx = 0
    max_r_idx = 0
    max_seq = 0

    count = 0
    for i in range(1, len(my_vector)):
      if(my_vector[i] == 'X'):
        seq += 1
        if(streak == False):
          l_idx = i
          streak = True

        r_idx = i

        if(max_seq < seq):
          max_l_idx = l_idx
          max_r_idx = r_idx
          max_seq = seq

      if(my_vector[i] == 'O'):
        streak = False

    if(max_seq != 0):
      answer_count += check_seq(max_l_idx, max_r_idx)

    # print(my_vector)
    seq = 0
    streak = False
    l_idx = 0
    r_idx = 0

    max_l_idx = 0
    max_r_idx = 0
    max_seq = 0

    count = 0
    for i in range(1, len(my_vector)):
      if(my_vector[i] == 'X'):
        seq += 1
        if(streak == False):
          l_idx = i
          streak = True

        r_idx = i

        if(max_seq < seq):
          max_l_idx = l_idx
          max_r_idx = r_idx
          max_seq = seq

      if(my_vector[i] != 'X'):
        streak = False

    if(max_seq != 0):
      # print(max_l_idx, max_r_idx)
      answer_count += check_seq(max_l_idx, max_r_idx)

    # print(my_vector[1:])
    print("Case #" + str(test) + ": " + str(answer_count / K))
