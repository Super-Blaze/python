import json
import sys
import webbrowser

from brew_simulator.doc import documentation
from brew_simulator.simulator import simulate


def main():
    run_mode = argument_checker()
    if run_mode == "doc":
        documentation()
    else:
        simulate(run_mode)


def argument_checker():
    run_modes = ["auto", "default", "doc"]

    if len(sys.argv) > 2:
        raise ValueError("Too many arguments given. Your options are: 'auto' or 'default' !  Read documentation by "
                         "running the script with doc argument!")
    elif len(sys.argv) < 2:
        raise ValueError("Too few arguments given. Your options are: 'auto' or 'default' !  Read documentation by "
                         "running the script with doc argument!")

    run_mode = sys.argv[1]

    if not run_mode in run_modes:
        raise ValueError("Wrong argument given. Your options are: auto , default or doc ! Read documentation by "
                         "running the script with doc argument!")

    return run_mode


if __name__ == '__main__':
    main()
