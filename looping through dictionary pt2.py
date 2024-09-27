#Checkpoint
#ride = {
#    "Emily": 89,
#    "Ryan": 190,
#    "Eli": 183,
#    "Savanna": 92,
#    "Tyler": 165
#}
#for x in ride.values():
#    if x >= 100:
#        print("This person is tall enough to ride.")
#    else:
#        print("This person is too short to ride.")
#Check for a key challenge
#dictionary = { 7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth" }

#my_list = [int(n) for n in input("Input a list of numbers").split()]

#for x in my_list:
#    if x in dictionary:
#        print("Yes")
#    else:
#        print("No")
#Word Frequency challenge
input_string = input("Enter a list of words separated by spaces: ")

words = input_string.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_word = ""
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        max_word = word
        max_count = count
print("The most frequent word is:", max_word)