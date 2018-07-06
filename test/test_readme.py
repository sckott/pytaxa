import doctest

def test_readme():
    doctest.testfile('../readme.rst', raise_on_error=True, report=True)