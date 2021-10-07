import pickle
# hello
dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
            except IndexError:
                print("예외 발생 : 이름, 나이, 점수를 입력해주세요")
            except ValueError:
                print("예외 발생 : 입력하신 것들을 다시 확인해주세요")
            else:
                scdb += [record]
        elif parse[0] == 'del':
            try:
                has_deleted = True
                while has_deleted:
                    has_deleted = False
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            scdb.remove(p)
                            has_deleted = True
            except IndexError:
                print('에러 발생 : 이름을 입력해주세요')

        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print("Age=" + str(p['Age']), "Name=" + str(p['Name']), "Score=" + str(p['Score']))
            except IndexError:
                print('예외 발생 : 이름을 입력해주세요')
            
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[2]))

            except IndexError:
                print('예외 발생 : 이름과 더하고 싶은 숫자를 입력해주세요')
            except ValueError:
                print('예외 발생 : 입력하신 것들을 다시 확인해주세요')
                
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
