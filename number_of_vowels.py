""" module that returns the number of vowels in a string"""

def num_of_vowels(sample):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for letter in sample:
        if letter in vowels:
            vowel_count += 1
    
    return vowel_count

def main():
    test_string = "Hello what are you doing?"
    print('number of vowels in "' + test_string + '" = ', num_of_vowels(test_string))

if __name__ ==  '__main__':
    main()