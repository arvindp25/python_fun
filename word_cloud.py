""" !pip install worcloud
    !pip install matplotlib
"""


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def genrate_wordcloud(text):

    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(text)
    return wordcloud
  
  if __name__ = "__main__":
    text = """
            Last time could have saved my life
            Pulling me in like a tide
            I feel the energy rise girl
            Too late to be giving me your two faces
            See ya riding a new wave
            But you're floating in my world
            Oooh
            You can't deny that you wanna stay, ooh
            Oooh
            I can't see this working any other way, ooh
            If you want
            Just say you wanna
            'Cause when I hold you
            I feel your aura
            If you want
            Just say you wanna
            'Cause when I hold you
            I feel your aura
            Blue I don't like, red lights
            Just might take it to edge baby girl
            I'll jump, you fly, I'm falling baby
            'Cause you shine
            I don't even need the moonlight
            Pulling me in like a tide
            I got your energy now girl
            Oooh
            You can't deny that you wanna stay, ooh
            Oooh
            I can't see this…

             """
    
    cloud = genrate_wordcloud(text)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    
    
