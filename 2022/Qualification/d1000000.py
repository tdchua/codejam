if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
      num_dice = int(input())
      list_dice = list(map(int, input().split()))
      list_dice = sorted(list_dice)
      
      num = 1
      straight = 0
      for j in list_dice:
        if(j >= num):
          num += 1
        else:
          continue

      print(f"Case #{i+1}: {num-1}")
