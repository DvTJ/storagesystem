import os

def check_ping(hostname):
    # hostname or IP is checked for availability
    hostname = hostname
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


print(check_ping("172.20.10.2"))


