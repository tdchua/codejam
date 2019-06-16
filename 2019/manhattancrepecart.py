

if __name__ == "__main__":

  for testcase in range(int(input())):
    p, q = map(int, input().split())

    my_manhat = [0 for a in range(q + 1)]
    my_manhat = [my_manhat[:] for a in range(q + 1)]

    # print(my_manhat)
    max = 0
    most_south = 0
    most_west = 0
    for person in range(p):
      command = input().split()
      x = int(command[0])
      y = int(command[1])

      dir = command[2]
      if(dir == 'N'):
        for a in range(1, q - y + 1):
          # print("Loop", a)

          for b in range(q + 1):
            # print(my_manhat)
            my_manhat[y + a][b] = my_manhat[y + a][b] + 1
            # print("Checking: ", y + a, b, my_manhat[y + a][b])
            if(max < my_manhat[y + a][b]):
              max = my_manhat[y + a][b]
              most_south = y + a
              most_west = b
            if(my_manhat[y + a][b] == max):
              if(most_west > b):
                most_west = b
                most_south = y + a
              if(most_south > y + a):
                most_west = b
                most_south = y + a
      elif(dir == 'S'):
        for a in range(y):
          for b in range(q + 1):
            my_manhat[a][b] += 1
            if(max < my_manhat[a][b]):
              max = my_manhat[a][b]
              most_south = a
              most_west = b
            if(my_manhat[a][b] == max):
              if(most_west > b):
                most_west = b
                most_south = a
              if(most_south > a):
                most_west = b
                most_south = a
      elif(dir == 'E'):
        for a in range(1, q - x + 1):
          for b in range(q + 1):
            # print(b, x+a)
            my_manhat[b][x + a] += 1
            if(max < my_manhat[b][x + a]):
              max = my_manhat[b][x + a]
              most_south = b
              most_west = x + a
            if(my_manhat[b][x + a] == max):
              if(most_west > x + a):
                most_west = x + a
                most_south = b
              if(most_south > b):
                most_west = x + a
                most_south = b
      elif(dir == 'W'):
        for a in range(x):
          for b in range(q + 1):
            my_manhat[b][a] += 1
            if(max < my_manhat[b][a]):
              max = my_manhat[b][a]
              most_south = b
              most_west = a
            if(my_manhat[b][a] == max):
              if(most_west > a):
                most_west = a
                most_south = b
              if(most_south > b):
                most_west = a
                most_south = b
      # print(my_manhat)


    print("Case #{}: {} {}".format(testcase + 1, most_west, most_south))
