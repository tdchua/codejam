def min_weight(weights_required, start, end):
  min_weights = []
  min_weights = [min(j[start: end]) for j in weights_required]

  
  return min_weights


if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    E, W = map(int, input().split())
    
    weights_required = [[] for j in range(W)]
    exercises = []
    for j in range(E):
      exercise = list(map(int, input().split()))
      exercises.append(exercise)
      for k in range(len(weights_required)):
        weights_required[k].append(exercise[k])
    
    print(weights_required)
    print(exercises)
    steps = 0
    
    # print(f"Case #{i+1}: {answer}")
    #Determine common weights for all exercises
    all_weight = [min(j) for j in weights_required]
    print("Weight required by all exercises: ", all_weight)
    steps += sum(all_weight)
    
    
    # Right to left
    right_to_left = []
    end = len(exercises)
    print(min_weight(weights_required, 0, end-1))
