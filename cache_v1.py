# Вантеев Руслан ИИАД_1
def cache(func):
    cached_results = {}
    
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    
    return wrapper


@cache
def my_sum(a, b):
    return a + b


def main():
    print(my_sum(2, 3)) 
    print(my_sum(2, 3))  
    print(my_sum(5, 7))  
    print(my_sum(5, 7))  


if __name__ == '__main__':
    main()
