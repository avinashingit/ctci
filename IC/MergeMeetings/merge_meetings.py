class MergeMeetings:
    def __init__(self, meetings):
        self.meetings = meetings

    def mergeMeetings(self):
        sorted_meetings = sorted(self.meetings)
        merged_meetings = [sorted_meetings[0]]
        for start, end in sorted_meetings[1:]:
            pstart, pend = merged_meetings[-1]
            if start <= pend:
                merged_meetings[-1] = (pstart, max(end, pend))
            else:
                merged_meetings.append((start, end))
        return merged_meetings


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
merged_meetings = MergeMeetings(meetings)
merged_meetings.mergeMeetings()
