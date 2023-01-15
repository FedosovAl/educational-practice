players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код

result = []
for key, score in players.items():
    name, surname = key
    score_1, score_2, score_3 = score
    result.append((name, surname, score_1, score_2, score_3))
print(result)