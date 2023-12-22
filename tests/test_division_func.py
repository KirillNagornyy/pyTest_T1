from utils import divison

import pytest
@pytest.mark.parametrize("a,b, expected_result", [(10,2,5),
                                                  (20,10,2),
                                                  (30,-3,-10),
                                                  (5,2,2.5)])
def test_divison_good(a,b, expected_result):
    assert divison(a, b) == expected_result

@pytest.mark.parametrize("a2,b2,Err",[(10,0,ZeroDivisionError),
                                      (10,"j",TypeError)])

def test_zero_divison(a2,b2,Err):
    with pytest.raises(Err):
        divison(a2,b2)
