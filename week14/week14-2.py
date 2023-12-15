# 但是，我們想慢慢理解 set() 到底怎麼用
s = {1,2,3,4}
print(s)
s = set( (1,3,5,7) )
print(s)
s = set( [1,2,4,3] )
print(s)
s = set( 'Hello' )
print(s)

s.add(100)
print(s)
s.remove('H')
print(s)