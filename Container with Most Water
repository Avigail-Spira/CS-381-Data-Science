height = [1,8,6,2,5,4,8,3,7]
max = 0

for i in range(0, len(height)+1):
  for k in range (i, len(height)):
    if height[i] < height[k]:
        area = height[i] * (k-i)
    elif height[k] < height[i]:
      area = height[k] * (k-i)
    
    if area > max:
      max = area
   
print(max)
