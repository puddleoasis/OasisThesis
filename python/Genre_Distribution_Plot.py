from numpy import deg2rad, cos, sign, sin
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# values taken from Genre_Distribution.rtf
values = [(193166, 'Pop_Rock'), (28352, 'Electronic'), (15953, 'Rap'), (15167, 'Latin'), (14345, 'Jazz'), (12008, 'International'), (10711, 'RnB'), (9763, 'Country'), (5639, 'Blues'), (5491, 'Reggae'), (5016, 'Folk'), (4696, 'Vocal'), (3162, 'New_Age')]
data = [x[0] for x in values]
label = [x[1] for x in values]

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = sin(deg2rad(ang))
    x = cos(deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(label[i], xy=(x, y), xytext=(1.35 * sign(x), 1.4 * y),
                horizontalalignment=horizontalalignment, **kw)

# ax.set_title("Matplotlib bakery: A donut")

plt.show()

# create a figure and set different background

# fig = plt.figure()
#
# # Change color of text
# plt.rcParams['text.color'] = 'white'
#
# # Create a circle for the center of the plot
# my_circle = plt.Circle((0, 0), 0.7, color='white')
#
# # Pieplot + circle on it
# plt.pie(data, labels=label)
# p = plt.gcf()
# p.gca().add_artist(my_circle)
# plt.show()
