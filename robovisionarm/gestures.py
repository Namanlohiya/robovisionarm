import math

def clamp(x, min_val, max_val):

    return max(min_val, min(x, max_val))


def map_range(x, in_min, in_max, out_min, out_max):

    return int(
        (x - in_min)
        * (out_max - out_min)
        / (in_max - in_min)
        + out_min
    )


def palm_size(hand):

    wrist = hand.landmark[0]
    index = hand.landmark[5]

    return math.sqrt(
        (wrist.x-index.x)**2 +
        (wrist.y-index.y)**2 +
        (wrist.z-index.z)**2
    )


def pinch_distance(hand):

    thumb = hand.landmark[4]
    index = hand.landmark[8]

    return math.sqrt(
        (thumb.x-index.x)**2 +
        (thumb.y-index.y)**2 +
        (thumb.z-index.z)**2
    )