import re
def fun(s):
    # if bool(re.match(r'^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{1,3})$',s)):
    #     return s
    # else:
    #     return None

    #Get elements
    try:
        user = s.index('@')
        web = s.index('.')
        if s.count('@') != 1 or s.count('.') != 1:
            return None
    except ValueError:
        return None

    #Order
    if user > web:
        return None
    
    #lens
    if not len(s[:user]) or not len(s[user+1:web]) or not (0 < len(s[web+1:]) < 4):
        return None

    #Username
    for c in s[:user]:
        if not c.isdigit() and not c.isalpha() and c not in ['-', '_']:
            return None

    #website
    for c in s[user+1:web]:
        if not c.isdigit() and not c.isalpha():
            return None
    
    #extension
    for c in s[web+1:]:
        if not c.isalpha():
            return None
    
    return s

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
