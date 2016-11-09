
from tokerynx.tokenizian import Tokenizian

if __name__ == "__main__":

    from datasets.allDataset import dataset
    import gc


    totalData = 0
    correctData = 0

    for data in dataset:
        print('Input:', data)
        expected = dataset[data]
        totalData += 1

        t = Tokenizian(data)

        gc.collect()

        if len(t.longestMatchingTokenizations) < 1:
            print('** Expected:', expected)
            print('** Failed to tokenize')
        else:
            actual = t.longestMatchingTokenizations[0]
            if expected == actual:
                correctData += 1
                print('Output:', actual)
            else:
                print('Expected:', expected)
                print('Actual:', actual)
                print('LongestMatchingTokenizations:', len(t.longestMatchingTokenizations))
                print('MatchingTokenizations:', len(t.possibleTokenizations))

        print(correctData, totalData)
        print('------------------------------------------------------')

    print('Accuracy:', correctData/totalData)
