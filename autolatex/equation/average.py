import numpy as np


def ave(nums, name, unit="mm"):
    '''
    计算平均值
    '''
    n = len(nums)
    fractop = ''
    for num in nums:
        fractop += str(num) + '+'
    fractop = fractop[:-1]
    tex = "测量${}$的平均值为\n".format(name)
    tex += '$$\\bar{' + name + '} = \\frac{' + fractop + '}{' + str(n) + '} \\mathrm{' + unit + \
        '}} = {:.3f}{{'.format(np.mean(nums)) + unit + "}$$\n"
    tex += "标准差为$\\sigma = {:.3f}$, 即\n".format(np.std(nums))
    tex += "$${} = {:.3f} \\pm {:.3f} \mathrm{{ {} }}$$".format(
        name, np.mean(nums), np.std(nums), unit)
    print(tex)
    return tex
