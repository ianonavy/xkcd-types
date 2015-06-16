def compute_ranges(values):
    all_values = []
    for first, second in zip(values, values[1:]):
        all_values += list(range(first, second, 1 if first < second else -1))
    return all_values + [values[-1]]
