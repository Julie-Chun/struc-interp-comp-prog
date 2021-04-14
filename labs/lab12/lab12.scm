; Lab 14: Final Review

(define (compose-all funcs)
	
	(define (compose fn input) 
		(cond
			((= (length fn) 0) input)
			(else (compose (cdr fn) ((car fn) input))  )
		)
	)

	(lambda (x) (compose funcs x))


)

