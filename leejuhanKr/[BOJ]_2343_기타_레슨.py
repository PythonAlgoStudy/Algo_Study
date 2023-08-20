from sys import stdin


def parametric_search(left, right, search_condition):
    """
    주어진 조건 함수를 사용하여 정렬된 배열에서 이진 탐색을 수행합니다.

    매개변수:
        arr (list): 탐색할 정렬된 배열입니다.
        left (int): 현재 탐색 범위의 왼쪽 인덱스입니다.
        right (int): 현재 탐색 범위의 오른쪽 인덱스입니다.
        condition_function (callable): 인덱스를 입력으로 받아 해당 인덱스의 요소가 조건을 만족하는지를
                                      판별하여 불리언 값을 반환하는 함수입니다.

    반환값:
        int: 주어진 조건을 만족하는 첫 번째 요소의 인덱스 또는 조건이 처음으로 거짓이 되는 삽입 지점입니다.

    이 함수는 'arr' 배열에서 'left'와 'right' 인덱스로 정의된 범위 내에서 이진 탐색을 수행합니다.
    'condition_function'은 요소의 조건을 판단하기 위해 사용됩니다. 만약 특정 인덱스의 요소가 조건을
    만족한다면, 탐색 범위는 왼쪽 하위 배열로 좁혀집니다. 그렇지 않으면 오른쪽 하위 배열로 좁혀집니다.
    함수는 조건이 처음으로 만족되는 인덱스나 조건이 처음으로 거짓이 되는 삽입 지점을 반환합니다.
    """
    while left <= right:
        mid = (left + right) // 2
        if search_condition(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def cumulative_exceeds_count(arr, threshold):
    """
    입력된 배열의 요소들을 누적하여 합한 값이 지정한 'threshold' 값을 넘거나 같게 되는 횟수를 반환
    """

    cumulative_sum = 0
    exceed_count = 1
    for element in arr:
        cumulative_sum += element
        if cumulative_sum > threshold:
            exceed_count += 1
            cumulative_sum = element

    return exceed_count


def solution(N, M, lecture_sizes):
    """
    강의 동영상을 블루레이로 녹화할 때, 블루레이의 크기(녹화 가능한 길이)를 최소값을 반환
    """

    min_disc_size = max(lecture_sizes)
    max_disc_size = N * min_disc_size
    can_fit_in_disc_condition = (
        lambda disc_size: cumulative_exceeds_count(lecture_sizes, disc_size) <= M
    )

    return parametric_search(
        min_disc_size,
        max_disc_size,
        can_fit_in_disc_condition,
    )


if __name__ == "__main__":
    N, M = map(int, stdin.readline().split())
    lecture_sizes = [*map(int, stdin.readline().split())]

    answer = solution(N, M, lecture_sizes)

    print(answer)
