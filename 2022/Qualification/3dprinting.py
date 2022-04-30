if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    c_min = 1000000
    m_min = 1000000
    y_min = 1000000
    k_min = 1000000
    
    for j in range(3):
      c, m, y, k = map(int, input().split())
      c_min = min(c, c_min)
      m_min = min(m, m_min)
      y_min = min(y, y_min)
      k_min = min(k, k_min)
    
    sum_ink = c_min + m_min + y_min + k_min
    list_ink = [c_min, m_min, y_min, k_min]
    
    if(sum_ink >= 1000000):
      excess_ink = (c_min + m_min + y_min + k_min) - 1000000
      while(excess_ink != 0):
        max_ink_idx = list_ink.index(max(list_ink))
        if(list_ink[max_ink_idx] >= excess_ink):
          list_ink[max_ink_idx] = list_ink[max_ink_idx] - excess_ink
          excess_ink = 0
        else:
          excess_ink = excess_ink - list_ink[max_ink_idx]
          list_ink[max_ink_idx] = 0
      print(f"Case #{i+1}:", list_ink[0], list_ink[1], list_ink[2], list_ink[3])
    else:
      print(f"Case #{i+1}: IMPOSSIBLE")
