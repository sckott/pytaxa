import doctest

def test_readme():
    doctest.testfile('../README.rst', raise_on_error=True)