(define (vir-fib n)
    (if (<= n 1)
        n
        (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
)
    