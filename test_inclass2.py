def test_function():
    from inclass2 import function
    x,y,x_new = (0,0),(2,2),1
    answer = function(x,y,x_new)
    assert(answer==1)
