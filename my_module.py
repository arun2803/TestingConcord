def test(ctx, x, a, b):
    print 'Hello from another module!'
    print x
    print a
    print b
    ctx.setVariable('y', x + 3)
