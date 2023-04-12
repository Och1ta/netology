my_list = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'
a_list = []


def count_letter(my_list):
    for word in my_list:
        if letter in word:
            a_list.append(word)
    print(len(a_list))
    return a_list


print(count_letter(my_list))
