a = list(map(int, input().split() ))  #斷開，整數，變數
ans = a[0]
for x in a: #取最前面的數字a[0]
  if x>ans: #for迴圈，把a的每個數字x都迴一次
    ans = x #如果現在的x比ans還大
print('最大值是', ans)  #更新答案

for x in a: #離開迴圈時，便找到ans
  print(x)