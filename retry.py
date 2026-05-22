# Вантеев Руслан ИИАД_1
from random import random, choice

import functools


def retry(count=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError:
                    if attempt == count - 1:
                        
                        raise
                    continue
                except OSError:
                   
                    print(f"{func.__name__} raise OSError exception.")
                    if attempt == count - 1:
                        
                        raise
                    continue
            
            
            raise RuntimeError(f"Function {func.__name__} failed after {count} attempts")
        
        return wrapper
    
    return decorator


exceptions = (ValueError, OSError)


@retry(count=5)
def random_exception() -> float:
    if (d := random()) > 0.5:
        raise choice(exceptions)
    return d


if __name__ == "__main__":
    for _ in range(10):
        print("result:", random_exception())
