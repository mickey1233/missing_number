def missingnumber(nums):
    length = len(nums)
    result = int(length * (length + 1) / 2)

    for i in nums:
        result -= i
    return result


def main():
    print(missingnumber([3, 0, 1]))
    print(missingnumber([0, 1]))
    print(missingnumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingnumber([0]))


if __name__ == "__main__":
    main()
