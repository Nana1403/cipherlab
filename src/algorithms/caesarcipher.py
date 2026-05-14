
alphabet_mapping = {  
              "a": 0, "b": 1,  "c": 2,
              "d": 3, "e": 4, "f": 5, 
              "g": 6, "h": 7, "i": 8,
              "j": 9, "k": 10, "l": 11,
              "m": 12, "n": 13, "o": 14, 
              "p": 15, "q": 16, "r": 17,
              "s": 18, "t": 19, "u": 20,
              "v": 21, "w": 22,  "x": 23,
              "y": 24,  "z": 25 } 

def encryption(message, key):
         
     current_nums =  []

     for i in range(len(message)):
         new_mes_num = alphabet_mapping[message[i]] + key
         
         #deals with negative numbers  or numbers greater than 26
         if new_mes_num < 0:
            new_mes_num += 26
         elif new_mes_num > 26:
            new_mes_num -=26

         current_nums.append(new_mes_num)
  
     letters = []

     for i in range(len(current_nums)):
        for let, num in alphabet_mapping.items():
            if num == current_nums[i]:
               letters.append(let)

     return "".join(letters)

    
def decryption(message, key): 

    current_nums = []

    for i in range(len(message)):
         new_mes_num = alphabet_mapping[message[i]] - key

         if new_mes_num < 0:
            new_mes_num += 26
         elif new_mes_num > 26:
            new_mes_num -=26

         current_nums.append(new_mes_num)

    letters = []

    for i in range(len(current_nums)):
        for let, num in alphabet_mapping.items():
            if num == current_nums[i]:
               letters.append(let)

    return "".join(letters)


def brute_force(message):  # alphabet_mapping, message

    results = []

    for k in alphabet_mapping.values():
        current_nums = []

        for i in range(len(message)):
            new_mes_num = alphabet_mapping[message[i]] - k

            if new_mes_num < 0:
               new_mes_num += 26
            elif new_mes_num > 26:
                 new_mes_num -=26

            current_nums.append(new_mes_num)
            
        letters = []

        for i in range(len(current_nums)): 
            for let , num in alphabet_mapping.items():
               if num == current_nums[i]:
                  letters.append(let)
                  section = len(message)

        for j in range(0, len(current_nums), section):
            chunk = letters[j:j+section]
            results.append(f"Key: {k}, {"".join(chunk)}")

    return "\n".join(results)
      
