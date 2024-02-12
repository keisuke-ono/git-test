def change_domain(email, domain):
    return '@'.join([email.split('@')[0],domain])

def reverse_totuple(ln):
    ln.reverse()
    return tuple(ln)

def add():
    prtin("add")

print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')
print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp'))
print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))