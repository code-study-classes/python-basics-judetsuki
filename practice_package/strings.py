extract_file_name = lambda file_name: file_name.rsplit("/", 1)[-1].split(".")[0]


def encrypt_sentence(sentence: str) -> str:
    odd_chars = sentence[1::2]
    even_chars = sentence[0::2][::-1]
    return odd_chars + even_chars


def check_brackets(str):
    stack = []
    for char in str:
        if (char == '('):
            stack.append(str.index(char))
        if (char == ')'):
            if ((len(stack)) == 0 and (str.index(char) == 0)):
                return 1
            elif (len(stack) == 0):
                return (str.index(char))
            else: stack.pop()
    if (len(stack) >0):
        return -1
    else: return 0
        
        
            


def reverse_domain(str):
    if '.' in str:
        parts = str.split('.')
        reversed_parts = parts[::-1]
        return '.'.join(reversed_parts)
    else:
        return str

            

def count_vowel_groups(word: str) -> int:
    vowels = set("aeiouy")
    word = word.lower()
    count = 0
    in_group = False

    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False

    return count
