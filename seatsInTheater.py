"""
https://app.codesignal.com/arcade/code-arcade/intro-gates/bszFiQAog96G9CXKg
"""


def seatsInTheater(nCols, nRows, col, row):
    return (nCols - (col - 1)) * (nRows - row)
