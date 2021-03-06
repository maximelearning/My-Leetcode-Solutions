
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[n + m - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[n + m - 1] = nums1[m - 1]
            m -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


a = [1, 2, 3, 0, 0, 0, 0, 0]
m = 3
b = [0, 2, 3, 5, 8]
n = 5
merge(a, m, b, n)
print(a)
