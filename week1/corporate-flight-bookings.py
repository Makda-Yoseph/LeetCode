class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*n
        for book in bookings:
            prefix[book[0]-1] += book[2]
            if book[1]<n:
                prefix[book[1]] += (book[2]*-1)
        
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        return prefix
        