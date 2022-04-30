



if __name__ == "__main__":
  testcases = int(input())

  for testcase in range(1, testcases+1):
    N, C = map(int, input().split())

    #Check edge cases.
    min = N - 1
    max = ((N * (N+1))/2) - 1
    if(C <= min or C >= max):
      answer = "IMPOSSIBLE"
    else:
      C = C - N - 1
      if(C == 0):
        answer = [i for i in range(1, N+1)]
      else:
        for i in reversed(range(1, N+1)):
            






    print("Case #%d: %s" % (testcase, answer))
