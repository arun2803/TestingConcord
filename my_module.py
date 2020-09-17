def test(ctx, x):
    print 'Hello from another module!'
    print x
    print a
    print b
    ctx.setVariable('y', x + 3)
