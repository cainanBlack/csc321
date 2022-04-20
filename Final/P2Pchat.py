import netifaces
import argparse
import os
import zmq
import threading 


def recieve(message):
    ctx = zmq.Context.instance()
    reciever = ctx.socket(zmq.SUB)
    for last in range(1, 255):
        reciever.connect("tcp://{0}.{1}:9000".format(message, last))

    reciever.setsockopt(zmq.SUBSCRIBE, b'')
    while True:
        try:
            print(reciever.recv_string())
        except (KeyboardInterrupt, zmq.ContextTerminated):
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("interface", type=str, help="the network interface", choices=interfaces())
    parser.add_argument("user", type=str, default=os.environ['USER'], nargs='?', help="Your username")

    args = parser.parse_args()
    inet = ifaddresses(args.interface)[AF_INET]
    addr = inet[0]['addr']
    message = addr.rsplit('.', 1)[0]

    ctx = zmq.Context.instance()
    recieve_thread = Thread(target=recieve, args=(message,))
    recieve_thread.start()
    serve = ctx.socket(zmq.PUB)
    serve.bind("tcp://%s:9000" % args.interface)

    print("starting chat on %s:9000 (%s.*)" % (args.interface, message))

    while True:
        try:
            msg = raw_input()
            serve.send_string("%s: %s" % (args.user, msg))
        except KeyboardInterrupt:
            break

    serve.close(linger=0)
    ctx.term()

if __name__ == '__main__':
    main()
