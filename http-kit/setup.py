
import subprocess
import sys
import setup_util

def start(args):

  try:
    subprocess.check_call("lein deps", shell=True, cwd="http-kit/hello")
    # lein run -- --help for more options
    command = "lein run -- --db-host " + args.database_host
    subprocess.Popen(command, shell=True, cwd="http-kit/hello")
    return 0
  except subprocess.CalledProcessError:
    return 1

def stop():
  try:
    # listen on 8080
    subprocess.check_call("lsof -t -sTCP:LISTEN -i:8080 | xargs kill", shell=True)
    return 0
  except subprocess.CalledProcessError:
    return 1
