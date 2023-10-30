""" Practice python code """

def sum_of_list(the_list):
    """
    Calculates the sum of all the elements in the given list.

    Parameters:
        the_list (list): A list of integers.

    Returns:
        int: The sum of all the elements in the list.
    """
    list_sum = 0
    for i in the_list:
        list_sum += i

    return list_sum

def main():
    """
    This function is the entry point of the program and is responsible for executing the main logic.
    It does not take any parameters and does not return any value.

    Parameters:
        None

    Returns:
        None
    """
    my_list = [1,2,3,4,5]
    print(sum_of_list(my_list))

if __name__ == '__main__':
    main()
