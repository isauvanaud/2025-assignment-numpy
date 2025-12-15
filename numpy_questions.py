"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
"""
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (max_i_line, max_i_column) : tuple(int)
        The row and column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    if isinstance(X, np.ndarray):
        X_shape = np.shape(X)
        if (len(X_shape) == 2):
            max_value = 0
            max_i_line = 0
            max_i_column = 0
            for k in range(X_shape[1]):
                for j in range(X_shape[0]):
                    if X[j, k] >= max_value:
                        max_value = X[j, k]
                        max_i_line = j
                        max_i_column = k
            return (max_i_line, max_i_column)
        else:
            raise ValueError('Argument is not a 2D array.')
    else:
        raise ValueError('Argument is not an array.')


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `2`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    pi = 2

    if n_terms > 0:
        for k in range(1, n_terms+1):
            pi = pi * (4*k**2)/(-1 + 4*k**2)
    return pi
