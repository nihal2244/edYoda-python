note=2510
note_dict={"10":0, "20":0, "50":0, "100":0, "500":0, "2000":0}
# print(note_dict)
while note >=9:
    if note >2000:
        note-=2000
        note_dict["2000"]+=1
        continue
    elif 500<note<2000:
        note-=500
        note_dict["500"]+=1
        continue
    elif 100<note<500:
        note-=100
        note_dict["100"]+=1
        continue
    elif 50<note<100:
        note-=50
        note_dict["50"]+=1
        continue
    elif 20<note<50:
        note-=20
        note_dict["20"]+=1
        continue
    elif 10<note<20:
        note-=10
        note_dict["10"]=1
        continue

print(note_dict)
