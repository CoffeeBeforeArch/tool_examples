# Step 2 of the pytest tutorial
# Test for our fixed method
# By: Nick from CoffeeBeforeArch

from myFunc import stat2Num


def test_stat2Num():
    """ Test for stat2Num """

    assert stat2Num(3, 2) == (5, 2.5)
    assert stat2Num(3, 2.01) != (5, 2.5)
    assert stat2Num(3, 2.0) == (5, 2.5)
    assert stat2Num(3.5, 2.5) == (6, 3)
    assert stat2Num(3.5, 2.5) == (6.0, 3.0)
