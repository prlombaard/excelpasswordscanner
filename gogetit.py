# gogetit.py

# Given a filename that point to a excelfile on disk. Try to get the password for the Excel file.
# Use either a wordlist or generate a sequence of letters / numbers

from zipfile import ZipFile

def scan_zip_passwords(filename='evil.zip', wordlist='dictionary.txt', verbose=False):
    with ZipFile(filename) as zFile:
        with open(wordlist) as passFile:
            for line in passFile.readlines():
                password = line.strip('\n')
                try:
                    zFile.extractall(pwd=bytes(password,'utf-8'))
                    print(f'[+] Password = {password}')
                    exit(0)
                except Exception as e:
                    if verbose:
                        print(e)



def main():
    print("main")
    scan_zip_passwords()


if __name__ == "__main__":
    print("This is excel password scanner")
    main()
