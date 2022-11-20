from colorama import Fore
import requests
import pprint
from time import sleep
import os
from passwordgenerator import pwgenerator
from faker import Faker
import socket
import sys
import time

color_1 = Fore.BLUE
color_2 = Fore.RED
color_3 = Fore.MAGENTA
color_4 = Fore.GREEN
color_5 = Fore.WHITE
color_6 = Fore.CYAN

user = 'root'
password = 'root'
user_input = str(input(f'{color_6}User{color_2}>'))
password_input = str(input(f'{color_6}Password{color_2}> '))
sleep(1)
print(f'{color_4}Successful login!')
sleep(1)
os.system('cls')

clock = time.strftime('%H:%M:%S')


def logo():
    main_logo = f"""
    {color_1}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    
                    {color_6}██████╗ ██████╗ ██╗      ██████╗  ██████╗   
                    {color_6}██╔══██╗██╔══██╗██║     ██╔═══██╗██╔════╝   
                    {color_6}██████╔╝██████╔╝██║     ██║   ██║██║         
                    {color_6}██╔══██╗██╔══██╗██║     ██║   ██║██║        
                    {color_6}██████╔╝██║  ██║███████╗╚██████╔╝╚██████╗   
                    {color_6}╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
                                                                 
    {color_1}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                {color_5}Credits: {color_4}Mogra#3124 | {color_4}github.com/Mograa
    """
    print(main_logo)


def menu():
    main_menu = f"""
   {color_2}[1] {color_6}GeoIP         {color_2}[5] {color_6}FakeAddr          {color_2}[9] {color_6} Portscan 
   {color_2}[2] {color_6}Ping          {color_2}[6] {color_6}Speedtest         {color_2}[10] {color_6}Traceroute                              
   {color_2}[3] {color_6}Pwgen         {color_2}[7] {color_6}Domain lookup     {color_2}[11] {color_6}Backup files                               
   {color_2}[4] {color_6}FakeN         {color_2}[8] {color_6}Flush DNS cache   {color_2}[12] {color_6}Exit
    
    
    {color_5}V1.1 | {color_5}Entry time: {color_4}{clock}
"""
    print(main_menu)


def returnf():
    print('\n')
    print(f'{color_5}▀' * 81)
    sleep(1)
    main()


def req_ip():
    try:
        sleep(0.5)
        os.system('cls')
        API_KEY = 'kBtOz67nfvQq8t8HN6fA'
        ip_input = str(input(f'{color_6}IP{color_2}> '))
        req = requests.get(f'https://extreme-ip-lookup.com/json/{ip_input}?key={API_KEY}')
        req_json = req.json()
        sleep(0.5)
        pprint.pprint(req_json)
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def ping():
    try:
        sleep(0.5)
        os.system('cls')
        hostname = input(f'{color_6}Host{color_2}> ')
        response = os.system(f'ping {hostname}')
        if response == 0:
            print(f'{color_5}Status: {color_4}Online')
        else:
            print(f'{color_5}Status: {color_2}Offline')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def pwgen():
    try:
        sleep(0.5)
        os.system('cls')
        passw = pwgenerator.generate()
        print(passw)
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def faken():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        name = fake.name()
        sleep(0.5)
        print(f'{color_5}fake name: {color_4}{name}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def fakeaddr():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        addr = fake.address()
        print(f'{color_5}fake address: {color_4}{addr}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def speedt():
    sleep(0.5)
    os.system('cls')
    os.system('speedtest --secure')
    returnf()


def dmlookup():

    domain = input(f'{color_6}domain{color_2}> ')
    sleep(0.5)
    os.system('cls')
    os.system(f'nslookup {domain}')
    returnf()


def flushdns():
    sleep(0.5)
    os.system('cls')
    os.system('ipconfig /flushdns')
    returnf()


def portscan():
    TPORTS = [22, 443, 80, 8080, 53, 19, 111, 17, 23, 67, 68, 69, 123, 135,
              136, 137, 138, 139, 161, 162, 1900, 3389, 5353, 5900, 1433, 21, 3306]
    host = input(f'{color_6}IP{color_2}> ')
    for ports in TPORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect_ex((host, ports))
        if connect == 0:
            print(f'{color_5}Port: {color_4}{ports} opened')
            s.close()
        else:
            print(f'{color_5}Port: {color_2}{ports} closed')
            s.close()


def tracing():
    host = input(f'{color_6}Host{color_2}> ')
    sleep(0.5)
    os.system('cls')
    os.system(f'tracert {host}')
    returnf()


def backupf():
    archive = input(f'{color_6}Archive/folder path{color_2}> ')
    new_path = input(f'{color_6}Backup path{color_2}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'robocopy {archive} {new_path}')
    returnf()


def exitl():
    os.system('cls')
    confirm = input(
        f'{color_5}Are you sure you want to leave? [{color_4}Y{color_5}/{color_2}N{color_5}]>'
    ).strip().upper()

    if confirm == 'Y':
        print(f'{color_5}departure time:{color_4}{clock}')
        sleep(2)
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        main()


def main():
    try:
        if user_input == user and password_input == password:

            os.system('cls')
            logo()
            menu()

            choice = int(input(f'{color_2}> '))
            match choice:
                case 1:
                    req_ip()
                case 2:
                    ping()
                case 3:
                    pwgen()
                case 4:
                    faken()
                case 5:
                    fakeaddr()
                case 6:
                    speedt()
                case 7:
                    dmlookup()
                case 8:
                    flushdns()
                case 9:
                    portscan()
                case 10:
                    tracing()
                case 11:
                    backupf()
                case 12:
                    exitl()
                case _:
                    print('the selected option does not exist')
                    sleep(2)
                    os.system('cls')
                    returnf()
        else:
            print(f'{color_6} User or Password is invalid!')
    except KeyboardInterrupt:
        print('Program interrupted')


main()
