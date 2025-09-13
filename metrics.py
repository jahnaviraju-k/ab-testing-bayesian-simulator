def cr(successes: int, trials: int) -> float:
    return successes / max(trials, 1)
