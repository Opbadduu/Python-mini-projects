#assingment 1 by me
import cv2

image_loader = input("enter your image path: ")
image = cv2.imread(image_loader)

if image is None:
    print("please insert a valid image path")
else:
    print("do you want to see image (press 1) or convert it into gray scale first (press 2): ")
    choice = int(input("enter your choice: "))
    if choice == 1:
        to_save = image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif choice == 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        to_save = gray
        cv2.imshow("Grayscale image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("invalid input")

    choice_2 = input("do you want to save this image? (yes/no): ")
    if choice_2 == 'yes':
        output_img_name = input("what is the name of your image: ")
        success = cv2.imwrite(output_img_name, to_save)
        print("success" if success else "error")
        
    elif choice_2 == 'no':
      print("exiting: thank you for using this program.") 
      
    else:
        print("kindly select 'yes' or 'no' properly, thank u.")
