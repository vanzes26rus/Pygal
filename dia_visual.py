from die import Dia
import pygal

# создание кубика D6
dia = Dia()
dia2 = Dia()
dia3 = Dia()


results = []
max_results = dia.num_saids + dia2.num_saids + dia3.num_saids
frequens = []
# Моделирование серии бросков с сохранением результатов в списке
for nam_result in range(1000):
    nam_result = dia.rool() + dia2.rool() + dia3.rool()
    results.append(nam_result)

# Анализ результатов
for values in range(3, max_results+1):
    frequen = results.count(values)
    frequens.append(frequen)

# Визуализация результатов
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = list(range(3, dia.num_saids + dia2.num_saids + dia3.num_saids + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6 + D6", frequens)
hist.render_to_file('die_visual.svg')
