#!/bin/python
import os
import sys

def run():
	#url = os.popen('echo $url').read().strip('\n')
	url = ""
	try:
		url = os.environ['url']
	except KeyError:
		print "[Warn] Container name cannot be none!"

        if url is not None and url != "":
                #print "url=" + url
		container_name = url.split('?')[1].split('name=')[1]
        else:
                container_name="ubuntu"
		print "[Error] Exit without container name!"
		sys.exit()
                #print "[Warn] Container name cannot be none!"

	while True:
		#os.system('/bin/bash')
		current_path = os.popen("sudo docker exec " +container_name + " pwd").read().strip('\n')
		current_user = os.popen("sudo docker exec " +container_name + " whoami").read().strip('\n')
		hostname = os.popen("sudo docker exec " +container_name + " hostname").read().strip('\n')
		prefix = current_user + "@" + hostname + ":" + current_path
		if current_user == "root":
			prefix = prefix + "# "
		else:
			prefix = prefix + "$ "
		user_input = raw_input(prefix)
		if user_input == "" or user_input == "\n":
			pass
		else:
			#res = os.popen(str(user_input))
			res = os.popen(str("sudo docker exec " +container_name + " " + user_input))
			while 1:
				line = res.readline()
				if not line:
					break
				print line.strip('\n')

def main():
	try:
		run()
	except KeyboardInterrupt:
		print "\nExit..."
		sys.exit()


main()
