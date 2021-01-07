# An iterable is an object that knows how to create an iterator.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()

our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
print(next(our_iterator))  # => "one"

# It main)tains st)ate as we iterate.
print(next(our_iterator))  # => "two"
print(next(our_iterator))  # => "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
# next(our_iterator)  # Raises StopIteration