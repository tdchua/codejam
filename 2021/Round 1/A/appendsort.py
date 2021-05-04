if __name__ == "__main__":


  testcase = 1
  num_testcases = int(input())

  while(testcase <= num_testcases):
    filler = input()
    numbers = input().split()

    prev_num = numbers[0]
    cost = 0
    for curr_num in range(1, len(numbers)):
      # print(numbers[curr_num])
      # print(numbers)
      num_to_reach = str(int(prev_num)+1)
      difference = len(num_to_reach) - len(numbers[curr_num])
      # print(num_to_reach)
      if(len(num_to_reach) > len(numbers[curr_num])): #Previous number has more characters than current number
        if(int(num_to_reach[0:len(numbers[curr_num])]) < int(numbers[curr_num])): #first digit of previous number is lower than current number
          # print("Hello1")
          numbers[curr_num] += "0" * difference
          cost += difference

        elif(int(num_to_reach[0:len(numbers[curr_num])]) == int(numbers[curr_num])): #First digit of prev is equal to first digit of current
          # print("Test")
          # print("Hello2")
          cost += difference
          numbers[curr_num] = num_to_reach
        elif(int(num_to_reach[0:len(numbers[curr_num])]) > int(numbers[curr_num])): #First digit of prev is bigger than first digit of curr
          # print("Hello3")
          numbers[curr_num] += "0" * (difference+1)
          cost += difference + 1

      elif(len(num_to_reach) == len(numbers[curr_num])):
        if(int(num_to_reach) > int(numbers[curr_num])):
          # print("Hello4")
          cost += difference + 1
          numbers[curr_num] += '0'

      prev_num = numbers[curr_num]

    print("Case #" + str(testcase) + ": " + str(cost))
    # print(numbers)
    testcase += 1
