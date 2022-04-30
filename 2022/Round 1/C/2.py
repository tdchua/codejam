if __name__ == "__main__":
  testcases = int(input())
  for case in range(testcases):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(N, K)
    # print(numbers)
    answer = "IMPOSSIBLE"
    answer_found = False
    
    zero_check = True
    for i in numbers:
      if(i != 0):
        zero_check = False
    
    if(zero_check):
      print(f"Case #{case+1}: 0")
    else:
      # print(numbers)
      for k in range(K):
        numbers_sum = sum(numbers)
        numbers_squared = sum([i**2 for i in numbers])
        if(numbers_sum == 0):
          print(f"Case #{case+1}: IMPOSSIBLE")
          continue
        answer = (numbers_squared - (numbers_sum**2)) // (2*numbers_sum)
        remainder = (numbers_squared - (numbers_sum**2)) % (2*numbers_sum)
        # print(answer)
        if(remainder == 0):
          print(f"Case #{case+1}: {answer}")
        else:
          print(f"Case #{case+1}: IMPOSSIBLE")
