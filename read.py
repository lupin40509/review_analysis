data = [] #存入 data
count = 0 #留言計次
w_count = 0 #字數計次
small = 0 #留言長度小於100的數量
big = 0 #留言長度大於100的數量

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		w_count += len(line)
		count += 1 
		if len(line) < 100:
			small += 1
		elif len(line) > 100:
			big += 1

print('檔案讀取完成,總共有', len(data),'筆資料')	
#print('共有%d字元' % w_count)
print('每筆留言平均長度為 %.2f' % (w_count / count))
print('留言長度小於100一共有 %d 筆' % small)
print('留言長度大於100一共有 %d 筆' % big)