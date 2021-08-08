import os
if __name__=="__main__":
    datasetname="inss_v1s"
    type="train"#test valid

    sub1=os.listdir(datasetname)
    pth=os.path.join(datasetname,type)

    imgs=[]
    for f in os.listdir(pth):
        if "jpg" in f[-4:]:
            imgs.append(f)
    # print(os.listdir(pth))
    print(imgs)

    with open(type+"_"+datasetname+".txt","w") as f:

        for img in imgs:
            p=os.path.join("data",datasetname,type,img)
            # print(p)
            f.writelines(p+"\n")
    f.close()