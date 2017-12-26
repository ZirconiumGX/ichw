"""wcount.py: count words from an Internet file.

__author__ = "Guoxiao"
__pkuid__  = "1700011795"
__email__  = "pkuguoxiao@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """                
    lines=list(lines)
    text=""
    for p in range(len(lines)):
        if lines[p] in ',.!?()[]-_<>\/;:"':
            lines[p]=""
        lines[p]=lines[p].lower()
        text=text+lines[p]
    text=text.split()
    word=tuple(text)
    wordlist=list(word)
    times=[]
    for i in range(len(wordlist)):
        times.append(0)
    timeslist=dict(zip(wordlist,times))
    for t in wordlist:
        repeated=[x for x in text if x==t]
        wordtime=len(repeated)
        timeslist[t]=wordtime
    timeslist=sorted(timeslist.items(),key=lambda x:x[1],reverse=True)
    return timeslist
    
                
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            tl=wcount(lines,topn)
            for s in range(10):
                partner=tl[s]
                print('{0:4}{1:5}'.format(partner[0],partner[1]))
    except Exception as err:
        print(err)
        sys.exit(1)
