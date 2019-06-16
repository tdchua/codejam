


if __name__ == "__main__":

  for testcase in range(int(input())):
    swords, diff = map(int, input().split())
    charles = list(map(int, input().split()))
    delilah = list(map(int, input().split()))

    # print(charles)
    # print(delilah)

    set_of_fight = set()

    for l in range(swords):
      for r in range(l, swords):
        # print("Fight:", l, r)
        charles_max = max(charles[l:r+1])
        delilah_max = max(delilah[l:r+1])
        # print(charles_max)
        # print(delilah_max)
        for a in range(l, r + 1):
          # print("C", charles[a])
          if(charles[a] == charles_max):
            for b in range(l, r + 1):
              # print("D", delilah[b])
              # print("D", b)
              # print(a, b)
              if(delilah[b] == delilah_max):
                if(abs(charles[a] - delilah[b]) <= diff):
                  # if(charles[a] > delilah[b]):
                  #   fight = (b, a)
                  # else:
                  #   fight = (a, b)
                  fight = (l, r)
                  if(fight not in set_of_fight):
                    # print(fight)
                    set_of_fight.add(fight)

    print("Case #{}: {}".format(testcase + 1, len(set_of_fight)))
