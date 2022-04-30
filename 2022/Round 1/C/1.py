# def gen_permutations(curr_word, word_choice, answers):
#   if(len(word_choice) == 0):
#     if(curr_word not in answers):
#       answer = checker(curr_word)
#       if(answer != "IMPOSSIBLE"):
#         answers.add(answer)
#     return answers
#   else:
#     curr_word_copy = curr_word
#     i = 0
#     while(i < len(word_choice)):
#       new_word = word_choice[i] + curr_word_copy 
#       word_choice_copy = word_choice.copy()
#       word_choice_copy.pop(i)
#       answers = gen_permutations(new_word, word_choice_copy, answers)
# 
#       new_word = curr_word_copy + word_choice[i]
#       answers = gen_permutations(new_word, word_choice_copy, answers)
#       i += 1
#     return answers
# 
def check_same_letter(word):
  same_letter = word[0]
  for char in word[1:]:
    if(char != same_letter):
      return False
    
  return True

def checker(word):
  explored = set()
  prev_char = word[0]
  explored.add(prev_char)
  answer = word
  for char in word[1:]:
    if(char == prev_char):
      continue
    else:
      if(char in explored):
        answer = "IMPOSSIBLE"
        break
      else:
        explored.add(char)

    prev_char = char

  return answer
# 
        
if __name__ == "__main__":
  testcases = int(input())
  for k in range(testcases):
    num_words = input()
    words = input().split()
    dict_words = {}
    # print(words)
    i = 0
    answers = set()
    
    for i in words:
      dict_words[i] = (i[0], i[-1])
    
    i = 0
    while(i < len(words)):
      base = words[i]
      j = i + 1
      while(j < len(words)):
        # print(words)
        # print(base, words[j])
        if(check_same_letter(words[j])):
          # print(words[j])
          start_letter = dict_words[base][0]
          end_letter = dict_words[base][1]
          # print("Start: {}, End: {}".format(start_letter,end_letter))
          if(dict_words[words[j]][0] == end_letter):
            words[i] = base + words[j]
            dict_words[words[i]] = (words[i][0], words[i][-1])
            base = words[i]
            words.pop(j)
            j = i + 1
          elif(dict_words[words[j]][1] == start_letter):
            words[i] = words[j] + base
            dict_words[words[i]] = (words[i][0], words[i][-1])
            base = words[i]
            words.pop(j)
            j = i + 1
          else:
            j += 1
        else:
          j += 1
      i += 1
    # print(words)
    i = 0
    while(i < len(words)):
      base = words[i]
      j = i + 1
      
      while(j < len(words)):
        # print(words)
        # print(base, words[j])
        start_letter = dict_words[base][0]
        end_letter = dict_words[base][1]
        # print("Start: {}, End: {}".format(start_letter,end_letter))
        if(dict_words[words[j]][0] == end_letter):
          words[i] = base + words[j]
          dict_words[words[i]] = (words[i][0], words[i][-1])
          base = words[i]
          words.pop(j)
          j = i + 1
        elif(dict_words[words[j]][1] == start_letter):
          words[i] = words[j] + base
          dict_words[words[i]] = (words[i][0], words[i][-1])
          base = words[i]
          words.pop(j)
          j = i + 1
        else:
          j += 1
      i += 1
    # print(words)
    answer = "".join(words)
    answer = checker(answer)
    

    print(f"Case #{k+1}: {answer}")
  
    
