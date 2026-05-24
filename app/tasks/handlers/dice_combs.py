import random
from collections import Counter
from app.tasks.exceptions import PermanentJobError


def extract_dice_payload(payload: dict | None) -> int:
    """Валидация payload для DICE_COMBS_SIMULATION"""
    if payload is None:
        raise PermanentJobError("DICE_COMBS_SIMULATION requires payload")

    trials = payload.get("trials")

    if trials is None:
        raise PermanentJobError("DICE_COMBS_SIMULATION requires trials")

    if not isinstance(trials, int) or trials <= 0:
        raise PermanentJobError("trials must be a positive integer")

    return trials


def simulate_dice_combinations(trials: int) -> dict:
    """Моделирование бросков 5 кубиков методом Монте-Карло"""
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for _ in range(trials):
        dice = [random.randint(1, 6) for _ in range(5)]
        freq = Counter(dice)
        max_count = max(freq.values())

        if max_count == 1:
            category = 1
        elif max_count == 2:
            category = 2
        elif max_count == 3:
            category = 3
        elif max_count == 4:
            category = 4
        else:
            category = 5

        counts[category] += 1

    probabilities = {
        k: round(count / trials, 3) for k, count in counts.items()
    }

    return {
        "trials": trials,
        "counts": counts,
        "probabilities": probabilities
    }