def _o(_p):
    _q = [0, 1, 1]
    for _ in range(3, _p + 1): 
        _q.append(_q[-1] + _q[-2])
    return _q

def _r(_p, _s, _q):
    while _p > 2:
        if _s > _q[_p-2]: 
            _s -= _q[_p-2]
            _p -= 1
        else: 
            _p -= 2
    return "N" if _p == 1 else "A"

_t = list(map(int, input().split()))
print(_r(_t[0], _t[1], _o(_t[0])))
