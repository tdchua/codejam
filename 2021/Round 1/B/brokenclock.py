def conv_to_time_fr_ticks(hour, min, second):

  hour_lower_bound = hour / 30
  min = min / 6
  second = second / 6


  return hour_lower_bound, min, second, 0



def generate_combinations(list_ticks):
  global hour
  global min
  global second

  if(len(list_ticks)==0): #We have our combination of ticks
    conv_to_time_fr_ticks(hour, min, second)
  else:
    i = 0
    while(i < len(list_ticks)):
      if(len(list_ticks) == 2):
        min = list_ticks[i]
      if(len(list_ticks) == 1):
        second = list_ticks[i]

      list_ticks_copy = list_ticks.copy()
      list_ticks_copy.pop(i)
      generate_combinations(list_ticks_copy)
      i += 1


if __name__ == "__main__":

  testcases = int(input())
  for test in range(1, testcases+1):
    A, B, C = map(float, input().split())
    list_ticks = [A, B, C]

    # print("In ticks: ", A, B, C)

    A_conv = A / (12 * (10**10))
    B_conv = B / (12 * (10**10))
    C_conv = C / (12 * (10**10))

    # print("In Degrees: ", A_conv, B_conv, C_conv)

    # hour, min, second, nano = conv_to_time_fr_ticks(C_conv, B_conv, A_conv)



    while(i < 3):
      hour = list_ticks[i]
      list_ticks_copy = list_ticks.copy()
      list_ticks_copy.pop(i)

      generate_combinations(list_ticks_copy)
      i += 1

    # print("Case #%d: %d %d %d %d" % (test, hour, min, second, nano))
