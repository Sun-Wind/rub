from django.shortcuts import render
from  django.http import HttpResponse
from PIL import Image
import time,os
import torch
import torchvision
from torchvision import transforms
test_transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 缩放
    transforms.ToTensor(),  # 图片转张量，同时归一化0-255 ---》 0-1
    torchvision.transforms.Normalize(0, 1)  # 标准化均值为0标准差为1
])
vgg16 = torch.load("./app/my_nn", map_location='cpu')
  # 载入神经网络文件

path = "./app/Types_garbage.txt"  # 读取垃圾类别文件
f = open(path, encoding="utf-8")
tabels = []
for line in f:
    tabels.append(line.split("    ")[2][:-1])  # [:-1]作用是删去最后的换行符
def predict_img(path=None):
    if path is None:
        return '请传入图片地址'
    image = Image.open(path)
    image = test_transform(image)
    image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
    # vgg16.eval()
    with torch.no_grad():
        outputs = vgg16(image)
        label = outputs.argmax(1)
    return tabels[label],torch.softmax(outputs, 1)[0][label].item()
def index(request):
    return render(request,'app/index.html')
def chanpin(request):
    return render(request,'app/chanpin.html')
def liyong(request):
    return render(request,'app/liyong.html')
def upload(request):
    return render(request,'app/upload.html')
def women(request):
    return render(request,'app/women.html')
def newsa(request):
    return render(request,'app/newsa.html')
def newsb(request):
    return render(request,'app/newsb.html')
def newsc(request):
    return render(request,'app/newsc.html')
def newsd(request):
    return render(request,'app/newsd.html')
def zhishi(request):
    return render(request,'app/zhishi.html')
def liuyan(request):
    return render(request,'app/liuyan.html')
def xinwen(request):
    return render(request,'app/xinwen.html')
def upload1(request):
    myfile = request.FILES.get('pic',None)
    if not myfile:
        return HttpResponse("没有上传的文件信息：")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/images/" + filename,"wb+")
    for chunk in myfile.chunks():      # 分块写入文件  
        destination.write(chunk) 
    destination.close()
    label ,pronb= predict_img(path="static/images/" + filename)
    print(label)
    # os.remove("./static/images/"+filename)
    context = {}
    context['result'] = label
    context['probabilty'] = pronb
    return render(request,'app/result.html',context)

