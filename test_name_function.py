from name_functions import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Jolpin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == "Janis Joplin"




    from name_functions import get_formatted_name

def test_first_last_name():
    """Do names like 'Andrew Johnson' work?"""
    formatted_name = get_formatted_name('andre', 'johnson')
    assert formatted_name == "Andrew Johnson"


def test_first_last_middle():
    """Do names like 'Sarah Rose Lucy' work?"""
    formatted_name = get_formatted_name('sarah', 'rose', 'lucy')
    assert formatted_name == 'Sarah Rose Lucy'

