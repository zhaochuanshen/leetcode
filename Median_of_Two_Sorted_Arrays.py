'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        def _kth(a, b, k):
            if not a:
                return b[k]
            if not b:
                return a[k]
            la = len(a) / 2
            lb = len(b) /2
            ma = a[la]
            mb = b[lb]
            if k > la + lb:
                if ma > mb:
                    return _kth(a, b[lb+1:], k-lb - 1)
                else:
                    return _kth(a[la+1:], b, k-la-1)
            else:
                if ma > mb:
                    return _kth(a[:la], b, k)
                else:
                    return _kth(a, b[:lb], k )
        if ( len(A) + len(B) )%2 == 1:
            return _kth(A, B, ( len(A) + len(B) )/2)
        else:
            return (_kth(A, B, ( len(A) + len(B) )/2) +  _kth(A, B, ( len(A) + len(B) )/2 -1) )/2.
