from numpy import deg2rad, cos, sign, sin
import matplotlib.pyplot as plt
import colorsys as color
# from palettable.colorbrewer.qualitative import Dark2_7



# def translate(value, leftMin=0, leftMax=13, rightMin=10, rightMax=360*1.75):
def translate(value, leftMin=0, leftMax=13, rightMin=0, rightMax=360*1.75):

    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def get_RGB_color(h, s=37, l=55):
    return color.hls_to_rgb((h%360)/360.0, l/100.0, s/100.0)

# return 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)


# values taken from Genre_Distribution.rtf
values = [(193166, 'Pop/Rock'), (28352, 'Electronic'), (15953, 'Rap'), (15167, 'Latin'), (14345, 'Jazz'), (12008, 'International'), (10711, 'RnB'), (9763, 'Country'), (5639, 'Blues'), (5491, 'Reggae'), (5016, 'Folk'), (4696, 'Vocal'), (3162, 'New_Age')]

label = [x[1] for x in values]
data = [x[0] for x in values]

# colors1 = ["#547294", "#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3", "#fdb462", "#b3de69", "#fccde5", "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f"]
# colors = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928"]
# s = set(colors).union(set(colors1))
# s = list(s)
# s = colors.append(colors1)

# OrRd = ["#fff7ec", "#fee8c8", "#fdd49e", "#fdbb84", "#fc8d59", "#ef6548", "#d7301f", "#b30000", "#7f0000"]
# RdPu = ["#fff7f3", "#fde0dd", "#fcc5c0", "#fa9fb5", "#f768a1", "#dd3497", "#ae017e", "#7a0177", "#49006a"]
#'#405ed6','#5ed640','#d6405e','#7B40D6',
# s = ['#4072D6','#7740d6','#d67740','#dec998','#98dec9','#c998de','#40c4d6','#c4d640','#d640c4','#d68040','#bf40d6','#40d6bf','#40c4d6',]
# s = [get_RGB_color(30), '#4072D6','#7740d6','#d67740','#dec998','#98dec9','#c998de','#40c4d6','#c4d640','#d640c4','#d68040','#bf40d6','#40d6bf','#40c4d6']
# percents = ['{0:3.1f}'.format(100.0 * x / sum(data)) for x in data]
# r_range = [int(x*12) for x in range(len(data))]
s = [get_RGB_color(translate(n)) for n in range(len(data))][::-1]
# s = [get_RGB_color(translate(n)) for n in data][::-1]
# max_chars = max([len(n_chars) for n_chars in label])
# label = [l.ljust(max_chars, ' ') for l in label]
# label = {'{ : <ma}'}.format{v[0]
# legend_values = [v[0] + ' ' + v[1] + '%' for v in zip(label, percents)]


explode = len(values)*[0.03]
# Plot
wedges, texts = plt.pie(data, startangle=90, explode=explode, radius=1.5, colors=s) #, autopct='%1.1f%%', pctdistance=0.85,
# [text.set_color('black') for text in texts]
# [text.set_color('black') for text in autotexts]
# [text.set_fontweight('regular') for text in autotexts]

plt.legend(wedges, label,
          title="Genre Distribution",
          loc="center left",
          bbox_to_anchor=(1.15, 0, 0.5, 1))

centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()

plt.savefig('/Users/nathanoasis/downloads/genre_distribution.eps', format='eps', dpi=1200)
plt.show()

# saveas(plt.gca(), 'genre_distrib.eps','epsc');

