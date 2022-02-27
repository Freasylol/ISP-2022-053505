class LogicUnit:

    @staticmethod
    def getWords(text):
        text = text.replace('\n', ' ')
        text = text.replace(',', '')
        text = text.replace('.', '').replace('?', '').replace('!', '')
        text = text.lower()
        words = text.split()
        words.sort()
        return words

    @staticmethod
    def getwordsDict(words, n):
        wordsDict = dict()

        for word in words:
            if len(word) == n:
                if word in wordsDict:
                    wordsDict[word] = wordsDict[word] + 1
                else:
                    wordsDict[word] = 1
        return wordsDict

    @staticmethod
    def getSortedDict(dict):
        sortedValues = sorted(dict.values(), reverse=True)
        sortedDict = {}
        counter = 0
        for value in sortedValues:
            for key in dict.keys():
                if dict[key] == value:
                    if sortedDict.get(key) is None:
                        sortedDict[key] = dict[key]
                        break
        return sortedDict

    @staticmethod
    def getAverageAmountOfWords(wordsDict, text):
        dotCounter = 0
        for el in text:
            if (el == '.'):
                dotCounter += 1
        return

    @staticmethod
    def calcWordsInSentence(text):
        wordArr = []
        counter = 1
        i = 0
        while (i < len(text) - 1):
            if (text[i] == ' '):
                counter += 1
            elif ((text[i] == '.' or text[i] == '!'or text[i] == '?') and
                  text[i + 1] == ' '):
                wordArr.append(counter)
                counter = 1
                i += 1
            i += 1
        wordArr.append(counter)
        return wordArr

    @staticmethod
    def countAverageAmount(wordArr):
        counter = 0
        for wordCount in wordArr:
            counter += wordCount
        return counter / len(wordArr)

    @staticmethod
    def countMedianCount(wordArr):
        if (len(wordArr) > 1):
            middleIndex = round(len(wordArr) / 2)
            return (wordArr[middleIndex - 1] + wordArr[middleIndex]) / 2

    @staticmethod
    def calcWords(text):
        wordArr = []
        counter = 1
        for el in text:
            if (el == ' '):
                counter += 1
            elif (el == '.'):
                wordArr.append(counter)
                counter = 1
        return wordArr

    @staticmethod
    def countAverageAmount(wordArr):
        counter = 0
        for wordCount in wordArr:
            counter += wordCount
        return counter / len(wordArr)

    @staticmethod
    def countMedianCount(wordArr):
        if (len(wordArr) > 1):
            wordArr = sorted(wordArr)
            middleIndex = round(len(wordArr) / 2)
            return (wordArr[middleIndex - 1] + wordArr[middleIndex]) / 2

    @staticmethod
    def showDict(dict, k):
        counter = 0
        for el in dict:
            if (counter < k):
                print(el.ljust(20), dict[el])
                counter += 1
