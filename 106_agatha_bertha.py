# Write a function that returns True if the total area of chocolate is the same for each sister

# Agatha's pieces: [4, 3], [2, 4], [1, 2]
# Bertha's pieces: [6, 2], [4, 2], [1, 1], [1, 1]

# Total area of Agatha's chocolate:       4x3 + 2x4 + 1x2 = = 22
# Total area of Bertha's chocolate:       6x2 + 4x2 + 1x1 + 1x1 = = 22

def test_fairness(a, b):
    return sum([i[0]*i[1] for i in a]) == sum([i[0]*i[1] for i in b])

agatha=[[4, 3], [2, 4], [1, 2]]
bertha=[[6, 2], [4, 2], [1, 1], [1, 1]]
print(test_fairness(agatha,bertha))

agatha=[[4, 4], [2, 1]]
bertha=[[1, 2], [4, 2], [1, 2], [1, 1]]
print(test_fairness(agatha,bertha))

"""
True
False
"""
