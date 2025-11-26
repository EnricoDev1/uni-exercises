def all_below(data: list[int], limit: int):
    if len(data) == 0:
        return True

    for _ in range(len(data)):
        head = data[0]
        tail = data[1:]

        if head > limit:
            return False 

        return all_below(tail, limit)

print(all_below([1,2,6], 4))