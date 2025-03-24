import pyroute2
import subprocess
import time

# 正常動作確認(2025/3/24)

ipdb = pyroute2.IPDB()
eth1 = ipdb.interfaces.eth1

def set_sr():
    if (eth1.operstate == "DOWN"):
        print("eth1 is DOWN!!")
        cmd = "ip -6 route add 2001:db8:7::/64 encap seg6 mode encap segs 2001:db8:2::2,2001:db8:5::2,2001:db8:6::2 dev eth2"
        subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
        return True


if __name__ == "__main__":
    while True:
        is_success = set_sr()
        if is_success:
            output = subprocess.run("ip -6 route", capture_output=True, text=True, check=True, shell=True)
            print(output)
            break
        time.sleep(1)