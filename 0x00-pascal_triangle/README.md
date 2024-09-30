# Pascal triangle

## GOAL

Create a method that return a pascal triangle of size `n`

## THINKING

- `n` represent number of rows.

- number of cells happen to be order of rows (row number 1 has 1 cell row number 2 has 2 cells and so on).

- each cell in row in rows is supposed to be `same cell in previous row + previous cell in previous row` if cell is not on edge of triangle else `1`.

- after calculating each cell add them to a list which represent a row.

- at the end add the row to the triangle.

## SOLUATION

- create triangle (list of list)
- loop over all required rows `n` = 1,2,3,...,n
-  create new list
-  loop over cells
-   calculate each cell (row, column) to be cell(row-1, column) + cell(row-1, column-1) if n > row > 0 else 1
-   add cell to list
-  add list to triangle
- return triangle
