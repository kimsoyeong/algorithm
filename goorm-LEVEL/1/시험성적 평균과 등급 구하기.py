scores = list(map(int, input().split()))
avg = round(sum(scores)/3, 2)

if avg >= 90:
	print(f'{avg:.2f} A')
elif avg >= 80:
	print(f'{avg:.2f} B')
elif avg >= 70:
	print(f'{avg:.2f} C')
elif avg >= 60:
	print(f'{avg:.2f} D')
else:
	print(f'{avg:.2f} F')