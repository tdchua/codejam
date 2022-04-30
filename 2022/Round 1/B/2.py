def codejamhelper(presses, current_pascal, choices, b):
  
  global X
  if(len(choices) == 0):
    b += 1
    if(b < len(X)):
      choices = X[b]
  # print(presses, current_pascal, choices)
  if(b >= len(X)):
    return presses
  if(b < len(X)):
    min_score = False
    memo = {}
    for choice_idx in range(len(choices)):
      new_pascal = current_pascal
      new_presses = presses
      choices_copy = choices.copy()
      new_pascal = choices_copy.pop(choice_idx)
      new_presses = presses + abs(new_pascal-current_pascal)
      if(new_pascal in memo):
        min_score = min(min_score, memo[new_pascal])
      else:
        if(min_score == False):
          min_score = codejamhelper(new_presses, new_pascal, choices_copy, b)
          memo[new_pascal] = min_score
        else:
          min_score = min(min_score, codejamhelper(new_presses, new_pascal, choices_copy, b))
          memo[new_pascal] = min_score
    
    return min_score




if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    N, P = map(int, input().split())
    X = []
    for j in range(N):
      x = list(map(int, input().split()))
      X.append(x)
      
    # print(X)  
    min_score = False
    memo = {}
    for j in range(len(X[0])):
      X0_copy = X[0].copy()
      pascal = X0_copy.pop(j)
      if(pascal in memo):
        min_score = min(min_score, memo[pascal])
      else:
        if(min_score == False):
          min_score = codejamhelper(pascal, pascal, X0_copy, 0)
          memo[pascal] = min_score
        else:
          min_score = min(min_score, codejamhelper(pascal, pascal, X0_copy, 0))
          memo[pascal] = min_score
    
    
    # print(memo)
    print(f"Case #{i+1}: {min_score}")
    
