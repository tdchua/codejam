#Qualification Round - Problem 3
#Timothy Joshua Dy Chua
if __name__ == "__main__":

  testcases = int(input())
  for testcase in range(testcases):

    jobs = int(input())
    list_of_jobs = []
    for job in range(jobs):

      start, end = map(int, input().split())
      my_tuple = [start, end, job]
      list_of_jobs.append(my_tuple)

    list_of_jobs.sort(key = lambda x : x[0])

    C_end = 0
    J_end = 0
    order_of_person = []
    impossible = False

    for job in list_of_jobs:

      if(C_end <= job[0]):
        C_end = job[1]
        job.append('C')

      elif(J_end <= job[0]):
        J_end = job[1]
        job.append('J')

      else:
        impossible = True
        break


    if(impossible == True):
      print("Case #" + str(testcase+1) + ": " + "IMPOSSIBLE")
    else:
      list_of_jobs.sort(key = lambda x : x[2])
      for job in list_of_jobs:
        order_of_person.append(job[3])
      print("Case #" + str(testcase+1) + ": " + "".join(order_of_person))
