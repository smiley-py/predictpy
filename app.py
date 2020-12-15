import os
import sys
import cmd
from src import CustomMenu, CustomProcesses, CustomDiabetes, CustomLogistic, CustomTripAdvisor

menu = CustomMenu()
processes = CustomProcesses()
testdiabetes = CustomDiabetes()
testlogistic = CustomLogistic()
testtripadvisor = CustomTwitter()


class MyShell(cmd.Cmd, object):
    intro = "Welcome to the Text AI shell.   Type help or ? to list commands.\n"
    prompt = "[Shell Prompt] :"

    # ----- basic commands -----
    def do_help(self, line):
        for item in menu.get_help_text():
            print(item)

    def do_testdiatebes(self, line):
        print("DIABETES TEST IS WORKING...")
        testdiabetes.run()

    def do_testlogistic(self, line):
        print("LOGISTIC TEST IS WORKING...")
        testlogistic.run()

    def do_testtripadvisor(self, line):
        print("TWITTER TEST IS WORKING...")
        testtwitter.run()

    def do_start(self, line):
        # service1.start()
        print("Scheduler Service started")

    def do_restart(self, line):
        # service1.restart()
        print("Schedular Service restarted")

    def do_stop(self, line):
        # service1.stop()
        print("Schedular Service stopped")

    def do_reset_config(self, line):
        print("All System Config was reset")

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ": "

    def do_clear(self, line):
        os.system("cls")  # on windows
        # os.system('clear')  # on linux / os x

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(MyShell, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")


# ----- out of class -----


def parse(arg):
    "Convert a series of zero or more numbers to an argument tuple"
    return tuple(map(str, arg.split()))


if __name__ == "__main__":
    app = MyShell()
    app.cmdloop()
