if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    min_score = min(scores, key=lambda x: x[1])
    scores = [score for score in scores if score[1] > min_score[1]]
    second_min_score = min(scores, key=lambda x: x[1])
    scores = [score for score in scores if score[1] == second_min_score[1]]
    scores.sort(key=lambda x: x[0])

    for score in scores:
        print(score[0])
