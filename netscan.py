import sys;
import getopt;
import subprocess


def write_ips(argv):
    try:
        opts, args = getopt.getopt(argv, "i:r")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-i']:
            net = arg
        elif opt in ['-r']:
            net = arg[:arg.index('-')] # still working on it
        else:
            sys.exit(print("usage \"python3 netscan.py -i <valid net>"))
    ips = open('current_ips.txt', "w")
    i = 1
    while(i < 254):
        ips.write(net + str(i) + '\n')
        i += 1
    ips.close()

def scan_net():
    ips = open('current_ips.txt', 'r')
    active_ips = open('active_ips.txt', 'w')
    tik = 1
    percent = 0
    for ip in ips: 
        process = subprocess.run(['./pinger.sh', str(ip[:len(ip)-1])])
        out = str(process)
        code = int(out[len(out)-2])
        if int(code) == 0:
            active_ips.write(ip)
            print("found ip " + ip + " Scanning ports...")
            # portraw = subprocess.run('nmap', ip, '|', 'grep \'open\'', '|', 'awk', '\'print $1\'') #issue
            # ports = str(portraw)
            # for p in ports:
            #   active_ips.write(p)
        if(int(tik*100/253) > percent):
            print(str(int(tik*100/253)) + '%')
            percent += 1
        tik += 1


if __name__ == '__main__':
    write_ips(sys.argv[1:])
    scan_net()
