# # for i in range(1,76) : 
# #     if i%5==0 :
# #         print(i)


# # x=input("metin girin : ") 
# # y=len(x)
# # print(y)

# print ("")

toplam = 0 
for i in range(100) : 
    sayi=int(input("sayi girin : ")) 
    if sayi >= 0 : 
        toplam=toplam + sayi
    else :
        break
print(f"girilen pozitif sayilar toplamı{toplam}")    