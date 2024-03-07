with open("dataset_24465_4.txt") as fr, open("answer_2.4.1", "w+") as fw:
    x = reversed(fr.read().split())
    fw.write("\n".join(x))
    #Очень красиво сделать одной строчкой так:
    #fw.writelines(fr.readlines()[::-1])