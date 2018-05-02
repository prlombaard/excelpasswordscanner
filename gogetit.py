# gogetit.py

# Given a filename that point to a excelfile on disk. Try to get the password for the Excel file.
# Use either a wordlist or generate a sequence of letters / numbers

import zipfile

def scan_zip_passwords(filename='evil.zip'):
    zFile = zipfile.ZipFile(filename)
    with open(zFile) as passFile:
        for line in passFile.readlines():
            password = line.strip('\n')
            try:
                zFile.extractall(pwd=password)
                print(f'[+] Password = {password}')
                exit(0)
            except Exception, e:
                print(e)



def main():
    print("main")


if "__name__" == "__main__":
    main()
