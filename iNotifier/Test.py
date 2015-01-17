'''import commands
failure, output = commands.getstatusoutput("ls")
if failure:
	print 'Failed\n'
	sys.exit(1)
print output'''

'''from subprocess import Popen, PIPE
popen = Popen("ls", shell=True, stdout=PIPE)
output, error = popen.communicate()
print output'''
import subprocess

p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
