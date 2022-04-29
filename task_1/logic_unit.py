from string import punctuation

punctuation_symb = [',', '.', '?', '!', '-']

end_sentence_symb = ['.', '?', '!']


class LogicUnit:

    @staticmethod
    def get_words(text):
        text = text.replace('\n', ' ')
        for symb in punctuation_symb:
            text = text.replace(symb, '')
        text = text.lower()
        words = text.split()
        words.sort()
        return words

    @staticmethod
    def get_words_dict(words, n):
        words_dict = {}

        for word in words:
            if len(word) == n:
                if word in words_dict:
                    words_dict[word] = words_dict[word] + 1
                else:
                    words_dict[word] = 1
        return words_dict

    @staticmethod
    def getsorted_dict(init_dict: dict):
        sorted_dict = dict(sorted(init_dict.items(), reverse=True, key=lambda x: x[1]))
        return sorted_dict

    @staticmethod
    def calc_words_in_sentence(text):
        word_arr = []
        counter = 1
        for el in text:
            if (el == ' '):
                counter += 1
            elif (el in end_sentence_symb):
                counter = 1 if 0 else counter
                word_arr.append(counter)
                counter = 0
        print(word_arr)
        return word_arr

    @staticmethod
    def count_average_amount(word_arr):
        counter = 0
        for word_count in word_arr:
            counter += word_count
        return counter / len(word_arr)

    @staticmethod
    def count_median_count(word_arr):
        if (len(word_arr) > 1):
            middle_index = round(len(word_arr) / 2)
            return (word_arr[middle_index - 1] + word_arr[middle_index]) / 2

    @staticmethod
    def calcWords(text):
        word_arr = []
        counter = 1
        for el in text:
            if (el == ' '):
                counter += 1
            elif (el == '.'):
                word_arr.append(counter)
                counter = 1
        return word_arr

    @staticmethod
    def count_average_amount(word_arr):
        return sum(word_arr) / len(word_arr)

    @staticmethod
    def count_median_count(word_arr):
        if (len(word_arr) > 1):
            word_arr = sorted(word_arr)
            middle_index = round(len(word_arr) / 2)
            return (word_arr[middle_index - 1] + word_arr[middle_index]) / 2

    @staticmethod
    def show_dict(dict, k):
        counter = 0
        for el in dict:
            if (counter < k):
                print(el.ljust(20), dict[el])
                counter += 1
