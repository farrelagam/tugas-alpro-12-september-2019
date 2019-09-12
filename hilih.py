listgpa = [3,2.7,2.5,4]
def  hadiah (gpa):
     bonus = 500000
     hadiah = gpa*bonus
     return hadiah
for gpa in listgpa : 
    if gpa > 3 :
        print("anda mendapatkan hadiah sebesar :",hadiah(gpa))
    else:
        print("kurang beruntung")