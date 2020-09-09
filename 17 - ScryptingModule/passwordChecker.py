import requests     #make a "browser" request
import hashlib      #use SHA1 hashing
import sys
#k-anonymity - technique that makes someone receive information yet keeping the anonymity from the source



def requestAPIData(queryChar):
    url = 'https://api.pwnedpasswords.com/range/' + queryChar
    res = requests.get(url)
    #print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def getPasswordLeaksCounter(hashes, hashToCheck):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashToCheck:
            return count
    return 0

def pwnedApiCheck(password):
    sha1Password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5Char, tail = sha1Password[:5], sha1Password[5:]
    reqReply = requestAPIData(first5Char)
    #print(first5Char, tail)
    return getPasswordLeaksCounter(reqReply, tail)

def main(args):
    for password in args:
        count = pwnedApiCheck(password)
        if count:
            print(f'Geez ... {password} was found {count} times...')
            print('You should change it!')
        else:
            print(f'{password} was NOT found! ')
            print('Carry on!')
    return 'done!'
 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))