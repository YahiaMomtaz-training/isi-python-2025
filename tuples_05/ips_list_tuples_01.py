# list of tuples
ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print(ips_List)
print(ips_List[1])  # ('192.168.0.22', 'y')
print(type(ips_List[1]))
print(ips_List[1]  [0])  #'192.168.0.22'
print(type(ips_List[1]  [0]))

print(ips_List[1]  [0]  [-2:]) # 22
print('------ Loop --- show only allowed IPs --------')
allowed_ips_list = []
for item in ips_List:
    if item[1] == 'y':
        print(item, item[0], item[1])
        allowed_ips_list.append(item[0])

print(allowed_ips_list)






