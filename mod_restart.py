from subprocess import call, check_output, CalledProcessError, STDOUT
import actions as actions

def execute(restart):
    return call(restart.split())

def restart():
    execute(actions.restart)
        