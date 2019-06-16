

def recurse(search_eng_list, queries_list, choice = "", minimum = 0, count = 0):

  most_minimum = len(queries_list)
  copy_queries_list = queries_list[:]
  if(choice != ""):
    while(len(copy_queries_list) > 0):
      print("COUNT:", count, "Choice:", choice, "Front of Query:", copy_queries_list[0])
      if(choice != copy_queries_list[0]):
        print("Popped")
        copy_queries_list.pop(0)
      else:
        break
    print("COUNT:", count, "Path:", choice, "After popping Query List:", copy_queries_list)

  if(len(copy_queries_list) == 0):
    return minimum

  for a in search_eng_list:
      # print("Path:", choice, "Query List:", copy_queries_list
    if(len(copy_queries_list) > 0):
      if(a != copy_queries_list[0]):
        # print("Possible Paths:", search_eng_list)
        print("COUNT:", count, "RECURSE Path:", a, "Queries:", copy_queries_list)
        minimum = recurse(search_eng_list, copy_queries_list, a, minimum + 1, count + 1)
        copy_queries_list = queries_list[:]
        if(minimum < most_minimum):
          most_minimum = minimum


  return most_minimum


if __name__ == "__main__":
  search_eng_list = ["Yeehaw", "NSM", "Dont Ask", "B9", "Googol"]
  # queries_list = ["Yeehaw", "Yeehaw", "Googol", "B9", "Googol", "NSM", "B9", "NSM", "Dont Ask", "Googol"]
  queries_list = ["Googol", "Dont Ask", "NSM", "NSM", "Yeehaw", "Yeehaw", "Googol"]

  my_minimum = recurse(search_eng_list, queries_list)
  print(my_minimum)
