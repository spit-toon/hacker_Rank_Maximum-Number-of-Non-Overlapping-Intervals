def maximizeNonOverlappingMeetings(meetings):
    # Edge case: no meetings
    if not meetings:
        return 0

    # Step 1: Sort meetings by end time
    meetings.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    # Step 2: Greedily select meetings
    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    return count




