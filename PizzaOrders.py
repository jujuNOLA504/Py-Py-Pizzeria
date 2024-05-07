def display_menu(pizza_menu):
    print('Welcome to PyPY Pizza!')
    print('Choose your pizza:')
    for i, pizza in enumerate(pizza_menu, start=1):
        print(f'{i}. {pizza['name']} - ${pizza['price']}')

def order_pizza(pizza_menu):
    selection = int(input('Enter the number of the pizza you want: '))
    selected_pizza = pizza_menu[selection - 1]

    size = input('Please enter a size (small, medium, large): ').lower()
    while size not in ['small', 'medium', 'large']:
        size = input('Please enter a valid size(small, medium, large): ').lower()

    toppings = input('Enter toppings (comma separated): ').split(',')
    num_pizzas = int(input('Enter the number of pizzas: '))

    total_price = selected_pizza['price'] * num_pizzas
    print('\nOrder Summary')
    print(f'Pizza: {selected_pizza['name']} - ${selected_pizza['price']}')
    print(f'Size: {size}')
    print(f'Toppings: {','.join(toppings)}')
    print(f'Number of pizzas: {num_pizzas}')
    print(f'Total Price: ${total_price}')

def main():
    pizza_menu = [
        {'name': 'Margherita', 'price': 10},
        {'name': 'Pepperoni', 'price': 12},
        {'name': 'Vegetarian', 'price': 11},
        {'name': 'Hawaiian', 'price': 13},
        {'name': 'BBQ Chicken', 'price': 14}
    ]

    display_menu(pizza_menu)
    order_pizza(pizza_menu)

if __name__ == '__main__':
    main()