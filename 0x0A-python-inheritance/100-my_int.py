#!/usr/bin/python3
"""Module 100-my_int
Creates a class that inherits from int
"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behaviour of != and ==
    """

    def __eq__(self, other):
        """Eq becomes ne"""

        return super().__ne__(other)

    def __ne__(self, other):
        """ne becomes eq"""

        return super().__eq__(other)
