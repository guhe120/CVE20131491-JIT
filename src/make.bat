del .\TestJIT*.class
gen.py %1 1400 xp
del Exploit.jar
javac Exploit.java TestJITApplet.java
copy.py %2
jar cvf Exploit.jar .\*.class  cff