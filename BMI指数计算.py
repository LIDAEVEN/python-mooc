height,weight = eval(input("请输入身高（米）和体重（公斤）【逗号隔开】："))

bmi= weight / pow(height,2)
print("BMI 数值为:{:.2f}".format(bmi))

glo = ""

dome =""

if (bmi<18.5):
    glo,dome = "s","s"

elif (18.5<=bmi<24):
    glo,dome = "z","z"

elif (24<=bmi<25):
    glo,dome = "f","f"

print(glo,dome)