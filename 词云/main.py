from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator





class ChineseWordUtil:

    my_words_list = []
    text = ""
    f_stop_text=''

    def __init__(self,my_words_list =None, text=None):
        self.my_words_list = my_words_list if my_words_list else []
        self.text = text if text else ''

    def read_file(self,file_path):
        # 读取要分析的文本文件
        with open(file_path,encoding='utf-8') as f:
            self.text = f.read()

    def add_word(self):
        # 添加自己的分词词库
        for items in self.my_words_list:
            jieba.add_word(items)

    def add_stopwords_file(self,stopwords_path):
        # 添加停用词文件
        with open(stopwords_path,encoding='utf-8') as f:
            self.f_stop_text = f.read()

    def chinese_word_segmentation(self):
        # 进行中文分词
        mywordlist = []
        seg_list = jieba.cut(self.text, cut_all=False)
        liststr = "/ ".join(seg_list)
        f_stop_seg_list = self.f_stop_text.split('\n')
        for myword in liststr.split('/'):
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)
        return ''.join(mywordlist)



def build_word_cloud(text,back_coloring_path=None,font_path=None,txt_freq=None,scale=5):
    """
    text: 词云的内容
    back_coloring_path: 使用背景图片
    font_path: 使用的字体所在路径
    txt_freq: 词云权重,覆盖词云的内容
    scale: 图片清晰度
    """

    # 设置词云属性
    wc = WordCloud(
                background_color="white",  # 背景颜色
                max_words=2000,  # 词云显示的最大词数
                max_font_size=100,  # 字体最大值
                random_state=42,
                scale=scale,
                width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )

    wc.font_path = font_path if font_path else 'SIMHEI.TTF'

    if back_coloring_path:  
        back_coloring = imread(back_coloring_path) 
        wc.mask = back_coloring

    if text:
        wc.generate(text)
    
    if txt_freq:
        wc.generate_from_frequencies(txt_freq)

    
    if back_coloring_path:
        image_colors = ImageColorGenerator(back_coloring)
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 绘制词云
    wc.to_file('WordCloudDefautColors.png')

    if back_coloring_path:
        image_colors = ImageColorGenerator(back_coloring)
        plt.imshow(wc.recolor(color_func=image_colors))
    else:
        plt.imshow(wc)
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    if back_coloring_path:
        plt.imshow(back_coloring, cmap=plt.cm.gray)
    else:
        plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 保存图片
    wc.to_file('WordCloudColorsByImg.png')

    
if __name__ == '__main__':
    word = ChineseWordUtil()
    word.read_file('txt.txt')
    word.add_stopwords_file('stopwords.txt')
    txt = word.chinese_word_segmentation()

    # d = {
    #     '品骏':647,
    #     '唯品会':699,
    #     '圆通':420,
    #     '顺丰':970,
    #     '韵达':240
    # }

    build_word_cloud(txt,font_path='HanyiSentyCrayon.ttf')