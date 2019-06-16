

def pylon(grid, travel, pos, options):
  if(len(options) == 0):
    travel.append(pos)
    # print("Finished Traveled:", travel)
    return travel

  new_travel = travel[:]
  new_travel.append(pos)
  grid[pos[0]][pos[1]] = 1
  have_option = False
  new_travel_2 = []
  # print("Traveled:", new_travel)
  for a in options:

    if(pos[0] != a[0] and pos[1] != a[1] and (abs(a[0] - pos[0]) != abs(a[1] - pos[1]))):
      # print("Options: ", options)
      # print("Next Path Taken: ", a)
      have_option = True
      # print("Options:",options)
      options_to_func = options[:]
      options_to_func.remove(a)
      # print("After removal, Options:",options)
      new_travel_2 = pylon(grid, new_travel, a, options_to_func)

    # print("Len of new travel 2:", len(new_travel_2))
    if(len(new_travel_2) == (len(grid) * len(grid[0]))):
      break
    else:
      have_option = False


  if(have_option == False):
    new_travel.pop()
    # print("No more options must retrace")
    return new_travel

  return new_travel_2





if __name__ == "__main__":

  for case in range(1, int(input()) + 1):
    R, C = map(int, input().split())

    grid = []
    for row in range(R):
      row = []
      for col in range(C):
        row.append(0)
      grid.append(row)

    init_travel = []
    options = []
    for a in range(R):
      for b in range(C):
        option = (a, b)
        options.append(option)
    answer = False

    for a in range(R):
      for b in range(C):
        pos = (a, b)
        # print("Started with: ", pos)
        # print(options)
        travel = []
        options_to_func = options[:]
        options_to_func.remove(pos)

        my_travel = pylon(grid, travel, pos, options_to_func)
        # print("Heyo", travel)
        if(len(my_travel) == (len(grid) * len(grid[0]))):
          answer = True
          break


    if(answer == True):
      print("Case #" + str(case) + ": POSSIBLE")
      for a in my_travel:
        print(a[0]+1, a[1]+1)
    else:
      print("Case #" + str(case) + ": IMPOSSIBLE")
