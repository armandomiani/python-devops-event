# argparse sample

## Topics

* Introducing argparse
* Command argument
* Optional argument
* Data Types
* Choices
* Groups 
* Passwords


## Reference
https://docs.python.org/3/howto/argparse.html
https://gist.github.com/namnv609/f462c194e80ed4048cd2


# Help 

```
class PasswordRetriever(argparse.Action):
    def __call__(self, parser, namespace, values, opts):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()
parser.add_argument('run', help='Run a webserver at specified port')

parser.add_argument(
    '-pwd',
    help='Specify the password',
    nargs='?',
    dest='password',
    action=PasswordRetriever
)```