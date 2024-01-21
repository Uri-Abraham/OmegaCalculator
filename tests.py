import pytest
from Main import main_tests


@pytest.mark.parametrize("invalid_input", [
    "",
    "(3+6",
    "452+52a",
    "      ",
    "500!",
    "((8-))",
    "5/0",
])
def test_invalid_expressions(invalid_input):
    with pytest.raises(SystemExit):
        main_tests(invalid_input)


@pytest.mark.parametrize("simple_input, simple_result", [
    ("63  -56", 7),
    ("6-2^2", 2),
    ("97+-4", 93),
    ("7$25  #", 7),
    ("3!+7*7", 55),
    ("10 /11.7&2.5", 4),
    ("-3", -3),
    ("~---6%5", 1),
    ("(52@50)*2", 102),
    ("(10!&(2/4)  )#", 5),
    ("-(5-(8-(-8)))", 11),
])
def test_simple_valid_expressions(simple_input, simple_result):
    result = main_tests(simple_input)
    assert result == simple_result


@pytest.mark.parametrize("complicated_input, complicated_result", [
    ("6^5#-(1.52#*52)+9&2#+25", 7387),
    ("52*(1$4&6-(--4*36))-(0)", -7280),
    ("525+9&4@6*(56^-1)^0%(0.5)", 530),
    ("(((55-5--55-5)-55)---55)", -10),
    ("(2^2^(2^2))+-(4.44#&2)", 254),
    ("5-----------5+5------5", 10),
    ("(((((((((((161.4)))))))))))", 161.4),
    ("(10^10^10/3)#@41-42*(0)", 53.5),
    ("      ~--4%2    + 4*45*6-(34)", 1046),
    ("~-4-~-4-~--4-(~4-4)-~-4", 8),
    ("1+1-1*1/1^-1%1&1$1@~-1#!", 1),
    ("3!!%3!---8+((74-8)-9)", 49),
    ("0.9999999###+3.3333333####", 15),
    ("10!##!##!##!##!##!##!##!##!##!", 362880),
    ("(6/9/6/9)/(6/(9/6)-9)", -0.0024691358024691358)
])
def test_complicated_valid_expressions(complicated_input, complicated_result):
    result = main_tests(complicated_input)
    assert result == complicated_result
