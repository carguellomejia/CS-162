queue = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
"E Mike", "E Joe", "P Dee", "E Vicky", "E George",
"P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
"P Dee", "S Bill", "S Chase", "E Price", "P Dee",
"E Sue"]
p_queue = []
s_queue = []
e_queue = []
q_input = len(queue)
q_counter = 1
while q_counter < 2:
    for l in range(q_input):
        q_list1 = queue[l]
        q_list2 = q_list1[0]
        if q_list2 == "P":
            p_queue.append(queue[l])
        elif q_list2 == "S":
            s_queue.append(queue[l])
        else:
            e_queue.append(queue[l])
    while q_input > 0:
        for t in range(3):
            print(p_queue[0])
            p_queue.pop(0)
        for u in range(2):
            print(s_queue[0])
            s_queue.pop(0)
        for n in range(1):
            print(e_queue[0])
            e_queue.pop(0)
    print(p_queue)
    print(s_queue)
    print(e_queue)
    q_counter = q_counter + 1