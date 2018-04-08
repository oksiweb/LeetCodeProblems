def judgeCircle(moves):
    u = moves.count('U')
    d = moves.count('D')
    l = moves.count('L')
    r = moves.count('R')
    if u - d ==  l - r :
        return True
    return False

print(judgeCircle("UD"))