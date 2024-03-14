import socket
import sys
import ipaddress


#This code is not neccessry because user will specify arguments 

# def scanRange(Network, startport, endport):
#     print(f"[+] starting port scan {Network}")
#     for host in range(1,300):
#         ip + "," + str(host)
#         sockscan(ip , startport, endport)

#     print(f"[+] TCP scan on host {Network} complete")


def message(ip_addr, startport, endport):
    print(f"[*] start tcp scan on : {ip_addr}")
    sockscan(ip_addr,startport,endport)
    print(f"[+] scan completed {ip_addr}")
    print(f"[+] Please Enter IP : ")


# Main Socket function : Connect IP and PORT with following range and print open ports
def sockscan(ip_addr, startport, endport ):
    for port in range(startport,endport + 1):
        try:
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            if not sock.connect_ex((ip_addr, port)):
                print(f"Open Ports {ip_addr} , {port}")
                sock.close()

        except Exception:
            pass


# Connect and recive the information of specified IP with 1024 byte and print service and version 
def bannergrab(My_IP, port):

    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((My_IP, port))
        banner = s.recv(1024)
        print(banner)
    except:
        return
 

# Execute function with extra feature: recive IP address and resolve it like DNS and vice versa 
def execut():
    My_IP = input("Enter Target IP Address : ")
    # stport = int(input ("Enter first range  number : "))
    enddport = int(input ("Enter port number  : "))
    for port in range(0, enddport + 1):
        banner = bannergrab(My_IP, port)
        if banner:
            print(f"[+] Result For: {My_IP}, {str(port)} : " + banner)
    try:
        resolve = socket.gethostbyname(My_IP)
        print(resolve[0])
    except socket.gaierror as e:
        print(f"cant resolve {str(e)}")

    try:
        resolve_addr = socket.gethostbyaddr(resolve)
        print(resolve_addr[0])
    except socket.herror as e:
        print(f"cant resolve host {str(e)}")


# Whene if statement work that main script run in file not imported by other script 
if __name__ == "__main__":
    socket.setdefaulttimeout(1)
    args = sys.argv
    ip_addr = args[1] #change ip to ip_addr
    
        
    try:
        ipaddress.ip_address(ip_addr)

    except ValueError:
        sys.exit("Argument 1 not a valid IP address.")
        
        
    try:
        x = int(args[2])

    except ValueError:
        sys.exit("Argument 2 not a valid port number.")

    try:
        y = int(args[3])
    except ValueError:
        sys.exit("Argument 3 not a valid port number")

    message(args[1], int(args[2]), int(args[3]))

# Extra feature
cont = input("Do you want grab banner [y/n] : ")
if cont == "y":
    execut()
    
else:
    exit(0)


# sockscan arguments will specify by the user so we dont need scanRange() function any more
    
# Inspired by https://github.com/starhound/PortScan/blob/main/PortScan-CLI.py#L6 great thanks to starhound