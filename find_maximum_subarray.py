def find_max_crossing_subarray(A, low, mid, high):
    now_left = A[mid]
    left_sum = A[mid]
    max_left = mid
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + A[i]
        if now_left > left_sum:
            left_sum = now_left
            max_left = i

    now_right = A[mid + 1]
    right_sum = A[mid + 1]
    max_right = mid + 1
    for j in range(mid + 2, high + 1):
        now_right = now_right + A[j]
        if now_right > right_sum:
            right_sum = now_right
            max_right = j
    return max_left, max_right, right_sum+left_sum

def find_maximum_subarray(low, high, A):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high)//2
        left_low, left_high, left_sum = find_maximum_subarray(low, mid, A)
        right_low, right_high, right_sum = find_maximum_subarray(mid + 1, high, A)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


A = [-23, 18, 20, -7, 12, -5, -8]
a, b, c, = find_maximum_subarray(0, 6, A)

print(a, b, c)


