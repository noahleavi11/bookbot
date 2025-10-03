def get_num_words(text):
    count = len(text.split())
    print(f"Found {count} total words")

def get_num_characters(text):
    lowers = text.lower()
    count_dict = {}
    for char in lowers:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def report(this_dict):
    dict_list = [] 
    for v in this_dict:
        dict_list.append({"char": v, "num": this_dict[v] })
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list
