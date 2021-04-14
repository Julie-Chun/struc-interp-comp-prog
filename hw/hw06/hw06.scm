;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond ((= x 0) 0) ((> x 0) 1) (else -1))

)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 1) 1) ((even? n) (* (square b) (pow b (/ n 2)))) ((odd? n) (* b (pow b (- n 1)))) )
)

(define (unique s)
	(cond
		((zero? (length s)) nil)
		(else 
			(append (list (car s)) (unique (filter (lambda (x) (not (equal? (car s) x))  ) (cdr s))))
			)
		)


)








