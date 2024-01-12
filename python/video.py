import cv2
import paddlehub as hub
import os
import time

def transform_video_to_image(video_file_path, img_path):
    '''
    将视频中每一帧保存成图片
    '''
    video_capture = cv2.VideoCapture(video_file_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    count = 0
    while(True):
        ret, frame = video_capture.read() 
        if ret:
            cv2.imwrite(img_path + '%d.jpg' % count, frame)
            count += 1
        else:
            break
    video_capture.release()
    print('视频图片保存成功, 共有 %d 张' % count)
    return fps,count


def get_combine_img(input_file_patha):
    #Pathname=""
    output_file_path="mp4_img2/"
    input_file_path="mp4_img/"+input_file_patha
    #print(input_file_path)
    #print(output_file_path)
    result = model.style_transfer(images=[cv2.imread(input_file_path)],visualization=True,output_dir=output_file_path)
    for root, dirs, files in os.walk(output_file_path):
        fils=files
    files=''.join(files)
    #print(files)
    dict1="mv "+output_file_path+files+" "+output_file_path+input_file_patha
    os.system(dict1)
    dict1="cp "+output_file_path+input_file_patha+" "+"./mp4_img3/"+input_file_patha
    #print(dict1)
    os.system(dict1)
    os.system("rm -rf ./mp4_img2")


def transform():
    print('count： %d' % count)
    os.system("mkdir ./mp4_img3")
    for i in range(0,count):
        name=str(i)+".jpg"
        #print(name)
        get_combine_img(name)
    print('视频图片转换成功, 共有 %d 张' % (i+1))


def combine_image_to_video(comb_path, output_file_path, fps, is_print=False):
    '''
        合并图像到视频
    '''
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    
    file_items = os.listdir(comb_path)
    file_len = len(file_items)
    print(comb_path, file_items)
    if file_len > 0 :
        temp_img = cv2.imread(os.path.join(comb_path, file_items[0]))
        img_height, img_width = temp_img.shape[0], temp_img.shape[1]
        
        out = cv2.VideoWriter(output_file_path, fourcc, fps, (img_width, img_height))
        
        for i in range(file_len):
            pic_name = os.path.join(comb_path, file_items[i])
            if is_print:
                print(i+1,'/', file_len, ' ', pic_name)
            img = cv2.imread(pic_name)
            out.write(img)
        out.release()



#input_video = 'D:\\python_project\\text2video\\demos\\demo.mp4'
#model = hub.Module(name='animegan_v2_shinkai_33', use_gpu=True)

#fps,count = transform_video_to_image(input_video, 'D:\\python_project\\mp4_img\\')

#transform()

#final_name="work/output/"+time.strftime("%Y%m%d%H%M%S", time.localtime())+".mp4"

#tran_name="! ffmpeg -i work/mp4_analysis.mp4 -i work/video.mp3 -c copy "+final_name

combine_image_to_video('D:\\python_project\\mp4_img2', './mp4_analysis.mp4' ,30)

''' 
! ffmpeg -i test.mp4 -vn work/video.mp3
os.system(tran_name)
'''
