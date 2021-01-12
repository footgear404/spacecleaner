import os
import hashlib

path = 'D:/python'
doublesFound = 0
doublesSize = 0
result = {}


def MD5(FileName):
    m = hashlib.md5()
    m.update(open(FileName, 'rb').read())
    return m.hexdigest()


def checkFiles(p, r, level=1):
    for i in os.listdir(p):
        f = p + '/' + i
        if os.path.isdir(f):
            checkFiles(f, r, level + 1)
        else:
            hashMD = MD5(f)
            if hashMD not in r:
                r[hashMD] = []
            r[hashMD].append(f)


if __name__ == '__main__':
    checkFiles(path, result)
    # print(result)

    log = open(path + "/log.txt", "w")
    for hashed in result:
        if len(result[hashed]) > 1:
            for j in result[hashed][1:]:
                doublesFound += 1
                doublesSize += os.path.getsize(j)
                # os.remove(j)
                log.write(f"{j} was removed \n")
                # os.symlink(result[hashed][0], j)
    log.write('Всего найдено дублей ' + str(doublesFound))
    log.write('Освобождено (Мб)' + str(doublesSize / (1024 * 1024)))
    log.close()
