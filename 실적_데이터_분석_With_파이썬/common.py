
# code 3-28 높은 신뢰 구간 계산하기
def compute_high_confidence_interval(likelihoods, bin_width):
    peak_index = likelihoods.argmax()
    area = likelihoods[peak_index] * bin_width
    start_index, end_index  = peak_index, peak_index + 1
    while area < 0.95:
        if start_index > 0:
            start_index -= 1
        if end_index < likelihoods.size-1:
            end_index += 1

        area = likelihoods[start_index : end_index+1].sum() * bin_width

    range_start, range_end = bin_edges[start_index], bin_edges[end_index]
    range_string = f"{range_start:.6f}-{range_end:.6f}"
    print((f"빈도 범위 {range_string} 는 {100 * area:.2f} % 신뢰 구간을 나타냅니다"))
    return start_index, end_index


def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space
                if event_condition(outcome)])

# from 코드 1-11
def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                    for outcome in event)
    return event_size / sum(generic_sample_space.values())


