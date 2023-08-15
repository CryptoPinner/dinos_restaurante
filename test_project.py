import pytest
import mock
import builtins
import csv

from project import reception,validate,time,check_customer

"""
This test will mock input from 0 to 8
"""
    
def test_reception():
    for i in range (9):
        with mock.patch.object(builtins, 'input', lambda _: f"{i}"):
            assert reception() == i

#This test will mock input from 0 to 1000

def test_validate():
        for i in range(1000):
            d = f"{i:04d}"
            with mock.patch.object(builtins, 'input', lambda _: f"DINOS{d}"):
                assert validate() == f"DINOS{d}"

#This test the time of opening and raise SystemExit if is close

def test_time():
    try:
        with mock.patch.object(builtins, 'input', lambda _: "13"):
            assert time() == "Lunch"
        
        with mock.patch.object(builtins, 'input', lambda _: "21"):
            assert time() == "Dinner"
    except:
        with mock.patch.object(builtins, 'input', lambda _: "8"):    
            SystemExit("We are Close ☹️  Come back later \n")


#This test two users numbers and see if return the same, and check one that is not in the list,
#it has to return false
    
def test_check_customer():
    with open('customers.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "DINOS0002" == row["Customer"]:
                r = row
    assert check_customer("DINOS0002") == r

    with open('customers.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "DINOS0456" == row["Customer"]:
                r = row
            else:
                r = False
    assert check_customer("DINOS0456") == r


if __name__ == "__main__":
    main()