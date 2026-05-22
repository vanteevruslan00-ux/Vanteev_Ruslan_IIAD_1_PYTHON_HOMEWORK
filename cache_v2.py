# Вантеев Руслан ИИАД_1
import json
import os


def cache(cache_file='cache.json', use_kwargs=False):
    def decorator(func):
        cached_results = {}
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    loaded_cache = json.load(f)
                    for key_str, value in loaded_cache.items():
                        key = eval(key_str)
                        cached_results[key] = value
                print(f'Загружен кеш из файла: {cache_file}')
                print(f'Размер кеша: {len(cached_results)}')
            except Exception as e:
                print(f'Ошибка при загрузке кеша: {e}')
                cached_results = {}
        
        def wrapper(*args, **kwargs):
            if use_kwargs:
                key = tuple(sorted(kwargs.items()))
            else:
                key = args
            
            if key not in cached_results:
                if use_kwargs:
                    result = func(**dict(key))
                else:
                    result = func(*args)
                
                cached_results[key] = result
                
                _save_cache(cached_results, cache_file)
                
                print(f'Результат вычислен и сохранён: {func.__name__}{args if not use_kwargs else kwargs}')
            else:
                print(f'Результат взят из кеша: {func.__name__}{args if not use_kwargs else kwargs}')
            
            return cached_results[key]
        
        wrapper.cache = cached_results
        wrapper.cache_file = cache_file
        
        def cache_clear():
            cached_results.clear()
            if os.path.exists(cache_file):
                os.remove(cache_file)
            print(f'Кеш очищен, файл {cache_file} удалён')
        
        wrapper.cache_clear = cache_clear
        
        def cache_info():
            print(f'Файл кеша: {cache_file}')
            print(f'Размер кеша: {len(cached_results)}')
            print(f'Ключи кеша: {list(cached_results.keys())}')
        
        wrapper.cache_info = cache_info
        
        return wrapper
    
    return decorator


def _save_cache(cached_results, cache_file):
    try:
        serializable_cache = {str(key): value for key, value in cached_results.items()}
        
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(serializable_cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'Ошибка при сохранении кеша: {e}')



@cache(cache_file='sum_cache.json', use_kwargs=False)
def my_sum(a, b):
    return a + b


@cache(cache_file='multiply_cache.json', use_kwargs=True)
def my_multiply(x, y):
    return x * y


def main():
    print('Тест с позиционными аргументами')
    print(f'my_sum(2, 3) = {my_sum(2, 3)}') 
    print(f'my_sum(2, 3) = {my_sum(2, 3)}')  
    print(f'my_sum(5, 7) = {my_sum(5, 7)}')  
    
    print('\n Тест с именованными аргументами')
    print(f'my_multiply(x=4, y=5) = {my_multiply(x=4, y=5)}')  
    print(f'my_multiply(x=4, y=5) = {my_multiply(x=4, y=5)}')  
    print(f'my_multiply(y=5, x=4) = {my_multiply(y=5, x=4)}')   
        
    print('\n Информация о кеше')
    my_sum.cache_info()
    my_multiply.cache_info()


if __name__ == '__main__':
    main()
