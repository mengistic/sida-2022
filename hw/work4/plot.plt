set terminal jpeg

set output "search.jpg"

plot "data.txt" using 1:3 with line


