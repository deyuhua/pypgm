#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_numpy_status():

    has_numpy = False

    try:

        import numpy
        has_numpy = True

    except Exception:

        pass

    return has_numpy


def setup_package():

    from setuptools import setup, find_packages

    metadata = dict(
        name = 'pypgm',
        version = '0.0.1',
        description = 'probability graph model library',
        author = 'deyuhua',
        author_email = 'deyuhua@gmail.com',
        packages=find_packages(exclude=['test'])
    )

    if not check_numpy_status:

        raise Exception('Must install numpy.')

    setup(**metadata)


if __name__ == '__main__':

    from setuptools import setup, find_packages

    metadata = dict(
        name = 'pypgm',
        version = '0.0.1',
        description = 'probability graph model library',
        author = 'deyuhua',
        author_email = 'deyuhua@gmail.com',
        packages=find_packages(exclude=['test'])
    )

    if not check_numpy_status:

        raise Exception('Must install numpy.')

    setup(**metadata)


if __name__ == '__main__':

    setup_package()
