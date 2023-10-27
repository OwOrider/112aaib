class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
               #剛剛沒寫完,.....如果n是負的,就錯了!!!! 0也是錯
        if n <= 0: return False #現在成功了
        while n >1: # 因為1是2的0次方 不用在餘了
            if n%2 !=0: #竟然餘數不是0
                return False #失敗