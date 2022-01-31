def test_function():
    from inclass2 import function
    a,b,x_new = (0,0),(2,2),1
    answer = function(a,b,x_new)
    assert(answer==1)
