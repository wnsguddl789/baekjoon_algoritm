x_list,y_list =[],[]
for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
       
sorted_x_list = sorted(x_list,reverse=True)
sorted_y_list = sorted(y_list,reverse=True)

if sorted_x_list[1] == max(sorted_x_list):
    x_list.append(sorted_x_list[2])
elif sorted_x_list[1] == min(sorted_x_list):
    x_list.append(sorted_x_list[0])
if sorted_y_list[1] == max(sorted_y_list):
    y_list.append(sorted_y_list[2])
elif sorted_y_list[1] == min(sorted_y_list):
    y_list.append(sorted_y_list[0])
    
print(x_list[3],y_list[3])