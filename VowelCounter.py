def vowel_counter(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter your text: ")

print("Number of vowels:", vowel_counter(input_string))
