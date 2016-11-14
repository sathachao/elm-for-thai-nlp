
from tokerynx.tokenizian import Tokenizian

if __name__ == "__main__":

    from datasets.allDataset import dataset
    import gc


    totalData = 0
    correctData = 0

    import time
    maxT = [0,0,0,0,0,0,0,0,0];
    minT = [100,100,100,100,100,100,100,100,100];
    # start = time.time()
    for data in dataset:

        start = time.time()

        # print('Input:', data)
        expected = dataset[data]
        totalData += 1

        t = Tokenizian(data)

        gc.collect()

        if len(t.longestMatchingTokenizations) < 1:
            pass
            # print('** Expected:', expected)
            # print('** Failed to tokenize')
        else:
            actual = t.longestMatchingTokenizations[0]
            if expected == actual:
                correctData += 1
                # print('Output:', actual)
            # else:
                # print('Expected:', expected)
                # print('Actual:', actual)
                # print('LongestMatchingTokenizations:', len(t.longestMatchingTokenizations))
                # print('MatchingTokenizations:', len(t.possibleTokenizations))

        # print(correctData, totalData)
        # print('------------------------------------------------------')

        end = time.time()
        maxT[expected.count('|') - 1] = max(maxT[expected.count('|') - 1], end - start)
        minT[expected.count('|') - 1] = min(minT[expected.count('|') - 1], end - start)
    print(maxT)
    print(minT)
    # print(end - start)
    print('Accuracy:', correctData/totalData)
