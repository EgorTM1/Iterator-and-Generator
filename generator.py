import types


def flat_generator(list_of_lists):
  cursor = 0
  inCursor = -1

  while True:
    if (len(list_of_lists[cursor]) - 1) > inCursor:
      inCursor += 1

      yield list_of_lists[cursor][inCursor]
    

    if (len(list_of_lists[cursor]) - 1) == inCursor:
        
      cursor += 1
      inCursor = 0

      if len(list_of_lists) == cursor:
        break
        
      else:
        yield list_of_lists[cursor][inCursor]
        

def test_2():

  list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]

  for flat_iterator_item, check_item in zip(
    flat_generator(list_of_lists_1),
      ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

    assert flat_iterator_item == check_item

  assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

  assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
  test_2()