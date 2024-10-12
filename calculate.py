import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
    Вычисляет заданную функцию для указанной фигуры с заданными размерами.

    Параметры:
    fig (str): Название фигуры ('circle' или 'square').
    func (str): Название функции ('perimeter' или 'area').
    size (list): Список параметров для функции.

	Возвращаемое значение:
	(float) - Периметр или площадь фигуры. Зависит от выбора пользователем фигуры и функции

    Исключения:
    AssertionError: Если фигура или функция не находятся в списках доступных фигур и функций.
    
    Пример:
    calc('circle', 'area', [5]) - вычисляет площадь круга радиусом 5.
    '''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



