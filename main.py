import math


def calculate_g():

    choice_calc_g = input('Do you want to calculate Gravitational Acceleration by latitude?(y/n): ')

    if choice_calc_g == 'y':
        lat = float(input("Enter the latitude of the object's location(°): "))
        r1 = 6378.137
        r2 = 6357.752
        B = math.radians(lat)

        a = (r1**2 * math.cos(B))**2
        b = (r2**2 * math.sin(B))**2
        x = math.sqrt(a + b)

        m = (r1 * math.cos(B))**2
        n = (r2 * math.sin(B))**2
        y = math.sqrt(m + n)

        r = x / y
        G = 6.673e-11
        M = 5.97219e24
        g = (G * M) / (r * 1000)**2
        print(f'The Gravitational Acceleration of the location is {g}')

    elif choice_calc_g == 'n':
        g = 9.8
        print('We took the value of Gravitational Acceleration 9.8 m/s²')

    return g


def calculate_h_falling_obj():
    print('''Calculate height of the Falling Object with --
    1. Gravitational Acceleration and Time
    2. Final Velocity and Gravitational Acceleration
    3. Final Velocity and Time''')

    choice_h_fall = input("Enter your option's number: ")

    if choice_h_fall == '1':
        g = calculate_g()
        t = float(input('Enter the Time(t)(s): '))
        h = (g * (t**2)) / 2
        print(f'The Height(h) is {h} m')

    elif choice_h_fall == '2':
        g = calculate_g()
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        h = v**2 / (2 * g)
        print(f'The Height(h) is {h} m')

    elif choice_h_fall == '3':
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = float(input('Enter the Time(t)(s): '))
        h = (v * t) / 2
        print(f'The Height(h) is {h} m')

    else:
        print('Enter a valid number....!')


def calculate_v_falling_obj():
    print('''Calculate Final Velocity of Falling Object with --
    1. Gravitational Acceleration and Time
    2. Gravitational Acceleration and Height
    3. Height and Time''')

    choice_v_fall = input("Enter your option's number: ")

    if choice_v_fall == '1':
        g = calculate_g()
        t = float(input('Enter the Time(t)(s): '))
        v = g * t
        print(f'The Final Velocity is {v} m/s')

    elif choice_v_fall == '2':
        g = calculate_g()
        h = float(input('Enter the Height(h)(m): '))
        v = math.sqrt(2 * g * h)
        print(f'The Final Velocity is {v} m/s')

    elif choice_v_fall == '3':
        h = float(input('Enter the Height(h)(m): '))
        t = float(input('Enter the Time(t)(s): '))
        v = (2 * h) / t
        print(f'The Final Velocity is {v} m/s')

    else:
        print('Enter a valid number....!')


def calculate_t_falling_obj():
    print('''Calculate Time of the Falling Object with --
    1. Final Velocity and Gravitational Acceleration
    2. Height and Gravitational Acceleration
    3. Height and Final Velocity''')

    choice_t_fall = input("Enter your option's number: ")

    if choice_t_fall == '1':
        g = calculate_g()
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = v / g
        print(f'The Time is {t} s')

    elif choice_t_fall == '2':
        g = calculate_g()
        h = float(input('Enter the Height(h)(m): '))
        t = math.sqrt((2 * h) / g)
        print(f'The Time is {t} s')

    elif choice_t_fall == '3':
        h = float(input('Enter the Height(h)(m): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = (2 * h) / v
        print(f'The Time is {t} s')

    else:
        print('Enter a valid number....!')


def calculate_g_eqn_fall():
    print('''Calculate Gravitational Aceeleration of the Falling Object with --
    1. Final Velocity and Time
    2. Final Velocity and Height
    3. Height and Time''')

    choice_g_fall = input("Enter your option's number: ")

    if choice_g_fall == '1':
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = float(input('Enter the Time(t)(s): '))
        g = v / t
        print(f'The Accelaration is {g} m/s²')

    elif choice_g_fall == '2':
        h = float(input('Enter the Height(h)(m): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        g = v**2 / 2 * h
        print(f'The Gravitational Accelaration is {g} m/s²')

    elif choice_g_fall == '3':
        h = float(input('Enter the Height(h)(m): '))
        t = float(input('Enter the Time(t)(s): '))
        g = 2 * h / t**2
        print(f'The Accelaration is {g} m/s²')

    else:
        print('Enter a valid number')


def calculate_u_thrown():
    print('''Calculate Initial Velocity of the Thrown Object with --
    1. Gravitational Aceeleration and Time
    2. Gravitational Aceeleration and Height
    3. Height and Time''')

    choice_u_thrown = input("Enter your option's number: ")

    if choice_u_thrown == '1':
        g = calculate_g()
        t = float(input('Enter the Time(t)(s): '))
        u = g * t
        print(f'The Initial Velocity is {u} m/s')

    elif choice_u_thrown == '2':
        g = calculate_g()
        h = float(input('Enter the Height(h)(m): '))
        u = math.sqrt(2 * g * h)
        print(f'The Initial Velocity is {u} m/s')

    elif choice_u_thrown == '3':
        h = float(input('Enter the Height(h)(m): '))
        t = float(input('Enter the Time(t)(s): '))
        u = (2 * h) / t
        print(f'The Initial Velocity is {u} m/s')

    else:
        print('Enter a valid number')


def calculate_h_thrown():
    print('''Calculate Initial Velocity of the Thrown Object with --
    1. Initial Velocity, Gravitational Acceleration and Time
    2. Initial Velocity and Gravitational Acceleration
    3. Initial Velocity and Time''')

    choice_h_thrown = input("Enter your option's number: ")

    if choice_h_thrown == '1':
        g = calculate_g()
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        t = float(input('Enter the Time(t)(s): '))
        h = (u * t) - (0.5 * g * (t**2))
        print(f'The Height(h) is {h} m')

    elif choice_h_thrown == '2':
        g = calculate_g()
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        h = (u**2) / (2 * g)
        print(f'The Height(h) is {h} m')

    elif choice_h_thrown == '3':
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        t = float(input('Enter the Time(t)(s): '))
        h = (u * t) / 2
        print(f'The Height(h) is {h} m')

    else:
        print('Enter a valid number')


def calculate_t_thrown():
    print('''Calculate Initial Velocity of the Thrown Object with --
    1. Initial Velocity and Gravitational Acceleration
    2. Initial Velocity and Height''')

    choice_t_thrown = input("Enter your option's number: ")

    if choice_t_thrown == '1':
        g = calculate_g()
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        t = u / g
        print(f'The Time is {t} s')

    elif choice_t_thrown == '2':
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        h = float(input('Enter the Height(h)(m): '))
        t = (2 * h) / u
        print(f'The Time is {t} s')

    else:
        print('Enter a valid number')


def calculate_g_eqn_thrown():
    print('''Calculate Gravitational Aceeleration of the Thrown Object with --
    1. Initial Velocity and Time
    2. Initial Velocity and Height''')

    choice_g_thrown = input("Enter your option's number: ")

    if choice_g_thrown == '1':
        t = float(input('Enter the Time(t)(s): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        g = t / u
        print(f'The Gravitational Accelaration is {g} m/s²')

    elif choice_g_thrown == '2':
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        h = float(input('Enter the Height(h)(m): '))
        g = (u**2) / (2 * h)
        print(f'The Gravitational Accelaration is {g} m/s²')

    else:
        print('Enter a valid number')


def main():
    print('Welcome to the Kinematic Calculator for Falling and Thrown Objects......!')
    
    while True:

        print('''Choose your option:
        1. Falling Object
        2. Thrown Object''')

        choice = input("Enter your option's number: ")

        if choice == '1':

            print('''Choose your quantity to calculate:
        1. Height(h)
        2. Final Velocity
        3. Gravitational Aceeleration
        4. Time''')

            choice_quan_fall = input(
                "Enter the quantity's number you want to calculate: ")

            if choice_quan_fall == '1':
                calculate_h_falling_obj()

            elif choice_quan_fall == '2':
                calculate_v_falling_obj()

            elif choice_quan_fall == '4':
                calculate_t_falling_obj()

            elif choice_quan_fall == '3':
                print('''Choose your option for calculate Gravitational Acceleration:
        1. Calculate by latitude
        2. Calculate by equation''')

                choice_quan_g = input("Enter your option's number: ")

                if choice_quan_g == '1':
                    g = calculate_g()
                    print(f'The Gravitational Accelertion is {g} m/s²')

                elif choice_quan_g == '2':
                    calculate_g_eqn_fall()

        if choice == '2':
            print('''Choose your quantity to calculate:
        1. Initial Velocity
        2. Height
        3. Time
        4. Soaring Time
        5. Gravitational Acceleration''')

            choice_quan_thrown = input(
                "Enter the quantity's number you want to calculate: ")

            if choice_quan_thrown == '1':
                calculate_u_thrown()

            elif choice_quan_thrown == '2':
                calculate_h_thrown()

            elif choice_quan_thrown == '3':
                calculate_t_thrown()

            elif choice_quan_thrown == '4':
                g = calculate_g()
                u = float(input('Enter the Initial Velocity(u)(m/s): '))
                t = (2 * u) / g
                print(f'The Soaring Time of the object is {t} s')

            elif choice_quan_thrown == '5':
                print('''Choose your option for calculate Gravitational Acceleration:
        1. Calculate by latitude
        2. Calculate by equation''')

                choice_quan_g = input("Enter your option's number: ")

                if choice_quan_g == '1':
                    g = calculate_g()
                    print(f'The Gravitational Accelertion is {g} m/s²')

                elif choice_quan_g == '2':
                    calculate_g_eqn_thrown()
                    
        another_calculation = input('Do you want to perform another calculation? (y/n): ')
        
        if another_calculation != 'y':
            print('Thank you for using Kinematic Calculator for Falling and Thrown Objects.....!')
            break


if __name__ == '__main__':
    main()
