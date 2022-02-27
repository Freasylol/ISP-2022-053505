from logicUnit import LogicUnit


with open('text.txt', 'r') as file:
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
        words = LogicUnit.getWords(text)
        wordsDict = LogicUnit.getwordsDict(words, n)
        wordArr = LogicUnit.calcWordsInSentence(text)
        print(f'Average amount of words in sentence:{LogicUnit.countAverageAmount(wordArr)}')
        print(f'Median amount of words in sentence:{LogicUnit.countMedianCount(wordArr)}')
        sortedDict = LogicUnit.getSortedDict(wordsDict)
        LogicUnit.showDict(sortedDict, k)


Program.main()
