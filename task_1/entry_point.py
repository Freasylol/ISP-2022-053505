from logic_unit import logic_unit


with open('text.txt', 'r') as file:
    text = file.read()


class program:

    def main():
        k = 10
        n = 4
        print('You want to use default values?(y/n)')
        choice = input()
        if (choice != 'y'):
            print('How many n-grams you want to see in list?(k)')
            k = int(input())
            print('Enter length of n-grams(n)')
            n = int(input())
        words = logic_unit.get_words(text)
        words_dict = logic_unit.get_words_dict(words, n)
        word_arr = logic_unit.calc_words_in_sentence(text)
        print(f'Average amount of words in sentence:{logic_unit.count_average_amount(word_arr)}')
        print(f'Median amount of words in sentence:{logic_unit.count_median_count(word_arr)}')
        sorted_dict = logic_unit.getsorted_dict(words_dict)
        logic_unit.show_dict(sorted_dict, k)


program.main()
