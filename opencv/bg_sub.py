from skimage import io as skio
url = 'http://i.stack.imgur.com/SYxmp.jpg'
img = skio.imread(url)



from skimage import filters
sobel = filters.sobel(img)