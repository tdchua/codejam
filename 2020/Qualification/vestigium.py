#Qualification Round - Problem 1
#Timothy Joshua Dy Chua



if __name__ == "__main__":

  testcases = int(input())
  for testcase in range(testcases):

    matrix_size = int(input())
    my_matrix = []
    my_matrix_transposed = []

    for row_idx in range(matrix_size):
      row_elements = list(map(int, input().split()))
      my_matrix.append(row_elements)

      for col_idx in range(matrix_size):
        if(row_idx == 0):
          my_matrix_transposed.append([])

        my_matrix_transposed[col_idx].append(row_elements[col_idx])

    #For the trace
    col_index = 0
    trace = 0
    for row in my_matrix:
      trace += row[col_index]
      col_index += 1

    #For the rows
    duplicate_in_row = 0
    for row in my_matrix:
      if(len(set(row)) != matrix_size):
        duplicate_in_row += 1

    #For the columns
    duplicate_in_column = 0
    for row in my_matrix_transposed:
      if(len(set(row)) != matrix_size):
        duplicate_in_column += 1

    print("Case #" + str(testcase+1) + ":", trace, duplicate_in_row, duplicate_in_column)
