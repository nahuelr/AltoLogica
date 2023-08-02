from math import sqrt
from typing import List

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


@api_view(['POST'])
def get_prime_numbers(request):
    """ Docstring here"""
    if 'numbers' not in request.data.keys():
        return Response({'message': 'Key \'numbers\' is required!'}, status=HTTP_400_BAD_REQUEST)
    data = request.data.get('numbers', None)
    try:
        prime_numbers = _get_prime_numbers(data)
    except ValueError as e:
        return Response({'message': f'** Exception: {str(e)}'}, status=HTTP_400_BAD_REQUEST)

    return Response({'prime_numbers': prime_numbers}, status=HTTP_200_OK)


def _get_prime_numbers(numbers: List[int]) -> List[int]:
    """ Docstring here """
    result: List[int] = []
    for n in numbers:
        if n < 0:
            raise ValueError(f"Number {n} is not a positive number")
        if n in [0, 1]:  # Exclusion list
            continue
        cap: int = int(sqrt(n)) + 1
        is_prime: bool = True
        for i in range(2, cap):
            is_prime &= n % i != 0
            if not is_prime:
                continue
        if is_prime:
            result.append(n)
    return result
