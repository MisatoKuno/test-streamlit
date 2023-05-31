def culc(**items):
    nums=items["nums"]
    s=sum(nums)
    r=0
    if items["types"]=="sum":
        return s
    elif items["types"]=="avg":
        return s/len(nums)
    elif items["types"]=="hiku":
        for i,num in enumerate(nums):
            if i==0:
                r=int(num)
            else:
                r=r-int(num)
        return r
    
ans1=culc(types="sum",nums=(1,2,3,4))
print(ans1)
ans2=culc(nums=(1,4,7),types="avg")
print(ans2)
ans3=culc(types="hiku",nums=(3,7,9,-3))
print(ans3)


"""
dict:listのインデックスを自由に設定できるver
"""
a=[1,4,7,9]
b=["a","b","d","i","l"]
c=dict(zip(a,b))
print(c)

c[1]="A"
c[8]="l"
print(c)