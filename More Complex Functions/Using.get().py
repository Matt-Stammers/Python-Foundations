# various ways to do it for a calculator

def eval_object(v):
    return {"+": v['a']+v['b'],
            "-": v['a']-v['b'],
            "/": v['a']/v['b'],
            "*": v['a']*v['b'],
            "%": v['a']%v['b'],
           "**": v['a']**v['b'], }.get(v['operation'])
           
def eval_object(v):
    print v
    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b']}.get(v['operation'],None)
        
def eval_object(v):
    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'] }.get(v.get('operation'),1)
        
# or using operator

import operator

OP_FUNCS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '%': operator.mod,
    '**': operator.pow,
}


def eval_object(o):
    f = OP_FUNCS.get(o['operation'])
    return f(o['a'], o['b']) if f else 0
