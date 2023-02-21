import frida
import sys


def on_message(message, data):
    print("[%s] => %s" % (message, data))


def main(argv):
    script = open("script.js").read()
    process_name = argv[1]
    pid = frida.spawn(process_name)
    session = frida.attach(pid)
    script_object = session.create_script(script)
    frida.resume(pid)
    script_object.on('message', on_message)
    script_object.load()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.detach()
        sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
