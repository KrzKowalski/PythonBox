fruits = ['apple', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple', 'apple', 'dupa', 'kiwi', 'apple']

# PROTOTYPE:
# for i in range(0, len(fruits)):
#     search = fruits.index('apple', i)
#     search_set = set(search)
#
#     print(f"The index position of an 'apple' => {search_set}")

# OUTCOME:
search = [fruits.index('apple', i) for i in range(len(fruits))]
print(set(search))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
plain_index = []
plain_text = "krzysztof"
for letter in plain_text:
    plain_index.append(alphabet.index(letter))
print(plain_index)
# search2 = [alphabet.index(i,i) for i in range(len(alphabet))]

dany_string = '{ExternalReference} == "xxxx151515"'
lista = ['{Fund}', '("FNMA","USTRESURY")', '{Exposure}', '"PrivatePlacement"', '{Exposure}', '"Bond"']
search2 = [dany_string.find('"', i) for i in range(len(dany_string))]
# search3 = list(set(search2))
# search3.sort()
# print(dany_string[search3[0]:search3[1]+1])
search_list = [dany_string.find('"', i) for i in range(len(dany_string))]