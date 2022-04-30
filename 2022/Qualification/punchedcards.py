def first_row(col):
  first_line = ".." + ("+-" * (col-1)) + "+\n"
  second_line = ".." + ("|." * (col-1)) + "|\n"
  return first_line + second_line
def succeeding_row(col):
  first_line = ("+-" * col) + "+\n"
  second_line = ("|." * col) + "|\n"
  return first_line + second_line
def last_line(col):
  last_line = ("+-" * col) + "+\n"
  return last_line


if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    row, col = map(int, input().split())
    print(f"Case #{i+1}:")
    for r in range(row):
      if(r == 0):
        print(first_row(col), end='')
      else:
        print(succeeding_row(col), end='')
    
    print(last_line(col), end='')
