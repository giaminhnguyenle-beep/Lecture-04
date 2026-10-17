shots = [
    {"shot_id": 1, "elbow_jitter_deg": 2.4, "release_height_norm": 1.31},
    {"shot_id": 2, "elbow_jitter_deg": 5.8, "release_height_norm": 1.18},
    {"shot_id": 3, "elbow_jitter_deg": 3.1, "release_height_norm": 1.27},
    {"shot_id": 4, "elbow_jitter_deg": 2.7, "release_height_norm": 1.29},
]


def mean_value(s, f):
    return sum(x[f] for x in s) / len(s)


def add_distance_from_mean(s, f):
    m = mean_value(s, f)
    return [{**x, "distance_from_mean": abs(x[f] - m)} for x in s]


def rank_by_(s):
    return sorted(
        add_distance_from_mean(s, "elbow_jitter_deg"),
        key=lambda x: x["distance_from_mean"],
    )


print(f"Mean Jitter: {mean_value(shots,'elbow_jitter_deg')}")
for r in rank_by_consistency(shots):
    print(r)
print(
    "A smaller distance from the group mean indicates less deviation in elbow jitter, representing higher consistency in shooting form. Shots closest to the mean are ranked first because they align most closely with the average performance baseline. Conversely, larger distances reflect greater variance and lower consistency."
)
