test_cases = int(input())

def trial(nums: list, score: list | None):
    for i, num in enumerate(nums):
        if (score and (sum(score) + num) % 2 == 1) or num % 2 == 1:
            nums.pop(i)
            score.append(num)
            trial(nums, score)
        elif i + 1 == len(nums):
            score.append(0)
        else:
            trial(nums, score)
    
    return score
for _ in range(test_cases):
    denominations = list(map(int, input().split()))

    denominations.sort()
    print(' '.join(trial(denominations, [])))