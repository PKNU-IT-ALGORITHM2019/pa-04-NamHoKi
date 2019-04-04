from operator import itemgetter

# 파일 읽어오기
def read_file(file_name):
    global ip,time,url,status,check
    ip = []
    time = []
    url = []
    status = []
    check = 0
    with open(file_name, 'rt', encoding='UTF8') as f:
        lines = f.read().split('\n')
    for i in range(1,len(lines)):
        token = lines[i].split(',')
        ip.append(token[0])
        time.append(token[1])
        url.append(token[2])
        status.append(token[3])

def time_split():
    global time

def my_print():
    global ip, time, url, status, check
    if check == 0:
        for i in range(0,10000):
            print(ip[i],time[i][1:],url[i],status[i])
    elif check == 1:
        for i in range(0, 10000):
            print(time[i])
            print('     IP:',ip[i])
            print('     URL:', url[i])
            print('     Status:', status[i])
    else:
        for i in range(0, 13000):
            print(ip[i])
            print('     Time:',time[i][1:])
            print('     URL:', url[i])
            print('     Status:', status[i])

def sort_time():
    global ip, time, url, status, check
    check = 1


def sort_ip():
    global ip, time, url, status, check
    check = 2
    print()

def main():
    while True:
        command = input('$ ')
        token = command.split()
        if token[0] == 'read':
            read_file(token[1])
        elif token[0] == 'print':
            my_print()
        elif token[0] == 'sort':
            if token[1] == '-t':
                sort_time()
            elif token[1] == '-ip':
                sort_ip()
            else:
                print('input error !')
        elif token[0] == 'exit':
            break
        else:
            print('input error !')

main()