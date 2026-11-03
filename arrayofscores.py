import sys

scores = list(map(int, sys.argv[1:]))

if len(scores) > 0:
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

else:
    print("Please enter scores")