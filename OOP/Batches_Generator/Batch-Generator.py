import sys
data = [1, 2, 3, 4, 5, 6, 7]
batch_size = 3
expected = [[1, 2, 3], [4, 5, 6], [7]]
def batch_generator (data, batch_size):
    
    for i in range(0,len(data),batch_size):

        batches = data[i:i+ batch_size]
        yield batches #Lazy Evaluation

#printing batch using for loop
for batch in batch_generator(data, batch_size):
    print(batch)

#It will pass the test
def test_batch_generator():
    result = list(batch_generator(data, batch_size))
    assert result == expected

#Intentionally raising assert error for testing 
def test_wrong_batch_generator():
    result_1 = list(batch_generator([], batch_size))
    assert result_1 == expected

# print(test_wrong_batch_generator())


#comparing memory usage
list_batches = list(batch_generator(data, batch_size))
generator_batches = batch_generator(data, batch_size)

#For tiny datasets, a generator object can genuinely be larger than a small list
print(f"Memory size of List is : {sys.getsizeof(list_batches)} and Memory size of Batches : {sys.getsizeof(generator_batches)}")

#Testing large data

large_data = range(100_000)
large_batch_size = 100
#comparing memory usage
large_list_batches = list(batch_generator(large_data, large_batch_size))
large_generator_batches = batch_generator(large_data, large_batch_size)
print(f"Memory size of List is : {sys.getsizeof(large_list_batches)} and Memory size of Batches : {sys.getsizeof(large_generator_batches)}")