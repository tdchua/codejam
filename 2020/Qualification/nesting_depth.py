#Qualification Round - Problem 2
#Timothy Joshua Dy Chua


if __name__ == "__main__":

  testcases = int(input())
  for test in range(testcases):

    input_string = input()
    input_string_converted = [int(letter) for letter in input_string]

    my_queue = []
    parenthesis_counter = 0

    for character in input_string_converted:

      if(character == 0 and parenthesis_counter == 0):
        my_queue.append(character)

      else:
        if(character > parenthesis_counter):
          while(character > parenthesis_counter):
            my_queue.append('(')
            parenthesis_counter += 1

        elif(character < parenthesis_counter):
          while(character < parenthesis_counter):
            my_queue.append(')')
            parenthesis_counter -= 1

        my_queue.append(character)

    while(parenthesis_counter > 0):
      my_queue.append(')')
      parenthesis_counter -= 1

    my_queue = map(str, my_queue)
    my_queue = "".join(my_queue)

    print("Case #" + str(test+1) + ": " + my_queue)
