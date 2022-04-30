def gen_word_permutations(list_characters, list_words, currentword):
  if(len(list_characters) == 0):
    list_words.append(currentword)
  else:
    newString = ""
    for character_idx in range(len(list_characters)):
      #Highlight and not highlight
      #Highlight
      newString = currentword + list_characters[character_idx] * 2
      gen_word_permutations(list_characters[character_idx+1:], list_words, newString)
      #Not Highlight
      newString = currentword + list_characters[character_idx] 
      gen_word_permutations(list_characters[character_idx+1:], list_words, newString)
      currentword = newString
      
  return None

if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    string_to_check = input()
    list_characters = [a for a in string_to_check]
    list_words = []
    gen_word_permutations(list_characters, list_words, "")
    list_words.sort()
    print(f"Case #{i+1}: {list_words[0]}")
