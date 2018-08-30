import helper
import math
import numpy as np
def fool_classifier(test_data): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    
    
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance=helper.strategy() 
    parameters={"gamma":'auto',"C":100,'kernel':'linear',"degree":2,"coef0":0.0}
    x_train=[]
    y_train=[]
    for i in range(len(strategy_instance.class0)):
        y_train.append(0)
    for i in range(len(strategy_instance.class1)):
        y_train.append(1)
    s=strategy_instance.class0+strategy_instance.class1
    dic={}
    m=0
    n=0
    for i in range(len(s)):
        for k in s[i]:
            if k not in dic:
                dic[k]=m
                m=m+1

    vv={}
    for k in dic:
        num1=0
        num2=0
        for i in range(len(strategy_instance.class0)):
            if k in strategy_instance.class0[i]:
                num1=num1+1
        for i in range(len(strategy_instance.class1)):
            if k in strategy_instance.class1[i]:
                num2=num2+1
        vv[k]=math.log(len(s)/(num1+num2))


    for i in range(len(s)):
        tz=[0 for li in range(m)]
        for j in range(len(s[i])):
            if s[i][j] in dic:
                tz[dic[s[i][j]]]=tz[dic[s[i][j]]]+1/len(s[i])*vv[s[i][j]]

        x_train.append(tz)
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    clf=strategy_instance.train_svm(parameters,x_train,y_train)
    cof=clf.coef_[0]
    a={}
    for i in dic:
        a[i]=cof[dic[i]]

    with open(test_data, 'r') as infile:
        data = [line for line in infile]
    file1=open('modified_data.txt','w')
    for line in data:
        p=line.strip().split(' ')
        s={}
        ss={}
        kk={}
        ttt=0
        for zz in range(len(p)):
            k=p[zz]
            if k in s:
                s[k]=s[k]+1
                if k in a:
                    ss[k]=ss[k]+a[k]
                else:
                    ss[k]=0
            else:
                ttt=ttt+1
                s[k]=1
                if k in a:
                    ss[k]=a[k]
                else:
                    ss[k]=0
        ti=0
        pp=0
        tj=0
        addd=[]
        delt=[]
        change=20
        xa = sorted(ss.items(), key=lambda item: item[1], reverse=True)
        if ttt<20:
            lll=ttt
        else:
            lll=20

        for i in range(lll):
            if xa[i][1]<=0:
                break
            delt.append(xa[i][0])
            change=change-1
        xa = sorted(a.items(), key=lambda item: item[1])
        for i in range(len(xa)):
            if change==0:
                break
            if xa[i][0] not in s:
                addd.append(xa[i][0])
                change=change-1



        k=0
        j=0

        for j in range(len(delt)):
            max=0
            maxi=0
            if j<len(addd):
                for k in delt:
                    if s[k]>max:
                        max=s[k]
                        maxi=k

                for ll in range(len(p)):
                    if p[ll]==maxi:
                        p[ll]=addd[j]
                s[maxi]=0
            else:
                break
        for j in range(len(delt)):
            for k in range(len(p)):
                if p[k]==delt[j]:
                    p[k]=''

        for j in range(len(delt),len(addd)):
            p.append(addd[j])
        str=''
        for j in range(len(p)):
            if str!='' and p[j]!='':
                str=str+' '
            if p[j]!='':
                str=str+p[j]

        str=str+'\n'
        file1.write(str)

    file1.close()
        # with open(test_data, 'r') as infile:
        #     data = [line for line in infile]
        # file1=open('modified_data.txt','w')
        # for line in data:
        #     p=line.strip().split(' ')
        #     s={}
        #     ss={}
        #     kk={}
        #     for zz in range(len(p)):
        #         k=p[zz]
        #         if k in s:
        #             s[k]=s[k]+1
        #             if k in a:
        #                 ss[k]=ss[k]+a[k]
        #             else:
        #                 ss[k]=ss[k]+(1/len(a))-(1/lenb)
        #         else:
        #             s[k]=1
        #             if k in a:
        #                 ss[k]=a[k]
        #             else:
        #                 ss[k]=(1/len(a))-(1/lenb)
        #     ti=0
        #     pp=0
        #     tj=0
        #     addd=[]
        #     delt=[]
        #     y = sorted(ss.items(), key=lambda item: item[1])
        #     for k in range(20):
        #         while x[ti][0] in s:
        #             ti=ti+1
        #         if -y[tj][1]>x[ti][1]:
        #             delt.append(y[tj][0])
        #             tj=tj+1
        #         else:
        #             addd.append(x[ti][0])
        #             ti=ti+1
        #     k=0
        #     j=0
        #     # hasdelt=[]
        #     # hasadd=[]
        #     # while len(addd)+len(delt)!=20:
        #     #     if xa[j][1]/ta>xb[k][1]/tb:
        #     #         hasadd.append(xa[j][0])
        #     #         if xa[j][0] in delt:
        #     #             delt.remove(xa[j][0])
        #     #             j=j+1
        #     #         else:
        #     #             if xa[j][0] in p or xa[j][0] in hasdelt:
        #     #                 j=j+1
        #     #             else:
        #     #                 addd.append(xa[j][0])
        #     #                 j=j+1
        #     #     else:
        #     #         hasdelt.append(xb[k][0])
        #     #         if xb[k][0] in addd:
        #     #             addd.remove(xb[k][0])
        #     #             k=k+1
        #     #         else:
        #     #             if xb[k][0] in p and xb[k][0] not in hasadd:
        #     #                 delt.append(xb[k][0])
        #     #                 k=k+1
        #     #             else:
        #     #                 k=k+1
        #     k=0
        #     # while len(addd)+len(delt)!=20:
        #     #     if xxx[k] not in p:
        #     #         addd.append(xxx[k])
        #     #     if len(addd)+len(delt)==20:
        #     #         break
        #     #     if yyy[k] in p:
        #     #         delt.append(yyy[k])
        #     #     k=k+1
        #     # print(addd)
        #     # print(delt)
        #     # print(hasadd)
        #     # print(hasdelt)
        #     for j in range(len(delt)):
        #         max=0
        #         maxi=0
        #         if j<len(addd):
        #             for k in delt:
        #                 if s[k]>max:
        #                     max=s[k]
        #                     maxi=k
        #
        #             for ll in range(len(p)):
        #                 if p[ll]==maxi:
        #                     p[ll]=addd[j]
        #             s[maxi]=0
        #         else:
        #             break
        #     for j in range(len(delt)):
        #         for k in range(len(p)):
        #             if p[k]==delt[j]:
        #                 p[k]=''
        #
        #     for j in range(len(delt),len(addd)):
        #         p.append(addd[j])
        #     str=''
        #     for j in range(len(p)):
        #         if str!='' and p[j]!='':
        #             str=str+' '
        #         if p[j]!='':
        #             str=str+p[j]
        #     print(line)
        #     print(str)
        #     print(addd)
        #     print(delt)
        #     print(p)
        #     str=str+'\n'
        #     file1.write(str)
        #
        # file1.close()
    # # dica={}
    # # dicb={}
    # # vv={}
    # # ta=0
    # # tb=0
    # # for i in range(len(strategy_instance.class0)):
    # #     for j in strategy_instance.class0[i]:
    # #         ta=ta+1
    # #         if j in dica:
    # #             dica[j]=dica[j]+1
    # #         else:
    # #             dica[j]=1
    # # xa = sorted(dica.items(), key=lambda item: item[1], reverse=True)
    # # print(xa)
    # # for i in range(len(strategy_instance.class1)):
    # #     for j in strategy_instance.class1[i]:
    # #         tb=tb+1
    # #         if j in dicb:
    # #             dicb[j] = dicb[j] + 1
    # #         else:
    # #             dicb[j] = 1
    # # xb = sorted(dicb.items(), key=lambda item: item[1], reverse=True)
    # # print(xb)
    # # m=0
    #
    # # for i in dicb:
    # #     if i not in dic:
    # #         aa = 0
    # #         if i in dica:
    # #             aa = dica[i]
    # #         aa = (aa + 1)/ta
    # #         dic[i] = m
    # #         m = m + 1
    # #         bb=(dicb[i]+1)/tb
    # #         if bb>aa:
    # #             vv[i] = -math.log(bb / aa,2)
    # #         else:
    # #             vv[i] = math.log(aa / bb,2)
    # # # print(dica)
    # # # print(dicb)
    # # x = sorted(vv.items(), key=lambda item: item[1], reverse=True)
    # # print(x)
    # stm={}
    # for i in range(len(s)):
    #     for j in s[i]:
    #         n=n+1
    #         if j not in dic :
    #             dic[j]=m
    #             m=m+1
    #             stm[j]=1
    #         else:
    #             stm[j]=stm[j]+1
    # x = sorted(stm.items(), key=lambda item: item[1], reverse=True)
    # print(x)
    # vv={}
    # dic2={}
    # ttt=0
    # x1=[]
    # for i in range(len(x)):
    #     x1.append(x[i][0])
    # # for k in dic:
    # #     num1=0
    # #     num2=0
    # #     for i in range(len(strategy_instance.class0)):
    # #         if k in strategy_instance.class0[i]:
    # #             num1=num1+1
    # #     for i in range(len(strategy_instance.class1)):
    # #         if k in strategy_instance.class1[i]:
    # #             num2=num2+1
    # #     vv[k]=math.log(1+abs(num1 / len(strategy_instance.class0) - num2 / len(strategy_instance.class1)))
    # #     num12=num1 / len(strategy_instance.class0)
    # #     num22=num2 / len(strategy_instance.class1)
    # #     if num1+num2<(len(strategy_instance.class0)+len(strategy_instance.class1))/5 or abs(num12-num22)>0.3*min(num12,num22):
    # #         dic2[k]=ttt
    # #         ttt=ttt+1
    # # m=ttt
    # # dic=dic2
    # x = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    # print(x)
    #
    # for i in range(len(s)):
    #     tz=[0 for li in range(m)]
    #     for j in range(len(s[i])):
    #         if s[i][j] in dic:
    #             tz[dic[s[i][j]]]=tz[dic[s[i][j]]]+1
    #
    #     x_train.append(tz)
    # x_train=np.array(x_train)
    # y_train=np.array(y_train)
    # clf=strategy_instance.train_svm(parameters,x_train,y_train)
    # with open(test_data, 'r') as infile:
    #     data = [line.strip().split(' ') for line in infile]
    # z_train=[]
    # for i in range(len(data)):
    #     tz=[0 for li in range(m)]
    #     for j in range(len(data[i])):
    #         if data[i][j] in dic:
    #
    #             tz[dic[data[i][j]]]=tz[dic[data[i][j]]]+1
    #     z_train.append(tz)
    # z_train=np.array(z_train)
    # dt=clf.predict(z_train)
    # kk=0
    # for i in range(len(dt)):
    #     if dt[i]==1:
    #         kk=kk+1
    # baset=dt
    # basek=kk
    # print(dt)
    # print(kk)
    #
    # # for word in x1:
    # #     print(word)
    # #     x_train = []
    # #     for i in range(len(s)):
    # #         tz = [0 for li in range(m)]
    # #         for j in range(len(s[i])):
    # #             if s[i][j] in dic and s[i][j]!=word:
    # #                 tz[dic[s[i][j]]] = tz[dic[s[i][j]]] + 1
    # #
    # #         x_train.append(tz)
    # #     x_train = np.array(x_train)
    # #
    # #     clf = strategy_instance.train_svm(parameters, x_train, y_train)
    # #     with open(test_data, 'r') as infile:
    # #         data = [line.strip().split(' ') for line in infile]
    # #     z_train = []
    # #     for i in range(len(data)):
    # #         tz = [0 for li in range(m)]
    # #         for j in range(len(data[i])):
    # #             if data[i][j] in dic and data[i][j]!=word:
    # #                 tz[dic[data[i][j]]] = tz[dic[data[i][j]]] + 1
    # #         z_train.append(tz)
    # #     z_train = np.array(z_train)
    # #     dt = clf.predict(z_train)
    # #     kk = 0
    # #     for i in range(len(dt)):
    # #         if dt[i] == 1:
    # #             kk = kk + 1
    # #     if kk>basek:
    # #         print(kk)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # # xaa=[]
    # # for i in range(len(xa)):
    # #     xaa.append(xa[i][0])
    # # xbb=[]
    # # for i in range(len(xb)):
    # #     xbb.append(xb[i][0])
    # # xxx=[]
    # # yyy=[]
    # # for i in range(len(xaa)):
    # #
    # #     if xaa[i] not in xbb or i<xbb.index(xaa[i])-3:
    # #         xxx.append(xaa[i])
    # # for i in range(len(xbb)):
    # #
    # #     if xbb[i] not in xaa or i<xaa.index(xbb[i])-3:
    # #         yyy.append(xbb[i])
    # # print(xxx)
    # # print(yyy)
    # #
    # # #
    # # #
    # # #
    # # # ##..................................#
    # # # #
    # # # #
    # # # #
    # # # ## Your implementation goes here....#
    # # # #
    # # # #
    # # # #
    # # # ##..................................#
    # # #
    # # #
    # # # ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...
    # a={}
    # lena=0
    # for i in range (len(strategy_instance.class0)):
    #     for k in strategy_instance.class0[i]:
    #         lena=lena+1
    #         if k in a:
    #             a[k]=a[k]+1
    #         else:
    #             a[k]=1
    #
    # b = {}
    # lenb = 0
    # for i in range(len(strategy_instance.class1)):
    #     for k in strategy_instance.class1[i]:
    #         lenb = lenb + 1
    #         if k in b:
    #             b[k] = b[k] + 1
    #         else:
    #             b[k] = 1
    # za={}
    # zb={}
    # for k in a:
    #     a[k]=a[k]/lena
    # for k in b:
    #     b[k]=b[k]/lenb
    # db={}
    # for k in b:
    #     if k in a:
    #         host=a[k]/(a[k]+b[k])
    #         if host>0.53 or host <0.47 :
    #             db[k]=a[k]-b[k]
    #     else:
    #         db[k]=-b[k]
    # a=db
    # to=len(strategy_instance.class1)+len(strategy_instance.class0)
    # x = sorted(a.items(), key=lambda item: item[1], reverse=True)
    # print(x)
    # # gp=[]
    # # for k in a:
    # #     num1=0
    # #     num2=0
    # #     for i in range(len(strategy_instance.class0)):
    # #         if k in strategy_instance.class0[i]:
    # #             num1=num1+1
    # #     for i in range(len(strategy_instance.class1)):
    # #         if k in strategy_instance.class1[i]:
    # #             num2=num2+1
    # #     gp.append(num1/len(strategy_instance.class0)-num2/len(strategy_instance.class1))
    # #     a[k]=a[k]*abs(math.log(1+abs(num1/len(strategy_instance.class0)-num2/len(strategy_instance.class1))))
    # #     if num1+num2>80:
    # #         a[k]=0
    # #     za[k]=num1
    # #     zb[k]=num2
    # #
    # # print(za)
    # # print(zb)
    # # x = sorted(a.items(), key=lambda item: item[1],reverse=True)
    # # print(x)
    # # print(xa)
    # # print(xb)
    # with open(test_data, 'r') as infile:
    #     data = [line for line in infile]
    # file1=open('modified_data.txt','w')
    # for line in data:
    #     p=line.strip().split(' ')
    #     s={}
    #     ss={}
    #     kk={}
    #     for zz in range(len(p)):
    #         k=p[zz]
    #         if k in s:
    #             s[k]=s[k]+1
    #             if k in a:
    #                 ss[k]=ss[k]+a[k]
    #             else:
    #                 ss[k]=ss[k]+(1/len(a))-(1/lenb)
    #         else:
    #             s[k]=1
    #             if k in a:
    #                 ss[k]=a[k]
    #             else:
    #                 ss[k]=(1/len(a))-(1/lenb)
    #     ti=0
    #     pp=0
    #     tj=0
    #     addd=[]
    #     delt=[]
    #     y = sorted(ss.items(), key=lambda item: item[1])
    #     for k in range(20):
    #         while x[ti][0] in s:
    #             ti=ti+1
    #         if -y[tj][1]>x[ti][1]:
    #             delt.append(y[tj][0])
    #             tj=tj+1
    #         else:
    #             addd.append(x[ti][0])
    #             ti=ti+1
    #     k=0
    #     j=0
    #     # hasdelt=[]
    #     # hasadd=[]
    #     # while len(addd)+len(delt)!=20:
    #     #     if xa[j][1]/ta>xb[k][1]/tb:
    #     #         hasadd.append(xa[j][0])
    #     #         if xa[j][0] in delt:
    #     #             delt.remove(xa[j][0])
    #     #             j=j+1
    #     #         else:
    #     #             if xa[j][0] in p or xa[j][0] in hasdelt:
    #     #                 j=j+1
    #     #             else:
    #     #                 addd.append(xa[j][0])
    #     #                 j=j+1
    #     #     else:
    #     #         hasdelt.append(xb[k][0])
    #     #         if xb[k][0] in addd:
    #     #             addd.remove(xb[k][0])
    #     #             k=k+1
    #     #         else:
    #     #             if xb[k][0] in p and xb[k][0] not in hasadd:
    #     #                 delt.append(xb[k][0])
    #     #                 k=k+1
    #     #             else:
    #     #                 k=k+1
    #     k=0
    #     # while len(addd)+len(delt)!=20:
    #     #     if xxx[k] not in p:
    #     #         addd.append(xxx[k])
    #     #     if len(addd)+len(delt)==20:
    #     #         break
    #     #     if yyy[k] in p:
    #     #         delt.append(yyy[k])
    #     #     k=k+1
    #     # print(addd)
    #     # print(delt)
    #     # print(hasadd)
    #     # print(hasdelt)
    #     for j in range(len(delt)):
    #         max=0
    #         maxi=0
    #         if j<len(addd):
    #             for k in delt:
    #                 if s[k]>max:
    #                     max=s[k]
    #                     maxi=k
    #
    #             for ll in range(len(p)):
    #                 if p[ll]==maxi:
    #                     p[ll]=addd[j]
    #             s[maxi]=0
    #         else:
    #             break
    #     for j in range(len(delt)):
    #         for k in range(len(p)):
    #             if p[k]==delt[j]:
    #                 p[k]=''
    #
    #     for j in range(len(delt),len(addd)):
    #         p.append(addd[j])
    #     str=''
    #     for j in range(len(p)):
    #         if str!='' and p[j]!='':
    #             str=str+' '
    #         if p[j]!='':
    #             str=str+p[j]
    #     print(line)
    #     print(str)
    #     print(addd)
    #     print(delt)
    #     print(p)
    #     str=str+'\n'
    #     file1.write(str)
    #
    # file1.close()
    #
    #
    #
    #
    #
    # #
    # # with open("./modified_data.txt", 'r') as infile:
    # #     data = [line.strip().split(' ') for line in infile]
    # # z_train=[]
    # # for i in range(len(data)):
    # #     tz=[0 for li in range(m)]
    # #     for j in range(len(data[i])):
    # #         if data[i][j] in dic:
    # #             tz[dic[data[i][j]]]=tz[dic[data[i][j]]]+1*vv[data[i][j]]
    # #     z_train.append(tz)
    # # z_train=np.array(z_train)
    # # dt=clf.predict(z_train)
    # # kk=0
    # # for i in range(len(dt)):
    # #     if dt[i]==1:
    # #         kk=kk+1
    # # print(dt)
    # # print(kk)
    #
    # You can check that the modified text is within the modification limits.
    modified_data='./modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance ## NOTE: You are required to return the instance of this class.

test_data='./test_data.txt'

fool_classifier(test_data)