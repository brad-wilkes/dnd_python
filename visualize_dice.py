from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import D6, D8, D10, D12, D20

# Create a D20.
d20 = D20()
d6 = D6()
d8 = D8()
d10 = D10()
d12 = D12()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    results.append(d20.roll())

# Analyze the results.
frequencies = []
for value in range(1, d20.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, d20.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_label = {'title': 'Result'}
y_axis_label = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D20 1000 times',
                   xaxis=x_axis_label, yaxis=y_axis_label)
offline.plot({'data': data, 'layout': my_layout}, filename='d20.html')


