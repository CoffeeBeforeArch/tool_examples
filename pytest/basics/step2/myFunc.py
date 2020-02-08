# Step 2 of the pytest tutorial
# Fix our method based on the results of our first test
# By: Nick from CoffeeBeforeArch


def stat2Num(x, y):
    """ Sum and mean value of two numbers

    Parameters
    ----------
    x : float
        Addend
    y : float
        Augend

    Returns
    -------
    x + y : float
        Sum of two numbers
    (x + y) / 2 : float
        Mean of two numbers
    """
    return (x + y, (x + y) / 2)
