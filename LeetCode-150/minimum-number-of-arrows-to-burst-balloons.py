def findMinArrowShots(points):
    """
    This function calculates the minimum number of arrows needed to shoot down all balloons.

    Parameters:
    points (list of tuples): A list of balloon intervals. Each interval is represented as a tuple (start, end), where start and end are integers.

    Returns:
    int: The minimum number of arrows needed to shoot down all balloons.
    """
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows = 1
    last_arrow_position = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > last_arrow_position:
            arrows += 1
            last_arrow_position = points[i][1]

    return arrows