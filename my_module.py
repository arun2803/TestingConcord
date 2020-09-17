def test(ctx, x):
    print 'Hello from another module!'
    print x
    ctx.setVariable('y', x + 3)
