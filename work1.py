# use for comsm0010_CW

import hashlib
import time


def pow(difnum):
    max_nonce = 2 ** 32
    header = 'COMSM0010cloud'
    print("Starting search...")
    start_time = time.time()
    for nonce in range(0, max_nonce):
        block_nonce = header + str(nonce)
        hashresult = hashlib.sha256(block_nonce.encode('utf-8')).hexdigest()
        if hashresult[:difnum] == str(0).zfill(difnum):
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hashresult)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Elapsed time: %.6f seconds" % elapsed_time)
            if elapsed_time > 0:
                hash_power = float(int(nonce) / elapsed_time)
                print("Hashing power: %ld hashes per second" % hash_power)
            return (hashresult, nonce)
    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':
# set the difficulty-level
    difnum = 3

    pow(difnum)

