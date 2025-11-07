import numpy as np

scores = np.array([75,72,61,64,78,79,66,63,77,75])
total_scores = np.array([475,172,661,264,78,179,266,763,177,275])

print("Average score:,",np.mean(scores))
print("Maxinum score:,",np.max(scores))
print("Minimum score:,",np.min(scores))
print("Total score:,",np.sum(scores))

print("Standard Deviation:,",np.std(scores))


print("first score:",scores[0])
print("last score:",scores[-1])
print("Scores > 75:",scores[scores>75])
