if __name__ == "__main__":
  testcases = int(input())
  for k in range(testcases):
    deque_len = int(input())
    deque = list(map(int, input().split()))
    
    i = 0
    j = len(deque) - 1
    highest_delic_level = 0 
    score = 0
    
    while(i <= j):
      # print(highest_delic_level)
      if(deque[i] <= deque[j]):
        if(deque[i] >= highest_delic_level):
          score += 1
          highest_delic_level = deque[i]
        i += 1
      else:
        if(deque[j] >= highest_delic_level):
          score += 1
          highest_delic_level = deque[j]
        j -= 1
    
    
    
    
    print(f"Case #{k+1}: {score}")
    
