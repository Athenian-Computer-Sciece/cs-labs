from variables import calc_age

age = 20

def test_calc_age():
    assert 20 == calc_age(age)

'''
def test_insert_to_list():
    assert [3, 18, 12, 2, 75, 8, 33, 123] == insert_to_list(list)


def test_remove_from_list():
    assert [3, 18, 12, 2, 75, 33, 123] == remove_from_list(list)


def test_sort_ascending():
    assert [2, 3, 12, 18, 33, 75, 123] == sort_ascending(list)


def test_check_list():
    assert True == check_list(list)

'''