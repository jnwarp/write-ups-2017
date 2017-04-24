import hashlib
from subprocess import call

def read_file_bytes(path):
    file = open(path, "rb")

    for line in file:
        # return the line, remove the newline char
        yield line[:-1]

    file.close()
    return


def read_file(path):
    file = open(path, "r")

    # read lines into array
    content = []
    for line in file:
        content.append(line)

    # return the array
    file.close()
    return content



if __name__ == '__main__':
    # open files for input and output
    #file_out = open('rockyou.md5', 'w')
    file_in = read_file_bytes('rockyou.txt')
    passwords = read_file('passwords.txt')
    content = []
    i = 0

    # pull another line from the file
    for line in file_in:
        # create a hash of the line
        m = hashlib.md5()
        m.update(line)
        md5hash = m.hexdigest()

        # save the hash
        #file_out.write(md5hash)

        # check if hash matches any passwords
        for password in passwords:
            if password.strip() == md5hash.strip():
                # print out the password if hash matches
                print(password, 'is', line)

    # close the output file
    #file_out.close()
