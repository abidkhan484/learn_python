def make_free(pagli):

    if not len(pagli):
        return ''

    if pagli[0] not in 'abcdefghijklmnopqrstuvwxyz':
        return '' + make_free(pagli[1:])

    return pagli[0] + make_free(pagli[1:])


def reverse(st):
    if not len(st):
        return ''

    if st[-1] not in 'abcdefghijklmnopqrstuvwxyz':
        return '' + reverse(st[:-1])
    
    return st[-1] + reverse(st[:-1])

ii = 'Reviled did I live, said I, as evil I did deliver'
ia = ii.lower()
ia = make_free(ia)
pr = reverse(ia)

print('palindrome') if pr==ia else print('not palindrome')
