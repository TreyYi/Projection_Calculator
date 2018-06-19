from fractions import Fraction
from decimal import Decimal

def print_result():
    keep_calculating = True
    while (keep_calculating == True):
        print ("___________________")
        print ("|   " + u"\u001b[1m<Equation> \u001b[0m" + "   |")
        print ("| " + u"\u001b[31m\u001b[4m\u001b[1m y\u001b[0m"+ u"\u001b[4m dot \u001b[0m" + u"\u001b[31m\u001b[4m\u001b[1mu1 \u001b[0m" + "* (u1)|")
        print ("| " + u"\u001b[31m\u001b[1m u1\u001b[0m"+ " dot " + u"\u001b[31m\u001b[1mu1\u001b[0m" + "      |")
        print ("|_________________|" + "\n")

        a = input("Enter y: ").strip().split()
        b = input("Enter u1: ").strip().split()
        if (len(a)!=len(b)):
            print ("Vectors must be the same size or each elements must be the number values.")
            break
        else:
            fractionARR = []
            upperValue, lowerValue, fraction_result, decimal_result = projection(a, b, b, b)
            for i in range(0, len(b)):
                b[i] = Fraction(Decimal(b[i]))
                fraction_arr = fraction_result * b[i]
                fractionARR.append(str(fraction_arr))

        # check original and fraction values
        str_original = str(upperValue) + "/" + str(lowerValue)
        str_fraction = str(fraction_result)
        if (str_original==str_fraction):
            print()
            print ("* The weight ( C_{j} where j = 1 ) is: ", str(upperValue)+"/"+str(lowerValue), "=", decimal_result)
            print (u"* The orthogonal of \u001b[4m("+" ".join(str(x) for x in a)+u")\u001b[0m onto the line through \u001b[4m("+" ".join(str(y) for y in b)+u")\u001b[0m and the \u001b[4morgin\u001b[0m is", u"\u001b[1m\u001b[36m("+" ".join(fractionARR)+u")\u001b[0m")
        else:
            print()
            print ("* The weight ( C_{j} where j = 1 ) is: ", str(upperValue)+"/"+str(lowerValue), "=", fraction_result, "=", decimal_result)
            print (u"* The orthogonal of \u001b[4m("+" ".join(str(x) for x in a)+u")\u001b[0m onto the line through \u001b[4m("+" ".join(str(y) for y in b)+u")\u001b[0m and the \u001b[4morgin\u001b[0m is", u"\u001b[1m\u001b[36m("+" ".join(fractionARR)+u")\u001b[0m")

        print()
        pre_status = input("Want to calculate the other projection? Y/N: ").strip().split()
        if (len(pre_status) == 1):
            status = pre_status[0].upper()
            print ()  #just for the new line
            if (status == "Y"):
                continue
            elif (status == "N"):
                print (u"\u001b[31m\u001b[1mGood Bye!")
                keep_calculating = False
            else:
                print ("Error occured, please run the program again.")
                keep_calculating = False
        else:
            print ("Error occured, please run the program again.")
            keep_calculating = False

def toIntElementsArr(a,b,c,d):
    for i in range(0,len(a)):
        a[i] = int(a[i])
        b[i] = int(b[i])
        c[i] = int(c[i])
        d[i] = int(d[i])
    return a,b,c,d

def projection(a1,b1,c1,d1):
    a,b,c,d = toIntElementsArr(a1,b1,c1,d1)
    # if (len(a) != len(b) or len(c) != len(d)):
    #     print ("Vectors must be same size.")
    # elif (len(a)==len(b) and len(c)==len(d)):
    inner_product_upper = 0
    inner_product_below = 0
    for i in range(0,len(a)):
        inner_product_upper = inner_product_upper + (a[i]*b[i])
    for j in range(0,len(c)):
        inner_product_below = inner_product_below + (c[j]*d[j])
    upper_value = inner_product_upper
    lower_value = inner_product_below
    # print ((inner_product_upper, inner_product_below))
    result_fraction = Fraction(inner_product_upper, inner_product_below)
    result_decimal = float(inner_product_upper)/float(inner_product_below)

    return upper_value, lower_value, result_fraction, result_decimal
# main method
if (__name__ == '__main__'):
    print()
    print(u"\u001b[36m\u001b[1m<Simple Orthogonal Projection Calculator>\u001b[0m")
    print_result()
