
# 🔄 Batch Generator — Python

## 🎯 Objective

Implement a memory-efficient batch generator using Python and understand the difference between **eager evaluation (lists)** and **lazy evaluation (generators)**.

This project is part of my [Machine Learning Foundations — From Scratch](../../) repository.

## 📚 Concepts Covered

- Python generators and `yield`
- Lazy vs eager evaluation
- Iteration using `range()`
- Dynamic batching using list slicing
- Unit testing with `assert`
- Edge-case testing
- Memory measurement using `sys.getsizeof()`

## ⚙️ Implementation

Developed `batch_generator(data, batch_size)` to divide a dataset into smaller batches.

Example:

**Input:**
```python
data = [1, 2, 3, 4, 5, 6, 7]
batch_size = 3
```

**Output:**
```text
[1, 2, 3]
[4, 5, 6]
[7]
```

The generator uses `yield` to produce batches on demand rather than storing all batches simultaneously.

## 🧪 Testing

Implemented assertion-based tests to verify batch contents and explore empty-dataset behaviour.

The main test compares the generated batches against manually defined expected output.

**Note:** The implementation also includes an intentionally failing assertion for demonstration purposes. It is not a passing test and should be excluded from normal automated test runs.

## 📊 Memory Comparison

Compared shallow object sizes using Python's `sys.getsizeof()`.

| Dataset Size | List | Generator |
|---|---:|---:|
| 7 observations | 120 bytes | 248 bytes |
| 100,000 observations | 8,856 bytes | 248 bytes |

For the larger dataset, the generator avoids materialising all 1,000 batches before iteration.

**Limitation:** `sys.getsizeof()` measures the shallow size of objects. The list measurements exclude the memory used by nested batches, so these results are not a complete measure of memory consumption.

## 📂 Project Structure

```text
Batches_Generator/
├── Batch-Generator.py
└── README.md
```

## 🚀 Run the Project

From the repository root:

```bash
python OOP/Batches_Generator/Batch-Generator.py
```

## ✅ Learning Outcomes

- Understood how generators pause and resume execution using `yield`.
- Implemented dynamic batching without storing every batch upfront.
- Practised assertion-based testing and investigated an intentional test failure.
- Measured and interpreted list and generator object sizes.
- Understood why generators can improve memory efficiency when working with large datasets.

## 🔧 Future Improvements

- Validate that `batch_size` is a positive integer.
- Add automated tests for additional edge cases.
- Measure peak memory allocation using `tracemalloc`.
