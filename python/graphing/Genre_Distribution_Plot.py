import matplotlib.pyplot as plt
import colorsys as color
from random import randint

def my_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 4 else ''

# def translate(value, leftMin=0, leftMax=13, rightMin=10, rightMax=360*1.75):
def translate(value, leftMin=0, leftMax=13, rightMin=0, rightMax=360*1.75):

    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#37
# def get_RGB_color(h, s=randint(32, 42), l=55):
#     return color.hls_to_rgb((h%360)/360.0, l/100.0, s/100.0)
def get_RGB_color(h, s=randint(47, 57), l=55):
    h = (h % 360) / 360.0
    l /= 100
    c = (h, l, s / 100.0)
    b = (h, l, (s + 10) / 100.0)
    return color.hls_to_rgb(c[0],c[1],c[2]), color.hls_to_rgb(b[0],b[1],b[2])


plt.figure(figsize=(12, 12))
plt.rcParams.update({'font.size': 20})


# values taken from Genre_Distribution.rtf
values = [(193166, 'Pop/Rock'), (28352, 'Electronic'), (15953, 'Rap'), (15167, 'Latin'), (14345, 'Jazz'), (12008, 'International'), (10711, 'RnB'), (9763, 'Country'), (5639, 'Blues'), (5491, 'Reggae'), (5016, 'Folk'), (4696, 'Vocal'), (3162, 'New Age')]

label = [x[1] for x in values]
data = [x[0] for x in values]
total = sum(data)
# pct = [v/total for v in data]
# pct_str = [pct_str(p) for p in pct]

main_n_border_colors = [get_RGB_color(translate(n)) for n in range(len(data))][::-1]
main = [x[0] for x in main_n_border_colors]
border = [x[1] for x in main_n_border_colors]


def mapFromTo(x,a,b,c,d):
   # return (x-a)/(b-a)*(d-c)+c
    return (x - a) / (b - a) * (d - c) + c

# explode = len(values)*[0.03]
explode = [mapFromTo(n, min(data), max(data), 0.1, 0.04) for n in data]
# Plot
wedges, texts, autotexts = plt.pie(data, startangle=90, explode=explode, radius=1.5, colors=main, autopct=my_autopct, pctdistance=0.52)
[text.set_color('white') for text in autotexts]
[wedge.set_edgecolor(border[i]) for i, wedge in enumerate(wedges)]
[wedge.set_linewidth(explode[i]*15) for i, wedge in enumerate(wedges)]


plt.legend(wedges, label,
          title="Genre Distribution",
          loc="center left",
          bbox_to_anchor=(1.2, 0, 0.5, 1))

centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()

plt.savefig('/Users/nathanoasis/downloads/genre_distribution1.eps', format='eps', dpi=300, bbox_inches='tight')
plt.show()
