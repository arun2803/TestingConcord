def test(ctx, x, a, b, c, d, e):
    print 'Hello from another module!'
    print x
    print a
    print b
    print c
    print d
    print e
    ctx.setVariable('y', x + 3)
