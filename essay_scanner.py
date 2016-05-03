import sys


def main():
    readfile()

def readfile():
    try:
        file = sys.argv[1]  # promt to call the file
        textfile = open(file, 'r')  # opens the file
        report = textfile.read()  # read and stores the file
    except IOError:
        print('Cannot open file %s for reading' % file)  # error message the shows
        sys.exit(0)
    checkfile(report)
    textfile.close()

def checkfile(report):
    a =0
    endofsentence = 0
    count=len(report)

    for a in range(0, count):
        if report[a] == '.' or report[a] == '!' or report[a] == '?' or report[a] == ';':
            endofsentence += 1

    words = report.split()
    testword = 0
    validwords = 0
    b=0
    c=0
    specialchar = 0

    for c in range(0, count):
        if report[c] == '@' or report[c] == '$' or report[c] == '#':
            specialchar +=1

    for a in words:
        testword = words[b]
        testword = len(testword)
        if testword >=3:
            validwords += 1
        b+=1

    numberwords=len(words)
    avgWordCount = validwords/endofsentence
    print("The average number word per sentence is", round(avgWordCount,3))

main()