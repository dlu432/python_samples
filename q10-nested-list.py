


if __name__ == '__main__':

    markList = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        markList.append([name,score])

    secondMark = sorted(list(set([score for name, score in markList])))[1]

    print("\n".join([name for name, score in sorted(markList) if score == secondMark]))
