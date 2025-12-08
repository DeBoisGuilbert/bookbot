def count_words(text):
    all_words = text.split()
    return len(all_words)

def count_characters(text):
    char_count = {}
    for c in text:
        ch = c.lower()
        if char_count.get(ch) == None:
            char_count[ch] = 1
        else:
            char_count[ch] += 1

    return char_count

def sort_on(items):
    return items["num"]

def sorted_list_of_dicts(char_dict):
    char_count_list = []
    for key, val in char_dict.items():
        char_count_list.append({"char":key, "num":val})

    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list
    
    
    