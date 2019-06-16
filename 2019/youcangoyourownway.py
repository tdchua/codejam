
if __name__ == "__main__":

  for case in range(int(input())):
    size = int(input())
    lydia = input()

    my_points = []
    for a in lydia:
      if(a == 'E'):
        my_points.append('S')
      else:
        my_points.append('E')

    my_journey = "".join(my_points)
    print("Case #" + str(case + 1) + ": " + my_journey)
