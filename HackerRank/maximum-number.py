if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = set(arr)
    unique_scores.remove(max(unique_scores))
    runner_up_score = max(unique_scores)
    print(runner_up_score)
