import pytest
from fatorial import fatorial # Assumindo que a função acima está no arquivo 'fatorial.py'

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),      # Caso especial 0!
    (1, 1),      # Caso especial 1!
    (2, 2),      # Positivo (2 * 1)
    (3, 6),      # Positivo (3 * 2 * 1)
    (5, 120),    # Positivo (5 * 4 * 3 * 2 * 1)
    (10, 3628800)
])
def test_fatorial_casos_validos(entrada, esperado):
    assert fatorial(entrada) == esperado
    