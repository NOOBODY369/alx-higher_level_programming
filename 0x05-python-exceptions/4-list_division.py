#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    n_list = []
    res = 0
    for i in range(0, list_length):
        try:
            res = (my_list_1[1] / my_list_2[i])
        except TypeError:
            res = 0
            print( "wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            n_list.append(res)
        return n_list
