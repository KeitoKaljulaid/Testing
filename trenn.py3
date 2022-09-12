onRatas = True
kasSajab = True
temp = int(input("Tänane temperaatur (täisarvuna): "))

if onRatas and (not kasSajab or temp > 15 ) and temp < 25:
    print("Täna saame trenni teha!")
else:
    print("Täna ei saa trenni teha!")