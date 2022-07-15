from subprocess import call, check_output, CalledProcessError, STDOUT
import actions as actions
def execute(start):
    return call(start.split())

def startup():
    execute(actions.start)


