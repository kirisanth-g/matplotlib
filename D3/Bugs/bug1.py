import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

if __name__ == '__main__':
    matplotlib.rcParams['figure.facecolor'] = 'ffffff'

    fig, ax = plt.subplots()

    ax.set_title('Draw image')
    ax.set_xlim((-2,2))
    ax.set_ylim((-2,2))

    img = image.imread('test.png')
    fig.figimage(img, 0, 0)

    imagebox = OffsetImage(img, zoom=1)
    annotation = AnnotationBbox(imagebox, (-1.5, -1.5), frameon=False, xycoords='data', boxcoords="offset points", pad=0)
    ax.add_artist(annotation)

    plt.show()
