# receive email
# verify if it is valid
# print valid Name and email
import re
import email.utils

regex = re.compile(r'^[A-Za-z0-9][\w._%+-]*[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{1,3}$')

for i in range(int(input())):
    u_name, u_email = email.utils.parseaddr(input())
    if re.search(regex, u_email):
        print(email.utils.formataddr((u_name, u_email)))
