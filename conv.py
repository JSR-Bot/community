import cv2, os
src = r"C:\bot\screenshots"
dst = r"C:\Users\bot\AppData\Local\Temp\opencode\issue35-assets"
items = [
 ("issue-35-before-settings.png","before_settings.jpg",1600),
 ("issue-35-after-settings.png","after_settings.jpg",1600),
 ("issue-35-before-corner.png","before_corner.jpg",1000),
 ("issue-35-after-corner.png","after_corner.jpg",1000),
 ("issue-35-after-fullscreen.png","after_fullscreen.jpg",1600),
]
for name,out,maxw in items:
    img = cv2.imread(os.path.join(src,name))
    h,w = img.shape[:2]
    if w>maxw:
        img = cv2.resize(img,(maxw,int(h*maxw/w)),interpolation=cv2.INTER_AREA)
    p = os.path.join(dst,out)
    cv2.imwrite(p,img,[cv2.IMWRITE_JPEG_QUALITY,88])
    print(out, os.path.getsize(p))
