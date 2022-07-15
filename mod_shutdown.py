from subprocess import call, check_output, CalledProcessError, STDOUT
import actions as actions
import time

def execute(stop):
    return call(stop.split())

def shutdown():
    execute(actions.stop)
