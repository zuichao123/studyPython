import pexpect
import sys

child = pexpect.spawn('ssh root@10.2.1.224')
child.logfile = sys.stdout

child.expect('password:')
child.sendline('ok')
child.expect('root.*')
child.sendline('ls /')
child.expect('root.*')
child.sendline('exit')
