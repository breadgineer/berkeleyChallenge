(define (list-concat a b)
    (if (null? a)
    b
    (cons (car a) (list-concat (cdr a) b)))
)

