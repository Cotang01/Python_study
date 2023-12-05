/**
Написать программу на языке Prolog для вычисления суммы
элементов списка. На вход подаётся целочисленный массив.
На выходе - сумма элементов массива.
**/

main :-
    process,
    halt.

process :-
    call(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Sum)),
    write(Sum).

sum_list([], 0).
sum_list([H|T], Sum) :-
    sum_list(T, Rest),
    Sum is H + Rest.

:- main.
