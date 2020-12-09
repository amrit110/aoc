def read_input(input_file):
    with open(input_file, "r") as f:
        return [line.split(",") for line in f.read().splitlines()]


class WireGridSolver:
    def __init__(self, traces):
        self.traces = traces
        self.paths = {0: [], 1: []}
        self.intersections = []
        self.wire_locs = {0: {"H": [], "V": []}, 1: {"H": [], "V": []}}

    def get_next_pos(self, curr_pos, direction, steps):
        if direction == "R":
            next_pos = (curr_pos[0] + steps, curr_pos[1])
            segment_type = "H"
        elif direction == "L":
            next_pos = (curr_pos[0] - steps, curr_pos[1])
            segment_type = "H"
        elif direction == "U":
            next_pos = (curr_pos[0], curr_pos[1] - steps)
            segment_type = "V"
        elif direction == "D":
            next_pos = (curr_pos[0], curr_pos[1] + steps)
            segment_type = "V"

        return next_pos, segment_type

    def run_trace(self):
        # assume central port at (0, 0) at bottom left
        for wire, trace in enumerate(self.traces):
            curr_pos = (0, 0)
            self.paths[wire].append(curr_pos)
            for t in trace:
                direction = t[0]
                steps = int(t[1:])
                next_pos, segment_type = self.get_next_pos(curr_pos, direction, steps)
                self.wire_locs[wire][segment_type].append((curr_pos, next_pos))
                self.paths[wire].append(next_pos)
                curr_pos = next_pos

    def compute_num_backtrace_steps(self, wire, pt):
        idx_pt = self.paths[wire].index(pt)
        backtrace = self.paths[wire][0 : idx_pt + 1]
        backtrace_len = 0
        for idx in range(len(backtrace) - 1):
            dist_bw_points = abs(backtrace[idx][0] - backtrace[idx + 1][0]) + abs(
                backtrace[idx][1] - backtrace[idx + 1][1]
            )
            backtrace_len += dist_bw_points

        return backtrace_len

    def compute_intersections(self):
        # horizontal segments of wire 0 with vertical segments of wire 1
        v_segments = self.wire_locs[1]["V"]
        for segment in self.wire_locs[0]["H"]:
            row_val = segment[0][1]
            segment_col_range = (segment[0][0], segment[1][0])
            left, right = min(segment_col_range), max(segment_col_range)
            v_segments_relevant = [
                s for s in v_segments if (s[0][0] > left) and (s[0][0] < right)
            ]
            for v_segment in v_segments_relevant:
                col_val = v_segment[0][0]
                segment_row_range = (v_segment[0][1], v_segment[1][1])
                top, bottom = min(segment_row_range), max(segment_row_range)
                if (row_val > top) and (row_val < bottom):
                    backtrace_len = (
                        self.compute_num_backtrace_steps(0, segment[0])
                        + abs(col_val - segment[0][0])
                        + self.compute_num_backtrace_steps(1, v_segment[0])
                        + abs(row_val - v_segment[0][1])
                    )
                    self.intersections.append((col_val, row_val, backtrace_len))

        # horizontal segments of wire 1 with vertical segments of wire 0
        v_segments = self.wire_locs[0]["V"]
        for segment in self.wire_locs[1]["H"]:
            row_val = segment[0][1]
            segment_col_range = (segment[0][0], segment[1][0])
            left, right = min(segment_col_range), max(segment_col_range)
            v_segments_relevant = [
                s for s in v_segments if (s[0][0] > left) and (s[0][0] < right)
            ]
            for v_segment in v_segments_relevant:
                col_val = v_segment[0][0]
                segment_row_range = (v_segment[0][1], v_segment[1][1])
                top, bottom = min(segment_row_range), max(segment_row_range)
                if (row_val > top) and (row_val < bottom):
                    backtrace_len = (
                        self.compute_num_backtrace_steps(1, segment[0])
                        + abs(col_val - segment[0][0])
                        + self.compute_num_backtrace_steps(0, v_segment[0])
                        + abs(row_val - v_segment[0][1])
                    )
                    self.intersections.append((col_val, row_val, backtrace_len))

    def find_closest_intersection(self):
        distances = []
        for point in self.intersections:
            distances.append(abs(point[0]) + abs(point[1]))

        return min(distances)

    def find_min_delay_intersection(self):
        return min([i[2] for i in self.intersections])

    def __call__(self):
        self.run_trace()
        self.compute_intersections()
        print(self.find_closest_intersection())  # Part One
        print(self.find_min_delay_intersection())  # Part Two


def solve():
    traces = read_input("input.txt")
    WireGridSolver(traces)()


if __name__ == "__main__":
    solve()
