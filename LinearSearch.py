def linearSearch(array, B):
    if not array:
        return "Empty Array."

    length = len(array)
    count = 0

    for i in range(length):
        if array[i] == B:
            count += 1

    return count


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    B = int(input())
    print(linearSearch(array, B))
