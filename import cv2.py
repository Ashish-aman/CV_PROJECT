import cv2
import numpy as np
# from PIL import Image
original_img1 = cv2.imread("C://Users//hp//OneDrive//Desktop//IMAGE//man-7813108__480.webp")
original_img=cv2.add(original_img1,4)
mask = np.zeros(original_img.shape[:2], dtype=np.uint8)
def mouse_callback(event, x, y, flags, param):
    global mask,start_point,end_point
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a circle on the mask
        
        cv2.circle(mask, (x, y), 10, (255, 255, 255), -1)
        start_point=(x,y)
    
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        # Draw a circle on the mask while the mouse button is pressed and moved
        cv2.circle(mask, (x, y), 10, (255, 255, 255), -1)
        end_point=(x,y)

    elif event == cv2.EVENT_LBUTTONUP:
        # Use the selected part of the image as a paint brush to mask the area
        brush = cv2.bitwise_and(original_img, original_img, mask=mask)
        cv2.bitwise_not(mask, mask)
        bg = np.ones_like(original_img, np.uint8) * 255
        cv2.bitwise_not(bg, bg)
        masked_bg = cv2.bitwise_and(bg, bg, mask=mask)
        cut_img = cv2.add(brush, masked_bg)
        original_img[:] = cut_img[:]
        mask.fill(0)
        
        # Show the modified image
        # cv2.imshow("Modified Image", original_img)
        # original_img[start_point[1]:end_point[1],start_point[0]:end_point[0]]=255
                #Convert an image from RGB to grayscale mode 
        gray_image = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)
        
        # masked= mask
        # BW= Image.convert('1')
        # print(start_point,end_point)

        #Convert a grayscale image to black and white using binary thresholding 
        # (thresh, BnW_image) = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV)
        (thresh, BnWmasked_image) = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)
        cv2.imshow("Modified Image", BnWmasked_image)
        # masked=original_img - BnWmaske  d_image
        # cv2.imshow("MaSKKK",masked)
        # (thresh, BnWmasked_image1) = cv2.threshold(masked, 0, 255, cv2.THRESH_BINARY)
        # cv2.imshow("MaSKKK2",BnWmasked_image1)
        cv2.imshow('Masked Image in pure black and white ', BnWmasked_image)
        e1 = cv2.getTickCount()
        #USING inpaint fn to just blend the empty portion with its surroundings
        dst = cv2.inpaint(original_img1,BnWmasked_image,3,cv2.INPAINT_TELEA)
        e2 = cv2.getTickCount()
        inpaint_time = (e2 - e1)/ cv2.getTickFrequency() 
        print("inpaint time:",inpaint_time)
        psnr = cv2.PSNR(original_img1, dst, 255)
        print("PSNR",psnr)
        cv2.imshow('THE IMAGE BLENDED WITH ITS BACKGROUND WITHOUT THE OBJECT',dst)
        cv2.imwrite('FINAL OUTPUT OF BlendInvision Image.jpg', dst)
        cv2.imwrite("Masked Image",BnWmasked_image)
        # cv2.imwrite("Masked Image",masked_image)
        
 

cv2.namedWindow("Drag like a paint brush the mouse cursor to select the portion of Image")
cv2.setMouseCallback("Drag like a paint brush the mouse cursor to select the portion of Image", mouse_callback)
cv2.imshow("Drag like a paint brush the mouse cursor to select the portion of Image", original_img)
while True:
    key = cv2.waitKey(1)
    
    # If the 'q' key is pressed, exit the loop
    if key == ord('s'):
        break
        
    # Show the mask in real time
    mask_display = cv2.bitwise_and(original_img, original_img, mask=mask)
    cv2.imshow("Mask", mask_display)
    
    # cv2.imshow('Masked Image in pure black and white ', BnWmasked_image)
    # cv2.imshow('THE IMAGE BLENDED WITH ITS BACKGROUND WITHOUT THE OBJECT',dst)
    # cv2.imshow("")
        
    # Show the original image
    cv2.imshow("Image", original_img)
