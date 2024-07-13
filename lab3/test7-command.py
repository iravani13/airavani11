#!/usr/bin/env python3

import os

ls_return = os.system('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)
