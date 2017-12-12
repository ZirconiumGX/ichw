"""currency.py: a module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.
__author__ = "GuoXiao"
__pkuid__  = "1700011795"
__email__  = "1700011795@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
    """This function is designed for changing the currency of current to the
currency of target according to imported information.
"""
    from urllib.request import urlopen
    errorlist=["f","a","l","s","e"]
    wrong="Wrong import! Please check your abbreviation of the currency and rerun this program!"
    numlist=[]
    orderlist=[]
    amttolist=[]
    amount_to=""
    webname="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="
    website=webname+currency_from+"&to="+currency_to+"&amt="+str(amount_from)
    doc = urlopen(website)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = list(jstr)
    for s in range(len(jstr)-5):
        if jstr[s]==errorlist[0]and jstr[s+1]==errorlist[1]and jstr[s+2]==errorlist[2]and jstr[s+3]==errorlist[3]and jstr[s+4]==errorlist[4]:
            return wrong
        else:
            continue
    for i in range(len(jstr)):
        if jstr[i] in "1234567890":
            numlist.append(jstr[i])
            orderlist.append(i)
    for j in range(len(orderlist)-1):
        if orderlist[j]+1==orderlist[j+1] or orderlist[j]+2==orderlist[j+1]:
            continue
        else:
            orderorigin=orderlist[j+1]
            orderoforderorigin=j+1
            for s in range(j+1,len(orderlist),1):
                amttolist.append(numlist[s])
    for i in range(orderoforderorigin,len(orderlist)-1,1):    
        if orderlist[i]+2==orderlist[i+1]:
            orderofpoint=i+1-orderoforderorigin
            amttolist.insert(orderofpoint,".")
    for h in range(len(amttolist)):
        amount_to=amount_to+amttolist[h]
    amount_to=float(amount_to)
    return amount_to


def test_exchange():
    """text if the function 'exchange' is all right"""
    assert(exchange("USD","EUR",8.3842)==7.026756099)

def testAll():
    """text all the functions"""
    test_exchange()
    print("All tests passed")

def main():
    print("Welcome!")
    testAll()
    cf=input("Please enter the abbreviation of your current currency:")
    ct=input("Please enter the abbreviation of your target currency:")
    af=float(input("Please enter the amount of your current currency:"))
    result=exchange(cf,ct,af)
    if type(result)==type(2.00):
        print("The result is:%r" % result +" "+ct)
        print("Thanks for using this service!")
    elif type(result)==type("Right"):
        print (result)


if __name__=="__main__":
    main()
