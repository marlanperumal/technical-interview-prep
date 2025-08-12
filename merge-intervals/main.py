def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given a collection of intervals, merge all overlapping intervals. For example, [[1,3],[2,6],[8,10],[15,18]] should become [[1,6],[8,10],[15,18]]
    """

    if len(intervals) == 0:
        return []

    sorted_intervals = sorted(intervals)
    merged_intervals = []
    current_interval = sorted_intervals[0]

    for interval in sorted_intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            merged_intervals.append(current_interval)
            current_interval = interval

    merged_intervals.append(current_interval)
    return merged_intervals


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
