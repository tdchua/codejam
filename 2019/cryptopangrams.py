
def isprime(a):

  sqrt_a = int(a ** (0.5))
  if(sqrt_a * sqrt_a == a):
    return False
  # print(sqrt_a)
  for b in range(2, sqrt_a):
    if(a % b == 0):
      return False

  return True


if __name__ == "__main__":

  for testcase in range(int(input())):
    N, L = map(int, input().split())
    list_of_prod = list(map(int, input().split()))

    # print(isprime(121))
    my_list_of_prime = []
    for a in range(2, N + 1):
      if(isprime(a)):
        for b in list_of_prod:
          if(b % a == 0):
            my_list_of_prime.append(a)
            break

    print(my_list_of_prime)
