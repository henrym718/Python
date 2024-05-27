from fizzbuzz import fizzbuzz

#Si el numero es divisible por 3, se devuelve ""
# - Si el numero es divisible por 5, se devuelve "Buzz"
# - Si el numero es divisible por 3 y 5, se devuelve "FizzBuzz"
# - En cualquier otro caso, se devuelve el numero

def test_pass_div_3():
    assert fizzbuzz(3) == "Fizz"    

def test_pass_div_5():
    assert fizzbuzz(10) == "Buzz"   

def test_pass_div_5_3():
    assert fizzbuzz(15) == "FizzBuzz"   

def test_pass_other_case():
    assert fizzbuzz(8) == 8   
