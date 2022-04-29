from LogicUnit import LogicUnit


file = open('text.txt', 'r')
text = file.read()


class Program:

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

        words = LogicUnit.get_words(text)
        words_dict = LogicUnit.get_words_dict(words, n)
        word_arr = LogicUnit.calc_words_in_sentence(text)

        print(f'Average amount of words in sentence:{LogicUnit.count_average_amount(word_arr)}')
        print(f'Median amount of words in sentence:{LogicUnit.count_median_count(word_arr)}')
        
        sorted_dict = LogicUnit.getsorted_dict(words_dict)
        LogicUnit.show_dict(sorted_dict, k)


Program.main()
