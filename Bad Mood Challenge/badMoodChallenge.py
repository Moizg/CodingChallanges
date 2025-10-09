def greatestImpact(schedule, low_threshold=7, scale_meals=True):
    counts = {"Weather": 0, "Meals": 0, "Sleep": 0}

    def meals_val(m):  # optional scaling
        return (m * 10 / 3) if scale_meals else m

    low_days = 0
    for mood, weather, meals, sleep in schedule:
        if mood < low_threshold:
            low_days += 1
            diffs = {
                "Weather": abs(mood - weather),
                "Meals":   abs(mood - meals_val(meals)),
                "Sleep":   abs(mood - sleep),
            }
            min_d = min(diffs.values())
            # award all ties (if any) to avoid bias
            for k, v in diffs.items():
                if v == min_d:
                    counts[k] += 1

    # If no low-mood days, you can choose to return None or analyze all days.
    if low_days == 0:
        return None

    # Pick the factor with the most “wins”. Dict preserves insertion order for tie-breaks.
    return max(counts, key=counts.get)


# Examples
print(greatestImpact([
  [1, 1, 3, 10],
  [1, 1, 3, 10],
  [1, 1, 3, 10]
]))  # -> "Weather"

print(greatestImpact([
  [8, 9, 3, 10],
  [2,10, 1,  9],
  [1, 9, 1,  8]
]))  # -> "Meals"

print(greatestImpact([
  [8, 9, 3, 10],
  [2, 10, 1, 9],
  [1, 9, 1, 8]
]))

print(greatestImpact([
  [10, 9, 3, 9],
  [1, 8, 3, 4],
  [10, 9, 2, 8],
  [2, 9, 3, 2]
]))