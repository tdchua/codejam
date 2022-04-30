if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    N = int(input())
    solution = [(j*2)+1 for j in range(N)]
    solution_char = [str((j*2)+1) for j in range(N)]
    print(" ".join(solution_char))
    addtl_set = input()
    print(addtl_set)
    
    
    
    
    
    
    # print(f"Case #{i+1}: {list_words[0]}")
