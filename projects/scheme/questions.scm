(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15

  (define (helper l)
    (cond
      ((or (eq? l nil) (eq? l undefined)) nil)
      (else
        (cons (cons (- (length s) (length l)) (cons (car l) nil)) (helper (cdr l)))
        )
      )
    )
  (helper s)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond 
    ((and (or (eq? list1 nil) (eq? list1 undefined)) (or (eq? list2 nil) (eq? list2 undefined))) nil)
    ((or (eq? list1 nil) (eq? list1 undefined)) (cons (car list2) (merge comp list1 (cdr list2))))
    ((or (eq? list2 nil) (eq? list2 undefined)) (cons (car list1) (merge comp (cdr list1) list2)))
    ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
    (else (cons (car list2) (merge comp  list1 (cdr list2))))
    )
  )
  ; END PROBLEM 16

(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (define (order l)
      (cond
        ((or (eq? (cdr l) nil) (eq? (cdr l) undefined)) l)
        ((or (< (car l) (cadr l)) (= (car l) (cadr l))) (cons (car l) (order (cdr l))))
        ((> (car l) (cadr l)) (cons (car l) nil))
        )
      )
    
    (define (remainder l)
      (cond
        ((or (eq? (cdr l) nil)(eq? (cdr l) undefined)) nil)
        ((or (< (car l) (cadr l)) (= (car l) (cadr l))) (remainder (cdr l)))
        (else (cdr l))
        )
      )
    
    
    (define (helper x)
      (cond
        ((or (eq? x nil) (eq? x undefined)) nil)

        (else (cons (order x) (helper (remainder x))))
        )
      )




    (define (original s)

      (cond
        ((or (eq? (cdr s) nil) (eq? (cdr s) undefined)) (cons (car s) nil))
        ((or(< (car s) (cadr s)) (= (car s) (cadr s)))  
           (cons (car s) (nondecreaselist (cdr s))) 
          )
        (else (cons (car s) (nondecreaselist (cdr s))))
        )
      
      
      )

    (helper s)
  )  

    ; END PROBLEM 17





















