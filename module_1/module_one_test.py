import string
import os

print("Where are we?\nType the number of the answer and press return.\n")
print("\t1 - Boston\n\t2 - Pensacola\n\t3 - Chromepet\n")
answer = int(input().strip())
if(answer is 1):
    print("சார்லஸ் ஆற்றின் குறுக்கே நடந்து செல்வோம்")
elif(answer is 2):
    print("பிளாக்வாட்டர் ஆற்றில் படகு சவாரி செய்வோம்")
elif(answer is 3):
    print("குரோம்பேட்டை அருகில் சுற்றுலா செல்வோம்")
else:
    print("என்னுடன் விளையாடுவதை நிறுத்துங்கள்.")

