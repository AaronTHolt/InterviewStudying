from sorting import qsort, msort


def test_qsort():
    assert qsort([]) == []
    assert qsort([1]) == [1]
    assert qsort([2,3,1]) == [1,2,3]
    assert (qsort([9, 2, 5, 6, 7, 1, 8, 4, 3]) == 
             [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert qsort(['c','b','a','d']) == ['a','b','c','d']

def test_msort():
    assert msort([]) == []
    assert msort([1]) == [1]
    assert msort([2,3,1]) == [1,2,3]
    assert (msort([9, 2, 5, 6, 7, 1, 8, 4, 3]) == 
             [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert msort(['c','b','a','d']) == ['a','b','c','d']