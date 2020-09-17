def test(ctx, x, a, b, c, d):
    print 'Hello from another module!'
    print x
    print a
    print b
    print c
    print d
    ctx.setVariable('y', x + 3)
