import random

def pack_greedy(C, boxes):
    '''
    Greedy algorithm described in question prompt
    '''
    total_trucks = 0
    all_trucks = []
    while len(boxes) != 0:
        curr_packing = []
        while sum(curr_packing) < C:
            if len(boxes) > 0:
                next_box = boxes[0]
                if sum(curr_packing) + next_box <= C:
                    curr_packing.append(boxes.pop(0))
                else:
                    total_trucks += 1
                    all_trucks.append(curr_packing)
                    break
            else:
                total_trucks += 1
                all_trucks.append(curr_packing)
                break


    return total_trucks, all_trucks


def pack_better(C, boxes):
    total_trucks = 0
    all_trucks = []
    while len(boxes) != 0:
        curr_packing = []
        while sum(curr_packing) < C:
            if len(boxes) > 0:
                next_box = boxes[-1]
                if sum(curr_packing) + next_box <= C:
                    curr_packing.append(boxes.pop(-1))
                else:
                    total_trucks += 1
                    all_trucks.append(curr_packing)
                    break
            else:
                total_trucks += 1
                all_trucks.append(curr_packing)
                break


    return total_trucks, all_trucks



if __name__ == '__main__':
    c = 100
    boxes = [random.randint(0, c//2) for _ in range(100)]

    # boxes = [13, 41, 21, 12, 12, 18, 16, 42, 35, 7, 40, 1, 8, 13, 26, 21, 0, 41, 29, 35, 34, 33, 33, 45, 40, 14, 24, 42, 21, 31, 19, 42, 34, 25, 8, 25, 33, 9, 10, 10, 10, 18, 2, 39, 25, 27, 39, 9, 26, 41, 18, 44, 17, 20, 0, 13, 25, 39, 1, 18, 11, 36, 36, 45, 8, 40, 21, 16, 35, 42, 30, 10, 0, 2, 23, 35, 15, 4, 18, 42, 38, 31, 23, 0, 39, 30, 37, 27, 23, 43, 23, 13, 22, 18, 47, 46, 7, 16, 39, 23]
    # boxes = [13, 41, 21, 12, 12, 18, 16, 42, 35, 7, 40, 1, 8, 13, 26]

    print(c, boxes)

    total, trucks = pack_greedy(c, boxes.copy())
    better_total, better_trucks = pack_better(c, boxes.copy())

    # for truck in trucks:
    #     print(sum(truck), truck)

    # for truck in better_trucks:
    #     print(sum(truck), truck)

    print(f'total number of trucks: {total}')
    print(f'with backwards algo: {better_total}')
    print(total >= better_total)