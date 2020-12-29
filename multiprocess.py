from multiprocessing import Process
import os
import math

from reverse import reverse

CPUS = os.cpu_count()

def get_i_ranges():
    ranges = [[0,0]] * CPUS

    RANGE_SLICE = 256 // CPUS

    leftover = 256 - RANGE_SLICE*CPUS

    ranges = [[i*RANGE_SLICE, (i+1)*RANGE_SLICE] for i in range(CPUS)]
    
    ranges[-1][1] += leftover

    return ranges

# hacker.org challenge
# encoded = "382d817119a18844865d880255a8221d90601ad164e8a8e1dd8a48f45846152255f839e09ab176154244faa95513d16e5e314078a97fdb8bb6da8d5615225695225674a4001a9177fb112277c45e17f85753c504d7187ed3cd43b107803827e09502559bf164292affe8aaa8e88ac898f9447119a188448692070056a2628864e6d7105edc5866b9b9b6ebcad6dc3982952a7674a62015025695225674a400d8715efb112277c45edb799f9728355c586f95b002e8aa815b83df3704571b99b6346426bd9862920721751857cb38f69bb3dee18ce1793bc857e27f74a400dd8a48d971bc15d07f521921b80948a86a8eb70457d1138279a796b8fbc43d9801e8ead669c8dcb10781788b5fe91097bad104d9ab952190a15ae706b50477b8dbe4d3cd437119c12842a42190e1a868aeb76446588d52b1078057e27cf7c65fa84aae5b8bbf6b88c19b9176a94a8eb7045778513712f1679b655d9c0255e88ac889b882b8f104711ba1dbabd7120520e188e195225655a802c184a0282affa86a8eb70457120542f7187658515f154244548a4212074278e7c6d3cd4595283e3d9a61d8ad56ba294878c5e69502551bf162487886280aff7b3309"
# MIN_SPACES = 10

# dummy message
encoded = "630f48c40e4d276ca8ae4649ae6648a40c2c2c6c086e8649a5aceaa52eac"
MIN_SPACES = 4

def calc(i_start, i_end):
    for i in range(i_start, i_end):
        for j in range(0, 256):
            if j % 32 == 0:
                print('i,j:', i, j)
            for k in range(0, 256):
                for l in range(0, 256):
                    key = [i, j, k, l]

                    reverse(encoded, key, min_number_of_spaces_expected=MIN_SPACES)

if __name__ == '__main__':
    processes = []

    ranges = get_i_ranges()

    for i in range(CPUS):
        print('registering process %d with i range' % i, ranges[i])
        processes.append(Process(target=calc, args=[ranges[i][0], ranges[i][1]]))

    for p in processes:
        p.start()

    for p in processes:
        p.join()