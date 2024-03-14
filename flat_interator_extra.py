import self as self


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_iterators = [iter(list_of_list)]
        self.current_iterator = None


    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current_iterator is None:
                try:
                    self.current_iterator = next(self.list_of_iterators[-1])
                except StopIteration:
                    if len(self.list_of_iterators) == 1:
                        raise StopIteration
                    self.list_of_iterators.pop()
                    continue

            try:
                item = next(self.current_iterator)
                if isinstance(item, list):
                    self.list_of_iterators.append(iter(item))
                    self.current_iterator = None
                else:
                    return item
            except StopIteration:
                self.current_iterator = None



def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
