(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((> num1 num2) 1)
    (else 0))
)