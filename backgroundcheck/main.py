import sys

from lib import Options

if __name__ == '__main__':
    options = Options()

    if len(sys.argv[1:]) == 0:
        options.help()
        sys.exit(0)

    opts = options.parse(sys.argv[1:])

    if opts.input_file == None:
        print "Please supply an input file"
        sys.exit(1)
    else:
        print "At this point I'll process", opts.input_file
        # TODO Create an object for the processer and pass
        # the input file to it

    sys.exit(0)
