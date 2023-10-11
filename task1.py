# Запитуємо користувача про довжину масива
N = int(input("Введіть довжину масива: "))

# Ініціалізуємо порожній масив
array = []

# Заповнюємо масив дійсними числами, введеними користувачем
for i in range(N):
    element = float(input(f"Введіть {i + 1}-й елемент масиву: "))
    array.append(element)

# Виводимо ненульові елементи у зворотному порядку
non_zero_elements = [elem for elem in array if elem != 0]
non_zero_elements.reverse()

print("Ненульові елементи у зворотному порядку:")
print(non_zero_elements)
