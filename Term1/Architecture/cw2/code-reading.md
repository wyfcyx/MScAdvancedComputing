## Input/Output

Take `nell-2.tns` as an example, it is a `12092x9184x28818` tensor, when `mode=0` and `r=16` by default the result is a `28816x16` matrix. This means that the length of row and column of the result matrix are $\max_{0\leq i<\text{input.nmodes}}\{\text{input.ndims[i]}\}$ and $r$ respectively.

## Important data structures

```c
typedef struct {
		sptIndex nmodes;      /// # modes
		sptIndex * sortorder;  /// the order in which the indices are sorted
		sptIndex * ndims;      /// size of each mode, length nmodes
		sptNnzIndex nnz;         /// # non-zeros
		sptIndexVector * inds;       /// indices of each element, length [nmodes][nnz]
		sptValueVector values;      /// non-zero values, length nnz
} sptSparseTensor;
```

which is the type of `X` we can found many times in the code.

`sptIndexVector` and `sptValueVector` are dynamically allocated vector just like `std::vector` in C++.

```c
typedef struct {
		sptIndex nrows;   /// # rows
		sptIndex ncols;   /// # columns
		sptIndex cap;     /// # of allocated rows
		sptIndex stride;  /// ncols rounded up to 8
		sptValue *values; /// values, length cap*stride
} sptMatrix;
```

## calculation

```c
// stride=16 here maybe because r=16

for(sptNnzIndex x=0; x<nnz; ++x) {
    // mode_i,tmp_i_1,tmp_i_2 -> [x] of inds[mode],inds[(mode+1)%nmodes],inds[(mode+2)%nmodes]
    mode_i = mode_ind[x];
    tmp_i_1 = times_inds_1[x];
    tmp_i_2 = times_inds_2[x];
    entry = vals[x];

    for(sptIndex r=0; r<R; ++r) {
        mvals[mode_i * stride + r] += entry * times_mat_1->values[tmp_i_1 * stride + r] * times_mat_2->values[tmp_i_2 * stride + r];
    }
}

```

for every $(i,j,k)$, $\text{result}_{i,r}$+=$\text{T}_{i,j,k}\times \text{R2}_{j,r}\times\text{R3}_{k,r}$

every `sptValue`: 4 bytes under default configuration



