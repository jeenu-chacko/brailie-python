import conversion

text="Enter the text that you want to convert to Braille"
res=""
for i in text:
    res=conversion.brailie[i]+res

print(res)



