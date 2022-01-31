def function(a,b,x_new):
    x1,x2,y1,y2 = a[0],b[0],a[1],b[1]
    y_new = (y2-y1)/(x2-x1)*(x_new-x1)+y1
    return y_new
