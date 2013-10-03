========================= Title =========================================

CVE-2013-1491 PoC using JIT-Spray by Yuki Chen (古河)


Twitter:  @guhe120

Weibo:    http://weibo.com/u/1874932054



========================= About this PoC =========================================

This exploit is a proof-of-concept exploit which demonstrates how to exploite java native vulnerabilities with Java-JIT-Spray technique.
It is developped and only tested on Windows 7 enterprise 32 bits.

This vulnerability was discovered by Jushua J Drake (jduck) of accuvantlabs.
For the detail of this vulnerability, see:
http://blog.accuvantlabs.com/sites/default/files/Papers/Pwn2Own%202013%20-%20Java%207%20SE%20Memory%20Corruption.pdf

For more details of java jit spray technique, see my slides at SyScan360:
http://aj43xnbacx.l31.yunpan.cn/lk/QGb98dgpj74YJ


========================= How to compile ======================================
To compile the source code, you need jdk and python installed.

1. Make sure "javac" and "python" is in your path environments.
2. Check out the source under "src", open a terminal and change the dir to the "src" folder.
3. run the following command: 
   make.bat 40 60

   Where the first parameter "40" means each class file contains 40 JIT functions, and the second parameter "60" means we will spray totally 60 classes.

4. After running the command, a jar file named "Exploit.jar" will be generated within the same folder.
	

========================= How to test =========================================
Environment:   JRE 7u17   + Windows 7 32bits (english version)

1. Put the two files "HelloApplet.html" and "Exploit.jar" in the same folder, copy them to your test machine.
2. Open HelloApplet.html in your web browser, if exploit success, you will see a calculator.

Note: The jit-spray takes some time (7 ~ ??  seconds depends on your test machine). Please wait with patient while spraying :)
