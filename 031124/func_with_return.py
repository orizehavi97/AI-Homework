def my_avg(x: int, y: int):
    return (x + y) / 2

def my_headline(str1: str):
    """Returns headline with ! at the end"""
    return str1.upper() + '!'

def concat_list(list1: list[int], list2: list[int], list3: list[int]):
    return list1 + list2 + list3

if __name__ == "__main__":
    avg1: float = my_avg(90,99)
    print(avg1)

    head1: str = my_headline("python has conquered the world")
    print(head1)
    print(head1)

    res_con: list[int] = concat_list([1,2], [3,4,5,6], [7,8,9])
    print(res_con , len(res_con))
