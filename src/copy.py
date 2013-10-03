import sys

def gen(buf, i):
    classname = 'TestJIT%06d' % i
    open('%s.class' % classname, 'wb').write(buf.replace('TestJITApplet', classname))


if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
    except:
        num = 1000

    buf = open('TestJITApplet.class', 'rb').read()

    for i in range(0, num):
        gen(buf, i)
